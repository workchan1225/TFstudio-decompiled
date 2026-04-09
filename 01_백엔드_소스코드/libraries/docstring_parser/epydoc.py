# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: epydoc.pyc (Python 3.11)

'''Epyoc-style docstring parsing.

.. seealso:: http://epydoc.sourceforge.net/manual-fields.html
'''
import inspect
import re
import typing as T
from common import Docstring, DocstringMeta, DocstringParam, DocstringRaises, DocstringReturns, DocstringStyle, ParseError, RenderingStyle

def _clean_str(string = None):
    string = string.strip()
    if len(string) > 0:
        return string


def parse(text = None):
    '''Parse the epydoc-style docstring into its components.

    :returns: parsed docstring
    '''
    ret = Docstring(style = DocstringStyle.EPYDOC)
    if not text:
        return ret
    text = None.cleandoc(text)
    match = re.search('^@', text, flags = re.M)
    if match:
        desc_chunk = None[text:match.start()]
        meta_chunk = text[match.start():]
    else:
        desc_chunk = text
        meta_chunk = ''
    parts = desc_chunk.split('\n', 1)
# WARNING: Decompyle incomplete


def compose(docstring = None, rendering_style = None, indent = None):
    '''Render a parsed docstring into docstring text.

    :param docstring: parsed docstring representation
    :param rendering_style: the style to render docstrings
    :param indent: the characters used as indentation in the docstring string
    :returns: docstring text
    '''
    pass
# WARNING: Decompyle incomplete
