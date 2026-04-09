# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parser.pyc (Python 3.11)

'''A parser for HTML and XHTML.'''
import re
import _markupbase
from html import unescape
__all__ = [
    'HTMLParser']
interesting_normal = re.compile('[&<]')
incomplete = re.compile('&[a-zA-Z#]')
entityref = re.compile('&([a-zA-Z][-.a-zA-Z0-9]*)[^a-zA-Z0-9]')
charref = re.compile('&#(?:[0-9]+|[xX][0-9a-fA-F]+)[^0-9a-fA-F]')
starttagopen = re.compile('<[a-zA-Z]')
piclose = re.compile('>')
commentclose = re.compile('--\\s*>')
tagfind_tolerant = re.compile('([a-zA-Z][^\\t\\n\\r\\f />\\x00]*)(?:\\s|/(?!>))*')
attrfind_tolerant = re.compile('((?<=[\\\'"\\s/])[^\\s/>][^\\s/=>]*)(\\s*=+\\s*(\\\'[^\\\']*\\\'|"[^"]*"|(?![\\\'"])[^>\\s]*))?(?:\\s|/(?!>))*')
locatestarttagend_tolerant = re.compile('\n  <[a-zA-Z][^\\t\\n\\r\\f />\\x00]*       # tag name\n  (?:[\\s/]*                          # optional whitespace before attribute name\n    (?:(?<=[\'"\\s/])[^\\s/>][^\\s/=>]*  # attribute name\n      (?:\\s*=+\\s*                    # value indicator\n        (?:\'[^\']*\'                   # LITA-enclosed value\n          |"[^"]*"                   # LIT-enclosed value\n          |(?![\'"])[^>\\s]*           # bare value\n         )\n        \\s*                          # possibly followed by a space\n       )?(?:\\s|/(?!>))*\n     )*\n   )?\n  \\s*                                # trailing whitespace\n', re.VERBOSE)
endendtag = re.compile('>')
endtagfind = re.compile('</\\s*([a-zA-Z][-.a-zA-Z0-9:_]*)\\s*>')

class HTMLParser(_markupbase.ParserBase):
    '''Find tags and other markup and call handler functions.

    Usage:
        p = HTMLParser()
        p.feed(data)
        ...
        p.close()

    Start tags are handled by calling self.handle_starttag() or
    self.handle_startendtag(); end tags by self.handle_endtag().  The
    data between tags is passed from the parser to the derived class
    by calling self.handle_data() with the data as argument (the data
    may be split up in arbitrary chunks).  If convert_charrefs is
    True the character references are converted automatically to the
    corresponding Unicode character (and self.handle_data() is no
    longer split in chunks), otherwise they are passed by calling
    self.handle_entityref() or self.handle_charref() with the string
    containing respectively the named or numeric reference as the
    argument.
    '''
    CDATA_CONTENT_ELEMENTS = ('script', 'style')
    
    def __init__(self = None, *, convert_charrefs):
        '''Initialize and reset this instance.

        If convert_charrefs is True (the default), all character references
        are automatically converted to the corresponding Unicode characters.
        '''
        self.convert_charrefs = convert_charrefs
        self.reset()

    
    def reset(self):
        '''Reset this instance.  Loses all unprocessed data.'''
        self.rawdata = ''
        self.lasttag = '???'
        self.interesting = interesting_normal
        self.cdata_elem = None
        _markupbase.ParserBase.reset(self)

    
    def feed(self, data):
        """Feed data to the parser.

        Call this as often as you want, with as little or as much text
        as you want (may include '\\n').
        """
        self.rawdata = self.rawdata + data
        self.goahead(0)

    
    def close(self):
        '''Handle any buffered data.'''
        self.goahead(1)

    __starttag_text = None
    
    def get_starttag_text(self):
        """Return full source of start tag: '<...>'."""
        return self.__starttag_text

    
    def set_cdata_mode(self, elem):
        self.cdata_elem = elem.lower()
        self.interesting = re.compile('</\\s*%s\\s*>' % self.cdata_elem, re.I)

    
    def clear_cdata_mode(self):
        self.interesting = interesting_normal
        self.cdata_elem = None

    
    def goahead(self, end):
        rawdata = self.rawdata
        i = 0
        n = len(rawdata)
    # WARNING: Decompyle incomplete

    
    def parse_html_declaration(self, i):
        rawdata = self.rawdata
    # WARNING: Decompyle incomplete

    
    def parse_bogus_comment(self, i, report = (1,)):
        rawdata = self.rawdata
    # WARNING: Decompyle incomplete

    
    def parse_pi(self, i):
        rawdata = self.rawdata
    # WARNING: Decompyle incomplete

    
    def parse_starttag(self, i):
        self.__starttag_text = None
        endpos = self.check_for_whole_start_tag(i)
        if endpos < 0:
            return endpos
        rawdata = None.rawdata
        self.__starttag_text = rawdata[i:endpos]
        attrs = []
        match = tagfind_tolerant.match(rawdata, i + 1)
    # WARNING: Decompyle incomplete

    
    def check_for_whole_start_tag(self, i):
        rawdata = self.rawdata
        m = locatestarttagend_tolerant.match(rawdata, i)
        if m:
            j = m.end()
            next = rawdata[j:j + 1]
            if next == '>':
                return j + 1
            if None == '/':
                if rawdata.startswith('/>', j):
                    return j + 2
                if None.startswith('/', j):
                    return -1
                if None > i:
                    return j
                return None + 1
            if None == '':
                return -1
            if None in 'abcdefghijklmnopqrstuvwxyz=/ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                return -1
            if None > i:
                return j
            return None + 1
        raise None('we should not get here!')

    
    def parse_endtag(self, i):
        rawdata = self.rawdata
    # WARNING: Decompyle incomplete

    
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    
    def handle_starttag(self, tag, attrs):
        pass

    
    def handle_endtag(self, tag):
        pass

    
    def handle_charref(self, name):
        pass

    
    def handle_entityref(self, name):
        pass

    
    def handle_data(self, data):
        pass

    
    def handle_comment(self, data):
        pass

    
    def handle_decl(self, decl):
        pass

    
    def handle_pi(self, data):
        pass

    
    def unknown_decl(self, data):
        pass
