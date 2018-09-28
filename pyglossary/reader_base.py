from typing import Iterator
from .entry_base import BaseEntry
from .glossary_type import GlossaryType

class BaseReader(object):
	def __init__(self, glos: GlossaryType, **kwargs) -> None:
		raise NotImplementedError

	@classmethod
	def __call__(cls, glos: GlossaryType, **kwargs):
		raise NotImplementedError

	def open(self, filename: str, **options) -> None:
		raise NotImplementedError

	def close(self) -> None:
		raise NotImplementedError

	def __iter__(self) -> Iterator[BaseEntry]:
		raise NotImplementedError
	
	def __len__(self) -> int:
		raise NotImplementedError


