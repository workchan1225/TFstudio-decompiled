# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _bootsubprocess.pyc (Python 3.11)

'''
Basic subprocess implementation for POSIX which only uses os functions. Only
implement features required by setup.py to build C extension modules when
subprocess is unavailable. setup.py is not used on Windows.
'''
import os

class Popen:
    
    def __init__(self, cmd, env = (None,)):
        self._cmd = cmd
        self._env = env
        self.returncode = None

    
    def wait(self):
        pid = os.fork()
    # WARNING: Decompyle incomplete



def _check_cmd(cmd):
    safe_chars = []
    for first, last in (('a', 'z'), ('A', 'Z'), ('0', '9')):
        for ch in range(ord(first), ord(last) + 1):
            safe_chars.append(chr(ch))
            safe_chars.append('./-')
            safe_chars = ''.join(safe_chars)
            if isinstance(cmd, (tuple, list)):
                check_strs = cmd
            elif isinstance(cmd, str):
                check_strs = [
                    cmd]
            else:
                return False
            for arg in None:
                if not isinstance(arg, str):
                    return False
                if not None:
                    return False
                for ch in None:
                    if ch not in safe_chars:
                        return False
                    return True


def check_output(cmd, **kwargs):
    if kwargs:
        raise NotImplementedError(repr(kwargs))
    if not _check_cmd(cmd):
        raise ValueError(f'''unsupported command: {cmd!r}''')
    tmp_filename = 'check_output.tmp'
    if not isinstance(cmd, str):
        cmd = ' '.join(cmd)
    cmd = f'''{cmd} >{tmp_filename}'''
    
    try:
        status = os.system(cmd)
        exitcode = os.waitstatus_to_exitcode(status)
        if exitcode:
            raise ValueError(f'''Command {cmd!r} returned non-zero exit status {exitcode!r}''')
        
        try:
            fp = open(tmp_filename, 'rb')
            stdout = fp.read()
            
            try:
                None(None, None)
            with None:
                if not None:
                    
                    try:
                        
                        try:
                            
                            try:
                                pass
                            except FileNotFoundError:
                                stdout = b''
                                
                                try:
                                    pass
                                try:
                                    
                                    try:
                                        os.unlink(tmp_filename)
                                    except OSError:
                                        pass

                                    return stdout
