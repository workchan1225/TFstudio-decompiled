# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''Defuse XML bomb denial of service vulnerabilities
'''
from __future__ import print_function, absolute_import
import warnings
from common import DefusedXmlException, DTDForbidden, EntitiesForbidden, ExternalReferenceForbidden, NotSupportedError, _apply_defusing

def defuse_stdlib():
    '''Monkey patch and defuse all stdlib packages

    :warning: The monkey patch is an EXPERIMETNAL feature.
    '''
    defused = { }
    warnings.catch_warnings()
    cElementTree = cElementTree
    import 
    None(None, None)

__version__ = '0.7.1'
__all__ = [
    'DefusedXmlException',
    'DTDForbidden',
    'EntitiesForbidden',
    'ExternalReferenceForbidden',
    'NotSupportedError']
