from formats_common import *

import sys
import os
from os.path import (
	join,
	split,
	splitext,
	isfile,
	isdir,
	exists,
)

from typing import (
	Optional,
	Any,
	AnyStr,
	Tuple,
	List,
	Dict,
	Iterator,
)

import logging

log = logging.getLogger("root")

from paths import rootDir
sys.path.insert(0, rootDir)

from pyglossary.flags import *

from pyglossary import core
from pyglossary.file_utils import FileLineWrapper
from pyglossary.text_utils import toStr, toBytes
from pyglossary.os_utils import indir
from pyglossary.entry_base import BaseEntry

from pyglossary.glossary import Glossary

enable = False
format = "Unknown"
description = "Unknown"
extentions = []
readOptions = []
writeOptions = []
supportsAlternates = False
sortOnWrite = DEFAULT_NO
sortKey = None
