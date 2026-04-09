# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: xml.pyc (Python 3.11)

'''
:mod:``pandas.io.xml`` is a module for reading XML.
'''
from __future__ import annotations
import io
from os import PathLike
from typing import TYPE_CHECKING, Any
from pandas._libs import lib
from pandas.compat._optional import import_optional_dependency
from pandas.errors import AbstractMethodError, ParserError
from pandas.util._decorators import set_module
from pandas.util._validators import check_dtype_backend
from pandas.core.dtypes.common import is_list_like
from pandas.io.common import get_handle, infer_compression, is_fsspec_url, is_url, stringify_path
from pandas.io.parsers import TextParser
if TYPE_CHECKING:
    from collections.abc import Callable, Sequence
    from xml.etree.ElementTree import Element
    from lxml import etree
    from pandas._typing import CompressionOptions, ConvertersArg, DtypeArg, DtypeBackend, FilePath, ParseDatesArg, ReadBuffer, StorageOptions, XMLParsers
    from pandas import DataFrame

class _XMLFrameParser:
    '''
    Internal subclass to parse XML into DataFrames.

    Parameters
    ----------
    path_or_buffer : a valid JSON ``str``, path object or file-like object
        Any valid string path is acceptable. The string could be a URL. Valid
        URL schemes include http, ftp, s3, and file.

    xpath : str or regex
        The ``XPath`` expression to parse required set of nodes for
        migration to :class:`~pandas.DataFrame`. ``etree`` supports limited ``XPath``.

    namespaces : dict
        The namespaces defined in XML document (``xmlns:namespace=\'URI\'``)
        as dicts with key being namespace and value the URI.

    elems_only : bool
        Parse only the child elements at the specified ``xpath``.

    attrs_only : bool
        Parse only the attributes at the specified ``xpath``.

    names : list
        Column names for :class:`~pandas.DataFrame` of parsed XML data.

    dtype : dict
        Data type for data or columns. E.g. {{\'a\': np.float64,
        \'b\': np.int32, \'c\': \'Int64\'}}

    converters : dict, optional
        Dict of functions for converting values in certain columns. Keys can
        either be integers or column labels.

    parse_dates : bool or list of int or names or list of lists or dict
        Converts either index or select columns to datetimes

    encoding : str
        Encoding of xml object or document.

    stylesheet : str or file-like
        URL, file, file-like object, or a raw string containing XSLT,
        ``etree`` does not support XSLT but retained for consistency.

    iterparse : dict, optional
        Dict with row element as key and list of descendant elements
        and/or attributes as value to be retrieved in iterparsing of
        XML document.

    compression : str or dict, default \'infer\'
        For on-the-fly decompression of on-disk data. If \'infer\' and
        \'path_or_buffer\' is path-like, then detect compression from the
        following extensions: \'.gz\', \'.bz2\', \'.zip\', \'.xz\', \'.zst\', \'.tar\',
        \'.tar.gz\', \'.tar.xz\' or \'.tar.bz2\' (otherwise no compression).
        If using \'zip\' or \'tar\', the ZIP file must contain only one data
        file to be read in. Set to ``None`` for no decompression.
        Can also be a dict with key ``\'method\'`` set to one of
        {``\'zip\'``, ``\'gzip\'``, ``\'bz2\'``, ``\'zstd\'``, ``\'xz\'``, ``\'tar\'``}
        and other key-value pairs are forwarded to ``zipfile.ZipFile``,
        ``gzip.GzipFile``, ``bz2.BZ2File``, ``zstandard.ZstdDecompressor``,
        ``lzma.LZMAFile`` or ``tarfile.TarFile``, respectively.
        As an example, the following could be passed for Zstandard
        decompression using a custom compression dictionary:
        ``compression={\'method\': \'zstd\', \'dict_data\': my_compression_dict}``.

    storage_options : dict, optional
        Extra options that make sense for a particular storage connection,
        e.g. host, port, username, password, etc. For HTTP(S) URLs the
        key-value pairs are forwarded to ``urllib.request.Request`` as header
        options. For other URLs (e.g. starting with "s3://", and "gcs://")
        the key-value pairs are forwarded to ``fsspec.open``. Please see
        ``fsspec`` and ``urllib`` for more details, and for more examples on
        storage options refer `here <https://pandas.pydata.org/docs/
        user_guide/io.html?highlight=storage_options#reading-writing-remote-
        files>`_.

    See also
    --------
    pandas.io.xml._EtreeFrameParser
    pandas.io.xml._LxmlFrameParser

    Notes
    -----
    To subclass this class effectively you must override the following methods:`
        * :func:`parse_data`
        * :func:`_parse_nodes`
        * :func:`_iterparse_nodes`
        * :func:`_parse_doc`
        * :func:`_validate_names`
        * :func:`_validate_path`


    See each method\'s respective documentation for details on their
    functionality.
    '''
    
    def __init__(self, path_or_buffer, xpath, namespaces, elems_only, attrs_only, names, dtype, converters, parse_dates, encoding, stylesheet = None, iterparse = None, compression = None, storage_options = ('path_or_buffer', 'FilePath | ReadBuffer[bytes] | ReadBuffer[str]', 'xpath', 'str', 'namespaces', 'dict[str, str] | None', 'elems_only', 'bool', 'attrs_only', 'bool', 'names', 'Sequence[str] | None', 'dtype', 'DtypeArg | None', 'converters', 'ConvertersArg | None', 'parse_dates', 'ParseDatesArg | None', 'encoding', 'str | None', 'stylesheet', 'FilePath | ReadBuffer[bytes] | ReadBuffer[str] | None', 'iterparse', 'dict[str, list[str]] | None', 'compression', 'CompressionOptions', 'storage_options', 'StorageOptions', 'return', 'None')):
        self.path_or_buffer = path_or_buffer
        self.xpath = xpath
        self.namespaces = namespaces
        self.elems_only = elems_only
        self.attrs_only = attrs_only
        self.names = names
        self.dtype = dtype
        self.converters = converters
        self.parse_dates = parse_dates
        self.encoding = encoding
        self.stylesheet = stylesheet
        self.iterparse = iterparse
        self.compression = compression
        self.storage_options = storage_options

    
    def parse_data(self = None):
        '''
        Parse xml data.

        This method will call the other internal methods to
        validate ``xpath``, names, parse and return specific nodes.
        '''
        raise AbstractMethodError(self)

    
    def _parse_nodes(self = None, elems = None):
        '''
        Parse xml nodes.

        This method will parse the children and attributes of elements
        in ``xpath``, conditionally for only elements, only attributes
        or both while optionally renaming node names.

        Raises
        ------
        ValueError
            * If only elements and only attributes are specified.

        Notes
        -----
        Namespace URIs will be removed from return node values. Also,
        elements with missing children or attributes compared to siblings
        will have optional keys filled with None values.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _iterparse_nodes(self = None, iterparse = None):
        '''
        Iterparse xml nodes.

        This method will read in local disk, decompressed XML files for elements
        and underlying descendants using iterparse, a method to iterate through
        an XML tree without holding entire XML tree in memory.

        Raises
        ------
        TypeError
            * If ``iterparse`` is not a dict or its dict value is not list-like.
        ParserError
            * If ``path_or_buffer`` is not a physical file on disk or file-like object.
            * If no data is returned from selected items in ``iterparse``.

        Notes
        -----
        Namespace URIs will be removed from return node values. Also,
        elements with missing children or attributes in submitted list
        will have optional keys filled with None values.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _validate_path(self = None):
        '''
        Validate ``xpath``.

        This method checks for syntax, evaluation, or empty nodes return.

        Raises
        ------
        SyntaxError
            * If xpah is not supported or issues with namespaces.

        ValueError
            * If xpah does not return any nodes.
        '''
        raise AbstractMethodError(self)

    
    def _validate_names(self = None):
        '''
        Validate names.

        This method will check if names is a list-like and aligns
        with length of parse nodes.

        Raises
        ------
        ValueError
            * If value is not a list and less then length of nodes.
        '''
        raise AbstractMethodError(self)

    
    def _parse_doc(self = None, raw_doc = None):
        '''
        Build tree from path_or_buffer.

        This method will parse XML object into tree
        either from string/bytes or file location.
        '''
        raise AbstractMethodError(self)



class _EtreeFrameParser(_XMLFrameParser):
    '''
    Internal class to parse XML into DataFrames with the Python
    standard library XML module: `xml.etree.ElementTree`.
    '''
    
    def parse_data(self = None):
        iterparse = iterparse
        import xml.etree.ElementTree
    # WARNING: Decompyle incomplete

    
    def _validate_path(self = None):
        '''
        Notes
        -----
        ``etree`` supports limited ``XPath``. If user attempts a more complex
        expression syntax error will raise.
        '''
        msg = 'xpath does not return any nodes or attributes. Be sure to specify in `xpath` the parent nodes of children and attributes to parse. If document uses namespaces denoted with xmlns, be sure to define namespaces and use them in xpath.'
    # WARNING: Decompyle incomplete

    
    def _validate_names(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _parse_doc(self = None, raw_doc = None):
        XMLParser = XMLParser
        parse = parse
        import xml.etree.ElementTree
        handle_data = get_data_from_filepath(filepath_or_buffer = raw_doc, encoding = self.encoding, compression = self.compression, storage_options = self.storage_options)
        xml_data = handle_data
        curr_parser = XMLParser(encoding = self.encoding)
        document = parse(xml_data, parser = curr_parser)
        None(None, None)



class _LxmlFrameParser(_XMLFrameParser):
    '''
    Internal class to parse XML into :class:`~pandas.DataFrame` with third-party
    full-featured XML library, ``lxml``, that supports
    ``XPath`` 1.0 and XSLT 1.0.
    '''
    
    def parse_data(self = None):
        '''
        Parse xml data.

        This method will call the other internal methods to
        validate ``xpath``, names, optionally parse and run XSLT,
        and parse original or transformed XML and return specific nodes.
        '''
        iterparse = iterparse
        import lxml.etree
    # WARNING: Decompyle incomplete

    
    def _validate_path(self = None):
        msg = 'xpath does not return any nodes or attributes. Be sure to specify in `xpath` the parent nodes of children and attributes to parse. If document uses namespaces denoted with xmlns, be sure to define namespaces and use them in xpath.'
        elems = self.xml_doc.xpath(self.xpath, namespaces = self.namespaces)
        children = elems()
        attrs = elems()
        if elems == []:
            raise ValueError(msg)
        if elems != []:
            if self.elems_only and children == []:
                raise ValueError(msg)
            if self.attrs_only and attrs == { }:
                raise ValueError(msg)
            if children == [] and attrs == { }:
                raise ValueError(msg)
        return elems

    
    def _validate_names(self = None):
        if self.names:
            if self.iterparse:
                children = self.iterparse[next(iter(self.iterparse))]
            else:
                children = self.xml_doc.xpath(self.xpath + '[1]/*', namespaces = self.namespaces)
            if is_list_like(self.names):
                if len(self.names) < len(children):
                    raise ValueError('names does not match length of child elements in xpath.')
                return None
            raise None(f'''{type(self.names).__name__} is not a valid type for names''')

    
    def _parse_doc(self = None, raw_doc = None):
        XMLParser = XMLParser
        fromstring = fromstring
        parse = parse
        import lxml.etree
        handle_data = get_data_from_filepath(filepath_or_buffer = raw_doc, encoding = self.encoding, compression = self.compression, storage_options = self.storage_options)
        xml_data = handle_data
        curr_parser = XMLParser(encoding = self.encoding)
    # WARNING: Decompyle incomplete

    
    def _transform_doc(self = None):
        '''
        Transform original tree using stylesheet.

        This method will transform original xml using XSLT script into
        am ideally flatter xml document for easier parsing and migration
        to Data Frame.
        '''
        XSLT = XSLT
        import lxml.etree
        transformer = XSLT(self.xsl_doc)
        new_doc = transformer(self.xml_doc)
        return new_doc



def get_data_from_filepath(filepath_or_buffer = None, encoding = None, compression = None, storage_options = ('filepath_or_buffer', 'FilePath | ReadBuffer[bytes] | ReadBuffer[str]', 'encoding', 'str | None', 'compression', 'CompressionOptions', 'storage_options', 'StorageOptions')):
    '''
    Extract raw XML data.

    The method accepts two input types:
        1. filepath (string-like)
        2. file-like object (e.g. open file object, StringIO)
    '''
    filepath_or_buffer = stringify_path(filepath_or_buffer)
    handle_obj = get_handle(filepath_or_buffer, 'r', encoding = encoding, compression = compression, storage_options = storage_options)
    None(None, None)
    return 
    with None:
        if not None, preprocess_data(handle_obj.handle.read()) if hasattr(handle_obj.handle, 'read') else handle_obj.handle:
            pass


def preprocess_data(data = None):
    '''
    Convert extracted raw data.

    This method will return underlying data of extracted XML content.
    The data either has a `read` attribute (e.g. a file object or a
    StringIO/BytesIO) or is a string or bytes that is an XML document.
    '''
    if isinstance(data, str):
        data = io.StringIO(data)
    elif isinstance(data, bytes):
        data = io.BytesIO(data)
    return data


def _data_to_frame(data = None, **kwargs):
    '''
    Convert parsed data to Data Frame.

    This method will bind xml dictionary data of keys and values
    into named columns of Data Frame using the built-in TextParser
    class that build Data Frame and infers specific dtypes.
    '''
    tags = next(iter(data))
    nodes = data()
# WARNING: Decompyle incomplete


def _parse(path_or_buffer, xpath, namespaces, elems_only, attrs_only, names, dtype, converters, parse_dates, encoding, parser, stylesheet = None, iterparse = None, compression = None, storage_options = (lib.no_default,), dtype_backend = ('path_or_buffer', 'FilePath | ReadBuffer[bytes] | ReadBuffer[str]', 'xpath', 'str', 'namespaces', 'dict[str, str] | None', 'elems_only', 'bool', 'attrs_only', 'bool', 'names', 'Sequence[str] | None', 'dtype', 'DtypeArg | None', 'converters', 'ConvertersArg | None', 'parse_dates', 'ParseDatesArg | None', 'encoding', 'str | None', 'parser', 'XMLParsers', 'stylesheet', 'FilePath | ReadBuffer[bytes] | ReadBuffer[str] | None', 'iterparse', 'dict[str, list[str]] | None', 'compression', 'CompressionOptions', 'storage_options', 'StorageOptions', 'dtype_backend', 'DtypeBackend | lib.NoDefault', 'return', 'DataFrame'), **kwargs):
    '''
    Call internal parsers.

    This method will conditionally call internal parsers:
    LxmlFrameParser and/or EtreeParser.

    Raises
    ------
    ImportError
        * If lxml is not installed if selected as parser.

    ValueError
        * If parser is not lxml or etree.
    '''
    pass
# WARNING: Decompyle incomplete

read_xml = (lambda path_or_buffer = None, *, xpath: check_dtype_backend(dtype_backend)# WARNING: Decompyle incomplete
)()
