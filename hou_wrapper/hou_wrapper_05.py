import os, sys
import subprocess
    
HOUDINI_INSTAL_PATH = "C:/Program Files/Side Effects Software/Houdini 13.0.260"
STARTPATH = [HOUDINI_INSTAL_PATH + "/bin/houdini.exe", "-s","kk_desktop"]
HOME = "G:/"
JOB = os.getcwd()

# Houdini instaled build
os.environ["HFS"] = HOUDINI_INSTAL_PATH

# PATH
os.environ["PATH"] = os.path.pathsep.join([HOUDINI_INSTAL_PATH + "/bin", os.environ["PATH"]])

# TOOLBARS
os.environ["HOUDINI_TOOLBAR_PATH"] = os.path.pathsep.join([JOB + "/toolbar", HOME + "/toolbar", "@/toolbar"])

# OTLs
os.environ["HOUDINI_OTLSCAN_PATH"] = os.path.pathsep.join([HOME + "/otls", JOB + "/assets", "@/otls"])

# HOME
os.environ["HOME"] = HOME

# JOB
os.environ["JOB"] = JOB

# Set bufeffere_save on for faster save over network
os.environ["HOUDINI_BUFFEREDSAVE"] = "1"

# Launch Houdini
subprocess.Popen(STARTPATH)
	

