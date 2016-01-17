import random
import hou

################################################
# Collection of useful Houdini Python snippets #
################################################

################################################
# Incremental random
start = 0
stop  = 1
step  = 0.15
precision = 0.01
f = 1 / precision
random.seed(hou.hscriptExpression('stamp("..", "FORVALUE", +0)'))
value = random.randrange(start*f, stop*f, step*f)/f
return value

################################################
# FBX Import
hou.hscript("fbximport '%s'" % (geo_dir + '/' + file))

################################################
# Mantra prerender script to create missing folders
import os

nodeOutPath = hou.node(".").parm("vm_picture").eval()
path, name = os.path.split(nodeOutPath)
if not(os.path.isdir(path)):
    os.makedirs(path)
    print "%s directory has been created" % path
