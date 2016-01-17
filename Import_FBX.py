# Import fbx files

import os
import hou

job = os.environ['JOB']
geo_dir = job + '/geo/work'

files = os.listdir(geo_dir)

for file in files:
    if file.endswith('.fbx'):
        hou.hscript("fbximport '%s'" % (geo_dir + '/' + file))