import os, subprocess

# Path to houdini lanch file.
STARTPATH = "C:/Program Files/Side Effects Software/Houdini 13.0.260/bin/hmaster.exe"

# Replace the value of HOME to you external hard drive to get rid off long lanch.
# The folder named "houdini13.0" will be created.
HOME = "G:/"

# Set HOME environmental variable 
os.environ["HOME"] = HOME


# Launch Houdini
subprocess.Popen(STARTPATH)
	

