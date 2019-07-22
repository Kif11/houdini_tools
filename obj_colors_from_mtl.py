# Quick and dirty way to transfer colors from .mtl file to polygon color attribute
# Place it in Python SOP afte you load your geometry.
# Make sure that the geometry has shop_materialpath poly attribute
# that corespond to material from .mtl file

node = hou.pwd()
geo = node.geometry()

text = hou.readFile("/path/to/myobj.mtl")

col_attrib = geo.addAttrib(hou.attribType.Prim, "Cd", (1.0, 1.0, 1.0))
mat_dict = {}

for i in text.split('newmtl'):
    if len(i) == 0:
        continue
    values = i.split("\n")
    if not values[0]:
        continue
    mat_name = values[0].strip()
    mat_color = values[1].strip().replace('Kd  ', '').split(' ')
    
    norm_color = hou.Color((
        pow(float(mat_color[0]), 2),
        pow(float(mat_color[1]), 2),
        pow(float(mat_color[2]), 2)
    ))

    mat_dict[mat_name] = norm_color
    
for p in geo.prims():
    geo_mat_name = p.attribValue("shop_materialpath").replace("/mat/", '')
    if mat_dict.get(geo_mat_name):
        p.setAttribValue(col_attrib, mat_dict.get(geo_mat_name).rgb())
        
