# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _docs_extraction.pyc (Python 3.11)

'''Utilities related to attribute docstring extraction.'''
from __future__ import annotations
import ast
import inspect
import sys
import textwrap
from typing import Any

class DocstringVisitor(ast.NodeVisitor):
    pass
# WARNING: Decompyle incomplete


def _dedent_source_lines(source = None):
    dedent_source = textwrap.dedent(''.join(source))
    if dedent_source.startswith((' ', '\t')):
        dedent_source = f'''def dedent_workaround():\n{dedent_source}'''
    return dedent_source


def _extract_source_from_frame(cls = None):
    frame = inspect.currentframe()
# WARNING: Decompyle incomplete


def extract_docstrings_from_cls(cls = None, use_inspect = None):
    '''Map model attributes and their corresponding docstring.

    Args:
        cls: The class of the Pydantic model to inspect.
        use_inspect: Whether to skip usage of frames to find the object and use
            the `inspect` module instead.

    Returns:
        A mapping containing attribute names and their corresponding docstring.
    '''
    if use_inspect or sys.version_info >= (3, 13):
        
        try:
            (source, _) = inspect.getsourcelines(cls)
        except OSError:
            return 

        if not source:
            return { }
        None(source) = None
        visitor = DocstringVisitor()
        visitor.visit(ast.parse(dedent_source))
        return visitor.attrs
