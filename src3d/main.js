import { ACESFilmicToneMapping, AmbientLight, BackSide, BoxGeometry, BufferAttribute, BufferGeometry, CanvasTexture, Color, ConeGeometry, CylinderGeometry, DirectionalLight, DoubleSide, Float32BufferAttribute, Fog, Group, HemisphereLight, IcosahedronGeometry, Mesh, MeshBasicMaterial, MeshLambertMaterial, MeshPhongMaterial, NearestFilter, Object3D, PCFShadowMap, PCFSoftShadowMap, PerspectiveCamera, PlaneGeometry, Points, PointsMaterial, Quaternion, RepeatWrapping, RingGeometry, SRGBColorSpace, Scene, ShaderMaterial, SphereGeometry, Vector3, WebGLRenderer } from 'three';
const THREE = { ACESFilmicToneMapping, AmbientLight, BackSide, BoxGeometry, BufferAttribute, BufferGeometry, CanvasTexture, Color, ConeGeometry, CylinderGeometry, DirectionalLight, DoubleSide, Float32BufferAttribute, Fog, Group, HemisphereLight, IcosahedronGeometry, Mesh, MeshBasicMaterial, MeshLambertMaterial, MeshPhongMaterial, NearestFilter, Object3D, PCFShadowMap, PCFSoftShadowMap, PerspectiveCamera, PlaneGeometry, Points, PointsMaterial, Quaternion, RepeatWrapping, RingGeometry, SRGBColorSpace, Scene, ShaderMaterial, SphereGeometry, Vector3, WebGLRenderer };
import * as CANNON from 'cannon-es';

/* ================= BIOMES ================= */
const BIOMES = {
  dune: { name:'DUNELE DE ARAMĂ',
    skyTop:0x4E8FCB, skyMid:0x9DC4E4, skyBot:0xF2DCB4, fog:0xE0C098, fogNear:70, fogFar:260,
    ground:0xC49A66, groundEdge:0xA87F4E, rock:0x8A7154, veg:0x7E7438, vegKind:'palm',
    sun:0xFFE0AE, sunI:3.1, amb:0x7FA6CE, ambI:.20, hemi:0xFFD9A0 },
  frost:{ name:'CREASTA ÎNGHEȚATĂ',
    skyTop:0x2A6FB8, skyMid:0x8FC4E8, skyBot:0xE2F1FA, fog:0xC8E2F2, fogNear:60, fogFar:240,
    ground:0xCADCEC, groundEdge:0x93B0CC, rock:0x74889C, veg:0x5E6B52, vegKind:'dead',
    sun:0xFFF6E6, sunI:2.7, amb:0x8FB6DE, ambI:.28, hemi:0xC4E0FA },
  night:{ name:'CÂMPIA DE MIEZ DE NOAPTE',
    skyTop:0x0A1738, skyMid:0x1E3A66, skyBot:0x4E7098, fog:0x22385A, fogNear:55, fogFar:230,
    ground:0x2E3D52, groundEdge:0x1D2838, rock:0x40506A, veg:0x243A2A, vegKind:'pine',
    sun:0xAFC8FF, sunI:1.9, amb:0x36507A, ambI:.5, hemi:0x5A76A4, moon:true }
};

/* ================= SETUP ================= */
const canvas = document.getElementById('gl');
const renderer = new THREE.WebGLRenderer({ canvas, antialias:true, powerPreference:'high-performance' });
const SMALL = Math.min(innerWidth, innerHeight) < 560 || /Mobi|Android|iPhone|iPad/i.test(navigator.userAgent);
renderer.setPixelRatio(Math.min(devicePixelRatio||1, SMALL?1.5:2));
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = SMALL ? THREE.PCFShadowMap : THREE.PCFSoftShadowMap;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = .92;

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
world.addContactMaterial(new CANNON.ContactMaterial(matProp, matProp, { friction:.5, restitution:.04 }));
const groundBody = new CANNON.Body({ mass:0, material:matGround, shape:new CANNON.Plane() });
groundBody.quaternion.setFromEuler(-Math.PI/2, 0, 0);
world.addBody(groundBody);

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
const surf=(color,map,shine,spec)=>new THREE.MeshPhongMaterial({
  color, map, shininess:shine||6, specular:spec||0x1a1a18, reflectivity:0 });
const MAT = {
  stone: surf(0xcfcabd, TEX.stone, 5,  0x161514),
  wood : surf(0xc99a5e, TEX.wood , 9,  0x241a10),
  beam : surf(0xa87a45, TEX.wood , 8,  0x201810),
  crate: surf(0xb98a52, TEX.crate, 10, 0x241a10),
  iron : surf(0x5b6472, null, 42, 0x8a94a4),
  cloth: surf(0x9d2f38, null, 3,  0x120608)
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
const TSEG=176, TSIZE=460;
let baseY=null, digY=null, terrainGeo=null, terrainCol=null, groundTone=null, digTone=null;
function terrainBase(x,z){
  // flat where the siege happens, rolling further out
  const edge=Math.max(Math.abs(x)/58, Math.max(-(z+64), z-16)/42);
  const w=Math.min(1, Math.max(0, (edge-1)/.85));
  const s=w*w*(3-2*w);
  return (Math.sin(x*.031)*1.7 + Math.sin(z*.026+1.3)*2.1 + Math.sin((x+z)*.015)*2.6
        + Math.sin(x*.088+z*.05)*.5) * s;
}
function buildGround(B){
  if(groundMesh){ scene.remove(groundMesh); groundMesh.geometry.dispose(); groundMesh.material.dispose(); }
  const geo=new THREE.PlaneGeometry(TSIZE,TSIZE,TSEG,TSEG);
  geo.rotateX(-Math.PI/2);
  const pos=geo.attributes.position, n=pos.count;
  baseY=new Float32Array(n); digY=new Float32Array(n);
  const cols=new Float32Array(n*3);
  groundTone=new THREE.Color(B.ground); digTone=new THREE.Color(B.groundEdge).multiplyScalar(.72);
  const edgeTone=new THREE.Color(B.groundEdge);
  for(let i=0;i<n;i++){
    const x=pos.getX(i), z=pos.getZ(i);
    const h=terrainBase(x,z);
    baseY[i]=h; pos.setY(i,h);
    const d=Math.min(1,Math.hypot(x,z)/210);
    // patchy tone so it never reads as one flat colour
    const patch=(Math.sin(x*.21)*Math.sin(z*.17)*.5+.5)*.09 + (Math.sin(x*.63+z*.41)*.5+.5)*.05;
    const c=groundTone.clone().lerp(edgeTone, Math.pow(d,1.5)*.9).offsetHSL(0,0,patch-.06);
    cols[i*3]=c.r; cols[i*3+1]=c.g; cols[i*3+2]=c.b;
  }
  geo.setAttribute('color', new THREE.Float32BufferAttribute(cols,3));
  geo.computeVertexNormals();
  terrainGeo=geo; terrainCol=geo.attributes.color;
  groundMesh=new THREE.Mesh(geo, new THREE.MeshLambertMaterial({ vertexColors:true }));
  groundMesh.receiveShadow=true;
  scene.add(groundMesh);
}
/* impact craters: bowl plus a raised rim, with darkened, disturbed soil */
function digCrater(cx,cz,R,D){
  if(!terrainGeo) return;
  const pos=terrainGeo.attributes.position, n=pos.count, R2=R*1.55;
  for(let i=0;i<n;i++){
    const dx=pos.getX(i)-cx, dz=pos.getZ(i)-cz;
    const r=Math.hypot(dx,dz);
    if(r>R2) continue;
    let d;
    if(r<R) d=-D*Math.pow(Math.cos(r/R*Math.PI*.5), 1.4);
    else { const t=1-(r-R)/(R2-R); d=D*.3*t*t; }
    digY[i]=Math.max(-2.4, Math.min(1.0, digY[i]+d));
    pos.setY(i, baseY[i]+digY[i]);
    if(digY[i]<-.04){
      const k=Math.min(1,-digY[i]/1.1);
      const c=groundTone.clone().lerp(digTone, k);
      terrainCol.setXYZ(i, c.r, c.g, c.b);
    }
  }
  pos.needsUpdate=true; terrainCol.needsUpdate=true;
  terrainGeo.computeVertexNormals();
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
  hemiLight.color.set(B.hemi);
  hemiLight.groundColor.set(new THREE.Color(B.ground).multiplyScalar(.5));
  buildGround(B); dressScene(B); buildClouds();
  TH_DUST=new THREE.Color(B.ground).offsetHSL(0,0,-.05).getHex();
  clouds.visible = !B.moon || true;
}
function buildLights(){
  hemiLight=new THREE.HemisphereLight(0xffe9c4, 0x5a4a38, .42); scene.add(hemiLight);
  ambLight=new THREE.AmbientLight(0xc9dcf0, .6); scene.add(ambLight);
  sunLight=new THREE.DirectionalLight(0xfff0d0, 1.6);
  sunLight.position.set(30, 26, 22);
  sunLight.castShadow=true;
  sunLight.shadow.mapSize.set(SMALL?1024:2048, SMALL?1024:2048);
  const s=sunLight.shadow.camera;
  s.left=-34; s.right=34; s.top=36; s.bottom=-24; s.near=1; s.far=140;
  sunLight.shadow.bias=-0.0009; sunLight.shadow.normalBias=.035;
  scene.add(sunLight); scene.add(sunLight.target);
  sunLight.target.position.set(0,0,-34);
}

/* ================= IMPACT PARTICLES ================= */
const PMAX=420;
let dustPts, dustPos, dustVel, dustLife, dustSize, dustHead=0;
function buildDust(){
  const c=document.createElement('canvas'); c.width=c.height=64;
  const g=c.getContext('2d');
  const rg=g.createRadialGradient(32,32,0,32,32,32);
  rg.addColorStop(0,'rgba(255,255,255,.95)'); rg.addColorStop(.45,'rgba(255,255,255,.35)');
  rg.addColorStop(1,'rgba(255,255,255,0)');
  g.fillStyle=rg; g.fillRect(0,0,64,64);
  const tex=new THREE.CanvasTexture(c);
  const geo=new THREE.BufferGeometry();
  dustPos=new Float32Array(PMAX*3); dustVel=new Float32Array(PMAX*3);
  dustLife=new Float32Array(PMAX); dustSize=new Float32Array(PMAX);
  const cols=new Float32Array(PMAX*3), sz=new Float32Array(PMAX);
  for(let i=0;i<PMAX;i++) dustPos[i*3+1]=-999;
  geo.setAttribute('position', new THREE.BufferAttribute(dustPos,3));
  geo.setAttribute('color', new THREE.BufferAttribute(cols,3));
  geo.setAttribute('psize', new THREE.BufferAttribute(sz,1));
  const mat=new THREE.PointsMaterial({ size:1, map:tex, transparent:true, depthWrite:false,
    vertexColors:true, sizeAttenuation:true, opacity:.92 });
  mat.onBeforeCompile=sh=>{
    sh.vertexShader='attribute float psize;\n'+sh.vertexShader
      .replace('gl_PointSize = size;','gl_PointSize = size * psize;');
  };
  dustPts=new THREE.Points(geo, mat); dustPts.frustumCulled=false;
  scene.add(dustPts);
}
function puff(x,y,z, n, spread, color, up){
  if(!dustPts) return;
  const col=dustPts.geometry.attributes.color, sz=dustPts.geometry.attributes.psize;
  const c=new THREE.Color(color||0xc8b48c);
  for(let k=0;k<n;k++){
    const i=dustHead=(dustHead+1)%PMAX;
    dustPos[i*3]=x+rnd(-spread,spread);
    dustPos[i*3+1]=y+rnd(0,spread*.6);
    dustPos[i*3+2]=z+rnd(-spread,spread);
    dustVel[i*3]=rnd(-1,1)*spread*.9;
    dustVel[i*3+1]=rnd(.4,1)*(up||3.2);
    dustVel[i*3+2]=rnd(-1,1)*spread*.9;
    dustLife[i]=rnd(.7,1.5); dustSize[i]=rnd(.8,2.6);
    const cc=c.clone().offsetHSL(0,0,rnd(-.06,.06));
    col.setXYZ(i,cc.r,cc.g,cc.b); sz.setX(i,dustSize[i]);
  }
  col.needsUpdate=true; sz.needsUpdate=true;
}
function stepDust(dt){
  if(!dustPts) return;
  const pos=dustPts.geometry.attributes.position, sz=dustPts.geometry.attributes.psize;
  let any=false;
  for(let i=0;i<PMAX;i++){
    if(dustLife[i]<=0) continue;
    any=true;
    dustLife[i]-=dt*.85;
    dustVel[i*3+1]-=dt*3.4;
    dustVel[i*3]*=.965; dustVel[i*3+2]*=.965;
    dustPos[i*3]+=dustVel[i*3]*dt;
    dustPos[i*3+1]+=dustVel[i*3+1]*dt;
    dustPos[i*3+2]+=dustVel[i*3+2]*dt;
    if(dustPos[i*3+1]<.1){ dustPos[i*3+1]=.1; dustVel[i*3+1]*=-.2; }
    sz.setX(i, Math.max(0, dustSize[i]*Math.min(1,dustLife[i]*1.4)*(1+(1.4-dustLife[i])*.5)));
    if(dustLife[i]<=0){ dustPos[i*3+1]=-999; sz.setX(i,0); }
  }
  if(any){ pos.needsUpdate=true; sz.needsUpdate=true; }
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
  const p={ mesh, body, kind:opts.kind||'stone', scored:false, y0:y, broken:false, frag:false };
  props.push(p); armFracture(p); return p;
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

function wakeAround(x,y,z,R){
  const R2=R*R;
  for(const p of props){ const d=p.body.position;
    const dx=d.x-x, dy=d.y-y, dz=d.z-z;
    if(dx*dx+dy*dy+dz*dz<R2) p.body.wakeUp(); }
  for(const g of guards){ if(g.dead) continue; const d=g.body.position;
    const dx=d.x-x, dy=d.y-y, dz=d.z-z;
    if(dx*dx+dy*dy+dz*dz<R2) g.body.wakeUp(); }
}

/* --- stone shatters into rubble under a hard hit --- */
let fragBudget=90;
function fracture(p, impulseDir){
  if(p.broken) return; p.broken=true;
  const pos=p.body.position, vel=p.body.velocity;
  const w=p.mesh.scale.x, h=p.mesh.scale.y, d=p.mesh.scale.z;
  propGroup.remove(p.mesh); world.removeBody(p.body);
  const idx=props.indexOf(p); if(idx>=0) props.splice(idx,1);
  if(!p.scored){
    p.scored=true;
    score+=p.kind==='stone'?70:45; gold+=p.kind==='stone'?14:9;
    hud.score.textContent=score; hud.gold.textContent=gold;
  }
  puff(pos.x,pos.y,pos.z, 9, Math.max(w,h)*.7, p.kind==='stone'?0xc4bdaf:0x9a6f42, 2.6);
  wakeAround(pos.x,pos.y,pos.z, 7);
  if(fragBudget<=0) return;
  // split the block on a grid so the rubble actually fits where the block was
  const nx=2, ny=h>1?2:1, nz=1;
  const cells=nx*ny*nz;
  if(fragBudget<cells) return;
  fragBudget-=cells;
  const mat=p.kind==='stone'?MAT.stone:MAT.wood;
  const q=p.body.quaternion;
  for(let ix=0;ix<nx;ix++) for(let iy=0;iy<ny;iy++) for(let iz=0;iz<nz;iz++){
    const fw=w/nx*.94, fh=h/ny*.94, fd=d/nz*.94;
    const lx=(ix+.5)/nx*w-w/2, ly=(iy+.5)/ny*h-h/2, lz=(iz+.5)/nz*d-d/2;
    const off=new CANNON.Vec3(lx,ly,lz); const gp=new CANNON.Vec3();
    q.vmult(off,gp);
    const m=new THREE.Mesh(boxGeo, mat);
    m.scale.set(fw,fh,fd); m.castShadow=true; m.receiveShadow=true; propGroup.add(m);
    const body=new CANNON.Body({ mass:Math.max(3,10*fw*fh*fd), material:matProp,
      shape:new CANNON.Box(new CANNON.Vec3(fw/2,fh/2,fd/2)),
      position:new CANNON.Vec3(pos.x+gp.x, pos.y+gp.y, pos.z+gp.z),
      quaternion:new CANNON.Quaternion(q.x,q.y,q.z,q.w),
      sleepSpeedLimit:.5, sleepTimeLimit:.4 });
    const sp=(impulseDir||1);
    body.velocity.set(vel.x*.7+lx*2.2*sp+rnd(-2,2), vel.y*.55+rnd(.5,3.5), vel.z*.7+lz*2.2*sp+rnd(-2,2));
    body.angularVelocity.set(rnd(-7,7),rnd(-7,7),rnd(-7,7));
    body.allowSleep=true; world.addBody(body);
    props.push({ mesh:m, body, kind:p.kind, scored:true, y0:pos.y+gp.y, frag:true, broken:true });
  }
}
function armFracture(p){
  p.body.addEventListener('collide', e=>{
    if(p.broken||p.frag) return;
    let v=0;
    try{ v=Math.abs(e.contact.getImpactVelocityAlongNormal()); }catch(_){ return; }
    const lim = p.kind==='stone' ? 13 : 10;
    if(v>8) wakeAround(p.body.position.x,p.body.position.y,p.body.position.z,6);
    if(v>lim) fracture(p);
  });
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
  const g=new THREE.Group();
  const body=new THREE.Mesh(new THREE.CylinderGeometry(.44,.44,1.0,12), MAT.crate);
  g.add(body);
  const hoopMat=new THREE.MeshLambertMaterial({ color:0x3a3f49 });
  for(const y of [-.3,.3]){
    const hp=new THREE.Mesh(new THREE.CylinderGeometry(.46,.46,.1,12), hoopMat);
    hp.position.y=y; g.add(hp);
  }
  const cap=new THREE.Mesh(new THREE.CylinderGeometry(.3,.3,.14,10),
    new THREE.MeshLambertMaterial({ color:0xE8B04B }));
  cap.position.y=.54; g.add(cap);
  g.traverse(o=>{ if(o.isMesh){ o.castShadow=true; o.receiveShadow=true; } });
  propGroup.add(g);
  const b=new CANNON.Body({ mass:14, material:matProp,
    shape:new CANNON.Cylinder(.44,.44,1.0,12),
    position:new CANNON.Vec3(x,.5,z), sleepSpeedLimit:.35 });
  b.allowSleep=true; b.sleep(); world.addBody(b);
  const p={ mesh:g, body:b, kind:'powder', scored:false, y0:.5, broken:false, frag:false };
  props.push(p);
  b.addEventListener('collide', e=>{
    if(p.broken) return;
    let v=0; try{ v=Math.abs(e.contact.getImpactVelocityAlongNormal()); }catch(_){ return; }
    if(v>7) detonate(p);
  });
  return p;
}
/* powder kegs go up, throwing everything nearby and shattering stone */
function detonate(p){
  if(p.broken) return; p.broken=true;
  const c=p.body.position.clone();
  propGroup.remove(p.mesh); world.removeBody(p.body);
  const idx=props.indexOf(p); if(idx>=0) props.splice(idx,1);
  if(!p.scored){ p.scored=true; score+=150; gold+=30;
    hud.score.textContent=score; hud.gold.textContent=gold; }
  puff(c.x,c.y,c.z, 34, 1.6, 0xFFC46A, 8.5);
  puff(c.x,c.y,c.z, 18, 2.4, 0x6b5a4a, 5.0);
  shake=Math.max(shake,.95);
  tmpV.set(c.x,c.y+1.6,c.z); popText(tmpV,'BUM!','gold');
  const R=7.5;
  wakeAround(c.x,c.y,c.z,R+3);
  for(const o of props.slice()){
    const d=o.body.position, dx=d.x-c.x, dy=d.y-c.y, dz=d.z-c.z;
    const r=Math.hypot(dx,dy,dz);
    if(r>R) continue;
    if(o.kind==='powder'){ setTimeout(()=>detonate(o), 90+Math.random()*160); continue; }
    const f=(1-r/R);
    if(!o.frag && f>.45 && o.kind==='stone' && fragBudget>0){ fracture(o, 1.6); continue; }
    o.body.wakeUp();
    const k=f*260/Math.max(1,o.body.mass);
    o.body.velocity.x+=dx/Math.max(.6,r)*k;
    o.body.velocity.y+=Math.abs(dy)/Math.max(.6,r)*k+f*7;
    o.body.velocity.z+=dz/Math.max(.6,r)*k;
  }
  for(const g of guards){
    if(g.dead) continue;
    const d=g.body.position, dx=d.x-c.x, dy=d.y-c.y, dz=d.z-c.z;
    const r=Math.hypot(dx,dy,dz);
    if(r>R) continue;
    const f=(1-r/R);
    g.body.wakeUp();
    g.body.velocity.x+=dx/Math.max(.6,r)*f*22;
    g.body.velocity.y+=f*13;
    g.body.velocity.z+=dz/Math.max(.6,r)*f*22;
    g.body.angularVelocity.set(rnd(-8,8),rnd(-8,8),rnd(-8,8));
  }
}

function clearField(){
  props.forEach(p=>{ propGroup.remove(p.mesh); world.removeBody(p.body);
    if(p.mesh.material&&p.mesh.material.dispose&&p.mesh.material!==MAT.stone) p.mesh.material.dispose?.(); });
  guards.forEach(g=>{ propGroup.remove(g.mesh); world.removeBody(g.body); });
  props=[]; guards=[];
}

const FORTS=[
 {name:'TURNUL DE STRAJĂ'},
 {name:'POARTA GEMENILOR'},
 {name:'DONJONUL'},
 {name:'ZIDUL LUNG'},
 {name:'CETATEA CU TURNURI'},
 {name:'CITADELA'}
];
function buildFort(seed){
  clearField();
  const Z=-34, kind=seed%FORTS.length, tier=Math.floor(seed/FORTS.length);
  const extra=Math.min(3,tier);            // garrison grows on later passes
  if(kind===0){
    const top=stoneTower(0,Z,4,6+extra);
    timberRoof(0,Z,top,2.6);
    makeGuard(0, top+.05, Z, Math.PI);
    makeGuard(-4.6,0,Z+2.4, Math.PI*.9);
    makeGuard(4.4,0,Z+1.6, Math.PI*1.1);
    palisade(-8.4,Z+3.2,6,0); palisade(8.4,Z+3.2,6,0);
    barrel(-2.6,Z+3.4); barrel(2.9,Z+3.1); barrel(-3.3,Z+4.2);
  } else if(kind===1){
    const a=stoneTower(-6.2,Z,3,6+extra), b=stoneTower(6.2,Z,3,6+extra);
    timberRoof(-6.2,Z,a,2.0); timberRoof(6.2,Z,b,2.0);
    for(let r=0;r<2;r++) for(let i=0;i<5;i++)
      addBox(1.25,.62,1.0, -2.4+i*1.2, .32+r*.64, Z, 22, MAT.stone,{kind:'stone'});
    addBox(6.6,.3,1.1, 0, 1.44, Z, 14, MAT.beam, {kind:'wood'});
    makeGuard(-6.2,a+.05,Z,Math.PI); makeGuard(6.2,b+.05,Z,Math.PI);
    makeGuard(0,1.6,Z,Math.PI);
    makeGuard(-9.5,0,Z+3, Math.PI); makeGuard(9.2,0,Z+2.6, Math.PI);
    barrel(0,Z+3.6); barrel(-4,Z+4.1);
  } else if(kind===2){
    const top=stoneTower(0,Z,5,5+extra,1.25,.66,1.4);
    timberRoof(0,Z,top,3.2);
    const l=stoneTower(-7.6,Z-1.5,2,4), r=stoneTower(7.6,Z-1.5,2,4);
    makeGuard(0,top+.05,Z,Math.PI);
    makeGuard(-7.6,l+.05,Z-1.5,Math.PI); makeGuard(7.6,r+.05,Z-1.5,Math.PI);
    makeGuard(-3.2,0,Z+3.2,Math.PI*.95); makeGuard(3.6,0,Z+3.0,Math.PI*1.05);
    makeGuard(0,0,Z+4.6,Math.PI);
    palisade(0,Z+5.6,9,0);
    barrel(-5.4,Z+3.2); barrel(5.6,Z+3.4);
  } else if(kind===3){
    // a long curtain wall with a gate and walkway
    for(let r=0;r<4+extra;r++)
      for(let i=0;i<11;i++){
        if(r<2 && i>=4 && i<=6) continue;          // gate opening
        addBox(1.25,.64,1.1, -6.25+i*1.25, .34+r*.64, Z, 22, MAT.stone,{kind:'stone'});
      }
    addBox(4.4,.34,1.3, 0, .34+2*.64, Z, 16, MAT.beam,{kind:'wood'});
    const wt=.34+(4+extra)*.64;
    for(const x of [-6.25,6.25]) makeGuard(x, wt, Z, Math.PI);
    makeGuard(0, wt, Z, Math.PI);
    makeGuard(-8.8,0,Z+2.6,Math.PI); makeGuard(8.6,0,Z+2.4,Math.PI);
    barrel(-2.2,Z+3.4); barrel(2.4,Z+3.6); barrel(0,Z+4.6);
  } else if(kind===4){
    const a=stoneTower(-8.5,Z-1,3,6+extra), b=stoneTower(8.5,Z-1,3,6+extra);
    const c=stoneTower(0,Z+1,4,4+extra);
    timberRoof(-8.5,Z-1,a,2.1); timberRoof(8.5,Z-1,b,2.1); timberRoof(0,Z+1,c,2.6);
    for(let r=0;r<3;r++) for(let i=0;i<4;i++){
      addBox(1.2,.62,1.0, -6.0+i*1.25, .32+r*.64, Z-1, 22, MAT.stone,{kind:'stone'});
      addBox(1.2,.62,1.0,  2.6+i*1.25, .32+r*.64, Z-1, 22, MAT.stone,{kind:'stone'});
    }
    makeGuard(-8.5,a+.05,Z-1,Math.PI); makeGuard(8.5,b+.05,Z-1,Math.PI);
    makeGuard(0,c+.05,Z+1,Math.PI);
    makeGuard(-4,0,Z+4,Math.PI); makeGuard(4.2,0,Z+3.6,Math.PI);
    palisade(-12,Z+4,7,0); palisade(12,Z+4,7,0);
    barrel(-6,Z+4.2); barrel(6.2,Z+4.4);
  } else {
    // citadel: keep on a raised stone platform, flanking towers, outer wall
    for(let r=0;r<2;r++) for(let i=0;i<8;i++)
      addBox(1.3,.66,3.2, -4.55+i*1.3, .34+r*.66, Z-1, 30, MAT.stone,{kind:'stone'});
    const keepBase=.34+2*.66;
    for(let r=0;r<5+extra;r++) for(let i=0;i<4;i++)
      addBox(1.25,.64,1.2, -1.9+i*1.25, keepBase+.34+r*.64, Z-1, 22, MAT.stone,{kind:'stone'});
    const kt=keepBase+.34+(5+extra)*.64;
    timberRoof(0,Z-1,kt-.3,2.8);
    const l=stoneTower(-9.5,Z,2,5), r2=stoneTower(9.5,Z,2,5);
    makeGuard(0,kt,Z-1,Math.PI);
    makeGuard(-9.5,l+.05,Z,Math.PI); makeGuard(9.5,r2+.05,Z,Math.PI);
    makeGuard(-5,keepBase,Z-1,Math.PI); makeGuard(5,keepBase,Z-1,Math.PI);
    makeGuard(0,0,Z+5,Math.PI);
    palisade(0,Z+6.4,13,0);
    barrel(-7,Z+3.6); barrel(7.2,Z+3.8); barrel(0,Z+3.2);
  }
  debrisBudget=0; fragBudget=90;
  return FORTS[kind].name;
}

/* ================= CATAPULT (foreground rig) ================= */
const cata = new THREE.Group();
rig.add(cata);
let slingPouch, slingRope, armPivot;

function buildCatapult(){
  const oak=new THREE.MeshLambertMaterial({ color:0x8f6236, map:TEX.wood });
  const dark=new THREE.MeshLambertMaterial({ color:0x5e421f, map:TEX.wood });
  const iron=MAT.iron;

  for(const sd of [-1,1]){
    const rail=new THREE.Mesh(boxGeo, dark);
    rail.scale.set(.26,.26,3.2); rail.position.set(sd*1.5,-.62,.5); cata.add(rail);
    const post=new THREE.Mesh(boxGeo, oak);
    post.scale.set(.24,1.5,.24); post.position.set(sd*1.5,.1,-.35);
    post.rotation.x=-.2; cata.add(post);
    const brace=new THREE.Mesh(boxGeo, oak);
    brace.scale.set(.19,1.5,.19); brace.position.set(sd*1.5,-.05,.9);
    brace.rotation.x=.55; cata.add(brace);
    const wheel=new THREE.Mesh(new THREE.CylinderGeometry(.46,.46,.2,12), dark);
    wheel.rotation.z=Math.PI/2; wheel.position.set(sd*1.62,-.9,1.5); cata.add(wheel);
    const hub=new THREE.Mesh(new THREE.CylinderGeometry(.12,.12,.26,8), iron);
    hub.rotation.z=Math.PI/2; hub.position.copy(wheel.position); cata.add(hub);
    for(let k=0;k<6;k++){
      const sp=new THREE.Mesh(boxGeo, oak);
      sp.scale.set(.07,.8,.07); sp.position.copy(wheel.position);
      sp.rotation.x=k*Math.PI/6; cata.add(sp);
    }
  }
  const beam=new THREE.Mesh(boxGeo, oak);
  beam.scale.set(3.4,.3,.34); beam.position.set(0,.62,-.3); cata.add(beam);
  for(const sd of [-1,1]){
    const band=new THREE.Mesh(boxGeo, iron);
    band.scale.set(.18,.4,.42); band.position.set(sd*1.2,.62,-.3); cata.add(band);
  }
  const pad=new THREE.Mesh(boxGeo, new THREE.MeshLambertMaterial({color:0x6b4a2c}));
  pad.scale.set(2.2,.16,.4); pad.position.set(0,.8,-.3); cata.add(pad);

  const skein=new THREE.Mesh(new THREE.CylinderGeometry(.34,.34,2.1,10),
    new THREE.MeshLambertMaterial({ color:0xd8c9a6 }));
  skein.rotation.z=Math.PI/2; skein.position.set(0,.55,-.1); cata.add(skein);
  for(const sd of [-1,1]){
    const cap=new THREE.Mesh(new THREE.CylinderGeometry(.4,.4,.22,10), iron);
    cap.rotation.z=Math.PI/2; cap.position.set(sd*1.1,.55,-.1); cata.add(cap);
  }

  armPivot=new THREE.Object3D(); armPivot.position.set(0,.55,-.1); cata.add(armPivot);
  const arm=new THREE.Mesh(boxGeo, oak);
  arm.scale.set(.3,.3,2.6); arm.position.set(0,0,1.3); armPivot.add(arm);
  const armIron=new THREE.Mesh(boxGeo, iron);
  armIron.scale.set(.38,.38,.22); armIron.position.set(0,0,2.4); armPivot.add(armIron);

  slingPouch=new THREE.Group(); slingPouch.position.set(0,.3,2.5); armPivot.add(slingPouch);
  const hide=new THREE.MeshLambertMaterial({ color:0x6b4a2c, side:THREE.DoubleSide });
  const cradle=new THREE.Mesh(new THREE.SphereGeometry(.5,16,10,0,Math.PI*2,Math.PI*.44,Math.PI*.56), hide);
  slingPouch.add(cradle);
  const sg=new THREE.IcosahedronGeometry(.42,1), sp2=sg.attributes.position;
  for(let i2=0;i2<sp2.count;i2++) sp2.setXYZ(i2, sp2.getX(i2)*rnd(.88,1.12), sp2.getY(i2)*rnd(.88,1.12), sp2.getZ(i2)*rnd(.88,1.12));
  sg.computeVertexNormals();
  const stone=new THREE.Mesh(sg, new THREE.MeshLambertMaterial({ color:0xa9a396, flatShading:true }));
  stone.position.y=.16; slingPouch.add(stone);

  cata.traverse(o=>{ if(o.isMesh){ o.castShadow=true; o.receiveShadow=true; } });
  cata.position.set(0,.85,-3.6);
}

/* ---- aiming aids: predicted arc and landing ring ---- */
const traj=new THREE.Group(); scene.add(traj);
const TDOTS=26, trajDots=[];
let landRing;
function buildAim(){
  const dotGeo=new THREE.SphereGeometry(.17,7,6);
  for(let i=0;i<TDOTS;i++){
    const m=new THREE.Mesh(dotGeo, new THREE.MeshBasicMaterial({
      color:0xFFE0A0, transparent:true, opacity:.9, depthWrite:false }));
    m.visible=false; traj.add(m); trajDots.push(m);
  }
  landRing=new THREE.Mesh(new THREE.RingGeometry(1.0,1.35,28),
    new THREE.MeshBasicMaterial({ color:0xFFC65A, transparent:true, opacity:.75,
      side:THREE.DoubleSide, depthWrite:false }));
  landRing.rotation.x=-Math.PI/2; landRing.visible=false; traj.add(landRing);
}
function updateAim(){
  if(state!=='aim'){ trajDots.forEach(d=>d.visible=false); if(landRing) landRing.visible=false; return; }
  const A=AMMO[ammoKind];
  const dir=new THREE.Vector3(0,0,-1)
    .applyAxisAngle(new THREE.Vector3(1,0,0), pitch)
    .applyAxisAngle(new THREE.Vector3(0,1,0), yaw);
  const v=A.speed*(.42+power*.58);
  const o=new THREE.Vector3(0,2.5,-2.6).applyAxisAngle(new THREE.Vector3(0,1,0), yaw);
  let px=o.x, py=o.y, pz=o.z;
  let vx=dir.x*v, vy=dir.y*v+2.2, vz=dir.z*v;
  const h=1/24;
  let idx=0, landed=false;
  for(let stp=0; stp<300 && idx<TDOTS; stp++){
    vy-=22*h; px+=vx*h; py+=vy*h; pz+=vz*h;
    if(py<=0){ landed=true;
      if(landRing){
        landRing.position.set(px,.07,pz); landRing.visible=true;
        const dr=camera.position.distanceTo(landRing.position);
        landRing.scale.setScalar(Math.max(.7, Math.min(2.6, dr*.022)));
      }
      break; }
    if(stp%4===0){
      const d=trajDots[idx++];
      d.position.set(px,py,pz); d.visible=true;
      const t=idx/TDOTS;
      d.material.opacity=.92*(1-t*.45);
      const dist=camera.position.distanceTo(d.position);
      d.scale.setScalar(Math.max(.5, Math.min(3.4, dist*.035)));
    }
  }
  for(let i=idx;i<TDOTS;i++) trajDots[i].visible=false;
  if(!landed&&landRing) landRing.visible=false;
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
  const origin=new THREE.Vector3(0,2.5,-2.6).applyAxisAngle(new THREE.Vector3(0,1,0), rig.rotation.y);
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
    shots.push({ mesh, body, life:0, r:A.r, hit:false });
  }
  shotsLeft--; hud.shots.textContent=shotsLeft;
  state='fly'; flyT=0; chase=shots[0];
  recoil=1; power=0; powerDir=1; armVel=-.55;
}

/* ================= AIM / TENSION INPUT ================= */
let pitch=.42, yaw=0, charging=false, power=0, powerDir=1, recoil=0;
let armAng=-.58, armVel=0, armTarget=-.58;
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
  yaw   -= dx*.0030;
  pitch -= dy*.0013;
  yaw=Math.max(-1.0,Math.min(1.0,yaw));
  pitch=Math.max(.10,Math.min(1.02,pitch));
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
  head:document.getElementById('tensionHead'),
  pct:document.getElementById('tensionPct'),
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
let gold=0, score=0, level=0, state='aim', flyT=0, chase=null, settle=0, shake=0;
let TH_DUST=0xc8b48c;
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
      hud.score.textContent=score; hud.gold.textContent=gold;
      puff(p.body.position.x,p.body.position.y,p.body.position.z, 5, .8,
           p.kind==='stone'?0xbdb6a8:0x9a6f42, 2.4); }
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
  const fortName=buildFort(level);
  hud.biome.textContent='ASEDIUL '+(level+1)+' · '+fortName;
  shotsLeft=6+Math.min(4,(level/2)|0); hud.shots.textContent=shotsLeft;
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
const camBase=new THREE.Vector3(.9,4.4,5.4);
const camLook=new THREE.Vector3(0,1.4,-26);
const camPos=camBase.clone(), camTgt=camLook.clone();

let portrait=false;
function resize(){
  const w=innerWidth, h=innerHeight;
  renderer.setSize(w,h,false);
  const a=w/h;
  camera.aspect=a;
  portrait = a<1;
  // portrait needs a taller field of view or the fort falls off the top
  camera.fov = a<.62 ? 74 : a<1 ? 64 : (a<1.5 ? 56 : 52);
  camera.updateProjectionMatrix();
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
  const pct=Math.round(power*100);
  hud.fill.style.width=pct+'%';
  hud.fill.classList.toggle('hot', power>.76);
  if(hud.head) hud.head.style.left='calc('+pct+'% - 1px)';
  if(hud.pct) hud.pct.textContent=pct+'%';

  recoil*=.86;
  cata.position.z=-3.6+recoil*.6;
  cata.rotation.x=-recoil*.1;
  // the arm cocks back with tension and whips forward on release
  armTarget = charging ? -.58+power*.82 : (state==='aim' ? -.58 : -2.25);
  armVel += (armTarget-armAng)*(state==='aim'?.24:.4);
  armVel *= .76; armAng += armVel;
  if(armAng<-2.4){ armAng=-2.4; armVel*=-.22; }
  if(armPivot) armPivot.rotation.x = armAng;
  if(slingPouch) slingPouch.visible = state==='aim';
  updateAim();

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
    if(!s.hit && s.body.position.y < s.r+.25){
      const sp=s.body.velocity.length();
      if(sp>6){
        s.hit=true;
        const pw=Math.min(1, sp/34);
        digCrater(s.body.position.x, s.body.position.z, s.r*(2.6+pw*2.4), s.r*(.75+pw*1.1));
        wakeAround(s.body.position.x, s.body.position.y, s.body.position.z, 9);
        puff(s.body.position.x, .3, s.body.position.z, 14+((pw*22)|0), s.r*2.2, TH_DUST, 4.5);
        shake=Math.max(shake, .3+pw*.5);
      }
    }
    if(s.body.position.y<-30 || s.life>14){
      scene.remove(s.mesh); world.removeBody(s.body); shots.splice(i,1);
      if(chase===s) chase=null;
    }
  }
  checkTargets();

  for(const c of clouds.children) c.rotation.y+=c.userData.spin*dt;
  stepDust(dt);
  shake*=.90;

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
    tp=camBase.clone();
    if(portrait){ tp.x*=.35; tp.y+=1.1; tp.z+=1.6; }
    tp.applyQuaternion(q);
    tp.y+=pitch*1.5;
    tl=new THREE.Vector3(0, 1.4+pitch*5.5, -26).applyQuaternion(q);
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
buildSky(); buildLights(); buildDust(); buildCatapult(); buildAim();
load(); resize(); startLevel();
hud.ammo.textContent=AMMO[ammoKind].label;
requestAnimationFrame(loop);
