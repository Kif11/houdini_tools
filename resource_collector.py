import hou
import shutil
import os
import re

# Create new project folder and copy selected files into it                     
def copyToNewProject(newProject, choose=False):

    hipPath = hou.hipFile.name()
    oldProject =  hou.hscript("echo $JOB")[0][:-1]

    def pathForExport():
        allPath = hou.hscript("opextern -rR -g -l /")[0].split("\n")[:-1]
        selectedPath = []
        if choose:
            selectedItem = hou.ui.selectFromList(allPath)
            for item in selectedItem:
                path = allPath[item]
                selectedPath.append(path)
        else:
            selectedPath = allPath

        return selectedPath

    def expandSequence(allPath):
        allPathExpanded = []
        for path in allPath:
            match = re.search(r"\[.+\]", path)
            if match:
                frameRange = re.findall("\d+", match.group())
                seqPath = path[:-len(match.group())-2]
                seqDir = os.path.split(seqPath)[0]
                if os.path.isdir(seqDir):
                    filesInDir = os.listdir(seqDir)
                    for file in filesInDir:
                            filePath = seqDir + "/" + file
                            allPathExpanded.append(filePath)
                else:
                        print seqDir, "- Folder do not exist"
            else:
                    allPathExpanded.append(path)
        return allPathExpanded

    def deleteMissingPaths(allPaths):
        allPathsCleaned = []
        for path in allPaths:
            if os.path.exists(path):
                allPathsCleaned.append(path)
        return allPathsCleaned

    selectedPath = pathForExport()
    allPathExpanded = expandSequence(selectedPath)
    allPath = deleteMissingPaths(allPathExpanded)
    allPath.append(hipPath)

    # Create folders
    for path in allPath:
        if os.path.isfile(path):
            newFilePath = path.replace(oldProject, newProject)
            newPath = os.path.split(newFilePath)[0]
            if len(newPath) > 0:
                if not os.path.isdir(newPath):
                    os.makedirs(newPath)
            if not os.path.isfile(newFilePath):
                shutil.copyfile(path, newFilePath)
                print newFilePath, "- File has been created"
            else:
                print newFilePath, "- File is already exist"
        else:
            print path, "- Do not exist"

    print "DONE!"
