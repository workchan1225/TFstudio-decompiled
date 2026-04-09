# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: progress.pyc (Python 3.11)

from __future__ import annotations
import io
import typing
import warnings
from abc import ABC, abstractmethod
from collections import deque
from dataclasses import dataclass, field
from datetime import timedelta
from io import RawIOBase, UnsupportedOperation
from math import ceil
from mmap import mmap
from operator import length_hint
from os import PathLike, stat
from threading import Event, RLock, Thread
from types import TracebackType
from typing import TYPE_CHECKING, Any, BinaryIO, Callable, ContextManager, Deque, Dict, Generic, Iterable, List, Literal, NamedTuple, NewType, Optional, TextIO, Tuple, Type, TypeVar, Union
if TYPE_CHECKING:
    from typing_extensions import Self
from  import filesize, get_console
from console import Console, Group, JustifyMethod, RenderableType
from highlighter import Highlighter
from jupyter import JupyterMixin
from live import Live
from progress_bar import ProgressBar
from spinner import Spinner
from style import StyleType
from table import Column, Table
from text import Text, TextType
TaskID = NewType('TaskID', int)
ProgressType = TypeVar('ProgressType')
GetTimeCallable = Callable[([], float)]
_I = typing.TypeVar('_I', TextIO, BinaryIO)

class _TrackThread(Thread):
    pass
# WARNING: Decompyle incomplete


def track(sequence, description, total, completed, auto_refresh, console, transient, get_time, refresh_per_second, style, complete_style, finished_style = None, pulse_style = None, update_period = None, disable = ('Working...', None, 0, True, None, False, None, 10, 'bar.back', 'bar.complete', 'bar.finished', 'bar.pulse', 0.1, False, True), show_speed = ('sequence', 'Iterable[ProgressType]', 'description', 'str', 'total', 'Optional[float]', 'completed', 'int', 'auto_refresh', 'bool', 'console', 'Optional[Console]', 'transient', 'bool', 'get_time', 'Optional[Callable[[], float]]', 'refresh_per_second', 'float', 'style', 'StyleType', 'complete_style', 'StyleType', 'finished_style', 'StyleType', 'pulse_style', 'StyleType', 'update_period', 'float', 'disable', 'bool', 'show_speed', 'bool', 'return', 'Iterable[ProgressType]')):
    '''Track progress by iterating over a sequence.

    You can also track progress of an iterable, which might require that you additionally specify ``total``.

    Args:
        sequence (Iterable[ProgressType]): Values you wish to iterate over and track progress.
        description (str, optional): Description of task show next to progress bar. Defaults to "Working".
        total: (float, optional): Total number of steps. Default is len(sequence).
        completed (int, optional): Number of steps completed so far. Defaults to 0.
        auto_refresh (bool, optional): Automatic refresh, disable to force a refresh after each iteration. Default is True.
        transient: (bool, optional): Clear the progress on exit. Defaults to False.
        console (Console, optional): Console to write to. Default creates internal Console instance.
        refresh_per_second (float): Number of times per second to refresh the progress information. Defaults to 10.
        style (StyleType, optional): Style for the bar background. Defaults to "bar.back".
        complete_style (StyleType, optional): Style for the completed bar. Defaults to "bar.complete".
        finished_style (StyleType, optional): Style for a finished bar. Defaults to "bar.finished".
        pulse_style (StyleType, optional): Style for pulsing bars. Defaults to "bar.pulse".
        update_period (float, optional): Minimum time (in seconds) between calls to update(). Defaults to 0.1.
        disable (bool, optional): Disable display of progress.
        show_speed (bool, optional): Show speed if total isn\'t known. Defaults to True.
    Returns:
        Iterable[ProgressType]: An iterable of the values in the sequence.

    '''
    pass
# WARNING: Decompyle incomplete


class _Reader(BinaryIO, RawIOBase):
    """A reader that tracks progress while it's being read from."""
    
    def __init__(self = None, handle = None, progress = None, task = (True,), close_handle = ('handle', 'BinaryIO', 'progress', "'Progress'", 'task', 'TaskID', 'close_handle', 'bool', 'return', 'None')):
        self.handle = handle
        self.progress = progress
        self.task = task
        self.close_handle = close_handle
        self._closed = False

    
    def __enter__(self = None):
        self.handle.__enter__()
        return self

    
    def __exit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'Optional[Type[BaseException]]', 'exc_val', 'Optional[BaseException]', 'exc_tb', 'Optional[TracebackType]', 'return', 'None')):
        self.close()

    
    def __iter__(self = None):
        return self

    
    def __next__(self = None):
        line = next(self.handle)
        self.progress.advance(self.task, advance = len(line))
        return line

    closed = (lambda self = None: self._closed)()
    
    def fileno(self = None):
        return self.handle.fileno()

    
    def isatty(self = None):
        return self.handle.isatty()

    mode = (lambda self = None: self.handle.mode)()
    name = (lambda self = None: self.handle.name)()
    
    def readable(self = None):
        return self.handle.readable()

    
    def seekable(self = None):
        return self.handle.seekable()

    
    def writable(self = None):
        return False

    
    def read(self = None, size = None):
        block = self.handle.read(size)
        self.progress.advance(self.task, advance = len(block))
        return block

    
    def readinto(self = None, b = None):
        n = self.handle.readinto(b)
        self.progress.advance(self.task, advance = n)
        return n

    
    def readline(self = None, size = None):
        line = self.handle.readline(size)
        self.progress.advance(self.task, advance = len(line))
        return line

    
    def readlines(self = None, hint = None):
        lines = self.handle.readlines(hint)
        self.progress.advance(self.task, advance = sum(map(len, lines)))
        return lines

    
    def close(self = None):
        if self.close_handle:
            self.handle.close()
        self._closed = True

    
    def seek(self = None, offset = None, whence = None):
        pos = self.handle.seek(offset, whence)
        self.progress.update(self.task, completed = pos)
        return pos

    
    def tell(self = None):
        return self.handle.tell()

    
    def write(self = None, s = None):
        raise UnsupportedOperation('write')

    
    def writelines(self = None, lines = None):
        raise UnsupportedOperation('writelines')



def _ReadContext():
    '''_ReadContext'''
    __doc__ = 'A utility class to handle a context for both a reader and a progress.'
    
    def __init__(self = None, progress = None, reader = None):
        self.progress = progress
        self.reader = reader

    
    def __enter__(self = None):
        self.progress.start()
        return self.reader.__enter__()

    
    def __exit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'Optional[Type[BaseException]]', 'exc_val', 'Optional[BaseException]', 'exc_tb', 'Optional[TracebackType]', 'return', 'None')):
        self.progress.stop()
        self.reader.__exit__(exc_type, exc_val, exc_tb)


_ReadContext = <NODE:27>(_ReadContext, '_ReadContext', ContextManager[_I], Generic[_I])

def wrap_file(file = None, total = None, *, description, auto_refresh, console, transient, get_time, refresh_per_second, style, complete_style, finished_style, pulse_style, disable):
    '''Read bytes from a file while tracking progress.

    Args:
        file (Union[str, PathLike[str], BinaryIO]): The path to the file to read, or a file-like object in binary mode.
        total (int): Total number of bytes to read.
        description (str, optional): Description of task show next to progress bar. Defaults to "Reading".
        auto_refresh (bool, optional): Automatic refresh, disable to force a refresh after each iteration. Default is True.
        transient: (bool, optional): Clear the progress on exit. Defaults to False.
        console (Console, optional): Console to write to. Default creates internal Console instance.
        refresh_per_second (float): Number of times per second to refresh the progress information. Defaults to 10.
        style (StyleType, optional): Style for the bar background. Defaults to "bar.back".
        complete_style (StyleType, optional): Style for the completed bar. Defaults to "bar.complete".
        finished_style (StyleType, optional): Style for a finished bar. Defaults to "bar.finished".
        pulse_style (StyleType, optional): Style for pulsing bars. Defaults to "bar.pulse".
        disable (bool, optional): Disable display of progress.
    Returns:
        ContextManager[BinaryIO]: A context manager yielding a progress reader.

    '''
    columns = [
        TextColumn('[progress.description]{task.description}')] if description else []
    columns.extend((BarColumn(style = style, complete_style = complete_style, finished_style = finished_style, pulse_style = pulse_style), DownloadColumn(), TimeRemainingColumn()))
# WARNING: Decompyle incomplete

open = (lambda file = None, mode = None, buffering = None, encoding = typing.overload, errors = (-1, None, None, None), newline = {
    'total': None,
    'description': 'Reading...',
    'auto_refresh': True,
    'console': None,
    'transient': False,
    'get_time': None,
    'refresh_per_second': 10,
    'style': 'bar.back',
    'complete_style': 'bar.complete',
    'finished_style': 'bar.finished',
    'pulse_style': 'bar.pulse',
    'disable': False }, *, total, description, auto_refresh, console, transient, get_time: pass)()
open = (lambda file = None, mode = None, buffering = None, encoding = typing.overload, errors = (-1, None, None, None), newline = {
    'total': None,
    'description': 'Reading...',
    'auto_refresh': True,
    'console': None,
    'transient': False,
    'get_time': None,
    'refresh_per_second': 10,
    'style': 'bar.back',
    'complete_style': 'bar.complete',
    'finished_style': 'bar.finished',
    'pulse_style': 'bar.pulse',
    'disable': False }, *, total, description, auto_refresh, console, transient, get_time: pass)()

def open(file = None, mode = None, buffering = None, encoding = None, errors = ('r', -1, None, None, None), newline = {
    'total': None,
    'description': 'Reading...',
    'auto_refresh': True,
    'console': None,
    'transient': False,
    'get_time': None,
    'refresh_per_second': 10,
    'style': 'bar.back',
    'complete_style': 'bar.complete',
    'finished_style': 'bar.finished',
    'pulse_style': 'bar.pulse',
    'disable': False }, *, total, description, auto_refresh, console, transient, get_time, refresh_per_second, style, complete_style, finished_style, pulse_style, disable):
    '''Read bytes from a file while tracking progress.

    Args:
        path (Union[str, PathLike[str], BinaryIO]): The path to the file to read, or a file-like object in binary mode.
        mode (str): The mode to use to open the file. Only supports "r", "rb" or "rt".
        buffering (int): The buffering strategy to use, see :func:`io.open`.
        encoding (str, optional): The encoding to use when reading in text mode, see :func:`io.open`.
        errors (str, optional): The error handling strategy for decoding errors, see :func:`io.open`.
        newline (str, optional): The strategy for handling newlines in text mode, see :func:`io.open`
        total: (int, optional): Total number of bytes to read. Must be provided if reading from a file handle. Default for a path is os.stat(file).st_size.
        description (str, optional): Description of task show next to progress bar. Defaults to "Reading".
        auto_refresh (bool, optional): Automatic refresh, disable to force a refresh after each iteration. Default is True.
        transient: (bool, optional): Clear the progress on exit. Defaults to False.
        console (Console, optional): Console to write to. Default creates internal Console instance.
        refresh_per_second (float): Number of times per second to refresh the progress information. Defaults to 10.
        style (StyleType, optional): Style for the bar background. Defaults to "bar.back".
        complete_style (StyleType, optional): Style for the completed bar. Defaults to "bar.complete".
        finished_style (StyleType, optional): Style for a finished bar. Defaults to "bar.finished".
        pulse_style (StyleType, optional): Style for pulsing bars. Defaults to "bar.pulse".
        disable (bool, optional): Disable display of progress.
        encoding (str, optional): The encoding to use when reading in text mode.

    Returns:
        ContextManager[BinaryIO]: A context manager yielding a progress reader.

    '''
    columns = [
        TextColumn('[progress.description]{task.description}')] if description else []
    columns.extend((BarColumn(style = style, complete_style = complete_style, finished_style = finished_style, pulse_style = pulse_style), DownloadColumn(), TimeRemainingColumn()))
# WARNING: Decompyle incomplete


class ProgressColumn(ABC):
    '''Base class for a widget to use in progress display.'''
    max_refresh: 'Optional[float]' = None
    
    def __init__(self = None, table_column = None):
        self._table_column = table_column
        self._renderable_cache = { }
        self._update_time = None

    
    def get_table_column(self = None):
        '''Get a table column, used to build tasks table.'''
        if not self._table_column:
            pass
        return Column()

    
    def __call__(self = None, task = None):
        '''Called by the Progress object to return a renderable for the given task.

        Args:
            task (Task): An object containing information regarding the task.

        Returns:
            RenderableType: Anything renderable (including str).
        '''
        current_time = task.get_time()
    # WARNING: Decompyle incomplete

    render = (lambda self = None, task = None: pass)()


class RenderableColumn(ProgressColumn):
    pass
# WARNING: Decompyle incomplete


class SpinnerColumn(ProgressColumn):
    pass
# WARNING: Decompyle incomplete


class TextColumn(ProgressColumn):
    pass
# WARNING: Decompyle incomplete


class BarColumn(ProgressColumn):
    pass
# WARNING: Decompyle incomplete


class TimeElapsedColumn(ProgressColumn):
    '''Renders time elapsed.'''
    
    def render(self = None, task = None):
        '''Show time elapsed.'''
        elapsed = task.finished_time if task.finished else task.elapsed
    # WARNING: Decompyle incomplete



class TaskProgressColumn(TextColumn):
    pass
# WARNING: Decompyle incomplete


class TimeRemainingColumn(ProgressColumn):
    pass
# WARNING: Decompyle incomplete


class FileSizeColumn(ProgressColumn):
    '''Renders completed filesize.'''
    
    def render(self = None, task = None):
        '''Show data completed.'''
        data_size = filesize.decimal(int(task.completed))
        return Text(data_size, style = 'progress.filesize')



class TotalFileSizeColumn(ProgressColumn):
    '''Renders total filesize.'''
    
    def render(self = None, task = None):
        '''Show data completed.'''
        pass
    # WARNING: Decompyle incomplete



class MofNCompleteColumn(ProgressColumn):
    pass
# WARNING: Decompyle incomplete


class DownloadColumn(ProgressColumn):
    pass
# WARNING: Decompyle incomplete


class TransferSpeedColumn(ProgressColumn):
    '''Renders human readable transfer speed.'''
    
    def render(self = None, task = None):
        '''Show data transfer speed.'''
        pass
    # WARNING: Decompyle incomplete



class ProgressSample(NamedTuple):
    completed: 'float' = 'Sample of progress for a given time.'

Task = <NODE:12>()

class Progress(JupyterMixin):
    '''Renders an auto-updating progress bar(s).

    Args:
        console (Console, optional): Optional Console instance. Defaults to an internal Console instance writing to stdout.
        auto_refresh (bool, optional): Enable auto refresh. If disabled, you will need to call `refresh()`.
        refresh_per_second (float, optional): Number of times per second to refresh the progress information. Defaults to 10.
        speed_estimate_period: (float, optional): Period (in seconds) used to calculate the speed estimate. Defaults to 30.
        transient: (bool, optional): Clear the progress on exit. Defaults to False.
        redirect_stdout: (bool, optional): Enable redirection of stdout, so ``print`` may be used. Defaults to True.
        redirect_stderr: (bool, optional): Enable redirection of stderr. Defaults to True.
        get_time: (Callable, optional): A callable that gets the current time, or None to use Console.get_time. Defaults to None.
        disable (bool, optional): Disable progress display. Defaults to False
        expand (bool, optional): Expand tasks table to fit width. Defaults to False.
    '''
    
    def __init__(self = None, *, console, auto_refresh, refresh_per_second, speed_estimate_period, transient, redirect_stdout, redirect_stderr, get_time, disable, expand, *columns):
        pass
    # WARNING: Decompyle incomplete

    get_default_columns = (lambda cls = None: (TextColumn('[progress.description]{task.description}'), BarColumn(), TaskProgressColumn(), TimeRemainingColumn()))()
    console = (lambda self = None: self.live.console)()
    tasks = (lambda self = None: self._lockNone(None, None)with None:
if not None, list(self._tasks.values()):
pass)()
    task_ids = (lambda self = None: self._lockNone(None, None)with None:
if not None, list(self._tasks.keys()):
pass)()
    finished = (lambda self = None: self._lockif not self._tasks:
None(None, None)TrueNone(None, None)with None:
if not None, (lambda .0: pass# WARNING: Decompyle incomplete
)(self._tasks.values()()):
                pass
)()
    
    def start(self = None):
        '''Start the progress display.'''
        if not self.disable:
            self.live.start(refresh = True)
            return None

    
    def stop(self = None):
        '''Stop the progress display.'''
        if not self.disable:
            self.live.stop()
            if not self.console.is_interactive or self.console.is_jupyter:
                self.console.print()
                return None
            return None
        return None

    
    def __enter__(self = None):
        self.start()
        return self

    
    def __exit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'Optional[Type[BaseException]]', 'exc_val', 'Optional[BaseException]', 'exc_tb', 'Optional[TracebackType]', 'return', 'None')):
        self.stop()

    
    def track(self, sequence, total = None, completed = None, task_id = None, description = (None, 0, None, 'Working...', 0.1), update_period = ('sequence', 'Iterable[ProgressType]', 'total', 'Optional[float]', 'completed', 'int', 'task_id', 'Optional[TaskID]', 'description', 'str', 'update_period', 'float', 'return', 'Iterable[ProgressType]')):
        '''Track progress by iterating over a sequence.

        You can also track progress of an iterable, which might require that you additionally specify ``total``.

        Args:
            sequence (Iterable[ProgressType]): Values you want to iterate over and track progress.
            total: (float, optional): Total number of steps. Default is len(sequence).
            completed (int, optional): Number of steps completed so far. Defaults to 0.
            task_id: (TaskID): Task to track. Default is new task.
            description: (str, optional): Description of task, if new task is created.
            update_period (float, optional): Minimum time (in seconds) between calls to update(). Defaults to 0.1.

        Returns:
            Iterable[ProgressType]: An iterable of values taken from the provided sequence.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def wrap_file(self = None, file = None, total = None, *, task_id, description):
        '''Track progress file reading from a binary file.

        Args:
            file (BinaryIO): A file-like object opened in binary mode.
            total (int, optional): Total number of bytes to read. This must be provided unless a task with a total is also given.
            task_id (TaskID): Task to track. Default is new task.
            description (str, optional): Description of task, if new task is created.

        Returns:
            BinaryIO: A readable file-like object in binary mode.

        Raises:
            ValueError: When no total value can be extracted from the arguments or the task.
        '''
        total_bytes = None
    # WARNING: Decompyle incomplete

    open = (lambda self = None, file = None, mode = None, buffering = typing.overload, encoding = (-1, None, None, None), errors = {
        'total': None,
        'task_id': None,
        'description': 'Reading...' }, newline = ('file', "Union[str, 'PathLike[str]', bytes]", 'mode', "Literal['rb']", 'buffering', 'int', 'encoding', 'Optional[str]', 'errors', 'Optional[str]', 'newline', 'Optional[str]', 'total', 'Optional[int]', 'task_id', 'Optional[TaskID]', 'description', 'str', 'return', 'BinaryIO'), *, total, task_id, description,
