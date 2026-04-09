# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: subprocess.pyc (Python 3.11)

'''Subprocesses with accessible I/O streams

This module allows you to spawn processes, connect to their
input/output/error pipes, and obtain their return codes.

For a complete description of this module see the Python documentation.

Main API
========
run(...): Runs a command, waits for it to complete, then returns a
          CompletedProcess instance.
Popen(...): A class for flexibly executing a command in a new process

Constants
---------
DEVNULL: Special value that indicates that os.devnull should be used
PIPE:    Special value that indicates a pipe should be created
STDOUT:  Special value that indicates that stderr should go to stdout


Older API
=========
call(...): Runs a command, waits for it to complete, then returns
    the return code.
check_call(...): Same as call() but raises CalledProcessError()
    if return code is not 0
check_output(...): Same as check_call() but returns the contents of
    stdout instead of a return code
getoutput(...): Runs a command in the shell, waits for it to complete,
    then returns the output
getstatusoutput(...): Runs a command in the shell, waits for it to complete,
    then returns a (exitcode, output) tuple
'''
import builtins
import errno
import io
import locale
import os
import time
import signal
import sys
import threading
import warnings
import contextlib
from time import monotonic as _time
import types

try:
    import fcntl
except ImportError:
    fcntl = None

__all__ = [
    'Popen',
    'PIPE',
    'STDOUT',
    'call',
    'check_call',
    'getstatusoutput',
    'getoutput',
    'check_output',
    'run',
    'CalledProcessError',
    'DEVNULL',
    'SubprocessError',
    'TimeoutExpired',
    'CompletedProcess']

try:
    import msvcrt
    _mswindows = True
except ModuleNotFoundError:
    _mswindows = False

_can_fork_exec = sys.platform not in frozenset({'wasi', 'emscripten'})
if _mswindows:
    import _winapi
    from _winapi import CREATE_NEW_CONSOLE, CREATE_NEW_PROCESS_GROUP, STD_INPUT_HANDLE, STD_OUTPUT_HANDLE, STD_ERROR_HANDLE, SW_HIDE, STARTF_USESTDHANDLES, STARTF_USESHOWWINDOW, ABOVE_NORMAL_PRIORITY_CLASS, BELOW_NORMAL_PRIORITY_CLASS, HIGH_PRIORITY_CLASS, IDLE_PRIORITY_CLASS, NORMAL_PRIORITY_CLASS, REALTIME_PRIORITY_CLASS, CREATE_NO_WINDOW, DETACHED_PROCESS, CREATE_DEFAULT_ERROR_MODE, CREATE_BREAKAWAY_FROM_JOB
    __all__.extend([
        'CREATE_NEW_CONSOLE',
        'CREATE_NEW_PROCESS_GROUP',
        'STD_INPUT_HANDLE',
        'STD_OUTPUT_HANDLE',
        'STD_ERROR_HANDLE',
        'SW_HIDE',
        'STARTF_USESTDHANDLES',
        'STARTF_USESHOWWINDOW',
        'STARTUPINFO',
        'ABOVE_NORMAL_PRIORITY_CLASS',
        'BELOW_NORMAL_PRIORITY_CLASS',
        'HIGH_PRIORITY_CLASS',
        'IDLE_PRIORITY_CLASS',
        'NORMAL_PRIORITY_CLASS',
        'REALTIME_PRIORITY_CLASS',
        'CREATE_NO_WINDOW',
        'DETACHED_PROCESS',
        'CREATE_DEFAULT_ERROR_MODE',
        'CREATE_BREAKAWAY_FROM_JOB'])
elif _can_fork_exec:
    from _posixsubprocess import fork_exec as _fork_exec
    _waitpid = os.waitpid
    _waitstatus_to_exitcode = os.waitstatus_to_exitcode
    _WIFSTOPPED = os.WIFSTOPPED
    _WSTOPSIG = os.WSTOPSIG
    _WNOHANG = os.WNOHANG
else:
    _fork_exec = None
    _waitpid = None
    _waitstatus_to_exitcode = None
    _WIFSTOPPED = None
    _WSTOPSIG = None
    _WNOHANG = None
import select
import selectors

class SubprocessError(Exception):
    pass


class CalledProcessError(SubprocessError):
    '''Raised when run() is called with check=True and the process
    returns a non-zero exit status.

    Attributes:
      cmd, returncode, stdout, stderr, output
    '''
    
    def __init__(self, returncode, cmd, output, stderr = (None, None)):
        self.returncode = returncode
        self.cmd = cmd
        self.output = output
        self.stderr = stderr

    
    def __str__(self):
        if self.returncode and self.returncode < 0:
            
            try:
                return f'''Command \'{self.cmd!s}\' died with {signal.Signals(-(self.returncode))!r}.'''
            except ValueError:
                return 
                return "Command '%s' returned non-zero exit status %d." % (self.cmd, self.returncode)


    stdout = (lambda self: self.output)()
    stdout = (lambda self, value: self.output = value)()


class TimeoutExpired(SubprocessError):
    '''This exception is raised when the timeout expires while waiting for a
    child process.

    Attributes:
        cmd, output, stdout, stderr, timeout
    '''
    
    def __init__(self, cmd, timeout, output, stderr = (None, None)):
        self.cmd = cmd
        self.timeout = timeout
        self.output = output
        self.stderr = stderr

    
    def __str__(self):
        return f'''Command \'{self.cmd!s}\' timed out after {self.timeout!s} seconds'''

    stdout = (lambda self: self.output)()
    stdout = (lambda self, value: self.output = value)()

PIPE = -1
STDOUT = -2
DEVNULL = -3

def _optim_args_from_interpreter_flags():
    '''Return a list of command-line arguments reproducing the current
    optimization settings in sys.flags.'''
    args = []
    value = sys.flags.optimize
    if value > 0:
        args.append('-' + 'O' * value)
    return args


def _args_from_interpreter_flags():
    '''Return a list of command-line arguments reproducing the current
    settings in sys.flags, sys.warnoptions and sys._xoptions.'''
    flag_opt_map = {
        'debug': 'd',
        'dont_write_bytecode': 'B',
        'no_site': 'S',
        'verbose': 'v',
        'bytes_warning': 'b',
        'quiet': 'q' }
    args = _optim_args_from_interpreter_flags()
    for flag, opt in flag_opt_map.items():
        v = getattr(sys.flags, flag)
        if v > 0:
            args.append('-' + opt * v)
        if sys.flags.isolated:
            args.append('-I')
        elif sys.flags.ignore_environment:
            args.append('-E')
    if sys.flags.no_user_site:
        args.append('-s')
    if sys.flags.safe_path:
        args.append('-P')
    warnopts = sys.warnoptions[:]
    xoptions = getattr(sys, '_xoptions', { })
    bytes_warning = sys.flags.bytes_warning
    dev_mode = sys.flags.dev_mode
    if bytes_warning > 1:
        warnopts.remove('error::BytesWarning')
    elif bytes_warning:
        warnopts.remove('default::BytesWarning')
    if dev_mode:
        warnopts.remove('default')
    for opt in warnopts:
        args.append('-W' + opt)
        if dev_mode:
            args.extend(('-X', 'dev'))
    for opt in ('faulthandler', 'tracemalloc', 'importtime', 'frozen_modules', 'showrefcount', 'utf8'):
        if opt in xoptions:
            value = xoptions[opt]
            if value is True:
                arg = opt
            else:
                arg = f'''{opt!s}={value!s}'''
            args.extend(('-X', arg))
        return args


def _text_encoding():
    pass
# WARNING: Decompyle incomplete


def call(*, timeout, *popenargs, **kwargs):
    '''Run command with arguments.  Wait for command to complete or
    timeout, then return the returncode attribute.

    The arguments are the same as for the Popen constructor.  Example:

    retcode = call(["ls", "-l"])
    '''
    pass
# WARNING: Decompyle incomplete


def check_call(*popenargs, **kwargs):
    '''Run command with arguments.  Wait for command to complete.  If
    the exit code was zero then return, otherwise raise
    CalledProcessError.  The CalledProcessError object will have the
    return code in the returncode attribute.

    The arguments are the same as for the call function.  Example:

    check_call(["ls", "-l"])
    '''
    pass
# WARNING: Decompyle incomplete


def check_output(*, timeout, *popenargs, **kwargs):
    '''Run command with arguments and return its output.

    If the exit code was non-zero it raises a CalledProcessError.  The
    CalledProcessError object will have the return code in the returncode
    attribute and output in the output attribute.

    The arguments are the same as for the Popen constructor.  Example:

    >>> check_output(["ls", "-l", "/dev/null"])
    b\'crw-rw-rw- 1 root root 1, 3 Oct 18  2007 /dev/null\\n\'

    The stdout argument is not allowed as it is used internally.
    To capture standard error in the result, use stderr=STDOUT.

    >>> check_output(["/bin/sh", "-c",
    ...               "ls -l non_existent_file ; exit 0"],
    ...              stderr=STDOUT)
    b\'ls: non_existent_file: No such file or directory\\n\'

    There is an additional optional argument, "input", allowing you to
    pass a string to the subprocess\'s stdin.  If you use this argument
    you may not also use the Popen constructor\'s "stdin" argument, as
    it too will be used internally.  Example:

    >>> check_output(["sed", "-e", "s/foo/bar/"],
    ...              input=b"when in the course of fooman events\\n")
    b\'when in the course of barman events\\n\'

    By default, all communication is in bytes, and therefore any "input"
    should be bytes, and the return value will be bytes.  If in text mode,
    any "input" should be a string, and the return value will be a string
    decoded according to locale encoding, or by "encoding" if set. Text mode
    is triggered by setting any of text, encoding, errors or universal_newlines.
    '''
    pass
# WARNING: Decompyle incomplete


class CompletedProcess(object):
    '''A process that has finished running.

    This is returned by run().

    Attributes:
      args: The list or str args passed to run().
      returncode: The exit code of the process, negative for signals.
      stdout: The standard output (None if not captured).
      stderr: The standard error (None if not captured).
    '''
    
    def __init__(self, args, returncode, stdout, stderr = (None, None)):
        self.args = args
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr

    
    def __repr__(self):
        args = [
            'args={!r}'.format(self.args),
            'returncode={!r}'.format(self.returncode)]
    # WARNING: Decompyle incomplete

    __class_getitem__ = classmethod(types.GenericAlias)
    
    def check_returncode(self):
        '''Raise CalledProcessError if the exit code is non-zero.'''
        if self.returncode:
            raise CalledProcessError(self.returncode, self.args, self.stdout, self.stderr)



def run(*, input, capture_output, timeout, check, *popenargs, **kwargs):
    '''Run command with arguments and return a CompletedProcess instance.

    The returned instance will have attributes args, returncode, stdout and
    stderr. By default, stdout and stderr are not captured, and those attributes
    will be None. Pass stdout=PIPE and/or stderr=PIPE in order to capture them,
    or pass capture_output=True to capture both.

    If check is True and the exit code was non-zero, it raises a
    CalledProcessError. The CalledProcessError object will have the return code
    in the returncode attribute, and output & stderr attributes if those streams
    were captured.

    If timeout is given, and the process takes too long, a TimeoutExpired
    exception will be raised.

    There is an optional argument "input", allowing you to
    pass bytes or a string to the subprocess\'s stdin.  If you use this argument
    you may not also use the Popen constructor\'s "stdin" argument, as
    it will be used internally.

    By default, all communication is in bytes, and therefore any "input" should
    be bytes, and the stdout and stderr will be bytes. If in text mode, any
    "input" should be a string, and stdout and stderr will be strings decoded
    according to locale encoding, or by "encoding" if set. Text mode is
    triggered by setting any of text, encoding, errors or universal_newlines.

    The other arguments are the same as for the Popen constructor.
    '''
    pass
# WARNING: Decompyle incomplete


def list2cmdline(seq):
    '''
    Translate a sequence of arguments into a command line
    string, using the same rules as the MS C runtime:

    1) Arguments are delimited by white space, which is either a
       space or a tab.

    2) A string surrounded by double quotation marks is
       interpreted as a single argument, regardless of white space
       contained within.  A quoted string can be embedded in an
       argument.

    3) A double quotation mark preceded by a backslash is
       interpreted as a literal double quotation mark.

    4) Backslashes are interpreted literally, unless they
       immediately precede a double quotation mark.

    5) If backslashes immediately precede a double quotation mark,
       every pair of backslashes is interpreted as a literal
       backslash.  If the number of backslashes is odd, the last
       backslash escapes the next double quotation mark as
       described in rule 3.
    '''
    result = []
    needquote = False
    for arg in map(os.fsdecode, seq):
        bs_buf = []
        if result:
            result.append(' ')
        if not ' ' in arg:
            if not '\t' in arg:
                needquote = not arg
                if needquote:
                    result.append('"')
        for c in arg:
            if c == '\\':
                bs_buf.append(c)
                continue
            if c == '"':
                result.append('\\' * len(bs_buf) * 2)
                bs_buf = []
                result.append('\\"')
                continue
            if bs_buf:
                result.extend(bs_buf)
                bs_buf = []
            result.append(c)
            if bs_buf:
                result.extend(bs_buf)
        if needquote:
            result.extend(bs_buf)
            result.append('"')
        return ''.join(result)


def getstatusoutput(cmd = None, *, encoding, errors):
    """Return (exitcode, output) of executing cmd in a shell.

    Execute the string 'cmd' in a shell with 'check_output' and
    return a 2-tuple (status, output). The locale encoding is used
    to decode the output and process newlines.

    A trailing newline is stripped from the output.
    The exit status for the command can be interpreted
    according to the rules for the function 'wait'. Example:

    >>> import subprocess
    >>> subprocess.getstatusoutput('ls /bin/ls')
    (0, '/bin/ls')
    >>> subprocess.getstatusoutput('cat /bin/junk')
    (1, 'cat: /bin/junk: No such file or directory')
    >>> subprocess.getstatusoutput('/bin/junk')
    (127, 'sh: /bin/junk: not found')
    >>> subprocess.getstatusoutput('/bin/kill $$')
    (-15, '')
    """
    
    try:
        data = check_output(cmd, shell = True, text = True, stderr = STDOUT, encoding = encoding, errors = errors)
        exitcode = 0
    except CalledProcessError:
        ex = None
        data = ex.output
        exitcode = ex.returncode
        ex = None
        del ex
    except:
        ex = None
        del ex

    if data[-1:] == '\n':
        data = data[:-1]
    return (exitcode, data)


def getoutput(cmd = None, *, encoding, errors):
    """Return output (stdout or stderr) of executing cmd in a shell.

    Like getstatusoutput(), except the exit status is ignored and the return
    value is a string containing the command's output.  Example:

    >>> import subprocess
    >>> subprocess.getoutput('ls /bin/ls')
    '/bin/ls'
    """
    return getstatusoutput(cmd, encoding = encoding, errors = errors)[1]


def _use_posix_spawn():
    '''Check if posix_spawn() can be used for subprocess.

    subprocess requires a posix_spawn() implementation that properly reports
    errors to the parent process, & sets errno on the following failures:

    * Process attribute actions failed.
    * File actions failed.
    * exec() failed.

    Prefer an implementation which can use vfork() in some cases for best
    performance.
    '''
    if not _mswindows or hasattr(os, 'posix_spawn'):
        return False
    if None.platform in ('darwin', 'sunos5'):
        return True
    
    try:
        ver = os.confstr('CS_GNU_LIBC_VERSION')
        parts = ver.split(maxsplit = 1)
        if len(parts) != 2:
            raise ValueError
        libc = parts[0]
        version = tuple(map(int, parts[1].split('.')))
        if sys.platform == 'linux' and libc == 'glibc' and version >= (2, 24):
            return True
    except (AttributeError, ValueError, OSError):
        pass

    return False

_USE_POSIX_SPAWN = _use_posix_spawn()
_USE_VFORK = True

class Popen:
