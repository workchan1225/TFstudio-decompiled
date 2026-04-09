# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rule.pyc (Python 3.11)

from typing import Union
from align import AlignMethod
from cells import cell_len, set_cell_size
from console import Console, ConsoleOptions, RenderResult
from jupyter import JupyterMixin
from measure import Measurement
from style import Style
from text import Text

class Rule(JupyterMixin):
    '''A console renderable to draw a horizontal rule (line).

    Args:
        title (Union[str, Text], optional): Text to render in the rule. Defaults to "".
        characters (str, optional): Character(s) used to draw the line. Defaults to "─".
        style (StyleType, optional): Style of Rule. Defaults to "rule.line".
        end (str, optional): Character at end of Rule. defaults to "\\\\n"
        align (str, optional): How to align the title, one of "left", "center", or "right". Defaults to "center".
    '''
    
    def __init__(self = None, title = None, *, characters, style, end, align):
        if cell_len(characters) < 1:
            raise ValueError("'characters' argument must have a cell width of at least 1")
        if align not in ('left', 'center', 'right'):
            raise ValueError(f'''invalid value for align, expected "left", "center", "right" (not {align!r})''')
        self.title = title
        self.characters = characters
        self.style = style
        self.end = end
        self.align = align

    
    def __repr__(self = None):
        return f'''Rule({self.title!r}, {self.characters!r})'''

    
    def __rich_console__(self = None, console = None, options = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _rule_line(self = None, chars_len = None, width = None):
        rule_text = Text(self.characters * (width // chars_len + 1), self.style)
        rule_text.truncate(width)
        rule_text.plain = set_cell_size(rule_text.plain, width)
        return rule_text

    
    def __rich_measure__(self = None, console = None, options = None):
        return Measurement(1, 1)


if __name__ == '__main__':
    import sys
    from rich.console import Console
    
    try:
        text = sys.argv[1]
    except IndexError:
        text = 'Hello, World'

    console = Console()
    console.print(Rule(title = text))
    console = Console()
    console.print(Rule('foo'), width = 4)
    return None
