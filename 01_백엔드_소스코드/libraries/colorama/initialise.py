# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: initialise.pyc (Python 3.11)

import atexit
import contextlib
import sys
from ansitowin32 import AnsiToWin32

def _wipe_internal_state_for_tests():
    global orig_stdout, orig_stderr, wrapped_stdout, wrapped_stderr, atexit_done, fixed_windows_console
    orig_stdout = None
    orig_stderr = None
    wrapped_stdout = None
    wrapped_stderr = None
    atexit_done = False
    fixed_windows_console = False
    
    try:
        atexit.unregister(reset_all)
        return None
    except AttributeError:
        return None



def reset_all():
    pass
# WARNING: Decompyle incomplete


def init(autoreset, convert, strip, wrap = (False, None, None, True)):
    global orig_stdout, orig_stderr
    if wrap and any([
        autoreset,
        convert,
        strip]):
        raise ValueError('wrap=False conflicts with any other arg=True')
    orig_stdout = sys.stdout
    orig_stderr = sys.stderr
# WARNING: Decompyle incomplete


def deinit():
    pass
# WARNING: Decompyle incomplete


def just_fix_windows_console():
    if sys.platform != 'win32':
        return None
    if None:
        return None
# WARNING: Decompyle incomplete

colorama_text = (lambda : pass# WARNING: Decompyle incomplete
)()

def reinit():
    pass
# WARNING: Decompyle incomplete


def wrap_stream(stream, convert, strip, autoreset, wrap):
    if wrap:
        wrapper = AnsiToWin32(stream, convert = convert, strip = strip, autoreset = autoreset)
        if wrapper.should_wrap():
            stream = wrapper.stream
    return stream

_wipe_internal_state_for_tests()
