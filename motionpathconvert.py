import bpy

ob = bpy.context.selected_pose_bones[0]
mp = ob.motion_path

mesh = bpy.data.meshes.new("myBeautifulMesh")  # add the new mesh
obj = bpy.data.objects.new(mesh.name, mesh)
col = bpy.data.collections.get("Collection")
col.objects.link(obj)


verts = []

for point in mp.points:
    verts.append(point.co)
    
edges = [[i, i+1] for i in range(len(verts)-1)]

faces = []

print('abc');

mesh.from_pydata(verts, edges, faces)
