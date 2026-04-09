# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _log_render.pyc (Python 3.11)

from datetime import datetime
from typing import Iterable, List, Optional, TYPE_CHECKING, Union, Callable
from text import Text, TextType
if TYPE_CHECKING:
    from console import Console, ConsoleRenderable, RenderableType
    from table import Table
FormatTimeCallable = Callable[([
    datetime], Text)]

class LogRender:
    
    def __init__(self, show_time, show_level = None, show_path = None, time_format = None, omit_repeated_times = (True, False, True, '[%x %X]', True, 8), level_width = ('show_time', bool, 'show_level', bool, 'show_path', bool, 'time_format', Union[(str, FormatTimeCallable)], 'omit_repeated_times', bool, 'level_width', Optional[int], 'return', None)):
        self.show_time = show_time
        self.show_level = show_level
        self.show_path = show_path
        self.time_format = time_format
        self.omit_repeated_times = omit_repeated_times
        self.level_width = level_width
        self._last_time = None

    
    def __call__(self, console, renderables, log_time, time_format = None, level = None, path = None, line_no = (None, None, '', None, None, None), link_path = ('console', 'Console', 'renderables', Iterable['ConsoleRenderable'], 'log_time', Optional[datetime], 'time_format', Optional[Union[(str, FormatTimeCallable)]], 'level', TextType, 'path', Optional[str], 'line_no', Optional[int], 'link_path', Optional[str], 'return', 'Table')):
        Renderables = Renderables
        import containers
        Table = Table
        import table
        output = Table.grid(padding = (0, 1))
        output.expand = True
        if self.show_time:
            output.add_column(style = 'log.time')
        if self.show_level:
            output.add_column(style = 'log.level', width = self.level_width)
        output.add_column(ratio = 1, style = 'log.message', overflow = 'fold')
        if self.show_path and path:
            output.add_column(style = 'log.path')
        row = []
        if self.show_time:
            if not log_time:
                log_time = console.get_datetime()
                if not time_format:
                    time_format = self.time_format
                    if callable(time_format):
                        log_time_display = time_format(log_time)
                    else:
                        log_time_display = Text(log_time.strftime(time_format))
            if log_time_display == self._last_time and self.omit_repeated_times:
                row.append(Text(' ' * len(log_time_display)))
            else:
                row.append(log_time_display)
                self._last_time = log_time_display
        if self.show_level:
            row.append(level)
        row.append(Renderables(renderables))
        if self.show_path and path:
            path_text = Text()
            path_text.append(path, style = f'''link file://{link_path}''' if link_path else '')
            if line_no:
                path_text.append(':')
                path_text.append(f'''{line_no}''', style = f'''link file://{link_path}#{line_no}''' if link_path else '')
            row.append(path_text)
    # WARNING: Decompyle incomplete


if __name__ == '__main__':
    from rich.console import Console
    c = Console()
    c.print('[on blue]Hello', justify = 'right')
    c.log('[on blue]hello', justify = 'right')
    return None
