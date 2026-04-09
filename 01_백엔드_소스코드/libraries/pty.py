# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pty.pyc (Python 3.11)

'''Pseudo terminal utilities.'''
from select import select
import os
import sys
import tty
from os import close, waitpid
from tty import setraw, tcgetattr, tcsetattr
__all__ = [
    'openpty',
    'fork',
    'spawn']
STDIN_FILENO = 0
STDOUT_FILENO = 1
STDERR_FILENO = 2
CHILD = 0

def openpty():
    '''openpty() -> (master_fd, slave_fd)
    Open a pty master/slave pair, using os.openpty() if possible.'''
    
    try:
        return os.openpty()
    except (AttributeError, OSError):
        pass

    (master_fd, slave_name) = _open_terminal()
    slave_fd = slave_open(slave_name)
    return (master_fd, slave_fd)


def master_open():
    '''master_open() -> (master_fd, slave_name)
    Open a pty master and return the fd, and the filename of the slave end.
    Deprecated, use openpty() instead.'''
    
    try:
        (master_fd, slave_fd) = os.openpty()
        slave_name = os.ttyname(slave_fd)
        os.close(slave_fd)
        return (master_fd, slave_name)
    except (AttributeError, OSError):
        pass

    return _open_terminal()


def _open_terminal():
    '''Open pty master and return (master_fd, tty_name).'''
    for x in 'pqrstuvwxyzPQRST':
        for y in '0123456789abcdef':
            pty_name = '/dev/pty' + x + y
            fd = os.open(pty_name, os.O_RDWR)
        except OSError:
            continue
        
        
        return None, None, (fd, '/dev/tty' + x + y)
        raise OSError('out of pty devices')


def slave_open(tty_name):
    '''slave_open(tty_name) -> slave_fd
    Open the pty slave and acquire the controlling terminal, returning
    opened filedescriptor.
    Deprecated, use openpty() instead.'''
    result = os.open(tty_name, os.O_RDWR)
    
    try:
        ioctl = ioctl
        I_PUSH = I_PUSH
        import fcntl
    except ImportError:
        return 

    
    try:
        ioctl(result, I_PUSH, 'ptem')
        ioctl(result, I_PUSH, 'ldterm')
    except OSError:
        pass

    return result


def fork():
    '''fork() -> (pid, master_fd)
    Fork and make the child a session leader with a controlling terminal.'''
    
    try:
        (pid, fd) = os.forkpty()
        if pid == CHILD:
            
            try:
                os.setsid()
            except OSError:
                pass

            return (pid, fd)
        except (AttributeError, OSError):
            pass
        (master_fd, slave_fd) = openpty()
        pid = os.fork()
        if pid == CHILD:
            os.setsid()
            os.close(master_fd)
            os.dup2(slave_fd, STDIN_FILENO)
            os.dup2(slave_fd, STDOUT_FILENO)
            os.dup2(slave_fd, STDERR_FILENO)
            if slave_fd > STDERR_FILENO:
                os.close(slave_fd)
            tmp_fd = os.open(os.ttyname(STDOUT_FILENO), os.O_RDWR)
            os.close(tmp_fd)
        else:
            os.close(slave_fd)

    return (pid, master_fd)


def _read(fd):
    '''Default read function.'''
    return os.read(fd, 1024)


def _copy(master_fd, master_read, stdin_read = (_read, _read)):
    '''Parent copy loop.
    Copies
            pty master -> standard output   (master_read)
            standard input -> pty master    (stdin_read)'''
    if os.get_blocking(master_fd):
        os.set_blocking(master_fd, False)
        
        try:
            _copy(master_fd, master_read = master_read, stdin_read = stdin_read)
            os.set_blocking(master_fd, True)
        except:
            os.set_blocking(master_fd, True)

        return None
    high_waterlevel = 4096
    stdin_avail = master_fd != STDIN_FILENO
    stdout_avail = master_fd != STDOUT_FILENO
    i_buf = b''
    o_buf = b''
    rfds = []
    wfds = []
    if stdin_avail and len(i_buf) < high_waterlevel:
        rfds.append(STDIN_FILENO)
    if stdout_avail and len(o_buf) < high_waterlevel:
        rfds.append(master_fd)
    if stdout_avail and len(o_buf) > 0:
        wfds.append(STDOUT_FILENO)
    if len(i_buf) > 0:
        wfds.append(master_fd)
    (rfds, wfds, _xfds) = select(rfds, wfds, [])
    if STDOUT_FILENO in wfds:
        
        try:
            n = os.write(STDOUT_FILENO, o_buf)
            o_buf = o_buf[n:]
        except OSError:
            stdout_avail = False

        if master_fd in rfds:
            
            try:
                data = master_read(master_fd)
            except OSError:
                data = b''

            if not data:
                return None
            None += data
    if master_fd in wfds:
        n = os.write(master_fd, i_buf)
        i_buf = i_buf[n:]
    if stdin_avail and STDIN_FILENO in rfds:
        data = stdin_read(STDIN_FILENO)
        if not data:
            stdin_avail = False
        else:
            i_buf += data
    continue


def spawn(argv, master_read, stdin_read = (_read, _read)):
    '''Create a spawned process.'''
    if type(argv) == type(''):
        argv = (argv,)
    sys.audit('pty.spawn', argv)
    (pid, master_fd) = fork()
# WARNING: Decompyle incomplete
