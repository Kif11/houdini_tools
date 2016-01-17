import hou

createGeoNodes = 1
createMaterials = 1

selected = hou.selectedNodes()
obj = hou.node("/obj")
shop = hou.node("/shop")

geo = selected[0].geometry()
primGroupsInGeo = geo.primGroups()

# Create empty geometry container

def createDummy(name):
    obj = hou.node("/obj")
    newGeo = obj.createNode("geo", name)
    newGeo.children()[0].destroy()

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
        geo = createDummy(group)
        geoPath = geo.path()
        objMerge = hou.node(geoPath).createNode("object_merge")
        objMerge.setParms({"objpath1":null.path(), "xformtype":1})

    if createGeoNodes and createMaterials:
        mantraSurface = hou.galleries.galleryEntries("mantrasurface")[0]
        material = mantraSurface.createChildNode(shop)
        hou.node(material.path()).setName(group.upper())
        geo.setParms({"shop_materialpath":"/shop/" + group.upper()})