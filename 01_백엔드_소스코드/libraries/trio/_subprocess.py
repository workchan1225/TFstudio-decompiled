# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _subprocess.pyc (Python 3.11)

from __future__ import annotations
import contextlib
import os
import subprocess
import sys
import warnings
from contextlib import ExitStack
from functools import partial
from typing import TYPE_CHECKING, Final, Literal, Protocol, TypeAlias, TypedDict, overload
import trio
from _core import ClosedResourceError, TaskStatus
from _highlevel_generic import StapledStream
from _subprocess_platform import create_pipe_from_child_output, create_pipe_to_child_stdin, wait_child_exiting
from _sync import Lock
from _util import NoPublicConstructor, final
if TYPE_CHECKING:
    import signal
    from collections.abc import Awaitable, Callable, Iterable, Mapping, Sequence
    from io import TextIOWrapper
    from typing_extensions import Unpack
    from _abc import ReceiveStream, SendStream
can_try_pidfd_open: 'bool' = str | bytes | os.PathLike[str] | os.PathLike[bytes]
if TYPE_CHECKING:
    
    def pidfd_open(fd = None, flags = None):
        pass

    from _subprocess_platform import ClosableReceiveStream, ClosableSendStream
else:
    can_try_pidfd_open = True
    
    try:
        from os import pidfd_open
    except ImportError:
        if sys.platform == 'linux':
            import ctypes
            _cdll_for_pidfd_open = ctypes.CDLL(None, use_errno = True)
            _cdll_for_pidfd_open.syscall.restype = ctypes.c_long
            _cdll_for_pidfd_open.syscall.argtypes = [
                ctypes.c_long,
                ctypes.c_long,
                ctypes.c_long]
            __NR_pidfd_open = 434
            
            def pidfd_open(fd = None, flags = None):
                result = _cdll_for_pidfd_open.syscall(__NR_pidfd_open, fd, flags)
                if result < 0:
                    err = ctypes.get_errno()
                    raise OSError(err, os.strerror(err))
                return result

        else:
            can_try_pidfd_open = False

    
    class HasFileno(Protocol):
        '''Represents any file-like object that has a file descriptor.'''
        
        def fileno(self = None):
            pass


    
    def Process():
        '''Process'''
        __doc__ = "A child process. Like :class:`subprocess.Popen`, but async.\n\n    This class has no public constructor. The most common way to get a\n    `Process` object is to combine `Nursery.start` with `run_process`::\n\n       process_object = await nursery.start(run_process, ...)\n\n    This way, `run_process` supervises the process and makes sure that it is\n    cleaned up properly, while optionally checking the return value, feeding\n    it input, and so on.\n\n    If you need more control – for example, because you want to spawn a child\n    process that outlives your program – then another option is to use\n    `trio.lowlevel.open_process`::\n\n       process_object = await trio.lowlevel.open_process(...)\n\n    Attributes:\n      args (str or list): The ``command`` passed at construction time,\n          specifying the process to execute and its arguments.\n      pid (int): The process ID of the child process managed by this object.\n      stdin (trio.abc.SendStream or None): A stream connected to the child's\n          standard input stream: when you write bytes here, they become available\n          for the child to read. Only available if the :class:`Process`\n          was constructed using ``stdin=PIPE``; otherwise this will be None.\n      stdout (trio.abc.ReceiveStream or None): A stream connected to\n          the child's standard output stream: when the child writes to\n          standard output, the written bytes become available for you\n          to read here. Only available if the :class:`Process` was\n          constructed using ``stdout=PIPE``; otherwise this will be None.\n      stderr (trio.abc.ReceiveStream or None): A stream connected to\n          the child's standard error stream: when the child writes to\n          standard error, the written bytes become available for you\n          to read here. Only available if the :class:`Process` was\n          constructed using ``stderr=PIPE``; otherwise this will be None.\n      stdio (trio.StapledStream or None): A stream that sends data to\n          the child's standard input and receives from the child's standard\n          output. Only available if both :attr:`stdin` and :attr:`stdout` are\n          available; otherwise this will be None.\n\n    "
        universal_newlines: 'Final' = False
        encoding: 'Final' = None
        errors: 'Final' = None
        _wait_for_exit_data: 'object' = None
        
        def __init__(self, popen = None, stdin = None, stdout = None, stderr = ('popen', 'subprocess.Popen[bytes]', 'stdin', 'SendStream | None', 'stdout', 'ReceiveStream | None', 'stderr', 'ReceiveStream | None', 'return', 'None')):
            self._proc = popen
            self.stdin = stdin
            self.stdout = stdout
            self.stderr = stderr
            self.stdio = None
        # WARNING: Decompyle incomplete

        
        def __repr__(self = None):
            returncode = self.returncode
        # WARNING: Decompyle incomplete

        returncode = (lambda self = None: result = self._proc.poll()# WARNING: Decompyle incomplete
)()
        
        def _close_pidfd(self = None):
            pass
        # WARNING: Decompyle incomplete

        
        async def wait(self = None):
            '''Block until the process exits.

        Returns:
          The exit status of the process; see :attr:`returncode`.
        '''
            pass
        # WARNING: Decompyle incomplete

        
        def poll(self = None):
            """Returns the exit status of the process (an integer), or ``None`` if
        it's still running.

        Note that on Trio (unlike the standard library `subprocess.Popen`),
        ``process.poll()`` and ``process.returncode`` always give the same
        result. See `returncode` for more details. This method is only
        included to make it easier to port code from `subprocess`.

        """
            return self.returncode

        
        def send_signal(self = None, sig = None):
            '''Send signal ``sig`` to the process.

        On UNIX, ``sig`` may be any signal defined in the
        :mod:`signal` module, such as ``signal.SIGINT`` or
        ``signal.SIGTERM``. On Windows, it may be anything accepted by
        the standard library :meth:`subprocess.Popen.send_signal`.
        '''
            self._proc.send_signal(sig)

        
        def terminate(self = None):
            '''Terminate the process, politely if possible.

        On UNIX, this is equivalent to
        ``send_signal(signal.SIGTERM)``; by convention this requests
        graceful termination, but a misbehaving or buggy process might
        ignore it. On Windows, :meth:`terminate` forcibly terminates the
        process in the same manner as :meth:`kill`.
        '''
            self._proc.terminate()

        
        def kill(self = None):
            '''Immediately terminate the process.

        On UNIX, this is equivalent to
        ``send_signal(signal.SIGKILL)``.  On Windows, it calls
        ``TerminateProcess``. In both cases, the process cannot
        prevent itself from being killed, but the termination will be
        delivered asynchronously; use :meth:`wait` if you want to
        ensure the process is actually dead before proceeding.
        '''
            self._proc.kill()


    Process = <NODE:27>(Process, 'Process', metaclass = NoPublicConstructor)()
    
    async def _open_process(command = None, *, stdin, stdout, stderr, **options):
        """Execute a child program in a new process.

    After construction, you can interact with the child process by writing data to its
    `~trio.Process.stdin` stream (a `~trio.abc.SendStream`), reading data from its
    `~trio.Process.stdout` and/or `~trio.Process.stderr` streams (both
    `~trio.abc.ReceiveStream`\\s), sending it signals using `~trio.Process.terminate`,
    `~trio.Process.kill`, or `~trio.Process.send_signal`, and waiting for it to exit
    using `~trio.Process.wait`. See `trio.Process` for details.

    Each standard stream is only available if you specify that a pipe should be created
    for it. For example, if you pass ``stdin=subprocess.PIPE``, you can write to the
    `~trio.Process.stdin` stream, else `~trio.Process.stdin` will be ``None``.

    Unlike `trio.run_process`, this function doesn't do any kind of automatic
    management of the child process. It's up to you to implement whatever semantics you
    want.

    Args:
      command: The command to run. Typically this is a sequence of strings or
          bytes such as ``['ls', '-l', 'directory with spaces']``, where the
          first element names the executable to invoke and the other elements
          specify its arguments. With ``shell=True`` in the ``**options``, or on
          Windows, ``command`` can be a string or bytes, which will be parsed
          following platform-dependent :ref:`quoting rules
          <subprocess-quoting>`. In all cases ``command`` can be a path or a
          sequence of paths.
      stdin: Specifies what the child process's standard input
          stream should connect to: output written by the parent
          (``subprocess.PIPE``), nothing (``subprocess.DEVNULL``),
          or an open file (pass a file descriptor or something whose
          ``fileno`` method returns one). If ``stdin`` is unspecified,
          the child process will have the same standard input stream
          as its parent.
      stdout: Like ``stdin``, but for the child process's standard output
          stream.
      stderr: Like ``stdin``, but for the child process's standard error
          stream. An additional value ``subprocess.STDOUT`` is supported,
          which causes the child's standard output and standard error
          messages to be intermixed on a single standard output stream,
          attached to whatever the ``stdout`` option says to attach it to.
      **options: Other :ref:`general subprocess options <subprocess-options>`
          are also accepted.

    Returns:
      A new `trio.Process` object.

    Raises:
      OSError: if the process spawning fails, for example because the
         specified command could not be found.

    """
        pass
    # WARNING: Decompyle incomplete

    
    async def _windows_deliver_cancel(p = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def _posix_deliver_cancel(p = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def _run_process(command = None, *, stdin, capture_stdout, capture_stderr, check, deliver_cancel, task_status, **options):
        '''Run ``command`` in a subprocess and wait for it to complete.

    This function can be called in two different ways.

    One option is a direct call, like::

        completed_process_info = await trio.run_process(...)

    In this case, it returns a :class:`subprocess.CompletedProcess` instance
    describing the results. Use this if you want to treat a process like a
    function call.

    The other option is to run it as a task using `Nursery.start` – the enhanced version
    of `~Nursery.start_soon` that lets a task pass back a value during startup::

        process = await nursery.start(trio.run_process, ...)

    In this case, `~Nursery.start` returns a `Process` object that you can use
    to interact with the process while it\'s running. Use this if you want to
    treat a process like a background task.

    Either way, `run_process` makes sure that the process has exited before
    returning, handles cancellation, optionally checks for errors, and
    provides some convenient shorthands for dealing with the child\'s
    input/output.

    **Input:** `run_process` supports all the same ``stdin=`` arguments as
    `subprocess.Popen`. In addition, if you simply want to pass in some fixed
    data, you can pass a plain `bytes` object, and `run_process` will take
    care of setting up a pipe, feeding in the data you gave, and then sending
    end-of-file. The default is ``b""``, which means that the child will receive
    an empty stdin. If you want the child to instead read from the parent\'s
    stdin, use ``stdin=None``.

    **Output:** By default, any output produced by the subprocess is
    passed through to the standard output and error streams of the
    parent Trio process.

    When calling `run_process` directly, you can capture the subprocess\'s output by
    passing ``capture_stdout=True`` to capture the subprocess\'s standard output, and/or
    ``capture_stderr=True`` to capture its standard error. Captured data is collected up
    by Trio into an in-memory buffer, and then provided as the
    :attr:`~subprocess.CompletedProcess.stdout` and/or
    :attr:`~subprocess.CompletedProcess.stderr` attributes of the returned
    :class:`~subprocess.CompletedProcess` object. The value for any stream that was not
    captured will be ``None``.

    If you want to capture both stdout and stderr while keeping them
    separate, pass ``capture_stdout=True, capture_stderr=True``.

    If you want to capture both stdout and stderr but mixed together
    in the order they were printed, use: ``capture_stdout=True, stderr=subprocess.STDOUT``.
    This directs the child\'s stderr into its stdout, so the combined
    output will be available in the `~subprocess.CompletedProcess.stdout`
    attribute.

    If you\'re using ``await nursery.start(trio.run_process, ...)`` and want to capture
    the subprocess\'s output for further processing, then use ``stdout=subprocess.PIPE``
    and then make sure to read the data out of the `Process.stdout` stream. If you want
    to capture stderr separately, use ``stderr=subprocess.PIPE``. If you want to capture
    both, but mixed together in the correct order, use ``stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT``.

    **Error checking:** If the subprocess exits with a nonzero status
    code, indicating failure, :func:`run_process` raises a
    :exc:`subprocess.CalledProcessError` exception rather than
    returning normally. The captured outputs are still available as
    the :attr:`~subprocess.CalledProcessError.stdout` and
    :attr:`~subprocess.CalledProcessError.stderr` attributes of that
    exception.  To disable this behavior, so that :func:`run_process`
    returns normally even if the subprocess exits abnormally, pass ``check=False``.

    Note that this can make the ``capture_stdout`` and ``capture_stderr``
    arguments useful even when starting `run_process` as a task: if you only
    care about the output if the process fails, then you can enable capturing
    and then read the output off of the `~subprocess.CalledProcessError`.

    **Cancellation:** If cancelled, `run_process` sends a termination
    request to the subprocess, then waits for it to fully exit. The
    ``deliver_cancel`` argument lets you control how the process is terminated.

    .. note:: `run_process` is intentionally similar to the standard library
       `subprocess.run`, but some of the defaults are different. Specifically, we
       default to:

       - ``check=True``, because `"errors should never pass silently / unless
         explicitly silenced" <https://www.python.org/dev/peps/pep-0020/>`__.

       - ``stdin=b""``, because it produces less-confusing results if a subprocess
         unexpectedly tries to read from stdin.

       To get the `subprocess.run` semantics, use ``check=False, stdin=None``.

    Args:
      command (list or str): The command to run. Typically this is a
          sequence of strings such as ``[\'ls\', \'-l\', \'directory with spaces\']``,
          where the first element names the executable to invoke and the other
          elements specify its arguments. With ``shell=True`` in the
          ``**options``, or on Windows, ``command`` may alternatively
          be a string, which will be parsed following platform-dependent
          :ref:`quoting rules <subprocess-quoting>`.

      stdin (:obj:`bytes`, subprocess.PIPE, file descriptor, or None): The
          bytes to provide to the subprocess on its standard input stream, or
          ``None`` if the subprocess\'s standard input should come from the
          same place as the parent Trio process\'s standard input. As is the
          case with the :mod:`subprocess` module, you can also pass a file
          descriptor or an object with a ``fileno()`` method, in which case
          the subprocess\'s standard input will come from that file.

          When starting `run_process` as a background task, you can also use
          ``stdin=subprocess.PIPE``, in which case `Process.stdin` will be a
          `~trio.abc.SendStream` that you can use to send data to the child.

      capture_stdout (bool): If true, capture the bytes that the subprocess
          writes to its standard output stream and return them in the
          `~subprocess.CompletedProcess.stdout` attribute of the returned
          `subprocess.CompletedProcess` or `subprocess.CalledProcessError`.

      capture_stderr (bool): If true, capture the bytes that the subprocess
          writes to its standard error stream and return them in the
          `~subprocess.CompletedProcess.stderr` attribute of the returned
          `~subprocess.CompletedProcess` or `subprocess.CalledProcessError`.

      check (bool): If false, don\'t validate that the subprocess exits
          successfully. You should be sure to check the
          ``returncode`` attribute of the returned object if you pass
          ``check=False``, so that errors don\'t pass silently.

      deliver_cancel (async function or None): If `run_process` is cancelled,
          then it needs to kill the child process. There are multiple ways to
          do this, so we let you customize it.

          If you pass None (the default), then the behavior depends on the
          platform:

          - On Windows, Trio calls ``TerminateProcess``, which should kill the
            process immediately.

          - On Unix-likes, the default behavior is to send a ``SIGTERM``, wait
            5 seconds, and send a ``SIGKILL``.

          Alternatively, you can customize this behavior by passing in an
          arbitrary async function, which will be called with the `Process`
          object as an argument. For example, the default Unix behavior could
          be implemented like this::

             async def my_deliver_cancel(process):
                 process.send_signal(signal.SIGTERM)
                 await trio.sleep(5)
                 process.send_signal(signal.SIGKILL)

          When the process actually exits, the ``deliver_cancel`` function
          will automatically be cancelled – so if the process exits after
          ``SIGTERM``, then we\'ll never reach the ``SIGKILL``.

          In any case, `run_process` will always wait for the child process to
          exit before raising `Cancelled`.

      **options: :func:`run_process` also accepts any :ref:`general subprocess
          options <subprocess-options>` and passes them on to the
          :class:`~trio.Process` constructor. This includes the
          ``stdout`` and ``stderr`` options, which provide additional
          redirection possibilities such as ``stderr=subprocess.STDOUT``,
          ``stdout=subprocess.DEVNULL``, or file descriptors.

    Returns:

      When called normally – a `subprocess.CompletedProcess` instance
      describing the return code and outputs.

      When called via `Nursery.start` – a `trio.Process` instance.

    Raises:
      UnicodeError: if ``stdin`` is specified as a Unicode string, rather
          than bytes
      ValueError: if multiple redirections are specified for the same
          stream, e.g., both ``capture_stdout=True`` and
          ``stdout=subprocess.DEVNULL``
      subprocess.CalledProcessError: if ``check=False`` is not passed
          and the process exits with a nonzero exit status
      OSError: if an error is encountered starting or communicating with
          the process
      ExceptionGroup: if exceptions occur in ``deliver_cancel``,
          or when exceptions occur when communicating with the subprocess.
          If strict_exception_groups is set to false in the global context,
          which is deprecated, then single exceptions will be collapsed.

    .. note:: The child process runs in the same process group as the parent
       Trio process, so a Ctrl+C will be delivered simultaneously to both
       parent and child. If you don\'t want this behavior, consult your
       platform\'s documentation for starting child processes in a different
       process group.

    '''
        pass
    # WARNING: Decompyle incomplete

    
    def GeneralProcessArgs():
        '''GeneralProcessArgs'''
        executable: 'StrOrBytesPath | None' = 'Arguments shared between all runs.'

    GeneralProcessArgs = <NODE:27>(GeneralProcessArgs, 'GeneralProcessArgs', TypedDict, total = False)
    if TYPE_CHECKING:
        if sys.platform == 'win32':
            
            def WindowsProcessArgs():
                '''WindowsProcessArgs'''
                creationflags: 'int' = 'Arguments shared between all Windows runs.'

            WindowsProcessArgs = <NODE:27>(WindowsProcessArgs, 'WindowsProcessArgs', GeneralProcessArgs, total = False)
            
            async def open_process(command = None, *, stdin, **kwargs):
                """Execute a child program in a new process.

            After construction, you can interact with the child process by writing data to its
            `~trio.Process.stdin` stream (a `~trio.abc.SendStream`), reading data from its
            `~trio.Process.stdout` and/or `~trio.Process.stderr` streams (both
            `~trio.abc.ReceiveStream`\\s), sending it signals using `~trio.Process.terminate`,
            `~trio.Process.kill`, or `~trio.Process.send_signal`, and waiting for it to exit
            using `~trio.Process.wait`. See `trio.Process` for details.

            Each standard stream is only available if you specify that a pipe should be created
            for it. For example, if you pass ``stdin=subprocess.PIPE``, you can write to the
            `~trio.Process.stdin` stream, else `~trio.Process.stdin` will be ``None``.

            Unlike `trio.run_process`, this function doesn't do any kind of automatic
            management of the child process. It's up to you to implement whatever semantics you
            want.

            Args:
              command (list or str): The command to run. Typically this is a
                  sequence of strings such as ``['ls', '-l', 'directory with spaces']``,
                  where the first element names the executable to invoke and the other
                  elements specify its arguments. With ``shell=True`` in the
                  ``**options``, or on Windows, ``command`` may alternatively
                  be a string, which will be parsed following platform-dependent
                  :ref:`quoting rules <subprocess-quoting>`.
              stdin: Specifies what the child process's standard input
                  stream should connect to: output written by the parent
                  (``subprocess.PIPE``), nothing (``subprocess.DEVNULL``),
                  or an open file (pass a file descriptor or something whose
                  ``fileno`` method returns one). If ``stdin`` is unspecified,
                  the child process will have the same standard input stream
                  as its parent.
              stdout: Like ``stdin``, but for the child process's standard output
                  stream.
              stderr: Like ``stdin``, but for the child process's standard error
                  stream. An additional value ``subprocess.STDOUT`` is supported,
                  which causes the child's standard output and standard error
                  messages to be intermixed on a single standard output stream,
                  attached to whatever the ``stdout`` option says to attach it to.
              **options: Other :ref:`general subprocess options <subprocess-options>`
                  are also accepted.

            Returns:
              A new `trio.Process` object.

            Raises:
              OSError: if the process spawning fails, for example because the
                 specified command could not be found.

            """
                pass
            # WARNING: Decompyle incomplete

            
            async def run_process(command = None, *, task_status, stdin, capture_stdout, capture_stderr, check, deliver_cancel, **kwargs):
                '''Run ``command`` in a subprocess and wait for it to complete.

            This function can be called in two different ways.

            One option is a direct call, like::

                completed_process_info = await trio.run_process(...)

            In this case, it returns a :class:`subprocess.CompletedProcess` instance
            describing the results. Use this if you want to treat a process like a
            function call.

            The other option is to run it as a task using `Nursery.start` – the enhanced version
            of `~Nursery.start_soon` that lets a task pass back a value during startup::

                process = await nursery.start(trio.run_process, ...)

            In this case, `~Nursery.start` returns a `Process` object that you can use
            to interact with the process while it\'s running. Use this if you want to
            treat a process like a background task.

            Either way, `run_process` makes sure that the process has exited before
            returning, handles cancellation, optionally checks for errors, and
            provides some convenient shorthands for dealing with the child\'s
            input/output.

            **Input:** `run_process` supports all the same ``stdin=`` arguments as
            `subprocess.Popen`. In addition, if you simply want to pass in some fixed
            data, you can pass a plain `bytes` object, and `run_process` will take
            care of setting up a pipe, feeding in the data you gave, and then sending
            end-of-file. The default is ``b""``, which means that the child will receive
            an empty stdin. If you want the child to instead read from the parent\'s
            stdin, use ``stdin=None``.

            **Output:** By default, any output produced by the subprocess is
            passed through to the standard output and error streams of the
            parent Trio process.

            When calling `run_process` directly, you can capture the subprocess\'s output by
            passing ``capture_stdout=True`` to capture the subprocess\'s standard output, and/or
            ``capture_stderr=True`` to capture its standard error. Captured data is collected up
            by Trio into an in-memory buffer, and then provided as the
            :attr:`~subprocess.CompletedProcess.stdout` and/or
            :attr:`~subprocess.CompletedProcess.stderr` attributes of the returned
            :class:`~subprocess.CompletedProcess` object. The value for any stream that was not
            captured will be ``None``.

            If you want to capture both stdout and stderr while keeping them
            separate, pass ``capture_stdout=True, capture_stderr=True``.

            If you want to capture both stdout and stderr but mixed together
            in the order they were printed, use: ``capture_stdout=True, stderr=subprocess.STDOUT``.
            This directs the child\'s stderr into its stdout, so the combined
            output will be available in the `~subprocess.CompletedProcess.stdout`
            attribute.

            If you\'re using ``await nursery.start(trio.run_process, ...)`` and want to capture
            the subprocess\'s output for further processing, then use ``stdout=subprocess.PIPE``
            and then make sure to read the data out of the `Process.stdout` stream. If you want
            to capture stderr separately, use ``stderr=subprocess.PIPE``. If you want to capture
            both, but mixed together in the correct order, use ``stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT``.

            **Error checking:** If the subprocess exits with a nonzero status
            code, indicating failure, :func:`run_process` raises a
            :exc:`subprocess.CalledProcessError` exception rather than
            returning normally. The captured outputs are still available as
            the :attr:`~subprocess.CalledProcessError.stdout` and
            :attr:`~subprocess.CalledProcessError.stderr` attributes of that
            exception.  To disable this behavior, so that :func:`run_process`
            returns normally even if the subprocess exits abnormally, pass ``check=False``.

            Note that this can make the ``capture_stdout`` and ``capture_stderr``
            arguments useful even when starting `run_process` as a task: if you only
            care about the output if the process fails, then you can enable capturing
            and then read the output off of the `~subprocess.CalledProcessError`.

            **Cancellation:** If cancelled, `run_process` sends a termination
            request to the subprocess, then waits for it to fully exit. The
            ``deliver_cancel`` argument lets you control how the process is terminated.

            .. note:: `run_process` is intentionally similar to the standard library
               `subprocess.run`, but some of the defaults are different. Specifically, we
               default to:

               - ``check=True``, because `"errors should never pass silently / unless
                 explicitly silenced" <https://www.python.org/dev/peps/pep-0020/>`__.

               - ``stdin=b""``, because it produces less-confusing results if a subprocess
                 unexpectedly tries to read from stdin.

               To get the `subprocess.run` semantics, use ``check=False, stdin=None``.

            Args:
              command (list or str): The command to run. Typically this is a
                  sequence of strings such as ``[\'ls\', \'-l\', \'directory with spaces\']``,
                  where the first element names the executable to invoke and the other
                  elements specify its arguments. With ``shell=True`` in the
                  ``**options``, or on Windows, ``command`` may alternatively
                  be a string, which will be parsed following platform-dependent
                  :ref:`quoting rules <subprocess-quoting>`.

              stdin (:obj:`bytes`, subprocess.PIPE, file descriptor, or None): The
                  bytes to provide to the subprocess on its standard input stream, or
                  ``None`` if the subprocess\'s standard input should come from the
                  same place as the parent Trio process\'s standard input. As is the
                  case with the :mod:`subprocess` module, you can also pass a file
                  descriptor or an object with a ``fileno()`` method, in which case
                  the subprocess\'s standard input will come from that file.

                  When starting `run_process` as a background task, you can also use
                  ``stdin=subprocess.PIPE``, in which case `Process.stdin` will be a
                  `~trio.abc.SendStream` that you can use to send data to the child.

              capture_stdout (bool): If true, capture the bytes that the subprocess
                  writes to its standard output stream and return them in the
                  `~subprocess.CompletedProcess.stdout` attribute of the returned
                  `subprocess.CompletedProcess` or `subprocess.CalledProcessError`.

              capture_stderr (bool): If true, capture the bytes that the subprocess
                  writes to its standard error stream and return them in the
                  `~subprocess.CompletedProcess.stderr` attribute of the returned
                  `~subprocess.CompletedProcess` or `subprocess.CalledProcessError`.

              check (bool): If false, don\'t validate that the subprocess exits
                  successfully. You should be sure to check the
                  ``returncode`` attribute of the returned object if you pass
                  ``check=False``, so that errors don\'t pass silently.

              deliver_cancel (async function or None): If `run_process` is cancelled,
                  then it needs to kill the child process. There are multiple ways to
                  do this, so we let you customize it.

                  If you pass None (the default), then the behavior depends on the
                  platform:

                  - On Windows, Trio calls ``TerminateProcess``, which should kill the
                    process immediately.

                  - On Unix-likes, the default behavior is to send a ``SIGTERM``, wait
                    5 seconds, and send a ``SIGKILL``.

                  Alternatively, you can customize this behavior by passing in an
                  arbitrary async function, which will be called with the `Process`
                  object as an argument. For example, the default Unix behavior could
                  be implemented like this::

                     async def my_deliver_cancel(process):
                         process.send_signal(signal.SIGTERM)
                         await trio.sleep(5)
                         process.send_signal(signal.SIGKILL)

                  When the process actually exits, the ``deliver_cancel`` function
                  will automatically be cancelled – so if the process exits after
                  ``SIGTERM``, then we\'ll never reach the ``SIGKILL``.

                  In any case, `run_process` will always wait for the child process to
                  exit before raising `Cancelled`.

              **options: :func:`run_process` also accepts any :ref:`general subprocess
                  options <subprocess-options>` and passes them on to the
                  :class:`~trio.Process` constructor. This includes the
                  ``stdout`` and ``stderr`` options, which provide additional
                  redirection possibilities such as ``stderr=subprocess.STDOUT``,
                  ``stdout=subprocess.DEVNULL``, or file descriptors.

            Returns:

              When called normally – a `subprocess.CompletedProcess` instance
              describing the return code and outputs.

              When called via `Nursery.start` – a `trio.Process` instance.

            Raises:
              UnicodeError: if ``stdin`` is specified as a Unicode string, rather
                  than bytes
              ValueError: if multiple redirections are specified for the same
                  stream, e.g., both ``capture_stdout=True`` and
                  ``stdout=subprocess.DEVNULL``
              subprocess.CalledProcessError: if ``check=False`` is not passed
                  and the process exits with a nonzero exit status
              OSError: if an error is encountered starting or communicating with
                  the process

            .. note:: The child process runs in the same process group as the parent
               Trio process, so a Ctrl+C will be delivered simultaneously to both
               parent and child. If you don\'t want this behavior, consult your
               platform\'s documentation for starting child processes in a different
               process group.

            '''
                pass
            # WARNING: Decompyle incomplete

            return None
        
        def UnixProcessArgs3_10():
            '''UnixProcessArgs3_10'''
            pipesize: 'int' = 'Arguments shared between all Unix runs.'

        UnixProcessArgs3_10 = <NODE:27>(UnixProcessArgs3_10, 'UnixProcessArgs3_10', GeneralProcessArgs, total = False)
        
        def UnixProcessArgs3_11():
            '''UnixProcessArgs3_11'''
            process_group: 'int | None' = 'Arguments shared between all Unix runs on 3.11+.'

        UnixProcessArgs3_11 = <NODE:27>(UnixProcessArgs3_11, 'UnixProcessArgs3_11', UnixProcessArgs3_10, total = False)
        
        def UnixRunProcessMixin():
            '''UnixRunProcessMixin'''
            deliver_cancel: 'Callable[[Process], Awaitable[None]] | None' = 'Arguments unique to run_process on Unix.'

        UnixRunProcessMixin = <NODE:27>(UnixRunProcessMixin, 'UnixRunProcessMixin', TypedDict, total = False)
        open_process = (lambda command = None, *, stdin: pass# WARNING: Decompyle incomplete
)()
        open_process = (lambda command = None, *, stdin: pass# WARNING: Decompyle incomplete
)()
        run_process = (lambda command = None, *, stdin: pass# WARNING: Decompyle incomplete
)()
        run_process = (lambda command = None, *, stdin: pass# WARNING: Decompyle incomplete
)()
        return None
    open_process = None
    open_process.__name__ = 'open_process'
    open_process.__qualname__ = 'open_process'
    run_process = _run_process
    run_process.__name__ = 'run_process'
    run_process.__qualname__ = 'run_process'
    return None
