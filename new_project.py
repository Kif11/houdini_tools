import os

def createProject(projectPath):
    """
    Create project structure inside your JOB folder
    """
	mainDirList = ["geo", "img", "ref", "export", "comp", "asset", "render", "old", "source", "script"]
	for d in mainDirList:
		if not(os.path.isdir(projectPath + "/" + d)):
			os.mkdir(projectPath + "/" + d)
			print "%s has been created." % d
		else:
			print '"%s" folder is already exist.' % d
