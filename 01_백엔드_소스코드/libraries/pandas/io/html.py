# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: html.pyc (Python 3.11)

'''
:mod:`pandas.io.html` is a module containing functionality for dealing with
HTML IO.

'''
from __future__ import annotations
from collections import abc
import errno
import numbers
import os
import re
from re import Pattern
from typing import TYPE_CHECKING, Literal, cast
from pandas._libs import lib
from pandas.compat._optional import import_optional_dependency
from pandas.errors import AbstractMethodError, EmptyDataError
from pandas.util._decorators import set_module
from pandas.util._validators import check_dtype_backend
from pandas.core.dtypes.common import is_list_like
from pandas import isna
from pandas.core.indexes.base import Index
from pandas.core.indexes.multi import MultiIndex
from pandas.core.series import Series
from pandas.io.common import get_handle, is_url, stringify_path, validate_header_arg
from pandas.io.formats.printing import pprint_thing
from pandas.io.parsers import TextParser
if TYPE_CHECKING:
    from collections.abc import Iterable, Sequence
    from pandas._typing import BaseBuffer, DtypeBackend, FilePath, HTMLFlavors, ReadBuffer, StorageOptions
    from pandas import DataFrame
_RE_WHITESPACE = re.compile('[\\r\\n]+|\\s{2,}')

def _remove_whitespace(s = None, regex = None):
    '''
    Replace extra whitespace inside of a string with a single space.

    Parameters
    ----------
    s : str or unicode
        The string from which to remove extra whitespace.
    regex : re.Pattern
        The regular expression to use to remove extra whitespace.

    Returns
    -------
    subd : str or unicode
        `s` with all extra whitespace replaced with a single space.
    '''
    return regex.sub(' ', s.strip())


def _get_skiprows(skiprows = None):
    '''
    Get an iterator given an integer, slice or container.

    Parameters
    ----------
    skiprows : int, slice, container
        The iterator to use to skip rows; can also be a slice.

    Raises
    ------
    TypeError
        * If `skiprows` is not a slice, integer, or Container

    Returns
    -------
    it : iterable
        A proper iterator to use to skip rows of a DataFrame.
    '''
    pass
# WARNING: Decompyle incomplete


def _read(obj = None, encoding = None, storage_options = None):
    '''
    Try to read from a url, file or string.

    Parameters
    ----------
    obj : str, unicode, path object, or file-like object

    Returns
    -------
    raw_text : str
    '''
    
    try:
        handles = get_handle(obj, 'r', encoding = encoding, storage_options = storage_options)
        
        try:
            None(None, None)
            return 
            with None:
                if not None, handles.handle.read():
                    
                    try:
                        
                        try:
                            return None
                        except OSError:
                            if not is_url(obj):
                                raise FileNotFoundError(f'''[Errno {errno.ENOENT}] {os.strerror(errno.ENOENT)}: {obj}'''), err
                            raise 
                            None = None
                            del err






class _HtmlFrameParser:
    '''
    Base class for parsers that parse HTML into DataFrames.

    Parameters
    ----------
    io : str or file-like
        This can be either a string path, a valid URL using the HTTP,
        FTP, or FILE protocols or a file-like object.

    match : str or regex
        The text to match in the document.

    attrs : dict
        List of HTML <table> element attributes to match.

    encoding : str
        Encoding to be used by parser

    displayed_only : bool
        Whether or not items with "display:none" should be ignored

    extract_links : {None, "all", "header", "body", "footer"}
        Table elements in the specified section(s) with <a> tags will have their
        href extracted.

    Attributes
    ----------
    io : str or file-like
        raw HTML, URL, or file-like object

    match : regex
        The text to match in the raw HTML

    attrs : dict-like
        A dictionary of valid table attributes to use to search for table
        elements.

    encoding : str
        Encoding to be used by parser

    displayed_only : bool
        Whether or not items with "display:none" should be ignored

    extract_links : {None, "all", "header", "body", "footer"}
        Table elements in the specified section(s) with <a> tags will have their
        href extracted.

    Notes
    -----
    To subclass this class effectively you must override the following methods:
        * :func:`_build_doc`
        * :func:`_attr_getter`
        * :func:`_href_getter`
        * :func:`_text_getter`
        * :func:`_parse_td`
        * :func:`_parse_thead_tr`
        * :func:`_parse_tbody_tr`
        * :func:`_parse_tfoot_tr`
        * :func:`_parse_tables`
        * :func:`_equals_tag`
    See each method\'s respective documentation for details on their
    functionality.
    '''
    
    def __init__(self, io, match, attrs = None, encoding = None, displayed_only = None, extract_links = (None,), storage_options = ('io', 'FilePath | ReadBuffer[str] | ReadBuffer[bytes]', 'match', 'str | Pattern', 'attrs', 'dict[str, str] | None', 'encoding', 'str', 'displayed_only', 'bool', 'extract_links', "Literal['header', 'footer', 'body', 'all'] | None", 'storage_options', 'StorageOptions', 'return', 'None')):
        self.io = io
        self.match = match
        self.attrs = attrs
        self.encoding = encoding
        self.displayed_only = displayed_only
        self.extract_links = extract_links
        self.storage_options = storage_options

    
    def parse_tables(self):
        '''
        Parse and return all tables from the DOM.

        Returns
        -------
        list of parsed (header, body, footer) tuples from tables.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _attr_getter(self, obj, attr):
        '''
        Return the attribute value of an individual DOM node.

        Parameters
        ----------
        obj : node-like
            A DOM node.

        attr : str or unicode
            The attribute, such as "colspan"

        Returns
        -------
        str or unicode
            The attribute value.
        '''
        return obj.get(attr)

    
    def _href_getter(self = None, obj = None):
        '''
        Return an href if the DOM node contains a child <a> or None.

        Parameters
        ----------
        obj : node-like
            A DOM node.

        Returns
        -------
        href : str or unicode
            The href from the <a> child of the DOM node.
        '''
        raise AbstractMethodError(self)

    
    def _text_getter(self, obj):
        '''
        Return the text of an individual DOM node.

        Parameters
        ----------
        obj : node-like
            A DOM node.

        Returns
        -------
        text : str or unicode
            The text from an individual DOM node.
        '''
        raise AbstractMethodError(self)

    
    def _parse_td(self, obj):
        '''
        Return the td elements from a row element.

        Parameters
        ----------
        obj : node-like
            A DOM <tr> node.

        Returns
        -------
        list of node-like
            These are the elements of each row, i.e., the columns.
        '''
        raise AbstractMethodError(self)

    
    def _parse_thead_tr(self, table):
        '''
        Return the list of thead row elements from the parsed table element.

        Parameters
        ----------
        table : a table element that contains zero or more thead elements.

        Returns
        -------
        list of node-like
            These are the <tr> row elements of a table.
        '''
        raise AbstractMethodError(self)

    
    def _parse_tbody_tr(self, table):
        '''
        Return the list of tbody row elements from the parsed table element.

        HTML5 table bodies consist of either 0 or more <tbody> elements (which
        only contain <tr> elements) or 0 or more <tr> elements. This method
        checks for both structures.

        Parameters
        ----------
        table : a table element that contains row elements.

        Returns
        -------
        list of node-like
            These are the <tr> row elements of a table.
        '''
        raise AbstractMethodError(self)

    
    def _parse_tfoot_tr(self, table):
        '''
        Return the list of tfoot row elements from the parsed table element.

        Parameters
        ----------
        table : a table element that contains row elements.

        Returns
        -------
        list of node-like
            These are the <tr> row elements of a table.
        '''
        raise AbstractMethodError(self)

    
    def _parse_tables(self, document, match, attrs):
        '''
        Return all tables from the parsed DOM.

        Parameters
        ----------
        document : the DOM from which to parse the table element.

        match : str or regular expression
            The text to search for in the DOM tree.

        attrs : dict
            A dictionary of table attributes that can be used to disambiguate
            multiple tables on a page.

        Raises
        ------
        ValueError : `match` does not match any text in the document.

        Returns
        -------
        list of node-like
            HTML <table> elements to be parsed into raw data.
        '''
        raise AbstractMethodError(self)

    
    def _equals_tag(self = None, obj = None, tag = None):
        """
        Return whether an individual DOM node matches a tag

        Parameters
        ----------
        obj : node-like
            A DOM node.

        tag : str
            Tag name to be checked for equality.

        Returns
        -------
        boolean
            Whether `obj`'s tag name is `tag`
        """
        raise AbstractMethodError(self)

    
    def _build_doc(self):
        '''
        Return a tree-like object that can be used to iterate over the DOM.

        Returns
        -------
        node-like
            The DOM from which to parse the table element.
        '''
        raise AbstractMethodError(self)

    
    def _parse_thead_tbody_tfoot(self, table_html):
        '''
        Given a table, return parsed header, body, and foot.

        Parameters
        ----------
        table_html : node-like

        Returns
        -------
        tuple of (header, body, footer), each a list of list-of-text rows.

        Notes
        -----
        Header and body are lists-of-lists. Top level list is a list of
        rows. Each row is a list of str text.

        Logic: Use <thead>, <tbody>, <tfoot> elements to identify
               header, body, and footer, otherwise:
               - Put all rows into body
               - Move rows from top of body to header only if
                 all elements inside row are <th>
               - Move rows from bottom of body to footer only if
                 all elements inside row are <th>
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _expand_colspan_rowspan(self = None, rows = None, section = None, remainder = (None, True), overflow = ('section', "Literal['header', 'footer', 'body']", 'remainder', 'list[tuple[int, str | tuple, int]] | None', 'overflow', 'bool', 'return', 'tuple[list[list], list[tuple[int, str | tuple, int]]]')):
        """
        Given a list of <tr>s, return a list of text rows.

        Parameters
        ----------
        rows : list of node-like
            List of <tr>s
        section : the section that the rows belong to (header, body or footer).
        remainder: list[tuple[int, str | tuple, int]] | None
            Any remainder from the expansion of previous section
        overflow: bool
            If true, return any partial rows as 'remainder'. If not, use up any
            partial rows. True by default.

        Returns
        -------
        list of list
            Each returned row is a list of str text, or tuple (text, link)
            if extract_links is not None.
        remainder
            Remaining partial rows if any. If overflow is False, an empty list
            is returned.

        Notes
        -----
        Any cell with ``rowspan`` or ``colspan`` will have its contents copied
        to subsequent cells.
        """
        all_texts = []
    # WARNING: Decompyle incomplete

    
    def _handle_hidden_tables(self = None, tbl_list = None, attr_name = None):
        '''
        Return list of tables, potentially removing hidden elements

        Parameters
        ----------
        tbl_list : list of node-like
            Type of list elements will vary depending upon parser used
        attr_name : str
            Name of the accessor for retrieving HTML attributes

        Returns
        -------
        list of node-like
            Return type matches `tbl_list`
        '''
        pass
    # WARNING: Decompyle incomplete



class _BeautifulSoupHtml5LibFrameParser(_HtmlFrameParser):
    '''
    HTML to DataFrame parser that uses BeautifulSoup under the hood.

    See Also
    --------
    pandas.io.html._HtmlFrameParser
    pandas.io.html._LxmlFrameParser

    Notes
    -----
    Documentation strings for this class are in the base class
    :class:`pandas.io.html._HtmlFrameParser`.
    '''
    
    def _parse_tables(self, document, match, attrs):
        element_name = 'table'
        tables = document.find_all(element_name, attrs = attrs)
        if not tables:
            raise ValueError('No tables found')
        result = []
        unique_tables = set()
        tables = self._handle_hidden_tables(tables, 'attrs')
    # WARNING: Decompyle incomplete

    
    def _href_getter(self = None, obj = None):
        a = obj.find('a', href = True)
        return None if not a else a['href']

    
    def _text_getter(self, obj):
        return obj.text

    
    def _equals_tag(self = None, obj = None, tag = None):
        return obj.name == tag

    
    def _parse_td(self, row):
        return row.find_all(('td', 'th'), recursive = False)

    
    def _parse_thead_tr(self, table):
        return table.select('thead tr')

    
    def _parse_tbody_tr(self, table):
        from_tbody = table.select('tbody tr')
        from_root = table.find_all('tr', recursive = False)
        return from_tbody + from_root

    
    def _parse_tfoot_tr(self, table):
        return table.select('tfoot tr')

    
    def _setup_build_doc(self):
        raw_text = _read(self.io, self.encoding, self.storage_options)
        if not raw_text:
            raise ValueError(f'''No text parsed from document: {self.io}''')
        return raw_text

    
    def _build_doc(self):
        BeautifulSoup = BeautifulSoup
        import bs4
        bdoc = self._setup_build_doc()
    # WARNING: Decompyle incomplete



def _build_xpath_expr(attrs = None):
    """
    Build an xpath expression to simulate bs4's ability to pass in kwargs to
    search for attributes when using the lxml parser.

    Parameters
    ----------
    attrs : dict
        A dict of HTML attributes. These are NOT checked for validity.

    Returns
    -------
    expr : unicode
        An XPath expression that checks for the given HTML attributes.
    """
    if 'class_' in attrs:
        attrs['class'] = attrs.pop('class_')
    s = (lambda .0: [ f'''@{k}={v!r}''' for k, v in .0 ])(attrs.items()())
    return f'''[{s}]'''

_re_namespace = {
    're': 'http://exslt.org/regular-expressions' }

class _LxmlFrameParser(_HtmlFrameParser):
    '''
    HTML to DataFrame parser that uses lxml under the hood.

    Warning
    -------
    This parser can only handle HTTP, FTP, and FILE urls.

    See Also
    --------
    _HtmlFrameParser
    _BeautifulSoupLxmlFrameParser

    Notes
    -----
    Documentation strings for this class are in the base class
    :class:`_HtmlFrameParser`.
    '''
    
    def _href_getter(self = None, obj = None):
        href = obj.xpath('.//a/@href')
        return None if not href else href[0]

    
    def _text_getter(self, obj):
        return obj.text_content()

    
    def _parse_td(self, row):
        return row.xpath('./td|./th')

    
    def _parse_tables(self, document, match, kwargs):
        pattern = match.pattern
        xpath_expr = f'''//table[.//text()[re:test(., {pattern!r})]]'''
        if kwargs:
            xpath_expr += _build_xpath_expr(kwargs)
        tables = document.xpath(xpath_expr, namespaces = _re_namespace)
        tables = self._handle_hidden_tables(tables, 'attrib')
        if self.displayed_only:
            for table in tables:
                for elem in table.xpath('.//style'):
                    elem.drop_tree()
                    for elem in table.xpath('.//*[@style]'):
                        if 'display:none' in elem.attrib.get('style', '').replace(' ', ''):
                            elem.drop_tree()
                        if not tables:
                            raise ValueError(f'''No tables found matching regex {pattern!r}''')
                        return tables

    
    def _equals_tag(self = None, obj = None, tag = None):
        return obj.tag == tag

    
    def _build_doc(self):
