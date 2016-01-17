
import os
import sys
import os.path
import hou


def launchgui(qubeguiPath='', submitDict={}, guiargs=''):
    '''launch the QubeGUI with the specified parameters'''
    # Construct parameter list
    cmdDict = {
                'qubeguiPath': qubeguiPath,
                'qubeguiArgString': '',
              }
    if len(submitDict) > 0:  cmdDict['qubeguiArgString'] += ' --submitDict "%s"'%submitDict
    if len(guiargs) > 0   :  cmdDict['qubeguiArgString'] += ' '+guiargs

    # Construct command for the specific platforms        
    if sys.platform[:3] == 'win':
        if cmdDict['qubeguiPath'] == '': cmdDict['qubeguiPath'] = 'C:/Program Files/pfx/qube/bin/qube.exe'
        if not os.path.exists(cmdDict['qubeguiPath']):
            cmdDict['qubeguiPath'] = 'C:/Program Files (x86)/pfx/qube/bin/qube.exe'
        cmd = r'start "QubeGUI Console" /B "%(qubeguiPath)s" %(qubeguiArgString)s'% cmdDict
    elif sys.platform == 'darwin':
        if cmdDict['qubeguiPath'] == '': cmdDict['qubeguiPath'] = '/Applications/pfx/qube/qube.app'
        cmd = r'%(qubeguiPath)s/Contents/MacOS/qube %(qubeguiArgString)s >/dev/null 2>&1  &'% cmdDict
    elif sys.platform[:5] == 'linux':
        if cmdDict['qubeguiPath'] == '': cmdDict['qubeguiPath'] = '/usr/local/pfx/qube/bin/qube'
        cmd = r'%(qubeguiPath)s %(qubeguiArgString)s >/dev/null 2>&1  &'% cmdDict
    else:
        raise "Unknown platform"
    
    # Run command
    print("COMMAND: %s"%cmd)
    #hou.ui.displayMessage("COMMAND: %s"%cmd)    
    os.system(cmd)


def qube_submit():
    # Get Scenefile
    filename = os.path.split(hou.hipFile.name())[1]
    scenefile = hou.hscript("job")[0].split("\n")[:-1][0] + "/" + filename
    
    # Get the ROP output node (under /out)
    # NOTE: Using the first one found
    #rops = hou.node("/out").children()
    rop = hou.selectedNodes()[0]
    outputNode = rop.name()
    frame_start = rop.parm( "f1" ).eval()
    frame_end   = rop.parm( "f2" ).eval()
    frame_step  = rop.parm( "f3" ).eval()
    frame_range = '%i-%i'%(frame_start, frame_end)
    if frame_step != 1:
        frame_range += 'x%i'%frame_step
	
    # Collect info for job submission
    artistName = "Ashlee"
    userName = os.environ["USERNAME"]
    projectName = "ASH"
    minPerFrame = "10minPerFrame"
    shot = "SH001"
    take = "001"
	
    jobname = "%s_%s_%s_%s_%s_%s" %(artistName,
                                    userName,
                                    projectName,
                                    minPerFrame,
                                    shot,
                                    take)

    # Launch QubeGUI Submission Dialog for "hython render"
    submitDict = {
        'name'      : jobname,
        'priority' : 3,
        'cpus' : 20,
        'prototype' : 'cmdrange',
        'package' : {
            'simpleCmdType': 'Houdini (hython render)',
            'hython' : 'C:/Program Files/Side Effects Software/Houdini 13.0.260/bin/hython.exe',
            'scene': scenefile,
            'outputNode' : outputNode,
            'range' : frame_range,
            }
        }
    return launchgui(submitDict=submitDict)


if __name__ == '__main__' or __name__ == '__builtin__':
    qube_submit()
