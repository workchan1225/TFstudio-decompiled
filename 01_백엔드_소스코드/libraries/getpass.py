# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: getpass.pyc (Python 3.11)

'''Utilities to get a password and/or the current user name.

getpass(prompt[, stream]) - Prompt for a password, with echo turned off.
getuser() - Get the user name from the environment or password database.

GetPassWarning - This UserWarning is issued when getpass() cannot prevent
                 echoing of the password contents while reading.

On Windows, the msvcrt module will be used.

'''
import contextlib
import io
import os
import sys
import warnings
__all__ = [
    'getpass',
    'getuser',
    'GetPassWarning']

class GetPassWarning(UserWarning):
    pass


def unix_getpass(prompt, stream = ('Password: ', None)):
    """Prompt for a password, with echo turned off.

    Args:
      prompt: Written on stream to ask for the input.  Default: 'Password: '
      stream: A writable file object to display the prompt.  Defaults to
              the tty.  If no tty is available defaults to sys.stderr.
    Returns:
      The seKr3t input.
    Raises:
      EOFError: If our input tty or stdin was closed.
      GetPassWarning: When we were unable to turn echo off on the input.

    Always restores terminal settings before returning.
    """
    passwd = None
    stack = contextlib.ExitStack()
    fd = os.open('/dev/tty', os.O_RDWR | os.O_NOCTTY)
    tty = io.FileIO(fd, 'w+')
    stack.enter_context(tty)
    input = io.TextIOWrapper(tty)
    stack.enter_context(input)
    if not stream:
        stream = input
    else:
        except OSError:
            stack.close()
            fd = sys.stdin.fileno()
        except (AttributeError, ValueError):
            fd = None
            passwd = fallback_getpass(prompt, stream)
        input = sys.stdin
        if not stream:
            stream = sys.stderr
# WARNING: Decompyle incomplete


def win_getpass(prompt, stream = ('Password: ', None)):
    '''Prompt for password with echo off, using Windows getwch().'''
    if sys.stdin is not sys.__stdin__:
        return fallback_getpass(prompt, stream)
    for c in None:
        msvcrt.putwch(c)
        pw = ''
        c = msvcrt.getwch()
        if c == '\r' or c == '\n':
            pass
        elif c == '\x03':
            raise KeyboardInterrupt
    if c == '\x08':
        pw = pw[:-1]
    else:
        pw = pw + c
    continue
    msvcrt.putwch('\r')
    msvcrt.putwch('\n')
    return pw


def fallback_getpass(prompt, stream = ('Password: ', None)):
    warnings.warn('Can not control echo on the terminal.', GetPassWarning, stacklevel = 2)
    if not stream:
        stream = sys.stderr
    print('Warning: Password input may be echoed.', file = stream)
    return _raw_input(prompt, stream)


def _raw_input(prompt, stream, input = ('', None, None)):
    if not stream:
        stream = sys.stderr
    if not input:
        input = sys.stdin
    prompt = str(prompt)
    if prompt:
        
        try:
            stream.write(prompt)
        except UnicodeEncodeError:
            prompt = prompt.encode(stream.encoding, 'replace')
            prompt = prompt.decode(stream.encoding)
            stream.write(prompt)

        stream.flush()
    line = input.readline()
    if not line:
        raise EOFError
    if line[-1] == '\n':
        line = line[:-1]
    return line


def getuser():
    '''Get the username from the environment or password database.

    First try various environment variables, then the password
    database.  This works on Windows as long as USERNAME is set.

    '''
    for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
        user = os.environ.get(name)
        if user:
            
            return None, user
        return pwd.getpwuid(os.getuid())[0]


try:
    import termios
    (termios.tcgetattr, termios.tcsetattr)
    getpass = unix_getpass
    return None
except (ImportError, AttributeError):
    import msvcrt
    getpass = win_getpass
    return None
    except ImportError:
        getpass = fallback_getpass
        return None
