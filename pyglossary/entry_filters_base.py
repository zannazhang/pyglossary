from typing import (
	Optional,
)

from .entry_base import BaseEntry
from .glossary_type import GlossaryType

class EntryFilter(object):
	name = ""
	desc = ""

	def __init__(self, glos: GlossaryType) -> None:
		self.glos = glos

	def run(self, entry: BaseEntry) -> Optional[BaseEntry]:
		"""
			returns an Entry object, or None to skip
				may return the same `entry`,
				or modify and return it,
				or return a new Entry object
		"""
		return entry

