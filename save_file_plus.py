import hou
import os
import re

# Put everything in the loop to have ability to break the execution
for file in range(0,1):

    hipPath = hou.hipFile.name()
    JOB = hou.expandString("$JOB")

    # Version up the name 
    # If file exist freeze the main version and only modyfy the fork
    def versionUp(fileExist=False, forkVersion=0, majorVersion=0, minorVersion=0, treshold=10):
    
        forkVersion = int(forkVersion)
        majorVersion = int(majorVersion)
        minorVersion = int(minorVersion)
    
        if fileExist or forkVersion != 0:
            forkVersion += 1
        else:
            if (minorVersion + 1) >= treshold:
                minorVersion = 0
                majorVersion += 1
            else:
                minorVersion += 1
        
        return "f%d_v%d_%d" %(forkVersion, majorVersion, minorVersion)

    # Chech if the file is unsaved prompt the user to enter a name
    if hipPath == 'untitled.hip':

        userFileNameButtons, userFileName = hou.ui.readInput("Enter the file name", buttons=("OK","CANCEL"))

        # Break file creation if canceled
        if userFileNameButtons == 1:
            break

        outFilePath = "%s/%s_%s.hip" %(JOB, userFileName, versionUp())
        
        # Seve hip file
        hou.hipFile.save(outFilePath)
    
    # If file is already been saved extract all versions value and version it up
    else:
        filePath, fileName = os.path.split(hipPath)
        name, ext = os.path.splitext(fileName)
    
        splitName = name.split("_")
        
        # Check if file name is valid
        if len(splitName) == 4:
            userFileName, forkVersion, majorVersion, minorVersion = splitName
            forkVersion = forkVersion.replace("f","")
            majorVersion = majorVersion.replace("v","")
    
            outFilePath = "%s/%s_%s.hip" %(JOB, userFileName, versionUp(False, forkVersion, majorVersion, minorVersion))
            
            # Check if the newer version exist only iterate the fork
            if os.path.isfile(outFilePath):
                createFork = hou.ui.displayMessage("Newer version of this file is already exist. Create fork?", buttons=("YES","NO"))
                if createFork == 0:
                    outFilePath = "%s/%s_%s.hip" %(JOB, userFileName, versionUp(True, forkVersion, majorVersion, minorVersion))
                else:
                    break

            hou.hipFile.save(outFilePath)
    
        else:
            print "The name of you file is node valid"