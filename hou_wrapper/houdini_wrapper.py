import os, sys
import subprocess

HOUDINI_MAJOR_RELEASE = "13"
HOUDINI_MINOR_RELESE = "0"
HOUDINI_BUILD_VERSION = "260"

HOUDINI_INSTAL_PATH = "C:/Program Files/Side Effects Software/Houdini"
HOUDINI_BIN = 
HOUDINI_PROD_PATH = "Z:/houdini"

HOME = "Z:/"

HOUDINI_BUILD = "%s.%s.%s" %(
	HOUDINI_MAJOR_RELEASE,
	HOUDINI_MINOR_RELESE,
	HOUDINI_BUILD_VERSION)

# Path to Houdini instaled build

HFS = "%s %s" %(
    HOUDINI_INSTAL_PATH,
    HOUDINI_BUILD)
	
os.environ["HFS"] = HFS

# Setup path location

HB = HFS + "/bin"

os.environ["PATH"] = os.path.pathsep.join([HB, os.environ["PATH"]])

## Setup houdini path variable

# Factory and costom shelf tools

os.environ["HOUDINI_TOOLBAR_PATH"] = os.path.pathsep.join(["%s/toolbar" %HOUDINI_PROD_PATH, "@/toolbar"])

# Scripts

os.environ["HOUDINI_SCRIPT_PATH"] = os.path.pathsep.join(["%s/scripts" %HOUDINI_PROD_PATH, "@/scripts"])

# OTLs

os.environ["HOUDINI_OTLSCAN_PATH"] = os.path.pathsep.join(["%s/otls" %HOUDINI_PROD_PATH, "@/otls"])

# Home

os.environ["HOME"] = HOME

# Set bufeffere_save on for faster save over network

os.environ["HOUDINI_BUFFEREDSAVE"] = "1"

##for i in os.environ:
##    print i
##
##print os.environ["HOUDINI_TOOLBAR_PATH"] 

# Test environment variable

#os.environ["HOUDINI_NO_SPLASH"] = "0"


# Launch Houdini

if __name__ == '__main__':
    startpath = "C:/Program Files/Side Effects Software/Houdini 13.0.260/bin/houdini.exe"
    subprocess.Popen(startpath)
	

