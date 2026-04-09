# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: win32_clipboard.pyc (Python 3.11)

import ctypes
from ctypes.wintypes import wintypes
from ctypes import addressof, c_buffer, c_char_p, c_int, c_size_t, c_void_p, c_wchar_p, cast, create_unicode_buffer, sizeof, windll, wstring_at
from typing import Union
from pyreadline3.keysyms.winconstants import CF_UNICODETEXT, GHND
from pyreadline3.unicode_helper import ensure_unicode
OpenClipboard = windll.user32.OpenClipboard
OpenClipboard.argtypes = [
    wintypes.HWND]
OpenClipboard.restype = wintypes.BOOL
EmptyClipboard = windll.user32.EmptyClipboard
GetClipboardData = windll.user32.GetClipboardData
GetClipboardData.argtypes = [
    wintypes.UINT]
GetClipboardData.restype = wintypes.HANDLE
GetClipboardFormatName = windll.user32.GetClipboardFormatNameA
GetClipboardFormatName.argtypes = [
    wintypes.UINT,
    c_char_p,
    c_int]
SetClipboardData = windll.user32.SetClipboardData
SetClipboardData.argtypes = [
    wintypes.UINT,
    wintypes.HANDLE]
SetClipboardData.restype = wintypes.HANDLE
EnumClipboardFormats = windll.user32.EnumClipboardFormats
EnumClipboardFormats.argtypes = [
    c_int]
CloseClipboard = windll.user32.CloseClipboard
CloseClipboard.argtypes = []
GlobalAlloc = windll.kernel32.GlobalAlloc
GlobalAlloc.argtypes = [
    wintypes.UINT,
    c_size_t]
GlobalAlloc.restype = wintypes.HGLOBAL
GlobalLock = windll.kernel32.GlobalLock
GlobalLock.argtypes = [
    wintypes.HGLOBAL]
GlobalLock.restype = c_void_p
GlobalUnlock = windll.kernel32.GlobalUnlock
GlobalUnlock.argtypes = [
    c_int]
_strncpy = ctypes.windll.kernel32.lstrcpynW
_strncpy.restype = c_wchar_p
_strncpy.argtypes = [
    c_wchar_p,
    c_wchar_p,
    c_size_t]

def _enum():
    OpenClipboard(0)
    q = EnumClipboardFormats(0)
# WARNING: Decompyle incomplete


def _get_format_name(format_str = None):
    buffer = c_buffer(100)
    bufferSize = sizeof(buffer)
    OpenClipboard(0)
    GetClipboardFormatName(format_str, buffer, bufferSize)
    CloseClipboard()
    return buffer.value


def get_clipboard_text():
    text = ''
    if OpenClipboard(0):
        h_clip_mem = GetClipboardData(CF_UNICODETEXT)
        if h_clip_mem:
            text = wstring_at(GlobalLock(h_clip_mem))
            GlobalUnlock(h_clip_mem)
        CloseClipboard()
    return text


def set_clipboard_text(text = None):
    buffer = create_unicode_buffer(ensure_unicode(text))
    buffer_size = sizeof(buffer)
    h_global_mem = GlobalAlloc(GHND, c_size_t(buffer_size))
    GlobalLock.restype = c_void_p
    lp_global_mem = GlobalLock(h_global_mem)
    _strncpy(cast(lp_global_mem, c_wchar_p), cast(addressof(buffer), c_wchar_p), c_size_t(buffer_size))
    GlobalUnlock(c_int(h_global_mem))
    if OpenClipboard(0):
        EmptyClipboard()
        SetClipboardData(CF_UNICODETEXT, h_global_mem)
        CloseClipboard()
        return None

if __name__ == '__main__':
    txt = get_clipboard_text()
    print(txt)
    return None
