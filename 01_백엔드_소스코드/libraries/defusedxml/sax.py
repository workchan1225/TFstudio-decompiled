# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sax.pyc (Python 3.11)

'''Defused xml.sax
'''
from __future__ import print_function, absolute_import
from xml.sax import InputSource as _InputSource
from xml.sax import ErrorHandler as _ErrorHandler
from  import expatreader
__origin__ = 'xml.sax'

def parse(source, handler, errorHandler, forbid_dtd, forbid_entities, forbid_external = (_ErrorHandler(), False, True, True)):
    parser = make_parser()
    parser.setContentHandler(handler)
    parser.setErrorHandler(errorHandler)
    parser.forbid_dtd = forbid_dtd
    parser.forbid_entities = forbid_entities
    parser.forbid_external = forbid_external
    parser.parse(source)


def parseString(string, handler, errorHandler, forbid_dtd, forbid_entities, forbid_external = (_ErrorHandler(), False, True, True)):
    BytesIO = BytesIO
    import io
# WARNING: Decompyle incomplete


def make_parser(parser_list = ([],)):
    return expatreader.create_parser()
