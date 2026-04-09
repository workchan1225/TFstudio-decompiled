# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: common.pyc (Python 3.11)

'''Common constants, exceptions and helpe functions
'''
import sys
import xml.parsers.expat as xml
PY3 = sys.version_info[0] == 3
if not hasattr(xml.parsers.expat, 'ParserCreate'):
    raise ImportError('pyexpat')

class DefusedXmlException(ValueError):
    '''Base exception'''
    
    def __repr__(self):
        return str(self)



class DTDForbidden(DefusedXmlException):
    pass
# WARNING: Decompyle incomplete


class EntitiesForbidden(DefusedXmlException):
    pass
# WARNING: Decompyle incomplete


class ExternalReferenceForbidden(DefusedXmlException):
    pass
# WARNING: Decompyle incomplete


class NotSupportedError(DefusedXmlException):
    '''The operation is not supported'''
    pass


def _apply_defusing(defused_mod):
    pass
# WARNING: Decompyle incomplete


def _generate_etree_functions(DefusedXMLParser, _TreeBuilder, _parse, _iterparse):
    '''Factory for functions needed by etree, dependent on whether
    cElementTree or ElementTree is used.'''
    pass
# WARNING: Decompyle incomplete
