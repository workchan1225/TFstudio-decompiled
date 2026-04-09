# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _inspect.pyc (Python 3.11)

import inspect
from inspect import cleandoc, getdoc, getfile, isclass, ismodule, signature
from typing import Any, Collection, Iterable, Optional, Tuple, Type, Union
from console import Group, RenderableType
from control import escape_control_codes
from highlighter import ReprHighlighter
from jupyter import JupyterMixin
from panel import Panel
from pretty import Pretty
from table import Table
from text import Text, TextType

def _first_paragraph(doc = None):
    '''Get the first paragraph from a docstring.'''
    (paragraph, _, _) = doc.partition('\n\n')
    return paragraph


class Inspect(JupyterMixin):
    '''A renderable to inspect any Python Object.

    Args:
        obj (Any): An object to inspect.
        title (str, optional): Title to display over inspect result, or None use type. Defaults to None.
        help (bool, optional): Show full help text rather than just first paragraph. Defaults to False.
        methods (bool, optional): Enable inspection of callables. Defaults to False.
        docs (bool, optional): Also render doc strings. Defaults to True.
        private (bool, optional): Show private attributes (beginning with underscore). Defaults to False.
        dunder (bool, optional): Show attributes starting with double underscore. Defaults to False.
        sort (bool, optional): Sort attributes alphabetically, callables at the top, leading and trailing underscores ignored. Defaults to True.
        all (bool, optional): Show all attributes. Defaults to False.
        value (bool, optional): Pretty print value of object. Defaults to True.
    '''
    
    def __init__(self = None, obj = None, *, title, help, methods, docs, private, dunder, sort, all, value):
