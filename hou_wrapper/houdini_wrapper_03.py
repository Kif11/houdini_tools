import os, sys
import subprocess

HOUDINI_MAJOR_RELEASE = "13"
HOUDINI_MINOR_RELEASE = "0"
HOUDINI_BUILD_VERSION = "260"

HOUDINI_BUILD = "%s.%s.%s" %(
	HOUDINI_MAJOR_RELEASE,
	HOUDINI_MINOR_RELEASE,
	HOUDINI_BUILD_VERSION)
    
HOUDINI_INSTAL_PATH = "C:/Program Files/Side Effects Software/Houdini"
STARTPATH = [HOUDINI_INSTAL_PATH + " " + HOUDINI_BUILD + "/bin/houdini.exe", "-s","kk_desktop"]
HOME = "G:/"
JOB = os.getcwd()

# Path to Houdini instaled build
HFS = "%s %s" %(HOUDINI_INSTAL_PATH, HOUDINI_BUILD)
HB = HFS + "/bin"

# Set up env variable to houdini instaled build
os.environ["HFS"] = HFS

# Setup path location
os.environ["PATH"] = os.path.pathsep.join([HB, os.environ["PATH"]])

# Shelfs
os.environ["HOUDINI_TOOLBAR_PATH"] = os.path.pathsep.join(["%s/toolbar" %JOB, "%shoudini%s.%s/toolbar" %(
	HOME,
	HOUDINI_MAJOR_RELEASE,
	HOUDINI_MINOR_RELEASE),
        "@/toolbar"])

# OTLs
os.environ["HOUDINI_OTLSCAN_PATH"] = os.path.pathsep.join(["%s/otls" %HOME,"%s/assets" %JOB,"@/otls"])

# HOME
os.environ["HOME"] = HOME

# JOB
os.environ["JOB"] = JOB

# Set bufeffere_save on for faster save over network
os.environ["HOUDINI_BUFFEREDSAVE"] = "1"

# Launch Houdini
subprocess.Popen(STARTPATH)
	

