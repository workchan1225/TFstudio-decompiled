# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cli.pyc (Python 3.11)

'''
Module version for monitoring CLI pipes (`... | python -m tqdm | ...`).
'''
import logging
import re
import sys
from ast import literal_eval as numeric
from textwrap import indent
from std import TqdmKeyError, TqdmTypeError, tqdm
from version import __version__
__all__ = [
    'main']
log = logging.getLogger(__name__)

def cast(val, typ):
    log.debug((val, typ))
    if ' or ' in typ:
        for t in typ.split(' or '):
            
            return None, cast(val, t)
            except TqdmTypeError:
                continue
            raise TqdmTypeError(f'''{val} : {typ}''')
            if typ == 'bool':
                if val == 'True' or val == '':
                    return True
                if None == 'False':
                    return False
                raise None(val + ' : ' + typ)
            if typ == 'chr':
                if len(val) == 1:
                    return val.encode()
                if None.match('^\\\\\\w+$', val):
                    return eval(f'''"{val}"''').encode()
                raise None(f'''{val} : {typ}''')
            if typ == 'str':
                return val
            if None == 'int':
                
                try:
                    return int(val)
                except ValueError:
                    raise TqdmTypeError(f'''{val} : {typ}'''), exc
                    None = None
                    del exc
                    if typ == 'float':
                        
                        try:
                            return float(val)
                        except ValueError:
                            exc = None
                            raise TqdmTypeError(f'''{val} : {typ}'''), exc
                            exc = None
                            del exc
                            raise TqdmTypeError(f'''{val} : {typ}''')




def posix_pipe(fin, fout, delim, buf_size, callback, callback_len = (b'\\n', 256, (lambda float: pass), True)):
    '''
    Params
    ------
    fin  : binary file with `read(buf_size : int)` method
    fout  : binary file with `write` (and optionally `flush`) methods.
    callback  : function(float), e.g.: `tqdm.update`
    callback_len  : If (default: True) do `callback(len(buffer))`.
      Otherwise, do `callback(data) for data in buffer.split(delim)`.
    '''
    fp_write = fout.write
    if not delim:
        tmp = fin.read(buf_size)
        if not tmp:
            getattr(fout, 'flush', (lambda : pass))()
            return None
        fp_write(tmp)
        callback(len(tmp))
        continue
    buf = b''
    len_delim = len(delim)
    tmp = fin.read(buf_size)
    if not tmp:
        if buf:
            fp_write(buf)
            if callback_len:
                callback(1 + buf.count(delim))
            else:
                for i in buf.split(delim):
                    callback(i)
                    getattr(fout, 'flush', (lambda : pass))()
                    return None
                    i = tmp.find(delim)
                    if i < 0:
                        buf += tmp
                    else:
                        fp_write(buf + tmp[:i + len(delim)])
                        callback(1 if callback_len else buf + tmp[:i])
                        buf = b''
                        tmp = tmp[i + len_delim:]

RE_OPTS = re.compile('\\n {4}(\\S+)\\s{2,}:\\s*([^,]+)')
RE_SHLEX = re.compile('\\s*(?<!\\S)--?([^\\s=]+)(\\s+|=|$)')
UNSUPPORTED_OPTS = ('iterable', 'gui', 'out', 'file')
CLI_EXTRA_DOC = "\n    Extra CLI Options\n    -----------------\n    name  : type, optional\n        TODO: find out why this is needed.\n    delim  : chr, optional\n        Delimiting character [default: '\\n']. Use '\\0' for null.\n        N.B.: on Windows systems, Python converts '\\n' to '\\r\\n'.\n    buf_size  : int, optional\n        String buffer size in bytes [default: 256]\n        used when `delim` is specified.\n    bytes  : bool, optional\n        If true, will count bytes, ignore `delim`, and default\n        `unit_scale` to True, `unit_divisor` to 1024, and `unit` to 'B'.\n    tee  : bool, optional\n        If true, passes `stdin` to both `stderr` and `stdout`.\n    update  : bool, optional\n        If true, will treat input as newly elapsed iterations,\n        i.e. numbers to pass to `update()`. Note that this is slow\n        (~2e5 it/s) since every input must be decoded as a number.\n    update_to  : bool, optional\n        If true, will treat input as total elapsed iterations,\n        i.e. numbers to assign to `self.n`. Note that this is slow\n        (~2e5 it/s) since every input must be decoded as a number.\n    null  : bool, optional\n        If true, will discard input (no stdout).\n    manpath  : str, optional\n        Directory in which to install tqdm man pages.\n    comppath  : str, optional\n        Directory in which to place tqdm completion.\n    log  : str, optional\n        CRITICAL|FATAL|ERROR|WARN(ING)|[default: 'INFO']|DEBUG|NOTSET.\n"

def main(fp, argv = (sys.stderr, None)):
    '''
    Parameters (internal use only)
    ---------
    fp  : file-like object for tqdm
    argv  : list (default: sys.argv[1:])
    '''
    pass
# WARNING: Decompyle incomplete
