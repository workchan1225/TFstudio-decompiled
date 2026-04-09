# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _subprocesses.pyc (Python 3.11)

from __future__ import annotations
import sys
from collections.abc import AsyncIterable, Iterable, Mapping, Sequence
from io import BytesIO
from os import PathLike
from subprocess import PIPE, CalledProcessError, CompletedProcess
from typing import IO, Any, Union, cast
from abc import Process
from _eventloop import get_async_backend
from _tasks import create_task_group
if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias
StrOrBytesPath: 'TypeAlias' = Union[(str, bytes, 'PathLike[str]', 'PathLike[bytes]')]

async def run_process(command = None, *, input, stdin, stdout, stderr, check, cwd, env, startupinfo, creationflags, start_new_session, pass_fds, user, group, extra_groups, umask):
    '''
    Run an external command in a subprocess and wait until it completes.

    .. seealso:: :func:`subprocess.run`

    :param command: either a string to pass to the shell, or an iterable of strings
        containing the executable name or path and its arguments
    :param input: bytes passed to the standard input of the subprocess
    :param stdin: one of :data:`subprocess.PIPE`, :data:`subprocess.DEVNULL`,
        a file-like object, or `None`; ``input`` overrides this
    :param stdout: one of :data:`subprocess.PIPE`, :data:`subprocess.DEVNULL`,
        a file-like object, or `None`
    :param stderr: one of :data:`subprocess.PIPE`, :data:`subprocess.DEVNULL`,
        :data:`subprocess.STDOUT`, a file-like object, or `None`
    :param check: if ``True``, raise :exc:`~subprocess.CalledProcessError` if the
        process terminates with a return code other than 0
    :param cwd: If not ``None``, change the working directory to this before running the
        command
    :param env: if not ``None``, this mapping replaces the inherited environment
        variables from the parent process
    :param startupinfo: an instance of :class:`subprocess.STARTUPINFO` that can be used
        to specify process startup parameters (Windows only)
    :param creationflags: flags that can be used to control the creation of the
        subprocess (see :class:`subprocess.Popen` for the specifics)
    :param start_new_session: if ``true`` the setsid() system call will be made in the
        child process prior to the execution of the subprocess. (POSIX only)
    :param pass_fds: sequence of file descriptors to keep open between the parent and
        child processes. (POSIX only)
    :param user: effective user to run the process as (Python >= 3.9, POSIX only)
    :param group: effective group to run the process as (Python >= 3.9, POSIX only)
    :param extra_groups: supplementary groups to set in the subprocess (Python >= 3.9,
        POSIX only)
    :param umask: if not negative, this umask is applied in the child process before
        running the given command (Python >= 3.9, POSIX only)
    :return: an object representing the completed process
    :raises ~subprocess.CalledProcessError: if ``check`` is ``True`` and the process
        exits with a nonzero return code

    '''
    pass
# WARNING: Decompyle incomplete


async def open_process(command = None, *, stdin, stdout, stderr, cwd, env, startupinfo, creationflags, start_new_session, pass_fds, user, group, extra_groups, umask):
    '''
    Start an external command in a subprocess.

    .. seealso:: :class:`subprocess.Popen`

    :param command: either a string to pass to the shell, or an iterable of strings
        containing the executable name or path and its arguments
    :param stdin: one of :data:`subprocess.PIPE`, :data:`subprocess.DEVNULL`, a
        file-like object, or ``None``
    :param stdout: one of :data:`subprocess.PIPE`, :data:`subprocess.DEVNULL`,
        a file-like object, or ``None``
    :param stderr: one of :data:`subprocess.PIPE`, :data:`subprocess.DEVNULL`,
        :data:`subprocess.STDOUT`, a file-like object, or ``None``
    :param cwd: If not ``None``, the working directory is changed before executing
    :param env: If env is not ``None``, it must be a mapping that defines the
        environment variables for the new process
    :param creationflags: flags that can be used to control the creation of the
        subprocess (see :class:`subprocess.Popen` for the specifics)
    :param startupinfo: an instance of :class:`subprocess.STARTUPINFO` that can be used
        to specify process startup parameters (Windows only)
    :param start_new_session: if ``true`` the setsid() system call will be made in the
        child process prior to the execution of the subprocess. (POSIX only)
    :param pass_fds: sequence of file descriptors to keep open between the parent and
        child processes. (POSIX only)
    :param user: effective user to run the process as (POSIX only)
    :param group: effective group to run the process as (POSIX only)
    :param extra_groups: supplementary groups to set in the subprocess (POSIX only)
    :param umask: if not negative, this umask is applied in the child process before
        running the given command (POSIX only)
    :return: an asynchronous process object

    '''
    pass
# WARNING: Decompyle incomplete
