import hou

createGeoNodes = True
createMaterials = True

selected = hou.selectedNodes()
obj = hou.node("/obj")
mat = hou.node("/mat")

if not selected:
    raise Exception("Nothing is selected")

geo = selected[0].geometry()
primGroupsInGeo = geo.primGroups()

# Find current working directory

cwd = ""
for i in selected[0].path().split("/")[1:-1]:
    cwd = cwd + "/" + i

# Create delete node for each primitive group

for i in range(0,len(primGroupsInGeo)):
    group = primGroupsInGeo[i].name()
    deleteGroup = hou.node(cwd).createNode("delete")
    deleteGroupNode = hou.node(deleteGroup.path())
    deleteGroupNode.setParms({"group":group, "negate":1})
    deleteGroupNode.setFirstInput(selected[0])

    # Create nulls

    null = hou.node(cwd).createNode("null", group)
    nullNode = hou.node(null.path())
    nullNode.setFirstInput(deleteGroupNode)

    # If active create geo node for each group    

    if createGeoNodes:
        geo = hou.node("/obj").createNode("geo", group)
        geoPath = geo.path()
        objMerge = hou.node(geoPath).createNode("object_merge")
        objMerge.setParms({"objpath1":null.path(), "xformtype":1})

    if createGeoNodes and createMaterials:
        principalSurface = hou.galleries.galleryEntries("principledshader")[0]
        material = principalSurface.createChildNode(mat)
        hou.node(material.path()).setName(group.upper())
        geo.setParms({"shop_materialpath":"/mat/" + group.upper()})
