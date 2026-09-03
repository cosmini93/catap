"""
Authors the game's props in Blender and exports them as one .glb.

Run with Blender as a Python module:
    pip install bpy==4.2.0
    python3 src3d/blender/build_assets.py src3d/assets.glb

Everything is modelled procedurally - no binary source files in the repo.
Each asset gets bevelled edges (so it catches a highlight instead of reading
flat) and ambient occlusion baked into vertex colours by ray casting, which
costs nothing at runtime.
"""
import sys, math, random
import bpy, bmesh
from mathutils import Vector, Matrix
from mathutils.bvhtree import BVHTree

random.seed(7)
OUT = sys.argv[1] if len(sys.argv) > 1 else "assets.glb"


# ----------------------------------------------------------------- scene ---
def reset():
    for c in (bpy.data.objects, bpy.data.meshes, bpy.data.materials,
              bpy.data.collections):
        for item in list(c):
            c.remove(item)


def new_mesh(name):
    me = bpy.data.meshes.new(name)
    ob = bpy.data.objects.new(name, me)
    bpy.context.scene.collection.objects.link(ob)
    return ob


def from_bm(name, bm):
    ob = new_mesh(name)
    bm.to_mesh(ob.data)
    bm.free()
    return ob


def bevel(ob, width=0.02, segments=2, angle=math.radians(30)):
    m = ob.modifiers.new("bev", "BEVEL")
    m.width = width
    m.segments = segments
    m.limit_method = "ANGLE"
    m.angle_limit = angle
    m.harden_normals = False
    apply_mods(ob)


def apply_mods(ob):
    dg = bpy.context.evaluated_depsgraph_get()
    me = bpy.data.meshes.new_from_object(ob.evaluated_get(dg))
    old = ob.data
    ob.data = me
    ob.modifiers.clear()
    bpy.data.meshes.remove(old)


def shade_flat(ob):
    """Flat shading keeps the faceted low-poly read; bevels do the softening."""
    for p in ob.data.polygons:
        p.use_smooth = False


# -------------------------------------------------------------------- AO ---
def bake_ao(ob, samples=40, dist=3.0, floor=0.30, gamma=1.25):
    """Ray-cast ambient occlusion straight into a vertex colour layer."""
    me = ob.data
    bm = bmesh.new()
    bm.from_mesh(me)
    bm.normal_update()
    tree = BVHTree.FromBMesh(bm, epsilon=0.0)

    # cosine-weighted hemisphere directions, reused for every vertex
    dirs = []
    for i in range(samples):
        u = (i + 0.5) / samples
        v = (i * 0.618033988749895) % 1.0
        r = math.sqrt(u)
        a = 2.0 * math.pi * v
        dirs.append(Vector((r * math.cos(a), r * math.sin(a), math.sqrt(max(0.0, 1.0 - u)))))

    occ = []
    for vert in bm.verts:
        n = vert.normal
        if n.length < 1e-6:
            occ.append(1.0)
            continue
        # basis around the normal
        up = Vector((0, 0, 1)) if abs(n.z) < 0.9 else Vector((1, 0, 0))
        t = n.cross(up).normalized()
        b = n.cross(t)
        origin = vert.co + n * 0.004
        hits = 0
        for d in dirs:
            w = (t * d.x + b * d.y + n * d.z).normalized()
            hit = tree.ray_cast(origin, w, dist)
            if hit[0] is not None:
                hits += 1
        occ.append(1.0 - hits / float(samples))
    bm.free()

    if not me.color_attributes:
        me.color_attributes.new(name="ao", type="BYTE_COLOR", domain="CORNER")
    layer = me.color_attributes[0]
    for poly in me.polygons:
        for li in poly.loop_indices:
            vi = me.loops[li].vertex_index
            a = floor + (1.0 - floor) * (occ[vi] ** gamma)
            a = max(0.0, min(1.0, a))
            layer.data[li].color = (a, a, a, 1.0)


def paint_verts(ob, pred, value):
    """Force a vertex colour on the verts a predicate selects (used for faces)."""
    me = ob.data
    if not me.color_attributes:
        return
    layer = me.color_attributes[0]
    for poly in me.polygons:
        for li in poly.loop_indices:
            co = me.vertices[me.loops[li].vertex_index].co
            if pred(co):
                layer.data[li].color = (value, value, value, 1.0)


# ---------------------------------------------------------------- pieces ---
def rough_box(name, sx, sy, sz, jitter=0.0, bev=0.022, seg=2):
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bmesh.ops.scale(bm, vec=Vector((sx, sy, sz)), verts=bm.verts)
    if jitter:
        for v in bm.verts:
            v.co.x += random.uniform(-jitter, jitter) * sx
            v.co.y += random.uniform(-jitter, jitter) * sy
            v.co.z += random.uniform(-jitter, jitter) * sz
    ob = from_bm(name, bm)
    bevel(ob, bev, seg)
    return ob


def make_block_stone():
    # ashlar block: chamfered, faintly irregular, with a chipped top corner
    ob = rough_box("block_stone", 1.0, 1.0, 1.0, jitter=0.012, bev=0.045, seg=3)
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    # knock a corner off so a wall of them is not perfectly uniform
    geom = [v for v in bm.verts if v.co.x > 0.4 and v.co.z > 0.4]
    for v in geom:
        v.co.x -= 0.05
        v.co.z -= 0.04
    bm.to_mesh(ob.data)
    bm.free()
    shade_flat(ob)
    bake_ao(ob, samples=24, dist=1.2, floor=0.55)
    return ob


def make_block_wood():
    ob = rough_box("block_wood", 1.0, 1.0, 1.0, jitter=0.004, bev=0.03, seg=2)
    shade_flat(ob)
    bake_ao(ob, samples=24, dist=1.2, floor=0.6)
    return ob


def make_barrel():
    bm = bmesh.new()
    # staves: a barrel of rotated boxes reads far better than a cylinder
    n = 14
    for i in range(n):
        a = i * 2 * math.pi / n
        stave = bmesh.new()
        bmesh.ops.create_cube(stave, size=1.0)
        # tangential width must cover 2*pi*r / n, with a little overlap
        bmesh.ops.scale(stave, vec=Vector((0.085, 0.215, 0.96)), verts=stave.verts)
        # barrel curve: pinch the ends
        for v in stave.verts:
            k = 1.0 - 0.22 * (abs(v.co.z) * 2.0) ** 2
            v.co.y *= k
            v.co.x *= k
        m = Matrix.Rotation(a, 4, "Z") @ Matrix.Translation(Vector((0, 0, 0)))
        off = Matrix.Translation(Vector((0.435, 0, 0)))
        bmesh.ops.transform(stave, matrix=Matrix.Rotation(a, 4, "Z") @ off, verts=stave.verts)
        me_tmp = bpy.data.meshes.new("t")
        stave.to_mesh(me_tmp)
        stave.free()
        bm.from_mesh(me_tmp)
        bpy.data.meshes.remove(me_tmp)
    # iron hoops
    for z in (-0.33, 0.33):
        hoop = bmesh.new()
        bmesh.ops.create_cone(hoop, cap_ends=False, segments=20,
                              radius1=0.475, radius2=0.475, depth=0.09)
        bmesh.ops.translate(hoop, vec=Vector((0, 0, z)), verts=hoop.verts)
        me_tmp = bpy.data.meshes.new("t")
        hoop.to_mesh(me_tmp)
        hoop.free()
        bm.from_mesh(me_tmp)
        bpy.data.meshes.remove(me_tmp)
    # lid
    lid = bmesh.new()
    bmesh.ops.create_cone(lid, cap_ends=True, segments=14,
                          radius1=0.30, radius2=0.26, depth=0.10)
    bmesh.ops.translate(lid, vec=Vector((0, 0, 0.52)), verts=lid.verts)
    me_tmp = bpy.data.meshes.new("t")
    lid.to_mesh(me_tmp)
    lid.free()
    bm.from_mesh(me_tmp)
    bpy.data.meshes.remove(me_tmp)

    ob = from_bm("barrel", bm)
    bevel(ob, 0.012, 1)
    shade_flat(ob)
    bake_ao(ob, samples=32, dist=1.4, floor=0.62)
    return ob


def make_boulder():
    bm = bmesh.new()
    bmesh.ops.create_icosphere(bm, subdivisions=2, radius=0.5)
    for v in bm.verts:
        v.co *= random.uniform(0.84, 1.16)
    ob = from_bm("boulder", bm)
    bevel(ob, 0.01, 1)
    shade_flat(ob)
    bake_ao(ob, samples=24, dist=1.2, floor=0.5)
    return ob


def make_rock():
    bm = bmesh.new()
    bmesh.ops.create_icosphere(bm, subdivisions=1, radius=0.5)
    for v in bm.verts:
        v.co.x *= random.uniform(0.85, 1.25)
        v.co.y *= random.uniform(0.85, 1.25)
        v.co.z *= random.uniform(0.75, 1.15)
    ob = from_bm("rock", bm)
    bevel(ob, 0.02, 1)
    shade_flat(ob)
    bake_ao(ob, samples=20, dist=1.5, floor=0.5)
    return ob


def _cube(bm, sx, sy, sz, pos, rot=None):
    tmp = bmesh.new()
    bmesh.ops.create_cube(tmp, size=1.0)
    bmesh.ops.scale(tmp, vec=Vector((sx, sy, sz)), verts=tmp.verts)
    m = Matrix.Translation(Vector(pos))
    if rot:
        m = m @ Matrix.Rotation(rot[1], 4, rot[0])
    bmesh.ops.transform(tmp, matrix=m, verts=tmp.verts)
    me_tmp = bpy.data.meshes.new("t")
    tmp.to_mesh(me_tmp)
    tmp.free()
    bm.from_mesh(me_tmp)
    bpy.data.meshes.remove(me_tmp)


def make_guard():
    """Blocky man-at-arms, one metre eighty, origin at his feet."""
    bm = bmesh.new()
    _cube(bm, 0.62, 0.42, 0.62, (0, 0, 1.46))          # head
    _cube(bm, 0.70, 0.52, 0.24, (0, 0, 1.80))          # helmet dome
    _cube(bm, 0.30, 0.30, 0.16, (0, -0.06, 1.92))      # helmet crest
    _cube(bm, 0.74, 0.46, 0.92, (0, 0, 0.86))          # torso
    _cube(bm, 0.80, 0.50, 0.10, (0, 0, 0.50))          # belt
    for s in (-1, 1):
        _cube(bm, 0.20, 0.20, 0.62, (s * 0.48, 0, 0.92))   # arms
        _cube(bm, 0.24, 0.26, 0.46, (s * 0.19, 0, 0.22))   # legs
        _cube(bm, 0.26, 0.34, 0.12, (s * 0.19, 0.04, 0.05))  # boots
    # eyes and mouth as shallow inset blocks, darkened after the AO pass
    face_y = 0.215
    _cube(bm, 0.13, 0.05, 0.13, (-0.16, face_y, 1.52))
    _cube(bm, 0.13, 0.05, 0.13, ( 0.16, face_y, 1.52))
    _cube(bm, 0.26, 0.05, 0.06, ( 0.00, face_y, 1.32))
    ob = from_bm("guard", bm)
    bevel(ob, 0.024, 2)
    shade_flat(ob)
    bake_ao(ob, samples=28, dist=1.6, floor=0.46)
    paint_verts(ob, lambda co: co.y > face_y - 0.005 and 1.24 < co.z < 1.60
                               and abs(co.x) < 0.32, 0.10)
    return ob


def make_shield():
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=10,
                          radius1=0.42, radius2=0.42, depth=0.09)
    bmesh.ops.create_icosphere(bm, subdivisions=1, radius=0.11)
    ob = from_bm("shield", bm)
    bevel(ob, 0.015, 2)
    shade_flat(ob)
    bake_ao(ob, samples=20, dist=1.0, floor=0.5)
    return ob


def make_wheel():
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=16,
                          radius1=0.5, radius2=0.5, depth=0.14)   # rim
    hub = bmesh.new()
    bmesh.ops.create_cone(hub, cap_ends=True, segments=10,
                          radius1=0.13, radius2=0.13, depth=0.22)
    me_tmp = bpy.data.meshes.new("t"); hub.to_mesh(me_tmp); hub.free()
    bm.from_mesh(me_tmp); bpy.data.meshes.remove(me_tmp)
    for i in range(6):                                            # spokes
        a = i * math.pi / 3
        _cube(bm, 0.075, 0.075, 0.92, (0, 0, 0), rot=("Y", math.pi / 2))
        # rotate the last spoke block around Z
        verts = bm.verts[-8:]
        bmesh.ops.rotate(bm, verts=list(verts), cent=Vector((0, 0, 0)),
                         matrix=Matrix.Rotation(a, 3, "X"))
    ob = from_bm("wheel", bm)
    bevel(ob, 0.012, 1)
    shade_flat(ob)
    bake_ao(ob, samples=20, dist=1.0, floor=0.45)
    return ob


def make_palm_frond():
    bm = bmesh.new()
    bmesh.ops.create_grid(bm, x_segments=6, y_segments=2, size=1.0)
    for v in bm.verts:
        u = v.co.x * 0.5 + 0.5            # 0 at base, 1 at tip
        v.co.x = u * 3.2
        v.co.y *= 0.42 * (1.0 - u * 0.78)
        v.co.z = -(u ** 2) * 1.25
    ob = from_bm("frond", bm)
    shade_flat(ob)
    return ob


ASSETS = [
    make_block_stone, make_block_wood, make_barrel, make_boulder,
    make_rock, make_guard, make_shield, make_wheel, make_palm_frond,
]


def main():
    reset()
    made = []
    for fn in ASSETS:
        ob = fn()
        made.append(ob.name)
        print("built", ob.name, len(ob.data.vertices), "verts")
    bpy.ops.export_scene.gltf(
        filepath=OUT, export_format="GLB",
        export_apply=True, export_yup=True,
        export_materials="NONE", export_cameras=False, export_lights=False,
    )
    print("exported", OUT, "with", len(made), "assets")


main()
