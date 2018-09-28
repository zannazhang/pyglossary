import sys
import os
from os.path import (
	join,
	isfile,
	isdir,
	exists,
	realpath,
	dirname,
)
import platform

from typing import (
	Dict,
	Tuple,
	Any,
	Optional,
	Type,
)

from .logger import log


VERSION = "3.1.0"


def checkCreateConfDir() -> None:
	if not isdir(confDir):
		if exists(confDir):  # file, or anything other than directory
			os.rename(confDir, confDir + ".bak")  # we do not import old config
		os.mkdir(confDir)
	if not exists(userPluginsDir):
		os.mkdir(userPluginsDir)
	if not isfile(confJsonFile):
		with open(rootConfJsonFile) as srcFp, \
		  open(confJsonFile, "w") as userFp:
			userFp.write(srcFp.read())


# __________________________________________________________________________ #



sysName = platform.system()

if hasattr(sys, "frozen"):
	rootDir = dirname(sys.executable)
	uiDir = join(rootDir, "ui")
else:
	uiDir = dirname(realpath(__file__))
	rootDir = dirname(uiDir)

dataDir = rootDir
if dataDir.endswith("dist-packages"):
	dataDir = dirname(sys.argv[0])

appResDir = join(dataDir, "res")

def mustgetenv(name: str) -> str:
	value = os.getenv(name, "")
	if value == "":
		raise OSError("Environment variable %r is not set" % name)
	return value

if os.sep == "/":  # Operating system is Unix-Like
	homeDir = mustgetenv("HOME")
	user = mustgetenv("USER")
	tmpDir = "/tmp"
	# os.name == "posix" # FIXME
	if sysName == "Darwin":  # MacOS X
		confDir = homeDir + "/Library/Preferences/PyGlossary"
		# or maybe: homeDir + "/Library/PyGlossary"
		# os.environ["OSTYPE"] == "darwin10.0"
		# os.environ["MACHTYPE"] == "x86_64-apple-darwin10.0"
		# platform.dist() == ("", "", "")
		# platform.release() == "10.3.0"
	else:  # GNU/Linux, ...
		confDir = homeDir + "/.pyglossary"
elif os.sep == "\\":  # Operating system is Windows
	homeDir = mustgetenv("HOMEDRIVE") + mustgetenv("HOMEPATH")
	user = mustgetenv("USERNAME")
	tmpDir = mustgetenv("TEMP")
	confDir = mustgetenv("APPDATA") + "\\" + "PyGlossary"
else:
	raise RuntimeError(
		"Unknown path seperator(os.sep==%r)" % os.sep +
		", unknown operating system!"
	)

confJsonFile = join(confDir, "config.json")
rootConfJsonFile = join(dataDir, "config.json")
userPluginsDir = join(confDir, "plugins")
