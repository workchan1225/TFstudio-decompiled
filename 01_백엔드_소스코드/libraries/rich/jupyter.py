# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: jupyter.pyc (Python 3.11)

from typing import TYPE_CHECKING, Any, Dict, Iterable, List, Sequence
if TYPE_CHECKING:
    from rich.console import ConsoleRenderable
from  import get_console
from segment import Segment
from terminal_theme import DEFAULT_TERMINAL_THEME
if TYPE_CHECKING:
    from rich.console import ConsoleRenderable
JUPYTER_HTML_FORMAT = '<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,\'DejaVu Sans Mono\',consolas,\'Courier New\',monospace">{code}</pre>\n'

class JupyterRenderable:
    '''A shim to write html to Jupyter notebook.'''
    
    def __init__(self = None, html = None, text = None):
        self.html = html
        self.text = text

    
    def _repr_mimebundle_(self = None, include = None, exclude = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete



class JupyterMixin:
    '''Add to an Rich renderable to make it render in Jupyter notebook.'''
    __slots__ = ()
    
    def _repr_mimebundle_(self = None, include = None, exclude = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete



def _render_segments(segments = None):
    
    def escape(text = None):
        '''Escape html.'''
        return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    fragments = []
    append_fragment = fragments.append
    theme = DEFAULT_TERMINAL_THEME
    for text, style, control in Segment.simplify(segments):
        if control:
            continue
        text = escape(text)
        if style:
            rule = style.get_html_style(theme)
            text = f'''<span style="{rule}">{text}</span>''' if rule else text
            if style.link:
                text = f'''<a href="{style.link}" target="_blank">{text}</a>'''
        append_fragment(text)
        code = ''.join(fragments)
        html = JUPYTER_HTML_FORMAT.format(code = code)
        return html


def display(segments = None, text = None):
    '''Render segments to Jupyter.'''
    html = _render_segments(segments)
    jupyter_renderable = JupyterRenderable(html, text)
    
    try:
        ipython_display = display
        import IPython.display
        ipython_display(jupyter_renderable)
        return None
    except ModuleNotFoundError:
        return None



def print(*args, **kwargs):
    '''Proxy for Console print.'''
    console = get_console()
# WARNING: Decompyle incomplete
