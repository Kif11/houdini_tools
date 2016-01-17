# HDA VERSION CREATER 1.0


import hou, sys, os, tempfile
selected = hou.selectedNodes()

assetPath = os.environ['JOB'] + "/assets"

for node in selected:
    
    # Check for proper name
    if len(node.name().split("_")) != 3:
        print 'Rename "%s" by following naming convention "user_asset_version"'  % node.name()
    
    # Create new HDA from selection if one not exist
    elif node.type().definition() == None:
        nodeName = node.name()
        nameSplit = nodeName.split("_")
        otlPrefix = nameSplit[0]
        otlName = nameSplit[1]
        otlVersion = nameSplit[2]
        otlPath = assetPath + "/" + nodeName + ".otl"

        newHDA = node.createDigitalAsset(otlPrefix + "_" + otlName, otlPath, otlPrefix + "_" + otlName)
        newHDA.matchCurrentDefinition()

        print 'The otl "%s" from "%s" has been created.' % (otlPath, nodeName)

    # If node is alredy an asset create a new version
    elif node.type().definition():
        hdaDef = node.type().definition()
        fileName = os.path.basename(hdaDef.libraryFilePath())
        nodeName = os.path.splitext(fileName)[0]
        nameSplit = nodeName.split("_")
        otlPrefix = nameSplit[0]
        otlName = nameSplit[1]
        otlVersion = nameSplit[2]
        otlPath = assetPath + "/" + nodeName + ".otl"
        otlNewVersion = "%02d" % (int(otlVersion) + 1)
        otlNewPath = assetPath + "/" + otlPrefix + "_" + otlName + "_" + otlNewVersion + ".otl"

        # Check if newer version is exist
        if os.path.isfile(otlNewPath):
            newVersionMsg = not(hou.ui.displayMessage('"%s" is already exist. Override?' % otlNewPath, buttons=("Yes","No")))
            if newVersionMsg == False:
                break
 
        # If asset unlocke save it in new version trough temp file
        isLocked = False
        if not(node.isLocked()):
            tempPath = tempfile.mkstemp()[1].replace("\\","/")
            tempHDAPath = tempPath + fileName
            # Save temp HDA
            hdaDef.save(tempHDAPath, node)
            # Import again and set definition
            hou.hda.installFile(tempHDAPath, None, False, True)
            # Define temp definition insted of current
            hdaDef = node.type().definition()
            hdaDef.setIsPreferred(False)
            print "Asset was unlocked hence it was saved as temp file %s" % tempHDAPath
            isLocked = True
        
        # Copy definition to new file
        hdaDef.copyToHDAFile(otlNewPath)
        hou.hda.installFile(otlNewPath, None, False, True)
        hdaDef = node.type().definition()
        hdaDef.setIsPreferred(True)
        
        # Save curent definition and lock asset
        hdaDef.updateFromNode(node)
        node.matchCurrentDefinition()

        # Uninstal temp HDA and remove file
        if isLocked:
            hou.hda.uninstallFile(tempHDAPath)
            os.remove(tempHDAPath)

        print 'Version "%s" of asset "%s" has been created' %(otlNewVersion, otlPath)
            