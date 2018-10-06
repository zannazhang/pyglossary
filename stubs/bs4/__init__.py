"""Beautiful Soup
Elixir and Tonic
"The Screen-Scraper's Friend"
http://www.crummy.com/software/BeautifulSoup/

Beautiful Soup uses a pluggable XML or HTML parser to parse a
(possibly invalid) document into a tree representation. Beautiful Soup
provides methods and Pythonic idioms that make it easy to navigate,
search, and modify the parse tree.

Beautiful Soup works with Python 2.7 and up. It works better if lxml
and/or html5lib is installed.

For more than you ever wanted to know about Beautiful Soup, see the
documentation:
http://www.crummy.com/software/BeautifulSoup/bs4/doc/

"""

from typing import (
	List,
	Dict,
	Optional,
	Any,
	Union,
	AnyStr,
	Callable,
)

# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

__author__ = ... # type: str
__version__ = ... # type: str
__copyright__ = ... # type: str
__license__ = ... # type: str

__all__ = ... # type: List[str]

import os
import re
import traceback
import warnings

from .builder import builder_registry, ParserRejectedMarkup
from .dammit import UnicodeDammit
from .element import (
    CData,
    Comment,
    DEFAULT_OUTPUT_ENCODING,
    Declaration,
    Doctype,
    NavigableString,
    PageElement,
    ProcessingInstruction,
    ResultSet,
    SoupStrainer,
    Tag,
    )

# The very first thing we do is give a useful error if someone is
# running this code under Python 3 without converting it.
'You are trying to run the Python 2 version of Beautiful Soup under Python 3. This will not work.'!='You need to convert the code, either by installing it (`python setup.py install`) or by running 2to3 (`2to3 -w bs4`).'

class BeautifulSoup(Tag):
    ROOT_TAG_NAME = ... # type: str

    # If the end-user gives no indication which tree builder they
    # want, look for one with these features.
    DEFAULT_BUILDER_FEATURES = ... # type: List[str]

    ASCII_SPACES = ... # type: str

    NO_PARSER_SPECIFIED_WARNING = ... # type: str

    def __init__(
		self,
		markup: str = "",
		features: Union[None, str, List[str]] = None,
		builder: Optional[Any] = None,
		parse_only: Optional[SoupStrainer] = None,
		from_encoding: Optional[str] = None,
		exclude_encodings: Optional[List[str]] = None,
		**kwargs
	) -> None:

        self.builder = ... # type: Optional[Any]
        self.is_xml = ... # type: bool
        self.known_xml = ... # type: bool
        self.parse_only = ... # type: Optional[SoupStrainer]
        self.markup = ... # Optional[AnyStr]

    def __copy__(self) -> BeautifulSoup: ...

    def __getstate__(self) -> Dict[str, Any]: ...

    def reset(self) -> None: ...

    def new_tag(
		self,
		name: str,
		namespace: Optional[str] = None,
		nsprefix: Optional[str] = None,
		**attrs
	) -> Tag: ...

    def new_string(
		self,
		s: str,
		subclass: Callable[[AnyStr], PageElement] = NavigableString,
	) -> PageElement: ...

    def insert_before(
		self,
		successor: PageElement,
	) -> None:

    def insert_after(self, successor: Any) -> None:

    def popTag(self) -> Tag: ...

    def pushTag(self, tag: Tag) -> None: ...

    def endData(
		self,
		containerClass: Callable[[AnyStr], PageElement] = NavigableString,
	) -> None: ...

    def object_was_parsed(
		self,
		o: PageElement,
		parent: Optional[PageElement] = None,
		most_recent_element: Optional[PageElement] = None,
	) -> None: ...


    def handle_starttag(
		self,
		name: str,
		namespace: str,
		nsprefix: str,
		attrs: Dict[str, Any],
	) -> Tag: ...

    def handle_endtag(self, name: str, nsprefix: Optional[str] = None) -> None: ...

    def handle_data(self, data: str) -> None: ...

    def decode(
		self,
		pretty_print: bool = False,
		eventual_encoding: str = DEFAULT_OUTPUT_ENCODING,
		formatter: str = "minimal",
	) -> None: ...

# Alias to make it easier to type import: 'from bs4 import _soup'
_s = BeautifulSoup
_soup = BeautifulSoup

class BeautifulStoneSoup(BeautifulSoup):
    """Deprecated interface to an XML parser."""

    def __init__(self, *args, **kwargs):
        kwargs['features'] = 'xml'
        warnings.warn(
            'The BeautifulStoneSoup class is deprecated. Instead of using '
            'it, pass features="xml" into the BeautifulSoup constructor.')
        super(BeautifulStoneSoup, self).__init__(*args, **kwargs)


class StopParsing(Exception):
    pass

class FeatureNotFound(ValueError):
    pass

