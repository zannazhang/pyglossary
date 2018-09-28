import sys
import logging
import traceback
import inspect

from pprint import pformat

from types import TracebackType

from typing import (
	Dict,
	Tuple,
	Any,
	Optional,
	Type,
)


levelsByVerbosity = (
	logging.CRITICAL,
	logging.ERROR,
	logging.WARNING,
	logging.INFO,
	logging.DEBUG,
	logging.NOTSET,
)
verbosityByLevels = {l: v for v, l in enumerate(levelsByVerbosity)}
levelNamesCap = [
	"Critical",
	"Error",
	"Warning",
	"Info",
	"Debug",
	"All",  # "Not-Set",
]



def format_var_dict(dct: Dict[str, Any], indent: int = 4, max_width: int = 80) -> str:
	lines = []
	pre = " " * indent
	for key, value in dct.items():
		line = pre + key + " = " + repr(value)
		if len(line) > max_width:
			line = line[:max_width-3] + "..."
			try:
				value_len = len(value)
			except:
				pass
			else:
				line += "\n" + pre + "len(%s) = %s"%(key, value_len)
		lines.append(line)
	return "\n".join(lines)



def format_exception(
	exc_info: Optional[Tuple[Optional[Type[BaseException]], Optional[BaseException], Optional[TracebackType]]] = None,
	add_locals: bool = False,
	add_globals: bool = False,
) -> str:
	if not exc_info:
		exc_info = sys.exc_info()
	_type, value, tback = exc_info
	text = "".join(traceback.format_exception(_type, value, tback))
	if tback is not None:
		if add_locals or add_globals:
			try:
				frame = inspect.getinnerframes(tback, context=0)[-1][0]
			except IndexError:
				pass
			else:
				if add_locals:
					text += "Traceback locals:\n%s\n" % format_var_dict(
						frame.f_locals,
					)
				if add_globals:
					text += "Traceback globals:\n%s\n" % format_var_dict(
						frame.f_globals,
					)

	return text


class StdLogHandler(logging.Handler):
	startRed = "\x1b[31m"
	endFormat = "\x1b[0;0;0m"  # len=8

	def __init__(self, noColor: bool = False) -> None:
		logging.Handler.__init__(self)
		self.noColor = noColor

	def emit(self, record: logging.LogRecord) -> None:
		msg = record.getMessage()
		###
		if record.exc_info:
			_type, value, tback = record.exc_info
			tback_text = format_exception(
				exc_info=record.exc_info,
				add_locals=(log.level <= logging.DEBUG),  # FIXME
				add_globals=False,
			)

			if not msg:
				msg = "unhandled exception:"
			msg += "\n"
			msg += tback_text
		###
		if record.levelname in ("CRITICAL", "ERROR"):
			if not self.noColor:
				msg = self.startRed + msg + self.endFormat
			fp = sys.stderr
		else:
			fp = sys.stdout
		###
		fp.write(msg + "\n")
		fp.flush()

#	def exception(self, msg: str) -> None:
#		if not self.noColor:
#			msg = self.startRed + msg + self.endFormat
#		sys.stderr.write(msg + "\n")
#		sys.stderr.flush()


# ==========================================================

log = logging.getLogger("root")

def excepthook(type_: Type[BaseException], value: BaseException, traceback: TracebackType) -> None:
	format_exception(
		exc_info=(type_, value, traceback),
		add_locals=(log.level <= logging.DEBUG),  # FIXME
		add_globals=False,
	)


def overrideExceptHook():
	sys.excepthook = excepthook

# ==========================================================

def setVerbosity(verbosity: int) -> None:
	log.setLevel(levelsByVerbosity[verbosity])

def getVerbosity() -> int:
	return verbosityByLevels.get(log.level, 3)


