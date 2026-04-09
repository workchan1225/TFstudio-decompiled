# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: markdown.pyc (Python 3.11)

from __future__ import annotations
import sys
from dataclasses import dataclass
from typing import ClassVar, Iterable, get_args
from markdown_it import MarkdownIt
from markdown_it.token import Token
from rich.table import Table
from  import box
from _loop import loop_first
from _stack import Stack
from console import Console, ConsoleOptions, JustifyMethod, RenderResult
from containers import Renderables
from jupyter import JupyterMixin
from rule import Rule
from segment import Segment
from style import Style, StyleStack
from syntax import Syntax
from text import Text, TextType

class MarkdownElement:
    new_line: 'ClassVar[bool]' = True
    create = (lambda cls = None, markdown = None, token = classmethod: cls())()
    
    def on_enter(self = None, context = None):
        '''Called when the node is entered.

        Args:
            context (MarkdownContext): The markdown context.
        '''
        pass

    
    def on_text(self = None, context = None, text = None):
        '''Called when text is parsed.

        Args:
            context (MarkdownContext): The markdown context.
        '''
        pass

    
    def on_leave(self = None, context = None):
        '''Called when the parser leaves the element.

        Args:
            context (MarkdownContext): [description]
        '''
        pass

    
    def on_child_close(self = None, context = None, child = None):
        '''Called when a child element is closed.

        This method allows a parent element to take over rendering of its children.

        Args:
            context (MarkdownContext): The markdown context.
            child (MarkdownElement): The child markdown element.

        Returns:
            bool: Return True to render the element, or False to not render the element.
        '''
        return True

    
    def __rich_console__(self = None, console = None, options = None):
        return ()



class UnknownElement(MarkdownElement):
    '''An unknown element.

    Hopefully there will be no unknown elements, and we will have a MarkdownElement for
    everything in the document.

    '''
    pass


class TextElement(MarkdownElement):
    '''Base class for elements that render text.'''
    style_name = 'none'
    
    def on_enter(self = None, context = None):
        self.style = context.enter_style(self.style_name)
        self.text = Text(justify = 'left')

    
    def on_text(self = None, context = None, text = None):
        self.text.append(text, context.current_style if isinstance(text, str) else None)

    
    def on_leave(self = None, context = None):
        context.leave_style()



class Paragraph(TextElement):
    '''A Paragraph.'''
    justify: 'JustifyMethod' = 'markdown.paragraph'
    create = (lambda cls = None, markdown = None, token = classmethod:
