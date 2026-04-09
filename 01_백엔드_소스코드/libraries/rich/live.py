# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: live.pyc (Python 3.11)

from __future__ import annotations
import sys
from threading import Event, RLock, Thread
from types import TracebackType
from typing import IO, TYPE_CHECKING, Any, Callable, List, Optional, TextIO, Type, cast
from  import get_console
from console import Console, ConsoleRenderable, Group, RenderableType, RenderHook
from control import Control
from file_proxy import FileProxy
from jupyter import JupyterMixin
from live_render import LiveRender, VerticalOverflowMethod
from screen import Screen
from text import Text
if TYPE_CHECKING:
    from typing_extensions import Self

class _RefreshThread(Thread):
    pass
# WARNING: Decompyle incomplete


class Live(RenderHook, JupyterMixin):
    '''Renders an auto-updating live display of any given renderable.

    Args:
        renderable (RenderableType, optional): The renderable to live display. Defaults to displaying nothing.
        console (Console, optional): Optional Console instance. Defaults to an internal Console instance writing to stdout.
        screen (bool, optional): Enable alternate screen mode. Defaults to False.
        auto_refresh (bool, optional): Enable auto refresh. If disabled, you will need to call `refresh()` or `update()` with refresh flag. Defaults to True
        refresh_per_second (float, optional): Number of times per second to refresh the live display. Defaults to 4.
        transient (bool, optional): Clear the renderable on exit (has no effect when screen=True). Defaults to False.
        redirect_stdout (bool, optional): Enable redirection of stdout, so ``print`` may be used. Defaults to True.
        redirect_stderr (bool, optional): Enable redirection of stderr. Defaults to True.
        vertical_overflow (VerticalOverflowMethod, optional): How to handle renderable when it is too tall for the console. Defaults to "ellipsis".
        get_renderable (Callable[[], RenderableType], optional): Optional callable to get renderable. Defaults to None.
    '''
    
    def __init__(self = None, renderable = None, *, console, screen, auto_refresh, refresh_per_second, transient, redirect_stdout, redirect_stderr, vertical_overflow, get_renderable):
        pass
    # WARNING: Decompyle incomplete

    is_started = (lambda self = None: self._started)()
    
    def get_renderable(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def start(self = None, refresh = None):
        '''Start live rendering display.

        Args:
            refresh (bool, optional): Also refresh. Defaults to False.
        '''
        self._lock
        if self._started:
            None(None, None)
            return None
        self._started = None
        if not self.console.set_live(self):
            self._nested = True
            None(None, None)
            return None
        if None._screen:
            self._alt_screen = self.console.set_alt_screen(True)
        self.console.show_cursor(False)
        self._enable_redirect_io()
        self.console.push_render_hook(self)
        if self.auto_refresh:
            self._refresh_thread = _RefreshThread(self, self.refresh_per_second)
            self._refresh_thread.start()
        None(None, None)
        return None
        with None:
            if not None if refresh else None:
                pass

    
    def stop(self = None):
        '''Stop live rendering display.'''
        self._lock
        if not self._started:
            None(None, None)
            return None
        self._started = None
        self.console.clear_live()
        if self._nested:
            if not self.transient:
                self.console.print(self.renderable)
            None(None, None)
            return None
    # WARNING: Decompyle incomplete

    
    def __enter__(self = None):
        self.start(refresh = self._renderable is not None)
        return self

    
    def __exit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'Optional[Type[BaseException]]', 'exc_val', 'Optional[BaseException]', 'exc_tb', 'Optional[TracebackType]', 'return', 'None')):
        self.stop()

    
    def _enable_redirect_io(self = None):
        '''Enable redirecting of stdout / stderr.'''
        if self.console.is_terminal or self.console.is_jupyter:
            if not self._redirect_stdout and isinstance(sys.stdout, FileProxy):
                self._restore_stdout = sys.stdout
                sys.stdout = cast('TextIO', FileProxy(self.console, sys.stdout))
            if not self._redirect_stderr or isinstance(sys.stderr, FileProxy):
                self._restore_stderr = sys.stderr
                sys.stderr = cast('TextIO', FileProxy(self.console, sys.stderr))
                return None
            return None
        return None

    
    def _disable_redirect_io(self = None):
        '''Disable redirecting of stdout / stderr.'''
        if self._restore_stdout:
            sys.stdout = cast('TextIO', self._restore_stdout)
            self._restore_stdout = None
        if self._restore_stderr:
            sys.stderr = cast('TextIO', self._restore_stderr)
            self._restore_stderr = None
            return None

    renderable = (lambda self = None: live_stack = self.console._live_stack# WARNING: Decompyle incomplete
)()
    
    def update(self = None, renderable = None, *, refresh):
        '''Update the renderable that is being displayed

        Args:
            renderable (RenderableType): New renderable to use.
            refresh (bool, optional): Refresh the display. Defaults to False.
        '''
        if isinstance(renderable, str):
            renderable = self.console.render_str(renderable)
        self._lock
        self._renderable = renderable
        if refresh:
            self.refresh()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def refresh(self = None):
        '''Update the display of the Live Render.'''
        self._lock
        self._live_render.set_renderable(self.renderable)
        if self._nested:
            if self.console._live_stack:
                self.console._live_stack[0].refresh()
            None(None, None)
            return None
    # WARNING: Decompyle incomplete

    
    def process_renderables(self = None, renderables = None):
        '''Process renderables to restore cursor and display progress.'''
        self._live_render.vertical_overflow = self.vertical_overflow
        if self.console.is_interactive:
            self._lock
            reset = Control.home() if self._alt_screen else self._live_render.position_cursor()
            renderables = None[self._live_render]
            None(None, None)
        else:
            with None:
                if not None:
                    pass
        if not self._started and self.transient:
            renderables = None[self._live_render]
        return renderables


if __name__ == '__main__':
    import random
    import time
    from itertools import cycle
    from typing import Dict, List, Tuple
    from align import Align
    from console import Console
    from live import Live
    from panel import Panel
    from rule import Rule
    from syntax import Syntax
    from table import Table
    console = Console()
    syntax = Syntax('def loop_last(values: Iterable[T]) -> Iterable[Tuple[bool, T]]:\n    """Iterate and generate a tuple with a flag for last value."""\n    iter_values = iter(values)\n    try:\n        previous_value = next(iter_values)\n    except StopIteration:\n        return\n    for value in iter_values:\n        yield False, previous_value\n        previous_value = value\n    yield True, previous_value', 'python', line_numbers = True)
    table = Table('foo', 'bar', 'baz')
    table.add_row('1', '2', '3')
    progress_renderables = [
        'You can make the terminal shorter and taller to see the live table hideText may be printed while the progress bars are rendering.',
        Panel('In fact, [i]any[/i] renderable will work'),
        'Such as [magenta]tables[/]...',
        table,
        'Pretty printed structures...',
        {
            'type': 'example',
            'text': 'Pretty printed' },
        'Syntax...',
        syntax,
        Rule('Give it a try!')]
    examples = cycle(progress_renderables)
    exchanges = [
        'SGD',
        'MYR',
        'EUR',
        'USD',
        'AUD',
        'JPY',
        'CNH',
        'HKD',
        'CAD',
        'INR',
        'DKK',
        'GBP',
        'RUB',
        'NZD',
        'MXN',
        'IDR',
        'TWD',
        'THB',
        'VND']
    live_table = Live(console = console)
    exchange_rate_dict: 'Dict[Tuple[str, str], float]' = { }
    for index in range(100):
        select_exchange = exchanges[index % len(exchanges)]
        for exchange in exchanges:
            if exchange == select_exchange:
                continue
            time.sleep(0.4)
            if random.randint(0, 10) < 1:
                console.log(next(examples))
            exchange_rate_dict[(select_exchange, exchange)] = 200 / (random.random() * 320 + 1)
            if len(exchange_rate_dict) > len(exchanges) - 1:
                exchange_rate_dict.pop(list(exchange_rate_dict.keys())[0])
            table = Table(title = 'Exchange Rates')
            table.add_column('Source Currency')
            table.add_column('Destination Currency')
            table.add_column('Exchange Rate')
            for source, dest in exchange_rate_dict.items():
                exchange_rate = None
                table.add_row(source, dest, Text(f'''{exchange_rate:.4f}''', style = 'red' if exchange_rate < 1 else 'green'))
                live_table.update(Align.center(table))
                None(None, None)
                return None
                with None:
                    if not None:
                        pass
    return None
