# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _osx_support.pyc (Python 3.11)

'''Shared OS X support functions.'''
import os
import re
import sys
__all__ = [
    'compiler_fixup',
    'customize_config_vars',
    'customize_compiler',
    'get_platform_osx']
_UNIVERSAL_CONFIG_VARS = ('CFLAGS', 'LDFLAGS', 'CPPFLAGS', 'BASECFLAGS', 'BLDSHARED', 'LDSHARED', 'CC', 'CXX', 'PY_CFLAGS', 'PY_LDFLAGS', 'PY_CPPFLAGS', 'PY_CORE_CFLAGS', 'PY_CORE_LDFLAGS')
_COMPILER_CONFIG_VARS = ('BLDSHARED', 'LDSHARED', 'CC', 'CXX')
_INITPRE = '_OSX_SUPPORT_INITIAL_'

def _find_executable(executable, path = (None,)):
    """Tries to find 'executable' in the directories listed in 'path'.

    A string listing directories separated by 'os.pathsep'; defaults to
    os.environ['PATH'].  Returns the complete filename or None if not found.
    """
    pass
# WARNING: Decompyle incomplete


def _read_output(commandstring, capture_stderr = (False,)):
    '''Output from successful command execution or None'''
    import contextlib
    
    try:
        import tempfile
        fp = tempfile.NamedTemporaryFile()
    except ImportError:
        fp = open(f'''/tmp/_osx_support.{os.getpid()!s}''', 'w+b')

    fp = contextlib.closing(fp)
    if capture_stderr:
        cmd = f'''{commandstring!s} >\'{fp.name!s}\' 2>&1'''
    else:
        cmd = f'''{commandstring!s} 2>/dev/null >\'{fp.name!s}\''''
    None(None, None)
    return 
    with None:
        if not None, fp.read().decode('utf-8').strip() if not os.system(cmd) else None:
            pass


def _find_build_tool(toolname):
