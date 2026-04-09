# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sgmllib.pyc (Python 3.11)

'''A parser for SGML, using the derived class as a static DTD.'''
import _markupbase
import re
__all__ = [
    'SGMLParser',
    'SGMLParseError']
interesting = re.compile('[&<]')
incomplete = re.compile('&([a-zA-Z][a-zA-Z0-9]*|#[0-9]*)?|<([a-zA-Z][^<>]*|/([a-zA-Z][^<>]*)?|![^<>]*)?')
entityref = re.compile('&([a-zA-Z][-.a-zA-Z0-9]*)[^a-zA-Z0-9]')
charref = re.compile('&#([0-9]+)[^0-9]')
starttagopen = re.compile('<[>a-zA-Z]')
shorttagopen = re.compile('<[a-zA-Z][-.a-zA-Z0-9]*/')
shorttag = re.compile('<([a-zA-Z][-.a-zA-Z0-9]*)/([^/]*)/')
piclose = re.compile('>')
endbracket = re.compile('[<>]')
tagfind = re.compile('[a-zA-Z][-_.a-zA-Z0-9]*')
attrfind = re.compile('\\s*([a-zA-Z_][-:.a-zA-Z_0-9]*)(\\s*=\\s*(\\\'[^\\\']*\\\'|"[^"]*"|[][\\-a-zA-Z0-9./,:;+*%?!&$\\(\\)_#=~\\\'"@]*))?')

class SGMLParseError(RuntimeError):
    '''Exception raised for all parse errors.'''
    pass


class SGMLParser(_markupbase.ParserBase):
    entity_or_charref = re.compile('&(?:([a-zA-Z][-.a-zA-Z0-9]*)|#([0-9]+))(;?)')
    
    def __init__(self, verbose = (0,)):
        '''Initialize and reset this instance.'''
        self.verbose = verbose
        self.reset()

    
    def reset(self):
        '''Reset this instance. Loses all unprocessed data.'''
        self._SGMLParser__starttag_text = None
        self.rawdata = ''
        self.stack = []
        self.lasttag = '???'
        self.nomoretags = 0
        self.literal = 0
        _markupbase.ParserBase.reset(self)

    
    def setnomoretags(self):
        '''Enter literal mode (CDATA) till EOF.

        Intended for derived classes only.
        '''
        self.nomoretags = 1
        self.literal = 1

    
    def setliteral(self, *args):
        '''Enter literal mode (CDATA).

        Intended for derived classes only.
        '''
        self.literal = 1

    
    def feed(self, data):
        """Feed some data to the parser.

        Call this as often as you want, with as little or as much text
        as you want (may include '
').  (This just saves the text,
        all the processing is done by goahead().)
        """
        self.rawdata = self.rawdata + data
        self.goahead(0)

    
    def close(self):
        '''Handle the remaining data.'''
        self.goahead(1)

    
    def error(self, message):
        raise SGMLParseError(message)

    
    def goahead(self, end):
        rawdata = self.rawdata
        i = 0
        n = len(rawdata)
    # WARNING: Decompyle incomplete

    _decl_otherchars = '='
    
    def parse_pi(self, i):
        rawdata = self.rawdata
        if rawdata[i:i + 2] != '<?':
            self.error('unexpected call to parse_pi()')
        match = piclose.search(rawdata, i + 2)
        if not match:
            return -1
        j = None.start(0)
        self.handle_pi(rawdata[i + 2:j])
        j = match.end(0)
        return j - i

    
    def get_starttag_text(self):
        return self._SGMLParser__starttag_text

    
    def parse_starttag(self, i):
        self._SGMLParser__starttag_text = None
        start_pos = i
        rawdata = self.rawdata
        if shorttagopen.match(rawdata, i):
            match = shorttag.match(rawdata, i)
            if not match:
                return -1
            (tag, data) = None.group(1, 2)
            self._SGMLParser__starttag_text = '<%s/' % tag
            tag = tag.lower()
            k = match.end(0)
            self.finish_shorttag(tag, data)
            self._SGMLParser__starttag_text = rawdata[start_pos:match.end(1) + 1]
            return k
        match = None.search(rawdata, i + 1)
        if not match:
            return -1
        j = None.start(0)
        attrs = []
        if rawdata[i:i + 2] == '<>':
            k = j
            tag = self.lasttag
        else:
            match = tagfind.match(rawdata, i + 1)
            if not match:
                self.error('unexpected call to parse_starttag')
            k = match.end(0)
            tag = rawdata[i + 1:k].lower()
            self.lasttag = tag
        self.entity_or_charref.sub(self._convert_ref, attrvalue) = None if k < j else attrvalue[1:-1]
        attrs.append((attrname.lower(), attrvalue))
        k = match.end(0)
    # WARNING: Decompyle incomplete

    
    def _convert_ref(self, match):
