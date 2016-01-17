import os, sys
import subprocess

PLATFORM = sys.platform

HOUDINI_MAJOR_RELEASE = "13"
HOUDINI_MINOR_RELESE = "0"
HOUDINI_BUILD_VERSION = "260"

HOUDINI_BUILD = "%s.%s.%s" %(
	HOUDINI_MAJOR_RELEASE,
	HOUDINI_MINOR_RELESE,
	HOUDINI_BUILD_VERSION)

if PLATFORM == "darwin":
    HOUDINI_INSTAL_PATH = "/Applications/Houdini"
    HOUDINI_PROD_PATH = "/home/kkirill2/houdini"
    JOB = os.getcwd()
    HOME = "/home/kkirill2/"
    HB = "/Library/Frameworks/Houdini.framework/Versions/"+ HOUDINI_BUILD + "/Resources/bin"
    # Path to Houdini instaled build
    HFS = "%s %s" %(
    HOUDINI_INSTAL_PATH,
    HOUDINI_BUILD)
    HB = HFS + "/bin"
    STARTPATH = ["open", "-a", "houdini fx", "-n"]
    
elif PLATFORM == "win32":
    HOUDINI_INSTAL_PATH = "C:/Program Files/Side Effects Software/Houdini"
    HOUDINI_PROD_PATH = "Z:/houdini"
    JOB = os.getcwd()
    # Path to Houdini instaled build
    HFS = "%s %s" %(
    HOUDINI_INSTAL_PATH,
    HOUDINI_BUILD)
    HB = HFS + "/bin"
    STARTPATH = "C:/Program Files/Side Effects Software/Houdini 13.0.260/bin/houdini.exe"

# Set up env variable to houdini instaled build

os.environ["HFS"] = HFS

# Setup path location

os.environ["PATH"] = os.path.pathsep.join([HB, os.environ["PATH"]])

# Shelfs

os.environ["HOUDINI_TOOLBAR_PATH"] = os.path.pathsep.join(["%s/toolbar" %HOUDINI_PROD_PATH, "@/toolbar"])

# OTLs

os.environ["HOUDINI_OTLSCAN_PATH"] = os.path.pathsep.join(["%s/otls" %HOUDINI_PROD_PATH, "@/otls"])

# Set bufeffere_save on for faster save over network

os.environ["HOUDINI_BUFFEREDSAVE"] = "1"


# Launch Houdini

subprocess.Popen(STARTPATH)
	

