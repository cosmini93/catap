import * as THREE from 'three';
import * as CANNON from 'cannon-es';

/* ================= BIOMES ================= */
const BIOMES = {
  dune: { name:'DUNELE DE ARAMĂ',
    skyTop:0x4E8FCB, skyMid:0x9DC4E4, skyBot:0xF2DCB4, fog:0xE0C098, fogNear:70, fogFar:260,
    ground:0xD9B383, groundEdge:0xC79A66, rock:0x9C8163, veg:0x8E8446, vegKind:'palm',
    sun:0xFFF0D0, sunI:1.65, amb:0xC9DCF0, ambI:.62, hemi:0xFFE9C4 },
  frost:{ name:'CREASTA ÎNGHEȚATĂ',
    skyTop:0x2A6FB8, skyMid:0x8FC4E8, skyBot:0xE2F1FA, fog:0xC8E2F2, fogNear:60, fogFar:240,
    ground:0xDCE9F5, groundEdge:0xA9C2DA, rock:0x8496A8, veg:0x6E7A5E, vegKind:'dead',
    sun:0xFFFFFF, sunI:1.35, amb:0x9FC4E8, ambI:.5, hemi:0xD8ECFF },
  night:{ name:'CÂMPIA DE MIEZ DE NOAPTE',
    skyTop:0x0A1738, skyMid:0x1E3A66, skyBot:0x4E7098, fog:0x22385A, fogNear:55, fogFar:230,
    ground:0x38495F, groundEdge:0x243146, rock:0x4C5B70, veg:0x2E4A34, vegKind:'pine',
    sun:0xCFE0FF, sunI:1.15, amb:0x53709E, ambI:1.05, hemi:0x7C97C0, moon:true }
};

/* ================= SETUP ================= */
const canvas = document.getElementById('gl');
const renderer = new THREE.WebGLRenderer({ canvas, antialias:true, powerPreference:'high-performance' });
const SMALL = Math.min(innerWidth, innerHeight) < 560 || /Mobi|Android|iPhone|iPad/i.test(navigator.userAgent);
renderer.setPixelRatio(Math.min(devicePixelRatio||1, SMALL?1.5:2));
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = SMALL ? THREE.PCFShadowMap : THREE.PCFSoftShadowMap;

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(52, 1, .3, 900);
const rig = new THREE.Object3D();      // the catapult yaws with aiming
scene.add(rig);
scene.add(camera);

const world = new CANNON.World({ gravity:new CANNON.Vec3(0,-22,0) });
world.broadphase = new CANNON.SAPBroadphase(world);
world.allowSleep = true;
world.defaultContactMaterial.friction = .45;
world.defaultContactMaterial.restitution = .06;

const matGround = new CANNON.Material('g'), matProp = new CANNON.Material('p');
world.addContactMaterial(new CANNON.ContactMaterial(matGround, matProp, { friction:.62, restitution:.05 }));

/* ================= SHARED ART ================= */
const rnd = (a,b)=>a+Math.random()*(b-a);
const tint = (hex,amt)=>{ const c=new THREE.Color(hex); c.offsetHSL(0,0,amt); return c; };

function grainTexture(base, spots, size=64){
  const c=document.createElement('canvas'); c.width=c.height=size;
  const g=c.getContext('2d');
  g.fillStyle=base; g.fillRect(0,0,size,size);
  for(let i=0;i<spots;i++){
    const r=Math.random()*.09+.02;
    g.fillStyle='rgba(0,0,0,'+r.toFixed(3)+')';
    g.fillRect(Math.random()*size,Math.random()*size,Math.random()*8+2,Math.random()*8+2);
    g.fillStyle='rgba(255,255,255,'+(r*.7).toFixed(3)+')';
    g.fillRect(Math.random()*size,Math.random()*size,Math.random()*6+2,Math.random()*6+2);
  }
  const t=new THREE.CanvasTexture(c);
  t.wrapS=t.wrapT=THREE.RepeatWrapping; t.colorSpace=THREE.SRGBColorSpace;
  return t;
}
const TEX = {
  stone: grainTexture('#b9b2a6', 90),
  wood : grainTexture('#8a5f34', 70),
  crate: grainTexture('#9c6f3d', 50)
};
const MAT = {
  stone: new THREE.MeshLambertMaterial({ color:0xcfcabd, map:TEX.stone }),
  wood : new THREE.MeshLambertMaterial({ color:0xc99a5e, map:TEX.wood }),
  beam : new THREE.MeshLambertMaterial({ color:0xa87a45, map:TEX.wood }),
  crate: new THREE.MeshLambertMaterial({ color:0xb98a52, map:TEX.crate }),
  iron : new THREE.MeshLambertMaterial({ color:0x5b6472 }),
  cloth: new THREE.MeshLambertMaterial({ color:0x9d2f38 })
};
const boxGeo = new THREE.BoxGeometry(1,1,1);

/* ================= WORLD DRESSING ================= */
let sky, sunLight, ambLight, hemiLight, groundMesh, decor=new THREE.Group(), clouds=new THREE.Group();
scene.add(decor); scene.add(clouds);

function buildSky(){
  const geo = new THREE.SphereGeometry(700, 24, 14);
  const mat = new THREE.ShaderMaterial({
    side: THREE.BackSide, depthWrite:false,
    uniforms:{ top:{value:new THREE.Color(0x4E8FCB)}, mid:{value:new THREE.Color(0x9DC4E4)},
               bot:{value:new THREE.Color(0xF2DCB4)} },
    vertexShader:`varying vec3 vP; void main(){ vP=position; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.); }`,
    fragmentShader:`varying vec3 vP; uniform vec3 top; uniform vec3 mid; uniform vec3 bot;
      void main(){ float h=clamp(vP.y/700.*1.9+.12,0.,1.);
        vec3 c = h<.38 ? mix(bot,mid,smoothstep(0.,.38,h))
                       : mix(mid,top,smoothstep(.38,1.,h));
        gl_FragColor=vec4(c,1.); }`
  });
  sky = new THREE.Mesh(geo, mat); sky.frustumCulled=false; scene.add(sky);
}
function puffCloud(scale){
  const g=new THREE.Group();
  const m=new THREE.MeshLambertMaterial({ color:0xffffff, emissive:0x9fb4cc, emissiveIntensity:.4 });
  const n=6+((Math.random()*4)|0);
  for(let i=0;i<n;i++){
    const r=rnd(6,13);
    const s=new THREE.Mesh(new THREE.SphereGeometry(r,7,6), m);
    s.position.set(i*rnd(6,9)-n*3.6, rnd(-3,4)-Math.abs(i-n/2)*1.2, rnd(-5,5));
    s.scale.y=rnd(.55,.8); g.add(s);
  }
  g.scale.setScalar(scale); return g;
}
function buildClouds(){
  clouds.clear();
  for(let i=0;i<(SMALL?7:11);i++){
    const c=puffCloud(rnd(.8,1.7));
    const a=rnd(0,Math.PI*2), d=rnd(240,430);
    c.position.set(Math.cos(a)*d, rnd(80,150), Math.sin(a)*d);
    c.userData.spin=rnd(.004,.012)*(Math.random()<.5?-1:1);
    clouds.add(c);
  }
}
function buildGround(B){
  if(groundMesh){ scene.remove(groundMesh); groundMesh.geometry.dispose(); }
  const geo=new THREE.CircleGeometry(420, 56);
  const col=new THREE.Color(B.ground), edge=new THREE.Color(B.groundEdge);
  const pos=geo.attributes.position, cols=[];
  for(let i=0;i<pos.count;i++){
    const d=Math.hypot(pos.getX(i),pos.getY(i))/420;
    const c=col.clone().lerp(edge, Math.pow(d,1.6));
    cols.push(c.r,c.g,c.b);
  }
  geo.setAttribute('color', new THREE.Float32BufferAttribute(cols,3));
  groundMesh=new THREE.Mesh(geo, new THREE.MeshLambertMaterial({ vertexColors:true }));
  groundMesh.rotation.x=-Math.PI/2; groundMesh.receiveShadow=true;
  scene.add(groundMesh);
}
function lowRock(size, color){
  const g=new THREE.IcosahedronGeometry(size, 0);
  const p=g.attributes.position;
  for(let i=0;i<p.count;i++) p.setXYZ(i, p.getX(i)*rnd(.7,1.3), p.getY(i)*rnd(.6,1.1), p.getZ(i)*rnd(.7,1.3));
  g.computeVertexNormals();
  const m=new THREE.Mesh(g, new THREE.MeshLambertMaterial({ color, flatShading:true }));
  m.castShadow=m.receiveShadow=true; return m;
}
function vegetation(kind){
  const g=new THREE.Group();
  if(kind==='pine'||kind==='dead'){
    const trunk=new THREE.Mesh(new THREE.CylinderGeometry(.13,.22,rnd(3.5,6),5),
      new THREE.MeshLambertMaterial({color:0x4a3826, flatShading:true}));
    trunk.position.y=trunk.geometry.parameters.height/2; g.add(trunk);
    if(kind==='pine'){
      for(let k=0;k<3;k++){
        const c=new THREE.Mesh(new THREE.ConeGeometry(1.7-k*.42, 2.2, 6),
          new THREE.MeshLambertMaterial({color:0x24422c, flatShading:true}));
        c.position.y=2.4+k*1.35; g.add(c);
      }
    } else {
      for(let k=0;k<4;k++){
        const b=new THREE.Mesh(new THREE.CylinderGeometry(.05,.1,rnd(1.2,2.2),4),
          new THREE.MeshLambertMaterial({color:0x51402e, flatShading:true}));
        b.position.set(rnd(-.3,.3), rnd(2.6,4.6), rnd(-.3,.3));
        b.rotation.z=rnd(-1,1); b.rotation.x=rnd(-1,1); g.add(b);
      }
    }
  } else {
    const trunk=new THREE.Mesh(new THREE.CylinderGeometry(.16,.26,rnd(4,6.5),5),
      new THREE.MeshLambertMaterial({color:0x8a6a42, flatShading:true}));
    trunk.position.y=trunk.geometry.parameters.height/2;
    trunk.rotation.z=rnd(-.14,.14); g.add(trunk);
    const top=trunk.geometry.parameters.height;
    const frondMat=new THREE.MeshLambertMaterial({color:0x7d8f3a, side:THREE.DoubleSide, flatShading:true});
    for(let k=0;k<7;k++){
      const a=k/7*Math.PI*2+rnd(-.2,.2);
      const shape=new THREE.PlaneGeometry(rnd(2.6,3.6), .78, 4, 1);
      const pos=shape.attributes.position;
      for(let i=0;i<pos.count;i++){
        const t=(pos.getX(i)/shape.parameters.width)+.5;
        pos.setY(i, pos.getY(i)*(1-t*.75));
        pos.setZ(i, -t*t*1.5);
      }
      shape.computeVertexNormals();
      const l=new THREE.Mesh(shape, frondMat);
      l.position.set(0, top+.05, 0);
      l.rotation.y=a; l.rotation.z=-.22;
      l.translateX(shape.parameters.width*.5);
      g.add(l);
    }
    const nut=new THREE.Mesh(new THREE.SphereGeometry(.18,6,5),
      new THREE.MeshLambertMaterial({color:0x6b5230}));
    nut.position.set(.2,top-.15,.1); g.add(nut);
  }
  g.traverse(o=>{ if(o.isMesh) o.castShadow=true; });
  return g;
}
function dressScene(B){
  decor.clear();
  const clear=(x,z)=>{
    if(Math.abs(x)<11 && z>-46 && z<6) return false;      // firing lane
    if(Math.abs(x)<17 && z>-44 && z<-24) return false;    // fort footprint
    return true;
  };
  for(let i=0;i<(SMALL?26:46);i++){
    const a=rnd(-Math.PI,Math.PI), d=rnd(16,190);
    const x=Math.cos(a)*d, z=Math.sin(a)*d-20;
    if(!clear(x,z)) continue;
    const r=lowRock(rnd(.5,3.2), B.rock);
    r.position.set(x, rnd(-.5,.35), z);
    r.rotation.y=rnd(0,6.3);
    decor.add(r);
  }
  for(let i=0;i<(SMALL?18:34);i++){
    const a=rnd(-Math.PI,Math.PI), d=rnd(20,170);
    const x=Math.cos(a)*d, z=Math.sin(a)*d-20;
    if(!clear(x,z)) continue;
    const v=vegetation(B.vegKind);
    v.position.set(x,0,z); v.rotation.y=rnd(0,6.3);
    decor.add(v);
  }
  // low scrub so the ground is not a bare plane
  const tuftMat=new THREE.MeshLambertMaterial({color:B.veg, side:THREE.DoubleSide});
  const bladeGeo=new THREE.PlaneGeometry(.5,.7,1,1);
  const bp=bladeGeo.attributes.position;
  for(let i=0;i<bp.count;i++) if(bp.getY(i)>0) bp.setX(i, bp.getX(i)*.18);
  bladeGeo.computeVertexNormals();
  for(let i=0;i<(SMALL?70:150);i++){
    const a=rnd(-Math.PI,Math.PI), d=rnd(12,140);
    const x=Math.cos(a)*d, z=Math.sin(a)*d-20;
    if(Math.abs(x)<7 && z>-40 && z<4) continue;
    const cl=new THREE.Group();
    for(let k=0;k<3;k++){
      const bl=new THREE.Mesh(bladeGeo, tuftMat);
      bl.rotation.y=k*1.05+rnd(-.3,.3); bl.rotation.z=rnd(-.22,.22);
      bl.scale.setScalar(rnd(.55,1.15)); cl.add(bl);
    }
    cl.position.set(x,.3,z); decor.add(cl);
  }
}
function applyBiome(B){
  scene.fog=new THREE.Fog(B.fog, B.fogNear, B.fogFar);
  sky.material.uniforms.top.value.set(B.skyTop);
  sky.material.uniforms.mid.value.set(B.skyMid);
  sky.material.uniforms.bot.value.set(B.skyBot);
  sunLight.color.set(B.sun); sunLight.intensity=B.sunI;
  ambLight.color.set(B.amb); ambLight.intensity=B.ambI;
  hemiLight.color.set(B.hemi); hemiLight.groundColor.set(B.ground);
  buildGround(B); dressScene(B); buildClouds();
  clouds.visible = !B.moon || true;
}
function buildLights(){
  hemiLight=new THREE.HemisphereLight(0xffe9c4, 0xc09a6a, .55); scene.add(hemiLight);
  ambLight=new THREE.AmbientLight(0xc9dcf0, .6); scene.add(ambLight);
  sunLight=new THREE.DirectionalLight(0xfff0d0, 1.6);
  sunLight.position.set(38, 54, 16);
  sunLight.castShadow=true;
  sunLight.shadow.mapSize.set(SMALL?1024:2048, SMALL?1024:2048);
  const s=sunLight.shadow.camera;
  s.left=-46; s.right=46; s.top=46; s.bottom=-30; s.near=1; s.far=170;
  sunLight.shadow.bias=-0.0012; sunLight.shadow.normalBias=.03;
  scene.add(sunLight); scene.add(sunLight.target);
  sunLight.target.position.set(0,0,-34);
}

/* ================= DESTRUCTIBLE PROPS ================= */
let props=[], guards=[], debrisBudget=0;
const propGroup=new THREE.Group(); scene.add(propGroup);

function addBox(w,h,d, x,y,z, mass, material, opts={}){
  const mesh=new THREE.Mesh(boxGeo, material);
  mesh.scale.set(w,h,d);
  mesh.castShadow=true; mesh.receiveShadow=true;
  if(material.map){
    mesh.material=material.clone();
    mesh.material.color=tint(material.color.getHex(), rnd(-.05,.05));
  }
  propGroup.add(mesh);
  const body=new CANNON.Body({
    mass, material:matProp,
    shape:new CANNON.Box(new CANNON.Vec3(w/2,h/2,d/2)),
    position:new CANNON.Vec3(x,y,z),
    sleepSpeedLimit:.35, sleepTimeLimit:.6
  });
  if(opts.rotY) body.quaternion.setFromEuler(0,opts.rotY,0);
  body.allowSleep=true; body.sleep();
  world.addBody(body);
  const p={ mesh, body, kind:opts.kind||'stone', scored:false, y0:y };
  props.push(p); return p;
}

/* --- blocky guard: cube head with a painted face --- */
function faceTexture(){
  const c=document.createElement('canvas'); c.width=c.height=64;
  const g=c.getContext('2d');
  g.fillStyle='#c8a882'; g.fillRect(0,0,64,64);
  g.fillStyle='#2a2018'; g.fillRect(12,26,9,9); g.fillRect(43,26,9,9);
  g.fillStyle='#ffffff'; g.fillRect(14,28,4,4); g.fillRect(45,28,4,4);
  g.fillStyle='#7b3f32'; g.fillRect(22,46,20,4);
  g.fillStyle='#3a2c1e'; g.fillRect(0,0,64,14);
  const t=new THREE.CanvasTexture(c); t.colorSpace=THREE.SRGBColorSpace;
  t.magFilter=THREE.NearestFilter; return t;
}
const FACE=faceTexture();
function makeGuard(x,y,z, facing){
  const g=new THREE.Group();
  const skin=new THREE.MeshLambertMaterial({ color:0xc8a882 });
  const cloth=new THREE.MeshLambertMaterial({ color:0x54606e });
  const head=new THREE.Mesh(boxGeo, [skin,skin,skin,skin,
    new THREE.MeshLambertMaterial({ map:FACE }), skin]);
  head.scale.set(.62,.62,.62); head.position.y=1.42; g.add(head);
  const helm=new THREE.Mesh(boxGeo, MAT.iron);
  helm.scale.set(.72,.26,.72); helm.position.y=1.74; g.add(helm);
  const body=new THREE.Mesh(boxGeo, cloth);
  body.scale.set(.68,.86,.44); body.position.y=.66; g.add(body);
  for(const s of [-1,1]){
    const arm=new THREE.Mesh(boxGeo, cloth);
    arm.scale.set(.2,.66,.2); arm.position.set(s*.46,.7,0); g.add(arm);
    const leg=new THREE.Mesh(boxGeo, new THREE.MeshLambertMaterial({color:0x3b3128}));
    leg.scale.set(.24,.5,.24); leg.position.set(s*.19,.0,0); g.add(leg);
  }
  const shield=new THREE.Mesh(new THREE.CylinderGeometry(.42,.42,.09,8), MAT.cloth);
  shield.rotation.x=Math.PI/2; shield.rotation.z=.2;
  shield.position.set(-.58,.78,.16); g.add(shield);
  g.traverse(o=>{ if(o.isMesh){ o.castShadow=true; o.receiveShadow=true; } });
  g.position.set(x,y,z); g.rotation.y=facing||0;
  propGroup.add(g);

  const body3=new CANNON.Body({
    mass:26, material:matProp,
    shape:new CANNON.Box(new CANNON.Vec3(.36,.95,.3)),
    position:new CANNON.Vec3(x,y+.95,z),
    sleepSpeedLimit:.4, sleepTimeLimit:.5
  });
  body3.quaternion.setFromEuler(0, facing||0, 0);
  body3.allowSleep=true; body3.sleep();
  world.addBody(body3);
  const gd={ mesh:g, body:body3, dead:false, y0:y };
  guards.push(gd); return gd;
}

/* --- fort assembly --- */
function stoneTower(cx,cz, cols, rows, bw=1.25, bh=.66, bd=1.05){
  const x0=cx-(cols-1)*bw/2;
  for(let r=0;r<rows;r++){
    const off=(r%2)?bw*.5:0;
    for(let c=0;c<cols;c++){
      const x=x0+c*bw+off*.35;
      addBox(bw*.96,bh*.94,bd, x, .34+r*bh, cz, 22, MAT.stone, {kind:'stone'});
    }
  }
  return .34+rows*bh;
}
function timberRoof(cx,cz,top,span){
  const beamMat=MAT.beam;
  for(const s of [-1,1]){
    const b=addBox(span*1.05,.16,.34, cx+s*span*.28, top+.62, cz, 8, beamMat, {kind:'wood'});
    b.body.quaternion.setFromEuler(0,0,s*.62);
  }
  addBox(span*1.5,.18,.4, cx, top+1.24, cz, 7, beamMat, {kind:'wood'});
  for(let i=0;i<4;i++)
    addBox(span*1.3,.12,.5, cx, top+.28+i*.02, cz-.6+i*.4, 5, MAT.wood, {kind:'wood'});
}
function palisade(cx,cz,len,rot){
  const n=Math.round(len/.46);
  for(let i=0;i<n;i++){
    const t=(i/(n-1)-.5)*len;
    const x=cx+Math.cos(rot)*t, z=cz+Math.sin(rot)*t;
    addBox(.42,rnd(1.9,2.3),.2, x, 1.05, z, 9, MAT.wood, {kind:'wood', rotY:rot});
  }
}
function barrel(x,z){
  const m=new THREE.Mesh(new THREE.CylinderGeometry(.42,.42,1.0,10), MAT.crate);
  m.castShadow=m.receiveShadow=true; propGroup.add(m);
  const b=new CANNON.Body({ mass:12, material:matProp,
    shape:new CANNON.Cylinder(.42,.42,1.0,10),
    position:new CANNON.Vec3(x,.5,z), sleepSpeedLimit:.35 });
  b.allowSleep=true; b.sleep(); world.addBody(b);
  props.push({ mesh:m, body:b, kind:'wood', scored:false, y0:.5 });
}

function clearField(){
  props.forEach(p=>{ propGroup.remove(p.mesh); world.removeBody(p.body);
    if(p.mesh.material&&p.mesh.material.dispose&&p.mesh.material!==MAT.stone) p.mesh.material.dispose?.(); });
  guards.forEach(g=>{ propGroup.remove(g.mesh); world.removeBody(g.body); });
  props=[]; guards=[];
}

function buildFort(seed){
  clearField();
  const Z=-34;
  const kind=seed%3;
  if(kind===0){
    const top=stoneTower(0,Z,4,7);
    timberRoof(0,Z,top,2.6);
    makeGuard(0, top+.05, Z, Math.PI);
    makeGuard(-4.6,0,Z+2.4, Math.PI*.9);
    makeGuard(4.4,0,Z+1.6, Math.PI*1.1);
    palisade(-8.4,Z+3.2,6,0); palisade(8.4,Z+3.2,6,0);
    barrel(-2.6,Z+3.4); barrel(2.9,Z+3.1); barrel(-3.3,Z+4.2);
  } else if(kind===1){
    const a=stoneTower(-6.2,Z,3,6), b=stoneTower(6.2,Z,3,6);
    timberRoof(-6.2,Z,a,2.0); timberRoof(6.2,Z,b,2.0);
    for(let i=0;i<5;i++) addBox(1.25,.62,1.0, -2.4+i*1.2, .32, Z, 22, MAT.stone,{kind:'stone'});
    for(let i=0;i<5;i++) addBox(1.25,.62,1.0, -2.4+i*1.2, .96, Z, 22, MAT.stone,{kind:'stone'});
    addBox(6.6,.3,1.1, 0, 1.44, Z, 14, MAT.beam, {kind:'wood'});
    makeGuard(-6.2,a+.05,Z,Math.PI); makeGuard(6.2,b+.05,Z,Math.PI);
    makeGuard(0,1.6,Z,Math.PI);
    makeGuard(-9.5,0,Z+3, Math.PI); makeGuard(9.2,0,Z+2.6, Math.PI);
    barrel(0,Z+3.6); barrel(-4,Z+4.1);
  } else {
    const top=stoneTower(0,Z,5,5,1.25,.66,1.4);
    timberRoof(0,Z,top,3.2);
    const l=stoneTower(-7.6,Z-1.5,2,4), r=stoneTower(7.6,Z-1.5,2,4);
    makeGuard(0,top+.05,Z,Math.PI);
    makeGuard(-7.6,l+.05,Z-1.5,Math.PI); makeGuard(7.6,r+.05,Z-1.5,Math.PI);
    makeGuard(-3.2,0,Z+3.2,Math.PI*.95); makeGuard(3.6,0,Z+3.0,Math.PI*1.05);
    makeGuard(0,0,Z+4.6,Math.PI);
    palisade(0,Z+5.6,9,0);
    barrel(-5.4,Z+3.2); barrel(5.6,Z+3.4);
  }
  debrisBudget=0;
}

/* ================= CATAPULT (foreground rig) ================= */
const cata = new THREE.Group();
rig.add(cata);
let slingPouch, slingRope, armPivot;

function buildCatapult(){
  const frameMat = new THREE.MeshLambertMaterial({ color:0x9a6f42, map:TEX.wood });
  // A-frame legs
  for(const s of [-1,1]){
    const leg=new THREE.Mesh(boxGeo, frameMat);
    leg.scale.set(.22,2.5,.22); leg.position.set(s*1.15,-.55,0);
    leg.rotation.z=s*.14; cata.add(leg);
    const foot=new THREE.Mesh(boxGeo, frameMat);
    foot.scale.set(.3,.22,1.5); foot.position.set(s*1.3,-1.75,0); cata.add(foot);
  }
  const beam=new THREE.Mesh(boxGeo, frameMat);
  beam.scale.set(2.9,.26,.3); beam.position.set(0,.34,0); cata.add(beam);
  for(const s of [-1,1]){
    const band=new THREE.Mesh(boxGeo, MAT.iron);
    band.scale.set(.16,.34,.36); band.position.set(s*.95,.34,0); cata.add(band);
    const rivet=new THREE.Mesh(new THREE.SphereGeometry(.055,6,5), MAT.iron);
    rivet.position.set(s*.95,.42,.19); cata.add(rivet);
  }
  // rope binding
  const rope=new THREE.Mesh(new THREE.CylinderGeometry(.13,.13,.5,8),
    new THREE.MeshLambertMaterial({ color:0xe8dcc0 }));
  rope.position.set(0,.1,0); cata.add(rope);
  slingRope=rope;
  // leather pouch holding the stone
  armPivot=new THREE.Object3D(); armPivot.position.set(0,.34,0); cata.add(armPivot);
  slingPouch=new THREE.Group(); slingPouch.position.y=.42; armPivot.add(slingPouch);
  // leather cradle
  const hide=new THREE.MeshLambertMaterial({ color:0x6b4a2c, side:THREE.DoubleSide });
  const cradle=new THREE.Mesh(new THREE.SphereGeometry(.46,16,10,0,Math.PI*2,Math.PI*.42,Math.PI*.58), hide);
  cradle.position.y=-.04; slingPouch.add(cradle);
  // the stone itself
  const sg=new THREE.IcosahedronGeometry(.4,1), sp=sg.attributes.position;
  for(let i=0;i<sp.count;i++) sp.setXYZ(i, sp.getX(i)*rnd(.88,1.12), sp.getY(i)*rnd(.88,1.12), sp.getZ(i)*rnd(.88,1.12));
  sg.computeVertexNormals();
  const stone=new THREE.Mesh(sg, new THREE.MeshLambertMaterial({ color:0xa9a396, flatShading:true }));
  stone.position.y=.1; slingPouch.add(stone);
  // rope strands running back to the frame
  const ropeMat=new THREE.MeshLambertMaterial({ color:0xd8c9a6 });
  for(const s2 of [-1,1]){
    const r2=new THREE.Mesh(new THREE.CylinderGeometry(.035,.035,.9,5), ropeMat);
    r2.position.set(s2*.34,.1,-.05); r2.rotation.z=s2*.32; slingPouch.add(r2);
  }
  slingPouch.traverse(o=>{ if(o.isMesh) o.castShadow=true; });
  cata.traverse(o=>{ if(o.isMesh) o.castShadow=true; });
  cata.position.set(0,1.35,-2.6);
}

/* ================= AMMO ================= */
const AMMO={
  boulder:{ label:'BOLOVAN', r:.78, mass:150, speed:41, count:1, spread:0, color:0xa9a396 },
  pebbles:{ label:'PIETRIȘ', r:.3, mass:22, speed:46, count:7, spread:.055, color:0x8f8a80 }
};
let ammoKind='boulder';
let shots=[], shotsLeft=6;

function fireShot(pw){
  const A=AMMO[ammoKind];
  const dir=new THREE.Vector3(0,0,-1)
    .applyAxisAngle(new THREE.Vector3(1,0,0), pitch)
    .applyAxisAngle(new THREE.Vector3(0,1,0), rig.rotation.y);
  const origin=new THREE.Vector3(0,2.1,-2.6).applyAxisAngle(new THREE.Vector3(0,1,0), rig.rotation.y);
  const v=A.speed*(.42+pw*.58);
  for(let i=0;i<A.count;i++){
    const d=dir.clone();
    if(A.spread) d.add(new THREE.Vector3(rnd(-1,1),rnd(-1,1),rnd(-1,1)).multiplyScalar(A.spread)).normalize();
    const geo=new THREE.IcosahedronGeometry(A.r, A.r>.5?1:0);
    const p=geo.attributes.position;
    for(let k=0;k<p.count;k++) p.setXYZ(k,p.getX(k)*rnd(.86,1.14),p.getY(k)*rnd(.86,1.14),p.getZ(k)*rnd(.86,1.14));
    geo.computeVertexNormals();
    const mesh=new THREE.Mesh(geo, new THREE.MeshLambertMaterial({ color:A.color, flatShading:true }));
    mesh.castShadow=true; scene.add(mesh);
    const body=new CANNON.Body({ mass:A.mass, material:matProp,
      shape:new CANNON.Sphere(A.r), position:new CANNON.Vec3(origin.x,origin.y,origin.z) });
    body.linearDamping=.005;
    body.velocity.set(d.x*v, d.y*v+2.2, d.z*v);
    body.angularVelocity.set(rnd(-4,4),rnd(-4,4),rnd(-4,4));
    world.addBody(body);
    shots.push({ mesh, body, life:0 });
  }
  shotsLeft--; hud.shots.textContent=shotsLeft;
  state='fly'; flyT=0; chase=shots[0];
  recoil=1; power=0; powerDir=1;
}

/* ================= AIM / TENSION INPUT ================= */
let pitch=.42, yaw=0, charging=false, power=0, powerDir=1, recoil=0;
let dragId=null, lastX=0, lastY=0, moved=0;

function pointerDown(e){
  if(state!=='aim') return;
  dragId=e.pointerId; lastX=e.clientX; lastY=e.clientY; moved=0;
  charging=true; power=0; powerDir=1;
  canvas.setPointerCapture?.(e.pointerId);
}
function pointerMove(e){
  if(dragId!==e.pointerId) return;
  const dx=e.clientX-lastX, dy=e.clientY-lastY;
  lastX=e.clientX; lastY=e.clientY; moved+=Math.abs(dx)+Math.abs(dy);
  yaw   -= dx*.0022;
  pitch -= dy*.0016;
  yaw=Math.max(-.55,Math.min(.55,yaw));
  pitch=Math.max(.08,Math.min(.92,pitch));
}
function pointerUp(e){
  if(dragId!==e.pointerId) return;
  dragId=null;
  if(charging && state==='aim'){ charging=false; if(power>.06) fireShot(power); else power=0; }
}
canvas.addEventListener('pointerdown',pointerDown);
canvas.addEventListener('pointermove',pointerMove);
canvas.addEventListener('pointerup',pointerUp);
canvas.addEventListener('pointercancel',pointerUp);
canvas.addEventListener('contextmenu',e=>e.preventDefault());

/* ================= HUD ================= */
const hud={
  bar:document.getElementById('tension'),
  fill:document.getElementById('tensionFill'),
  sweet:document.getElementById('sweet'),
  gold:document.getElementById('gold'),
  shots:document.getElementById('shots'),
  ammo:document.getElementById('ammoName'),
  biome:document.getElementById('biome'),
  banner:document.getElementById('banner'),
  bTitle:document.getElementById('bTitle'),
  bText:document.getElementById('bText'),
  bBtn:document.getElementById('bBtn'),
  score:document.getElementById('score')
};
let gold=0, score=0, level=0, state='aim', flyT=0, chase=null, settle=0;
const SAVE='catapult3d.v1';
function load(){ try{ const d=JSON.parse(localStorage.getItem(SAVE)||'{}');
  gold=d.gold||0; level=d.level||0; }catch(e){} }
function save(){ try{ localStorage.setItem(SAVE,JSON.stringify({gold,level})); }catch(e){} }

function popText(worldPos, txt, cls){
  const el=document.createElement('div');
  el.className='pop '+(cls||''); el.textContent=txt;
  document.getElementById('pops').appendChild(el);
  el.dataset.x=worldPos.x; el.dataset.y=worldPos.y; el.dataset.z=worldPos.z;
  el.dataset.t='0';
  setTimeout(()=>el.remove(), 1400);
}

/* ================= SCORING ================= */
const tmpV=new THREE.Vector3();
function checkTargets(){
  for(const g of guards){
    if(g.dead) continue;
    const up=new CANNON.Vec3(0,1,0); const local=new CANNON.Vec3();
    g.body.quaternion.vmult(up, local);
    const toppled = local.y<.55 || g.body.position.y<g.y0-1.2;
    const speed=g.body.velocity.length();
    if(toppled || speed>7){
      g.dead=true; score+=500; gold+=100;
      hud.score.textContent=score; hud.gold.textContent=gold;
      tmpV.set(g.body.position.x,g.body.position.y+1.4,g.body.position.z);
      popText(tmpV,'+100','gold');
      g.mesh.traverse(o=>{ if(o.isMesh&&o.material.color) o.material=o.material.clone(); });
      g.mesh.traverse(o=>{ if(o.isMesh&&o.material.color) o.material.color.multiplyScalar(.45); });
    }
  }
  for(const p of props){
    if(p.scored) continue;
    const moved=Math.abs(p.body.position.y-p.y0)>.8 || p.body.velocity.length()>4.5;
    if(moved){ p.scored=true; score+=p.kind==='stone'?40:25; gold+=p.kind==='stone'?8:5;
      hud.score.textContent=score; hud.gold.textContent=gold; }
  }
}
function allDown(){ return guards.length>0 && guards.every(g=>g.dead); }

function nextLevel(){
  level++; save(); startLevel();
}
function startLevel(){
  const keys=Object.keys(BIOMES);
  const B=BIOMES[keys[level%keys.length]];
  applyBiome(B);
  hud.biome.textContent=B.name;
  buildFort(level);
  shotsLeft=6+Math.min(3,(level/3)|0); hud.shots.textContent=shotsLeft;
  score=0; hud.score.textContent=0; hud.gold.textContent=gold;
  yaw=0; pitch=.42; power=0; state='aim';
  rig.rotation.y=0;
  shots.forEach(s=>{ scene.remove(s.mesh); world.removeBody(s.body); }); shots=[];
  hud.banner.classList.remove('show');
}
function endLevel(won){
  state='done';
  hud.bTitle.textContent = won?'CETATE DĂRÂMATĂ':'ZIDURILE AU ȚINUT';
  hud.bText.textContent = won
    ? 'Scor '+score+' · ai strâns '+gold+' aur.'
    : 'Ai rămas fără proiectile. Încearcă altă traiectorie.';
  hud.bBtn.textContent = won?'ASEDIUL URMĂTOR':'DIN NOU';
  hud.banner.classList.add('show');
  save();
}
hud.bBtn.addEventListener('click',()=>{
  if(hud.bTitle.textContent==='CETATE DĂRÂMATĂ') nextLevel(); else startLevel();
});
document.getElementById('ammoBtn').addEventListener('click',()=>{
  ammoKind = ammoKind==='boulder'?'pebbles':'boulder';
  hud.ammo.textContent=AMMO[ammoKind].label;
});

/* ================= LOOP ================= */
let last=performance.now(), acc=0;
const FIXED=1/60;
const camBase=new THREE.Vector3(0,3.0,4.6);
const camLook=new THREE.Vector3(0,2.2,-20);
const camPos=camBase.clone(), camTgt=camLook.clone();

function resize(){
  const w=innerWidth, h=innerHeight;
  renderer.setSize(w,h,false);
  camera.aspect=w/h; camera.updateProjectionMatrix();
}
addEventListener('resize',resize);

function updatePops(){
  const el=document.getElementById('pops');
  for(const c of el.children){
    const t=parseFloat(c.dataset.t)+1; c.dataset.t=t;
    tmpV.set(+c.dataset.x, +c.dataset.y + t*.02, +c.dataset.z);
    tmpV.project(camera);
    if(tmpV.z>1){ c.style.display='none'; continue; }
    c.style.display='block';
    c.style.left=((tmpV.x*.5+.5)*innerWidth)+'px';
    c.style.top =((-tmpV.y*.5+.5)*innerHeight)+'px';
    c.style.opacity=Math.max(0,1-t/70);
  }
}

function step(dt){
  // tension: rises, then swings back - release at the right moment
  if(charging){
    power+=powerDir*dt*.85;
    if(power>=1){ power=1; powerDir=-1; }
    else if(power<=0 && powerDir<0){ power=0; powerDir=1; }
  }
  hud.fill.style.width=(power*100)+'%';
  hud.fill.classList.toggle('hot', power>.82);

  recoil*=.86;
  cata.position.z=-2.6+recoil*.5;
  cata.rotation.x=-recoil*.16;
  if(armPivot) armPivot.rotation.x = -power*.5 + recoil*.5;
  if(slingPouch) slingPouch.visible = state==='aim';

  world.step(FIXED, dt, 3);

  for(const p of props){
    p.mesh.position.copy(p.body.position);
    p.mesh.quaternion.copy(p.body.quaternion);
  }
  for(const g of guards){
    g.mesh.position.set(g.body.position.x, g.body.position.y-.95, g.body.position.z);
    g.mesh.quaternion.copy(g.body.quaternion);
  }
  for(let i=shots.length-1;i>=0;i--){
    const s=shots[i];
    s.mesh.position.copy(s.body.position);
    s.mesh.quaternion.copy(s.body.quaternion);
    s.life+=dt;
    if(s.body.position.y<-30 || s.life>14){
      scene.remove(s.mesh); world.removeBody(s.body); shots.splice(i,1);
      if(chase===s) chase=null;
    }
  }
  checkTargets();

  for(const c of clouds.children) c.rotation.y+=c.userData.spin*dt;

  // flow
  if(state==='fly'){
    flyT+=dt;
    const moving=shots.some(s=>s.body.velocity.length()>2.5);
    if((flyT>1.2 && !moving) || flyT>7){ state='settle'; settle=0; }
  } else if(state==='settle'){
    settle+=dt;
    if(allDown()){ endLevel(true); }
    else if(settle>1.4){
      shots.forEach(s=>{ scene.remove(s.mesh); world.removeBody(s.body); }); shots=[];
      chase=null;
      if(shotsLeft<=0) endLevel(false); else state='aim';
    }
  } else if(state==='aim'){
    if(allDown()) endLevel(true);
  }
}

function render(dt){
  rig.rotation.y=yaw;
  const q=new THREE.Quaternion().setFromAxisAngle(new THREE.Vector3(0,1,0), yaw);
  let tp, tl, k=3.2;
  if(chase && (state==='fly'||state==='settle')){
    const b=chase.body.position, v=chase.body.velocity;
    let dx=v.x, dz=v.z, l=Math.hypot(dx,dz);
    if(l<1){ dx=-Math.sin(yaw); dz=-Math.cos(yaw); l=1; }
    dx/=l; dz/=l;
    tp=new THREE.Vector3(b.x-dx*17, Math.max(b.y+7.5, 4.5), b.z-dz*17);
    tl=new THREE.Vector3(b.x+dx*5, b.y+1.2, b.z+dz*5);
    k=state==='settle'?1.6:3.6;
  } else {
    tp=camBase.clone().applyQuaternion(q);
    tp.y=camBase.y+pitch*1.7;
    tl=new THREE.Vector3(0, 1.6+pitch*9, -22).applyQuaternion(q);
  }
  camPos.lerp(tp, Math.min(1,dt*k));
  camTgt.lerp(tl, Math.min(1,dt*(k+.6)));
  camera.position.copy(camPos);
  camera.lookAt(camTgt);
  sky.position.copy(camera.position);
  updatePops();
  renderer.render(scene,camera);
}

function loop(now){
  requestAnimationFrame(loop);
  let dt=Math.min(.05,(now-last)/1000); last=now;
  acc+=dt;
  let guard=0;
  while(acc>=FIXED && guard++<4){ step(FIXED); acc-=FIXED; }
  render(dt);
}

/* ================= BOOT ================= */
buildSky(); buildLights(); buildCatapult();
load(); resize(); startLevel();
hud.ammo.textContent=AMMO[ammoKind].label;
requestAnimationFrame(loop);
