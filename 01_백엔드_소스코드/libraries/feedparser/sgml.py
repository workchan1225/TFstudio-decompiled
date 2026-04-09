# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sgml.pyc (Python 3.11)

import re
import sgmllib
__all__ = [
    'sgmllib',
    'charref',
    'tagfind',
    'attrfind',
    'entityref',
    'incomplete',
    'interesting',
    'shorttag',
    'shorttagopen',
    'starttagopen',
    'endbracket']
charref = re.compile('&#(\\d+|[xX][0-9a-fA-F]+);')
tagfind = re.compile('[a-zA-Z][-_.:a-zA-Z0-9]*')
attrfind = re.compile('\\s*([a-zA-Z_][-:.a-zA-Z_0-9]*)[$]?(\\s*=\\s*(\'[^\']*\'|"[^"]*"|[][\\-a-zA-Z0-9./,:;+*%?!&$()_#=~\'"@]*))?')
entityref = sgmllib.entityref
incomplete = sgmllib.incomplete
interesting = sgmllib.interesting
shorttag = sgmllib.shorttag
shorttagopen = sgmllib.shorttagopen
starttagopen = sgmllib.starttagopen

class _EndBracketRegEx:
    
    def __init__(self):
        self.endbracket = re.compile('([^\'"<>]|"[^"]*"(?=>|/|\\s|\\w+=)|\'[^\']*\'(?=>|/|\\s|\\w+=))*(?=[<>])|.*?(?=[<>])')

    
    def search(self, target, index = (0,)):
        match = self.endbracket.match(target, index)
    # WARNING: Decompyle incomplete



class EndBracketMatch:
    
    def __init__(self, match):
        self.match = match

    
    def start(self, n):
        return self.match.end(n)


endbracket = _EndBracketRegEx()
