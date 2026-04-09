# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: testing.pyc (Python 3.11)

import contextlib
import io
import os
import shlex
import shutil
import sys
import tempfile
import typing as t
from types import TracebackType
from  import _compat
from  import formatting
from  import termui
from  import utils
from _compat import _find_binary_reader
if t.TYPE_CHECKING:
    from core import BaseCommand

class EchoingStdin:
    
    def __init__(self = None, input = None, output = None):
        self._input = input
        self._output = output
        self._paused = False

    
    def __getattr__(self = None, x = None):
        return getattr(self._input, x)

    
    def _echo(self = None, rv = None):
        if not self._paused:
            self._output.write(rv)
        return rv

    
    def read(self = None, n = None):
        return self._echo(self._input.read(n))

    
    def read1(self = None, n = None):
        return self._echo(self._input.read1(n))

    
    def readline(self = None, n = None):
        return self._echo(self._input.readline(n))

    
    def readlines(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return repr(self._input)


_pause_echo = (lambda stream = None: pass# WARNING: Decompyle incomplete
)()

class _NamedTextIOWrapper(io.TextIOWrapper):
    pass
# WARNING: Decompyle incomplete


def make_input_stream(input = None, charset = None):
    pass
# WARNING: Decompyle incomplete


class Result:
    '''Holds the captured result of an invoked CLI script.'''
    
    def __init__(self, runner, stdout_bytes, stderr_bytes = None, return_value = None, exit_code = None, exception = (None,), exc_info = ('runner', 'CliRunner', 'stdout_bytes', bytes, 'stderr_bytes', t.Optional[bytes], 'return_value', t.Any, 'exit_code', int, 'exception', t.Optional[BaseException], 'exc_info', t.Optional[t.Tuple[(t.Type[BaseException], BaseException, TracebackType)]])):
        self.runner = runner
        self.stdout_bytes = stdout_bytes
        self.stderr_bytes = stderr_bytes
        self.return_value = return_value
        self.exit_code = exit_code
        self.exception = exception
        self.exc_info = exc_info

    output = (lambda self = None: self.stdout)()
    stdout = (lambda self = None: self.stdout_bytes.decode(self.runner.charset, 'replace').replace('\r\n', '\n'))()
    stderr = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def __repr__(self = None):
        exc_str = repr(self.exception) if self.exception else 'okay'
        return f'''<{type(self).__name__} {exc_str}>'''



class CliRunner:
    '''The CLI runner provides functionality to invoke a Click command line
    script for unittesting purposes in a isolated environment.  This only
    works in single-threaded systems without any concurrency as it changes the
    global interpreter state.

    :param charset: the character set for the input and output data.
    :param env: a dictionary with environment variables for overriding.
    :param echo_stdin: if this is set to `True`, then reading from stdin writes
                       to stdout.  This is useful for showing examples in
                       some circumstances.  Note that regular prompts
                       will automatically echo the input.
    :param mix_stderr: if this is set to `False`, then stdout and stderr are
                       preserved as independent streams.  This is useful for
                       Unix-philosophy apps that have predictable stdout and
                       noisy stderr, such that each may be measured
                       independently
    '''
    
    def __init__(self = None, charset = None, env = None, echo_stdin = ('utf-8', None, False, True), mix_stderr = ('charset', str, 'env', t.Optional[t.Mapping[(str, t.Optional[str])]], 'echo_stdin', bool, 'mix_stderr', bool, 'return', None)):
