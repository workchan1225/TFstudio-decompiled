# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: xml.pyc (Python 3.11)

'''
:mod:`pandas.io.formats.xml` is a module for formatting data in XML.
'''
from __future__ import annotations
import codecs
import io
from typing import TYPE_CHECKING, Any, final
from pandas.errors import AbstractMethodError
from pandas.util._decorators import cache_readonly
from pandas.core.dtypes.common import is_list_like
from pandas.core.dtypes.missing import isna
from pandas.io.common import get_handle
from pandas.io.xml import get_data_from_filepath
if TYPE_CHECKING:
    from pandas._typing import CompressionOptions, FilePath, ReadBuffer, StorageOptions, WriteBuffer
    from pandas import DataFrame

class _BaseXMLFormatter:
    '''
    Subclass for formatting data in XML.

    Parameters
    ----------
    path_or_buffer : str or file-like
        This can be either a string of raw XML, a valid URL,
        file or file-like object.

    index : bool
        Whether to include index in xml document.

    row_name : str
        Name for root of xml document. Default is \'data\'.

    root_name : str
        Name for row elements of xml document. Default is \'row\'.

    na_rep : str
        Missing data representation.

    attrs_cols : list
        List of columns to write as attributes in row element.

    elem_cols : list
        List of columns to write as children in row element.

    namespaces : dict
        The namespaces to define in XML document as dicts with key
        being namespace and value the URI.

    prefix : str
        The prefix for each element in XML document including root.

    encoding : str
        Encoding of xml object or document.

    xml_declaration : bool
        Whether to include xml declaration at top line item in xml.

    pretty_print : bool
        Whether to write xml document with line breaks and indentation.

    stylesheet : str or file-like
        A URL, file, file-like object, or a raw string containing XSLT.

    compression : str or dict, default \'infer\'
        For on-the-fly compression of the output data. If \'infer\' and \'path_or_buffer\'
        is path-like, then detect compression from the following extensions: \'.gz\',
        \'.bz2\', \'.zip\', \'.xz\', \'.zst\', \'.tar\', \'.tar.gz\', \'.tar.xz\' or \'.tar.bz2\'
        (otherwise no compression).
        Set to ``None`` for no compression.
        Can also be a dict with key ``\'method\'`` set
        to one of {``\'zip\'``, ``\'gzip\'``, ``\'bz2\'``, ``\'zstd\'``, ``\'xz\'``, ``\'tar\'``}
        and other key-value pairs are forwarded to
        ``zipfile.ZipFile``, ``gzip.GzipFile``,
        ``bz2.BZ2File``, ``zstandard.ZstdCompressor``, ``lzma.LZMAFile`` or
        ``tarfile.TarFile``, respectively.
        As an example, the following could be passed for faster compression and to
        create a reproducible gzip archive:
        ``compression={\'method\': \'gzip\', \'compresslevel\': 1, \'mtime\': 1}``.

    storage_options : dict, optional
        Extra options that make sense for a particular storage connection, e.g.
        host, port, username, password, etc. For HTTP(S) URLs the key-value pairs
        are forwarded to ``urllib.request.Request`` as header options. For other
        URLs (e.g. starting with "s3://", and "gcs://") the key-value pairs are
        forwarded to ``fsspec.open``. Please see ``fsspec`` and ``urllib`` for more
        details, and for more examples on storage options refer `here
        <https://pandas.pydata.org/docs/user_guide/io.html?
        highlight=storage_options#reading-writing-remote-files>`_.

    See also
    --------
    pandas.io.formats.xml.EtreeXMLFormatter
    pandas.io.formats.xml.LxmlXMLFormatter

    '''
    
    def __init__(self, frame, path_or_buffer, index, root_name, row_name, na_rep, attr_cols, elem_cols, namespaces, prefix, encoding, xml_declaration = None, pretty_print = None, stylesheet = None, compression = (None, True, 'data', 'row', None, None, None, None, None, 'utf-8', True, True, None, 'infer', None), storage_options = ('frame', 'DataFrame', 'path_or_buffer', 'FilePath | WriteBuffer[bytes] | WriteBuffer[str] | None', 'index', 'bool', 'root_name', 'str | None', 'row_name', 'str | None', 'na_rep', 'str | None', 'attr_cols', 'list[str] | None', 'elem_cols', 'list[str] | None', 'namespaces', 'dict[str | None, str] | None', 'prefix', 'str | None', 'encoding', 'str', 'xml_declaration', 'bool | None', 'pretty_print', 'bool | None', 'stylesheet', 'FilePath | ReadBuffer[str] | ReadBuffer[bytes] | None', 'compression', 'CompressionOptions', 'storage_options', 'StorageOptions | None', 'return', 'None')):
        self.frame = frame
        self.path_or_buffer = path_or_buffer
        self.index = index
        self.root_name = root_name
        self.row_name = row_name
        self.na_rep = na_rep
        self.attr_cols = attr_cols
        self.elem_cols = elem_cols
        self.namespaces = namespaces
        self.prefix = prefix
        self.encoding = encoding
        self.xml_declaration = xml_declaration
        self.pretty_print = pretty_print
        self.stylesheet = stylesheet
        self.compression = compression
        self.storage_options = storage_options
        self.orig_cols = self.frame.columns.tolist()
        self.frame_dicts = self._process_dataframe()
        self._validate_columns()
        self._validate_encoding()
        self.prefix_uri = self._get_prefix_uri()
        self._handle_indexes()

    
    def _build_tree(self = None):
        '''
        Build tree from  data.

        This method initializes the root and builds attributes and elements
        with optional namespaces.
        '''
        raise AbstractMethodError(self)

    _validate_columns = (lambda self = None: if not self.attr_cols and is_list_like(self.attr_cols):
raise TypeError(f'''{type(self.attr_cols).__name__} is not a valid type for attr_cols''')if not self.elem_cols or is_list_like(self.elem_cols):
raise TypeError(f'''{type(self.elem_cols).__name__} is not a valid type for elem_cols''')None)()
    _validate_encoding = (lambda self = None: codecs.lookup(self.encoding))()
    _process_dataframe = (lambda self = None: df = self.frameif self.index:
df = df.reset_index()# WARNING: Decompyle incomplete
)()
    _handle_indexes = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def _get_prefix_uri(self = None):
        '''
        Get uri of namespace prefix.

        This method retrieves corresponding URI to prefix in namespaces.

        Raises
        ------
        KeyError
            *If prefix is not included in namespace dict.
        '''
        raise AbstractMethodError(self)

    _other_namespaces = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    _build_attribs = (lambda self = None, d = None, elem_row = final: if not self.attr_cols:
elem_rowfor col in None.attr_cols:
attr_name = self._get_flat_col_name(col)if not isna(d[col]):
elem_row.attrib[attr_name] = str(d[col])except KeyError:
err = Noneraise KeyError(f'''no valid column, {col}'''), errerr = Nonedel errelem_row)()
    _get_flat_col_name = (lambda self = None, col = None: flat_col = colif isinstance(col, tuple):
flat_col = '_'.join if '' in col else (lambda .0: [ str(c) for c in .0 ])(col()).strip()
        return f'''{self.prefix_uri}{flat_col}'''
)()
    _sub_element_cls = (lambda self: raise AbstractMethodError(self))()
    _build_elems = (lambda self = None, d = cache_readonly, elem_row = final: sub_element_cls = self._sub_element_clsif not self.elem_cols:
Nonefor col in None.elem_cols:
elem_name = self._get_flat_col_name(col)val = None if isna(d[col]) or d[col] == '' else str(d[col])sub_element_cls(elem_row, elem_name).text = valexcept KeyError:
err = Noneraise KeyError(f'''no valid column, {col}'''), errerr = Nonedel errNone)()
    write_output = (lambda self = None: xml_doc = self._build_tree()# WARNING: Decompyle incomplete
)()


class EtreeXMLFormatter(_BaseXMLFormatter):
    '''
    Class for formatting data in xml using Python standard library
    modules: `xml.etree.ElementTree` and `xml.dom.minidom`.
    '''
    
    def _build_tree(self = None):
        Element = Element
        SubElement = SubElement
        tostring = tostring
        import xml.etree.ElementTree
        self.root = Element(f'''{self.prefix_uri}{self.root_name}''', attrib = self._other_namespaces())
        for d in self.frame_dicts.values():
            elem_row = SubElement(self.root, f'''{self.prefix_uri}{self.row_name}''')
            if not self.attr_cols and self.elem_cols:
                self.elem_cols = list(d.keys())
                self._build_elems(d, elem_row)
                continue
            elem_row = self._build_attribs(d, elem_row)
            self._build_elems(d, elem_row)
            self.out_xml = tostring(self.root, method = 'xml', encoding = self.encoding, xml_declaration = self.xml_declaration)
            if self.pretty_print:
                self.out_xml = self._prettify_tree()
    # WARNING: Decompyle incomplete

    
    def _get_prefix_uri(self = None):
        register_namespace = register_namespace
        import xml.etree.ElementTree
        uri = ''
        if self.namespaces:
            for p, n in self.namespaces.items():
                if isinstance(p, str) and isinstance(n, str):
                    register_namespace(p, n)
                if self.prefix:
                    
                    try:
                        uri = f'''{{{self.namespaces[self.prefix]}}}'''
                    except KeyError:
                        err = None
                        raise KeyError(f'''{self.prefix} is not included in namespaces'''), err
                        err = None
                        del err

        return uri

    _sub_element_cls = (lambda self: SubElement = SubElementimport xml.etree.ElementTreeSubElement)()
    
    def _prettify_tree(self = None):
        '''
        Output tree for pretty print format.

        This method will pretty print xml with line breaks and indentation.
        '''
        parseString = parseString
        import xml.dom.minidom
        dom = parseString(self.out_xml)
        return dom.toprettyxml(indent = '  ', encoding = self.encoding)



class LxmlXMLFormatter(_BaseXMLFormatter):
    pass
# WARNING: Decompyle incomplete
