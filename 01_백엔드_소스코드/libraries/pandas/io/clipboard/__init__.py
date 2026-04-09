# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
Pyperclip

A cross-platform clipboard module for Python,
with copy & paste functions for plain text.
By Al Sweigart al@inventwithpython.com
Licence at LICENSES/PYPERCLIP_LICENSE

Usage:
  import pyperclip
  pyperclip.copy(\'The text to be copied to the clipboard.\')
  spam = pyperclip.paste()

  if not pyperclip.is_available():
    print("Copy functionality unavailable!")

On Windows, no additional modules are needed.
On Mac, the pyobjc module is used, falling back to the pbcopy and pbpaste cli
    commands. (These commands should come with OS X.).
On Linux, install xclip, xsel, or wl-clipboard (for "wayland" sessions) via
package manager.
For example, in Debian:
    sudo apt-get install xclip
    sudo apt-get install xsel
    sudo apt-get install wl-clipboard

Otherwise on Linux, you will need the PyQt5 modules installed.

This module does not work with PyGObject yet.

Cygwin is currently not supported.

Security Note: This module runs programs with these names:
    - pbcopy
    - pbpaste
    - xclip
    - xsel
    - wl-copy/wl-paste
    - klipper
    - qdbus
A malicious user could rename or add programs with these names, tricking
Pyperclip into running them with whatever permissions the Python process has.

'''
__version__ = '1.8.2'
import contextlib
import ctypes
from ctypes import c_size_t, c_wchar, c_wchar_p, get_errno, sizeof
import os
import platform
from shutil import which as _executable_exists
import subprocess
import time
import warnings
from pandas.errors import PyperclipException, PyperclipWindowsException
from pandas.util._exceptions import find_stack_level
HAS_DISPLAY = os.getenv('DISPLAY')
EXCEPT_MSG = '\n    Pyperclip could not find a copy/paste mechanism for your system.\n    For more information, please visit\n    https://pyperclip.readthedocs.io/en/latest/index.html#not-implemented-error\n    '
ENCODING = 'utf-8'

class PyperclipTimeoutException(PyperclipException):
    pass


def _stringifyText(text = None):
    acceptedTypes = (str, int, float, bool)
    if not isinstance(text, acceptedTypes):
        raise PyperclipException(f'''only str, int, float, and bool values can be copied to the clipboard, not {type(text).__name__}''')
    return str(text)


def init_osx_pbcopy_clipboard():
    
    def copy_osx_pbcopy(text):
        text = _stringifyText(text)
        p = subprocess.Popen([
            'pbcopy',
            'w'], stdin = subprocess.PIPE, close_fds = True)
        p.communicate(input = text.encode(ENCODING))
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def paste_osx_pbcopy():
        p = subprocess.Popen([
            'pbpaste',
            'r'], stdout = subprocess.PIPE, close_fds = True)
        stdout = p.communicate()[0]
        None(None, None)

    return (copy_osx_pbcopy, paste_osx_pbcopy)


def init_osx_pyobjc_clipboard():
    
    def copy_osx_pyobjc(text):
        '''Copy string argument to clipboard'''
        text = _stringifyText(text)
        newStr = Foundation.NSString.stringWithString_(text).nsstring()
        newData = newStr.dataUsingEncoding_(Foundation.NSUTF8StringEncoding)
        board = AppKit.NSPasteboard.generalPasteboard()
        board.declareTypes_owner_([
            AppKit.NSStringPboardType], None)
        board.setData_forType_(newData, AppKit.NSStringPboardType)

    
    def paste_osx_pyobjc():
        '''Returns contents of clipboard'''
        board = AppKit.NSPasteboard.generalPasteboard()
        content = board.stringForType_(AppKit.NSStringPboardType)
        return content

    return (copy_osx_pyobjc, paste_osx_pyobjc)


def init_qt_clipboard():
    pass
# WARNING: Decompyle incomplete


def init_xclip_clipboard():
    pass
# WARNING: Decompyle incomplete


def init_xsel_clipboard():
    pass
# WARNING: Decompyle incomplete


def init_wl_clipboard():
    pass
# WARNING: Decompyle incomplete


def init_klipper_clipboard():
    
    def copy_klipper(text):
        text = _stringifyText(text)
        p = subprocess.Popen([
            'qdbus',
            'org.kde.klipper',
            '/klipper',
            'setClipboardContents',
            text.encode(ENCODING)], stdin = subprocess.PIPE, close_fds = True)
        p.communicate(input = None)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def paste_klipper():
        p = subprocess.Popen([
            'qdbus',
            'org.kde.klipper',
            '/klipper',
            'getClipboardContents'], stdout = subprocess.PIPE, close_fds = True)
        stdout = p.communicate()[0]
        None(None, None)
    # WARNING: Decompyle incomplete

    return (copy_klipper, paste_klipper)


def init_dev_clipboard_clipboard():
    
    def copy_dev_clipboard(text):
        text = _stringifyText(text)
        if text == '':
            warnings.warn('Pyperclip cannot copy a blank string to the clipboard on Cygwin. This is effectively a no-op.', stacklevel = find_stack_level())
        if '\r' in text:
            warnings.warn('Pyperclip cannot handle \\r characters on Cygwin.', stacklevel = find_stack_level())
        fd = open('/dev/clipboard', 'w', encoding = 'utf-8')
        fd.write(text)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def paste_dev_clipboard():
        fd = open('/dev/clipboard', encoding = 'utf-8')
        content = fd.read()
        None(None, None)

    return (copy_dev_clipboard, paste_dev_clipboard)


def init_no_clipboard():
    
    class ClipboardUnavailable:
        
        def __call__(self, *args, **kwargs):
            raise PyperclipException(EXCEPT_MSG)

        
        def __bool__(self = None):
            return False


    return (ClipboardUnavailable(), ClipboardUnavailable())


class CheckedCall:
    pass
# WARNING: Decompyle incomplete


def init_windows_clipboard():
    pass
# WARNING: Decompyle incomplete


def init_wsl_clipboard():
    
    def copy_wsl(text):
        text = _stringifyText(text)
        p = subprocess.Popen([
            'clip.exe'], stdin = subprocess.PIPE, close_fds = True)
        p.communicate(input = text.encode(ENCODING))
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def paste_wsl():
        p = subprocess.Popen([
            'powershell.exe',
            '-command',
            'Get-Clipboard'], stdout = subprocess.PIPE, stderr = subprocess.PIPE, close_fds = True)
        stdout = p.communicate()[0]
        None(None, None)

    return (copy_wsl, paste_wsl)


def determine_clipboard():
