# Merge selected nodes into separate geo containers 

import hou

cuspNormal = input("Add vertex node to cust normals? > ")
selected = hou.selectedNodes()

for i in range(0,len(selected)):
    
    def createDummy(name):
        global newGeo
        obj = hou.node("/obj")
        newGeo = obj.createNode("geo", name)
        newGeo.children()[0].destroy()

    # Merge selected object in new geo container

    createDummy(selected[i].name())
    objMerge = hou.node(newGeo.path()).createNode("object_merge")
    hou.node(objMerge.path()).setParms({"objpath1":selected[i].path(),"xformtype":1})
    
    # If active cusp normals

    if cuspNormal:
        vertex = hou.node(newGeo.path()).createNode("vertex")
        vertexNode = hou.node(vertex.path())
        vertexNode.setFirstInput(objMerge)
        vertexNode.setParms({"donormal":2})
        vertexNode.setRenderFlag(True)
        vertexNode.setDisplayFlag(True)
