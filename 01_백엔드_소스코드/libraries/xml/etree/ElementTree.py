# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ElementTree.pyc (Python 3.11)

"""Lightweight XML support for Python.

 XML is an inherently hierarchical data format, and the most natural way to
 represent it is with a tree.  This module has two classes for this purpose:

    1. ElementTree represents the whole XML document as a tree and

    2. Element represents a single node in this tree.

 Interactions with the whole document (reading and writing to/from files) are
 usually done on the ElementTree level.  Interactions with a single XML element
 and its sub-elements are done on the Element level.

 Element is a flexible container object designed to store hierarchical data
 structures in memory. It can be described as a cross between a list and a
 dictionary.  Each Element has a number of properties associated with it:

    'tag' - a string containing the element's name.

    'attributes' - a Python dictionary storing the element's attributes.

    'text' - a string containing the element's text content.

    'tail' - an optional string containing text after the element's end tag.

    And a number of child elements stored in a Python sequence.

 To create an element instance, use the Element constructor,
 or the SubElement factory function.

 You can also use the ElementTree class to wrap an element structure
 and convert it to and from XML.

"""
__all__ = [
    'Comment',
    'dump',
    'Element',
    'ElementTree',
    'fromstring',
    'fromstringlist',
    'indent',
    'iselement',
    'iterparse',
    'parse',
    'ParseError',
    'PI',
    'ProcessingInstruction',
    'QName',
    'SubElement',
    'tostring',
    'tostringlist',
    'TreeBuilder',
    'VERSION',
    'XML',
    'XMLID',
    'XMLParser',
    'XMLPullParser',
    'register_namespace',
    'canonicalize',
    'C14NWriterTarget']
VERSION = '1.3.0'
import sys
import re
import warnings
import io
import collections
import collections.abc as collections
import contextlib
import weakref
from  import ElementPath

class ParseError(SyntaxError):
    """An error when parsing an XML document.

    In addition to its exception value, a ParseError contains
    two extra attributes:
        'code'     - the specific exception code
        'position' - the line and column of the error

    """
    pass


def iselement(element):
    '''Return True if *element* appears to be an Element.'''
    return hasattr(element, 'tag')


class Element:
    """An XML element.

    This class is the reference implementation of the Element interface.

    An element's length is its number of subelements.  That means if you
    want to check if an element is truly empty, you should check BOTH
    its length AND its text attribute.

    The element tag, attribute names, and attribute values can be either
    bytes or strings.

    *tag* is the element name.  *attrib* is an optional dictionary containing
    element attributes. *extra* are additional element attributes given as
    keyword arguments.

    Example form:
        <tag attrib>text<child/>...</tag>tail

    """
    tag = None
    attrib = None
    text = None
    tail = None
    
    def __init__(self, tag, attrib = ({ },), **extra):
        if not isinstance(attrib, dict):
            raise TypeError(f'''attrib must be dict, not {attrib.__class__.__name__!s}''')
        self.tag = tag
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return '<%s %r at %#x>' % (self.__class__.__name__, self.tag, id(self))

    
    def makeelement(self, tag, attrib):
        '''Create a new element with the same type.

        *tag* is a string containing the element name.
        *attrib* is a dictionary containing the element attributes.

        Do not call this method, use the SubElement factory function instead.

        '''
        return self.__class__(tag, attrib)

    
    def copy(self):
        '''Return copy of current element.

        This creates a shallow copy. Subelements will be shared with the
        original tree.

        '''
        warnings.warn('elem.copy() is deprecated. Use copy.copy(elem) instead.', DeprecationWarning)
        return self.__copy__()

    
    def __copy__(self):
        elem = self.makeelement(self.tag, self.attrib)
        elem.text = self.text
        elem.tail = self.tail
        elem[:] = self
        return elem

    
    def __len__(self):
        return len(self._children)

    
    def __bool__(self):
        warnings.warn("The behavior of this method will change in future versions.  Use specific 'len(elem)' or 'elem is not None' test instead.", FutureWarning, stacklevel = 2)
        return len(self._children) != 0

    
    def __getitem__(self, index):
        return self._children[index]

    
    def __setitem__(self, index, element):
        if isinstance(index, slice):
            for elt in element:
                self._assert_is_element(elt)
        else:
            self._assert_is_element(element)
        self._children[index] = element

    
    def __delitem__(self, index):
        del self._children[index]

    
    def append(self, subelement):
        """Add *subelement* to the end of this element.

        The new element will appear in document order after the last existing
        subelement (or directly after the text, if it's the first subelement),
        but before the end tag for this element.

        """
        self._assert_is_element(subelement)
        self._children.append(subelement)

    
    def extend(self, elements):
        '''Append subelements from a sequence.

        *elements* is a sequence with zero or more elements.

        '''
        for element in elements:
            self._assert_is_element(element)
            self._children.append(element)
            return None

    
    def insert(self, index, subelement):
        '''Insert *subelement* at position *index*.'''
        self._assert_is_element(subelement)
        self._children.insert(index, subelement)

    
    def _assert_is_element(self, e):
        if not isinstance(e, _Element_Py):
            raise TypeError('expected an Element, not %s' % type(e).__name__)

    
    def remove(self, subelement):
        '''Remove matching subelement.

        Unlike the find methods, this method compares elements based on
        identity, NOT ON tag value or contents.  To remove subelements by
        other means, the easiest way is to use a list comprehension to
        select what elements to keep, and then use slice assignment to update
        the parent element.

        ValueError is raised if a matching element could not be found.

        '''
        self._children.remove(subelement)

    
    def find(self, path, namespaces = (None,)):
        '''Find first matching element by tag name or path.

        *path* is a string having either an element tag or an XPath,
        *namespaces* is an optional mapping from namespace prefix to full name.

        Return the first matching element, or None if no element was found.

        '''
        return ElementPath.find(self, path, namespaces)

    
    def findtext(self, path, default, namespaces = (None, None)):
        '''Find text for first matching element by tag name or path.

        *path* is a string having either an element tag or an XPath,
        *default* is the value to return if the element was not found,
        *namespaces* is an optional mapping from namespace prefix to full name.

        Return text content of first matching element, or default value if
        none was found.  Note that if an element is found having no text
        content, the empty string is returned.

        '''
        return ElementPath.findtext(self, path, default, namespaces)

    
    def findall(self, path, namespaces = (None,)):
        '''Find all matching subelements by tag name or path.

        *path* is a string having either an element tag or an XPath,
        *namespaces* is an optional mapping from namespace prefix to full name.

        Returns list containing all matching elements in document order.

        '''
        return ElementPath.findall(self, path, namespaces)

    
    def iterfind(self, path, namespaces = (None,)):
        '''Find all matching subelements by tag name or path.

        *path* is a string having either an element tag or an XPath,
        *namespaces* is an optional mapping from namespace prefix to full name.

        Return an iterable yielding all matching elements in document order.

        '''
        return ElementPath.iterfind(self, path, namespaces)

    
    def clear(self):
        '''Reset element.

        This function removes all subelements, clears all attributes, and sets
        the text and tail attributes to None.

        '''
        self.attrib.clear()
        self._children = []
        self.text = None
        self.tail = None

    
    def get(self, key, default = (None,)):
        '''Get element attribute.

        Equivalent to attrib.get, but some implementations may handle this a
        bit more efficiently.  *key* is what attribute to look for, and
        *default* is what to return if the attribute was not found.

        Returns a string containing the attribute value, or the default if
        attribute was not found.

        '''
        return self.attrib.get(key, default)

    
    def set(self, key, value):
        '''Set element attribute.

        Equivalent to attrib[key] = value, but some implementations may handle
        this a bit more efficiently.  *key* is what attribute to set, and
        *value* is the attribute value to set it to.

        '''
        self.attrib[key] = value

    
    def keys(self):
        '''Get list of attribute names.

        Names are returned in an arbitrary order, just like an ordinary
        Python dict.  Equivalent to attrib.keys()

        '''
        return self.attrib.keys()

    
    def items(self):
        '''Get element attributes as a sequence.

        The attributes are returned in arbitrary order.  Equivalent to
        attrib.items().

        Return a list of (name, value) tuples.

        '''
        return self.attrib.items()

    
    def iter(self, tag = (None,)):
        '''Create tree iterator.

        The iterator loops over the element and all subelements in document
        order, returning all elements with a matching tag.

        If the tree structure is modified during iteration, new or removed
        elements may or may not be included.  To get a stable set, use the
        list() function on the iterator, and loop over the resulting list.

        *tag* is what tags to look for (default is to return all elements)

        Return an iterator containing all the matching elements.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def itertext(self):
        '''Create text iterator.

        The iterator loops over the element and all subelements in document
        order, returning all inner text.

        '''
        pass
    # WARNING: Decompyle incomplete



def SubElement(parent, tag, attrib = ({ },), **extra):
    '''Subelement factory which creates an element instance, and appends it
    to an existing parent.

    The element tag, attribute names, and attribute values can be either
    bytes or Unicode strings.

    *parent* is the parent element, *tag* is the subelements name, *attrib* is
    an optional directory containing element attributes, *extra* are
    additional attributes given as keyword arguments.

    '''
    pass
# WARNING: Decompyle incomplete


def Comment(text = (None,)):
    '''Comment element factory.

    This function creates a special element which the standard serializer
    serializes as an XML comment.

    *text* is a string containing the comment string.

    '''
    element = Element(Comment)
    element.text = text
    return element


def ProcessingInstruction(target, text = (None,)):
    '''Processing Instruction element factory.

    This function creates a special element which the standard serializer
    serializes as an XML comment.

    *target* is a string containing the processing instruction, *text* is a
    string containing the processing instruction contents, if any.

    '''
    element = Element(ProcessingInstruction)
    element.text = target
    if text:
        element.text = element.text + ' ' + text
    return element

PI = ProcessingInstruction

class QName:
    '''Qualified name wrapper.

    This class can be used to wrap a QName attribute value in order to get
    proper namespace handing on output.

    *text_or_uri* is a string containing the QName value either in the form
    {uri}local, or if the tag argument is given, the URI part of a QName.

    *tag* is an optional argument which if given, will make the first
    argument (text_or_uri) be interpreted as a URI, and this argument (tag)
    be interpreted as a local name.

    '''
    
    def __init__(self, text_or_uri, tag = (None,)):
        if tag:
            text_or_uri = f'''{{{text_or_uri!s}}}{tag!s}'''
        self.text = text_or_uri

    
    def __str__(self):
        return self.text

    
    def __repr__(self):
        return f'''<{self.__class__.__name__!s} {self.text!r}>'''

    
    def __hash__(self):
        return hash(self.text)

    
    def __le__(self, other):
        if isinstance(other, QName):
            return self.text <= other.text
        return None.text <= other

    
    def __lt__(self, other):
        if isinstance(other, QName):
            return self.text < other.text
        return None.text < other

    
    def __ge__(self, other):
        if isinstance(other, QName):
            return self.text >= other.text
        return None.text >= other

    
    def __gt__(self, other):
        if isinstance(other, QName):
            return self.text > other.text
        return None.text > other

    
    def __eq__(self, other):
        if isinstance(other, QName):
            return self.text == other.text
        return None.text == other



class ElementTree:
    '''An XML element hierarchy.

    This class also provides support for serialization to and from
    standard XML.

    *element* is an optional root element node,
    *file* is an optional file handle or file name of an XML file whose
    contents will be used to initialize the tree with.

    '''
    
    def __init__(self, element, file = (None, None)):
        self._root = element
        if file:
            self.parse(file)
            return None

    
    def getroot(self):
        '''Return root element of this tree.'''
        return self._root

    
    def _setroot(self, element):
        '''Replace root element of this tree.

        This will discard the current contents of the tree and replace it
        with the given element.  Use with care!

        '''
        self._root = element

    
    def parse(self, source, parser = (None,)):
        '''Load external XML document into element tree.

        *source* is a file name or file object, *parser* is an optional parser
        instance that defaults to XMLParser.

        ParseError is raised if the parser fails to parse the document.

        Returns the root element of the given source document.

        '''
        close_source = False
        if not hasattr(source, 'read'):
            source = open(source, 'rb')
            close_source = True
    # WARNING: Decompyle incomplete

    
    def iter(self, tag = (None,)):
        '''Create and return tree iterator for the root element.

        The iterator loops over all elements in this tree, in document order.

        *tag* is a string with the tag name to iterate over
        (default is to return all elements).

        '''
        return self._root.iter(tag)

    
    def find(self, path, namespaces = (None,)):
        '''Find first matching element by tag name or path.

        Same as getroot().find(path), which is Element.find()

        *path* is a string having either an element tag or an XPath,
        *namespaces* is an optional mapping from namespace prefix to full name.

        Return the first matching element, or None if no element was found.

        '''
        if path[:1] == '/':
            path = '.' + path
            warnings.warn('This search is broken in 1.3 and earlier, and will be fixed in a future version.  If you rely on the current behaviour, change it to %r' % path, FutureWarning, stacklevel = 2)
        return self._root.find(path, namespaces)

    
    def findtext(self, path, default, namespaces = (None, None)):
        '''Find first matching element by tag name or path.

        Same as getroot().findtext(path),  which is Element.findtext()

        *path* is a string having either an element tag or an XPath,
        *namespaces* is an optional mapping from namespace prefix to full name.

        Return the first matching element, or None if no element was found.

        '''
        if path[:1] == '/':
            path = '.' + path
            warnings.warn('This search is broken in 1.3 and earlier, and will be fixed in a future version.  If you rely on the current behaviour, change it to %r' % path, FutureWarning, stacklevel = 2)
        return self._root.findtext(path, default, namespaces)

    
    def findall(self, path, namespaces = (None,)):
        '''Find all matching subelements by tag name or path.

        Same as getroot().findall(path), which is Element.findall().

        *path* is a string having either an element tag or an XPath,
        *namespaces* is an optional mapping from namespace prefix to full name.

        Return list containing all matching elements in document order.

        '''
        if path[:1] == '/':
            path = '.' + path
            warnings.warn('This search is broken in 1.3 and earlier, and will be fixed in a future version.  If you rely on the current behaviour, change it to %r' % path, FutureWarning, stacklevel = 2)
        return self._root.findall(path, namespaces)

    
    def iterfind(self, path, namespaces = (None,)):
        '''Find all matching subelements by tag name or path.

        Same as getroot().iterfind(path), which is element.iterfind()

        *path* is a string having either an element tag or an XPath,
        *namespaces* is an optional mapping from namespace prefix to full name.

        Return an iterable yielding all matching elements in document order.

        '''
        if path[:1] == '/':
            path = '.' + path
            warnings.warn('This search is broken in 1.3 and earlier, and will be fixed in a future version.  If you rely on the current behaviour, change it to %r' % path, FutureWarning, stacklevel = 2)
        return self._root.iterfind(path, namespaces)

    
    def write(self, file_or_filename, encoding, xml_declaration = None, default_namespace = (None, None, None, None), method = {
        'short_empty_elements': True }, *, short_empty_elements):
        '''Write element tree to a file as XML.

        Arguments:
          *file_or_filename* -- file name or a file object opened for writing

          *encoding* -- the output encoding (default: US-ASCII)

          *xml_declaration* -- bool indicating if an XML declaration should be
                               added to the output. If None, an XML declaration
                               is added if encoding IS NOT either of:
                               US-ASCII, UTF-8, or Unicode

          *default_namespace* -- sets the default XML namespace (for "xmlns")

          *method* -- either "xml" (default), "html, "text", or "c14n"

          *short_empty_elements* -- controls the formatting of elements
                                    that contain no content. If True (default)
                                    they are emitted as a single self-closed
                                    tag, otherwise they are emitted as a pair
                                    of start/end tags

        '''
        if not method:
            method = 'xml'
        elif method not in _serialize:
            raise ValueError('unknown method %r' % method)
        if not encoding:
            if method == 'c14n':
                encoding = 'utf-8'
            else:
                encoding = 'us-ascii'
        (write, declared_encoding) = _get_writer(file_or_filename, encoding)
    # WARNING: Decompyle incomplete

    
    def write_c14n(self, file):
        return self.write(file, method = 'c14n')


_get_writer = (lambda file_or_filename, encoding: pass# WARNING: Decompyle incomplete
)()

def _namespaces(elem, default_namespace = (None,)):
    pass
# WARNING: Decompyle incomplete


def _serialize_xml(write, elem, qnames, namespaces, short_empty_elements, **kwargs):
    tag = elem.tag
    text = elem.text
    if tag is Comment:
        write('<!--%s-->' % text)
    elif tag is ProcessingInstruction:
        write('<?%s?>' % text)
# WARNING: Decompyle incomplete

HTML_EMPTY = {
    'br',
    'hr',
    'col',
    'img',
    'wbr',
    'area',
    'base',
    'link',
    'meta',
    'embed',
    'frame',
    'input',
    'param',
    'track',
    'source',
    'isindex',
    'basefont'}

def _serialize_html(write, elem, qnames, namespaces, **kwargs):
    tag = elem.tag
    text = elem.text
    if tag is Comment:
        write('<!--%s-->' % _escape_cdata(text))
    elif tag is ProcessingInstruction:
        write('<?%s?>' % _escape_cdata(text))
# WARNING: Decompyle incomplete


def _serialize_text(write, elem):
    for part in elem.itertext():
        write(part)
        if elem.tail:
            write(elem.tail)
            return None
        return None

_serialize = {
    'xml': _serialize_xml,
    'html': _serialize_html,
    'text': _serialize_text }

def register_namespace(prefix, uri):
    '''Register a namespace prefix.

    The registry is global, and any existing mapping for either the
    given prefix or the namespace URI will be removed.

    *prefix* is the namespace prefix, *uri* is a namespace uri. Tags and
    attributes in this namespace will be serialized with prefix if possible.

    ValueError is raised if prefix is reserved or is invalid.

    '''
    if re.match('ns\\d+$', prefix):
        raise ValueError('Prefix format reserved for internal use')
    for k, v in list(_namespace_map.items()):
        if k == uri or v == prefix:
            del _namespace_map[k]
        _namespace_map[uri] = prefix
        return None

_namespace_map = {
    'http://www.w3.org/XML/1998/namespace': 'xml',
    'http://www.w3.org/1999/xhtml': 'html',
    'http://www.w3.org/1999/02/22-rdf-syntax-ns#': 'rdf',
    'http://schemas.xmlsoap.org/wsdl/': 'wsdl',
    'http://www.w3.org/2001/XMLSchema': 'xs',
    'http://www.w3.org/2001/XMLSchema-instance': 'xsi',
    'http://purl.org/dc/elements/1.1/': 'dc' }
register_namespace._namespace_map = _namespace_map

def _raise_serialization_error(text):
    raise TypeError(f'''cannot serialize {text!r} (type {type(text).__name__!s})''')


def _escape_cdata(text):
    
    try:
        if '&' in text:
            text = text.replace('&', '&amp;')
        if '<' in text:
            text = text.replace('<', '&lt;')
        if '>' in text:
            text = text.replace('>', '&gt;')
        return text
    except (TypeError, AttributeError):
        _raise_serialization_error(text)
        return None



def _escape_attrib(text):
    
    try:
        if '&' in text:
            text = text.replace('&', '&amp;')
        if '<' in text:
            text = text.replace('<', '&lt;')
        if '>' in text:
            text = text.replace('>', '&gt;')
        if '"' in text:
            text = text.replace('"', '&quot;')
        if '\r' in text:
            text = text.replace('\r', '&#13;')
        if '\n' in text:
            text = text.replace('\n', '&#10;')
        if '\t' in text:
            text = text.replace('\t', '&#09;')
        return text
    except (TypeError, AttributeError):
        _raise_serialization_error(text)
        return None



def _escape_attrib_html(text):
    
    try:
        if '&' in text:
            text = text.replace('&', '&amp;')
        if '>' in text:
            text = text.replace('>', '&gt;')
        if '"' in text:
            text = text.replace('"', '&quot;')
        return text
    except (TypeError, AttributeError):
        _raise_serialization_error(text)
        return None



def tostring(element = contextlib.contextmanager, encoding = (None, None), method = {
    'xml_declaration': None,
    'default_namespace': None,
    'short_empty_elements': True }, *, xml_declaration, default_namespace, short_empty_elements):
    '''Generate string representation of XML element.

    All subelements are included.  If encoding is "unicode", a string
    is returned. Otherwise a bytestring is returned.

    *element* is an Element instance, *encoding* is an optional output
    encoding defaulting to US-ASCII, *method* is an optional output which can
    be one of "xml" (default), "html", "text" or "c14n", *default_namespace*
    sets the default XML namespace (for "xmlns").

    Returns an (optionally) encoded string containing the XML data.

    '''
    stream = io.StringIO() if encoding == 'unicode' else io.BytesIO()
    ElementTree(element).write(stream, encoding, xml_declaration = xml_declaration, default_namespace = default_namespace, method = method, short_empty_elements = short_empty_elements)
    return stream.getvalue()


class _ListDataStream(io.BufferedIOBase):
    '''An auxiliary stream accumulating into a list reference.'''
    
    def __init__(self, lst):
        self.lst = lst

    
    def writable(self):
        return True

    
    def seekable(self):
        return True

    
    def write(self, b):
        self.lst.append(b)

    
    def tell(self):
        return len(self.lst)



def tostringlist(element = None, encoding = (None, None), method = {
    'xml_declaration': None,
    'default_namespace': None,
    'short_empty_elements': True }, *, xml_declaration, default_namespace, short_empty_elements):
    lst = []
    stream = _ListDataStream(lst)
    ElementTree(element).write(stream, encoding, xml_declaration = xml_declaration, default_namespace = default_namespace, method = method, short_empty_elements = short_empty_elements)
    return lst


def dump(elem):
    """Write element tree or element structure to sys.stdout.

    This function should be used for debugging only.

    *elem* is either an ElementTree, or a single Element.  The exact output
    format is implementation dependent.  In this version, it's written as an
    ordinary XML file.

    """
    if not isinstance(elem, ElementTree):
        elem = ElementTree(elem)
    elem.write(sys.stdout, encoding = 'unicode')
    tail = elem.getroot().tail
    if tail or tail[-1] != '\n':
        sys.stdout.write('\n')
        return None


def indent(tree, space, level = ('  ', 0)):
    '''Indent an XML document by inserting newlines and indentation space
    after elements.

    *tree* is the ElementTree or Element to modify.  The (root) element
    itself will not be changed, but the tail text of all elements in its
    subtree will be adapted.

    *space* is the whitespace to insert for each indentation level, two
    space characters by default.

    *level* is the initial indentation level. Setting this to a higher
    value than 0 can be used for indenting subtrees that are more deeply
    nested inside of a document.
    '''
    pass
# WARNING: Decompyle incomplete


def parse(source, parser = (None,)):
    '''Parse XML document into element tree.

    *source* is a filename or file object containing XML data,
    *parser* is an optional parser instance defaulting to XMLParser.

    Return an ElementTree instance.

    '''
    tree = ElementTree()
    tree.parse(source, parser)
    return tree


def iterparse(source, events, parser = (None, None)):
    '''Incrementally parse XML document into ElementTree.

    This class also reports what\'s going on to the user based on the
    *events* it is initialized with.  The supported events are the strings
    "start", "end", "start-ns" and "end-ns" (the "ns" events are used to get
    detailed namespace information).  If *events* is omitted, only
    "end" events are reported.

    *source* is a filename or file object containing XML data, *events* is
    a list of events to report back, *parser* is an optional parser instance.

    Returns an iterator providing (event, elem) pairs.

    '''
    pass
# WARNING: Decompyle incomplete


class XMLPullParser:
    
    def __init__(self = None, events = (None,), *, _parser):
        self._events_queue = collections.deque()
        if not _parser:
            pass
        self._parser = XMLParser(target = TreeBuilder())
    # WARNING: Decompyle incomplete

    
    def feed(self, data):
        '''Feed encoded data to parser.'''
        pass
    # WARNING: Decompyle incomplete

    
    def _close_and_return_root(self):
        root = self._parser.close()
        self._parser = None
        return root

    
    def close(self):
        '''Finish feeding data to parser.

        Unlike XMLParser, does not return the root element. Use
        read_events() to consume elements from XMLPullParser.
        '''
        self._close_and_return_root()

    
    def read_events(self):
        '''Return an iterator over currently available (event, elem) pairs.

        Events are consumed from the internal event queue as they are
        retrieved from the iterator.
        '''
        pass
    # WARNING: Decompyle incomplete



def XML(text, parser = (None,)):
    '''Parse XML document from string constant.

    This function can be used to embed "XML Literals" in Python code.

    *text* is a string containing XML data, *parser* is an
    optional parser instance, defaulting to the standard XMLParser.

    Returns an Element instance.

    '''
    if not parser:
        parser = XMLParser(target = TreeBuilder())
    parser.feed(text)
    return parser.close()


def XMLID(text, parser = (None,)):
    '''Parse XML document from string constant for its IDs.

    *text* is a string containing XML data, *parser* is an
    optional parser instance, defaulting to the standard XMLParser.

    Returns an (Element, dict) tuple, in which the
    dict maps element id:s to elements.

    '''
    if not parser:
        parser = XMLParser(target = TreeBuilder())
    parser.feed(text)
    tree = parser.close()
    ids = { }
    for elem in tree.iter():
        id = elem.get('id')
        if id:
            ids[id] = elem
        return (tree, ids)

fromstring = XML

def fromstringlist(sequence, parser = (None,)):
    '''Parse XML document from sequence of string fragments.

    *sequence* is a list of other sequence, *parser* is an optional parser
    instance, defaulting to the standard XMLParser.

    Returns an Element instance.

    '''
    if not parser:
        parser = XMLParser(target = TreeBuilder())
    for text in sequence:
        parser.feed(text)
        return parser.close()


class TreeBuilder:
    '''Generic element structure builder.

    This builder converts a sequence of start, data, and end method
    calls to a well-formed element structure.

    You can use this class to build an element structure using a custom XML
    parser, or a parser for some other XML-like format.

    *element_factory* is an optional element factory which is called
    to create new Element instances, as necessary.

    *comment_factory* is a factory to create comments to be used instead of
    the standard factory.  If *insert_comments* is false (the default),
    comments will not be inserted into the tree.

    *pi_factory* is a factory to create processing instructions to be used
    instead of the standard factory.  If *insert_pis* is false (the default),
    processing instructions will not be inserted into the tree.
    '''
    
    def __init__(self = None, element_factory = (None,), *, comment_factory, pi_factory, insert_comments, insert_pis):
        self._data = []
        self._elem = []
        self._last = None
        self._root = None
        self._tail = None
    # WARNING: Decompyle incomplete

    
    def close(self):
        '''Flush builder buffers and return toplevel document Element.'''
        pass
    # WARNING: Decompyle incomplete

    
    def _flush(self):
        pass
    # WARNING: Decompyle incomplete

    
    def data(self, data):
        '''Add text to current element.'''
        self._data.append(data)

    
    def start(self, tag, attrs):
        '''Open new element and return it.

        *tag* is the element name, *attrs* is a dict containing element
        attributes.

        '''
        self._flush()
        self._last = self._factory(tag, attrs)
        elem = self._factory(tag, attrs)
        if self._elem:
            self._elem[-1].append(elem)
    # WARNING: Decompyle incomplete

    
    def end(self, tag):
        '''Close and return current Element.

        *tag* is the element name.

        '''
        self._flush()
        self._last = self._elem.pop()
    # WARNING: Decompyle incomplete

    
    def comment(self, text):
        '''Create a comment using the comment_factory.

        *text* is the text of the comment.
        '''
        return self._handle_single(self._comment_factory, self.insert_comments, text)

    
    def pi(self, target, text = (None,)):
        """Create a processing instruction using the pi_factory.

        *target* is the target name of the processing instruction.
        *text* is the data of the processing instruction, or ''.
        """
        return self._handle_single(self._pi_factory, self.insert_pis, target, text)

    
    def _handle_single(self, factory, insert, *args):
        pass
    # WARNING: Decompyle incomplete



class XMLParser:
    '''Element structure builder for XML source data based on the expat parser.

    *target* is an optional target object which defaults to an instance of the
    standard TreeBuilder class, *encoding* is an optional encoding string
    which if given, overrides the encoding specified in the XML file:
    http://www.iana.org/assignments/character-sets

    '''
    
    def __init__(self = None, *, target, encoding):
        
        try:
            expat = expat
            import xml.parsers
        except ImportError:
            import pyexpat as expat
        except ImportError:
            raise ImportError('No module named expat; use SimpleXMLTreeBuilder instead')

        parser = expat.ParserCreate(encoding, '}')
    # WARNING: Decompyle incomplete

    
    def _setevents(self, events_queue, events_to_report):
        parser = self._parser
        append = events_queue.append
        for event_name in events_to_report:
            if event_name == 'start':
                parser.ordered_attributes = 1
                
                def handler(tag, attrib_in, event, append, start = (event_name, append, self._start)):
                    append((event, start(tag, attrib_in)))

                parser.StartElementHandler = handler
                continue
            if event_name == 'end':
                
                def handler(tag, event, append, end = (event_name, append, self._end)):
                    append((event, end(tag)))

                parser.EndElementHandler = handler
                continue
            if event_name == 'start-ns':
                if hasattr(self.target, 'start_ns'):
                    
                    def handler(prefix, uri, event, append, start_ns = (event_name, append, self._start_ns)):
                        append((event, start_ns(prefix, uri)))

                else:
                    
                    def handler(prefix, uri, event, append = (event_name, append)):
