# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _markupbase.pyc (Python 3.11)

'''Shared support for scanning document type declarations in HTML and XHTML.

This module is used as a foundation for the html.parser module.  It has no
documented public API and should not be used directly.

'''
import re
_declname_match = re.compile('[a-zA-Z][-_.a-zA-Z0-9]*\\s*').match
_declstringlit_match = re.compile('(\\\'[^\\\']*\\\'|"[^"]*")\\s*').match
_commentclose = re.compile('--\\s*>')
_markedsectionclose = re.compile(']\\s*]\\s*>')
_msmarkedsectionclose = re.compile(']\\s*>')
del re

class ParserBase:
    '''Parser base class which provides some common support methods used
    by the SGML/HTML and XHTML parsers.'''
    
    def __init__(self):
        if self.__class__ is ParserBase:
            raise RuntimeError('_markupbase.ParserBase must be subclassed')

    
    def reset(self):
        self.lineno = 1
        self.offset = 0

    
    def getpos(self):
        '''Return current line number and offset.'''
        return (self.lineno, self.offset)

    
    def updatepos(self, i, j):
        if i >= j:
            return j
        rawdata = None.rawdata
        nlines = rawdata.count('\n', i, j)
        if nlines:
            self.lineno = self.lineno + nlines
            pos = rawdata.rindex('\n', i, j)
            self.offset = j - (pos + 1)
        else:
            self.offset = self.offset + j - i
        return j

    _decl_otherchars = ''
    
    def parse_declaration(self, i):
        rawdata = self.rawdata
        j = i + 2
    # WARNING: Decompyle incomplete

    
    def parse_marked_section(self, i, report = (1,)):
        rawdata = self.rawdata
    # WARNING: Decompyle incomplete

    
    def parse_comment(self, i, report = (1,)):
        rawdata = self.rawdata
        if rawdata[i:i + 4] != '<!--':
            raise AssertionError('unexpected call to parse_comment()')
        match = _commentclose.search(rawdata, i + 4)
        if not match:
            return -1
        if None:
            j = match.start(0)
            self.handle_comment(rawdata[i + 4:j])
        return match.end(0)

    
    def _parse_doctype_subset(self, i, declstartpos):
        rawdata = self.rawdata
        n = len(rawdata)
        j = i
    # WARNING: Decompyle incomplete

    
    def _parse_doctype_element(self, i, declstartpos):
        (name, j) = self._scan_name(i, declstartpos)
        if j == -1:
            return -1
        rawdata = None.rawdata
        if '>' in rawdata[j:]:
            return rawdata.find('>', j) + 1

    
    def _parse_doctype_attlist(self, i, declstartpos):
        rawdata = self.rawdata
        (name, j) = self._scan_name(i, declstartpos)
        c = rawdata[j:j + 1]
        if c == '':
            return -1
        if None == '>':
            return j + 1
        (name, j) = self._scan_name(j, declstartpos)
        if j < 0:
            return j
        c = None[j:j + 1]
        if c == '':
            return -1
    # WARNING: Decompyle incomplete

    
    def _parse_doctype_notation(self, i, declstartpos):
        (name, j) = self._scan_name(i, declstartpos)
        if j < 0:
            return j
        rawdata = None.rawdata
        c = rawdata[j:j + 1]
        if not c:
            return -1
        if None == '>':
            return j + 1
        if None in '\'"':
            m = _declstringlit_match(rawdata, j)
            if not m:
                return -1
            j = None.end()
        else:
            (name, j) = self._scan_name(j, declstartpos)
            if j < 0:
                return j

    
    def _parse_doctype_entity(self, i, declstartpos):
