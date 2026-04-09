# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: panel.pyc (Python 3.11)

from typing import TYPE_CHECKING, Optional
from align import AlignMethod
from box import ROUNDED, Box
from cells import cell_len
from jupyter import JupyterMixin
from measure import Measurement, measure_renderables
from padding import Padding, PaddingDimensions
from segment import Segment
from style import Style, StyleType
from text import Text, TextType
if TYPE_CHECKING:
    from console import Console, ConsoleOptions, RenderableType, RenderResult

class Panel(JupyterMixin):
    '''A console renderable that draws a border around its contents.

    Example:
        >>> console.print(Panel("Hello, World!"))

    Args:
        renderable (RenderableType): A console renderable object.
        box (Box): A Box instance that defines the look of the border (see :ref:`appendix_box`. Defaults to box.ROUNDED.
        title (Optional[TextType], optional): Optional title displayed in panel header. Defaults to None.
        title_align (AlignMethod, optional): Alignment of title. Defaults to "center".
        subtitle (Optional[TextType], optional): Optional subtitle displayed in panel footer. Defaults to None.
        subtitle_align (AlignMethod, optional): Alignment of subtitle. Defaults to "center".
        safe_box (bool, optional): Disable box characters that don\'t display on windows legacy terminal with *raster* fonts. Defaults to True.
        expand (bool, optional): If True the panel will stretch to fill the console width, otherwise it will be sized to fit the contents. Defaults to True.
        style (str, optional): The style of the panel (border and contents). Defaults to "none".
        border_style (str, optional): The style of the border. Defaults to "none".
        width (Optional[int], optional): Optional width of panel. Defaults to None to auto-detect.
        height (Optional[int], optional): Optional height of panel. Defaults to None to auto-detect.
        padding (Optional[PaddingDimensions]): Optional padding around renderable. Defaults to 0.
        highlight (bool, optional): Enable automatic highlighting of panel title (if str). Defaults to False.
    '''
    
    def __init__(self = None, renderable = None, box = None, *, title, title_align, subtitle, subtitle_align, safe_box, expand, style, border_style, width, height, padding, highlight):
        self.renderable = renderable
        self.box = box
        self.title = title
        self.title_align = title_align
        self.subtitle = subtitle
        self.subtitle_align = subtitle_align
        self.safe_box = safe_box
        self.expand = expand
        self.style = style
        self.border_style = border_style
        self.width = width
        self.height = height
        self.padding = padding
        self.highlight = highlight

    fit = (lambda cls = None, renderable = None, box = None, *, title, title_align, subtitle: cls(renderable, box, title = title, title_align = title_align, subtitle = subtitle, subtitle_align = subtitle_align, safe_box = safe_box, style = style, border_style = border_style, width = width, height = height, padding = padding, highlight = highlight, expand = False))()
    _title = (lambda self = None: if self.title:
title_text = Text.from_markup(self.title) if isinstance(self.title, str) else self.title.copy()title_text.end = ''title_text.plain = title_text.plain.replace('\n', ' ')title_text.no_wrap = Truetitle_text.expand_tabs()title_text.pad(1)title_text)()
    _subtitle = (lambda self = None: if self.subtitle:
subtitle_text = Text.from_markup(self.subtitle) if isinstance(self.subtitle, str) else self.subtitle.copy()subtitle_text.end = ''subtitle_text.plain = subtitle_text.plain.replace('\n', ' ')subtitle_text.no_wrap = Truesubtitle_text.expand_tabs()subtitle_text.pad(1)subtitle_text)()
    
    def __rich_console__(self = None, console = None, options = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __rich_measure__(self = None, console = None, options = None):
        _title = self._title
        (_, right, _, left) = Padding.unpack(self.padding)
        padding = left + right
        renderables = [
            self.renderable,
            _title] if _title else [
            self.renderable]
    # WARNING: Decompyle incomplete


if __name__ == '__main__':
    from console import Console
    c = Console()
    from box import DOUBLE, ROUNDED
    from padding import Padding
    p = Panel('Hello, World!', title = 'rich.Panel', style = 'white on blue', box = DOUBLE, padding = 1)
    c.print()
    c.print(p)
    return None
