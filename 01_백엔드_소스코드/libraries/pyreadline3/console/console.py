# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: console.pyc (Python 3.11)

from event import Event
import os
import re
import sys
import traceback
from pyreadline3.unicode_helper import unicode_helper
from pyreadline3.console.ansi import AnsiState, AnsiWriter
from pyreadline3.keysyms import KeyPress, make_KeyPress
from pyreadline3.logger import log
from pyreadline3.unicode_helper import ensure_str, ensure_unicode

try:
    import ctypes.util as ctypes
    from ctypes import *
    from ctypes.wintypes import *
    from _ctypes import call_function
except ImportError:
    raise ImportError('You need ctypes to run this code')


def nolog(string):
    pass

log = nolog
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
ENABLE_WINDOW_INPUT = 8
ENABLE_MOUSE_INPUT = 16
ENABLE_PROCESSED_INPUT = 1
WHITE = 7
BLACK = 0
MENU_EVENT = 8
KEY_EVENT = 1
MOUSE_MOVED = 1
MOUSE_EVENT = 2
WINDOW_BUFFER_SIZE_EVENT = 4
FOCUS_EVENT = 16
MENU_EVENT = 8
VK_SHIFT = 16
VK_CONTROL = 17
VK_MENU = 18
GENERIC_READ = int(0x80000000)
GENERIC_WRITE = 1073741824

class COORD(Structure):
    _fields_ = [
        ('X', c_short),
        ('Y', c_short)]


class SMALL_RECT(Structure):
    _fields_ = [
        ('Left', c_short),
        ('Top', c_short),
        ('Right', c_short),
        ('Bottom', c_short)]


class CONSOLE_SCREEN_BUFFER_INFO(Structure):
    _fields_ = [
        ('dwSize', COORD),
        ('dwCursorPosition', COORD),
        ('wAttributes', c_short),
        ('srWindow', SMALL_RECT),
        ('dwMaximumWindowSize', COORD)]


class CHAR_UNION(Union):
    _fields_ = [
        ('UnicodeChar', c_wchar),
        ('AsciiChar', c_char)]


class CHAR_INFO(Structure):
    _fields_ = [
        ('Char', CHAR_UNION),
        ('Attributes', c_short)]


class KEY_EVENT_RECORD(Structure):
    _fields_ = [
        ('bKeyDown', c_byte),
        ('pad2', c_byte),
        ('pad1', c_short),
        ('wRepeatCount', c_short),
        ('wVirtualKeyCode', c_short),
        ('wVirtualScanCode', c_short),
        ('uChar', CHAR_UNION),
        ('dwControlKeyState', c_int)]


class MOUSE_EVENT_RECORD(Structure):
    _fields_ = [
        ('dwMousePosition', COORD),
        ('dwButtonState', c_int),
        ('dwControlKeyState', c_int),
        ('dwEventFlags', c_int)]


class WINDOW_BUFFER_SIZE_RECORD(Structure):
    _fields_ = [
        ('dwSize', COORD)]


class MENU_EVENT_RECORD(Structure):
    _fields_ = [
        ('dwCommandId', c_uint)]


class FOCUS_EVENT_RECORD(Structure):
    _fields_ = [
        ('bSetFocus', c_byte)]


class INPUT_UNION(Union):
    _fields_ = [
        ('KeyEvent', KEY_EVENT_RECORD),
        ('MouseEvent', MOUSE_EVENT_RECORD),
        ('WindowBufferSizeEvent', WINDOW_BUFFER_SIZE_RECORD),
        ('MenuEvent', MENU_EVENT_RECORD),
        ('FocusEvent', FOCUS_EVENT_RECORD)]


class INPUT_RECORD(Structure):
    _fields_ = [
        ('EventType', c_short),
        ('Event', INPUT_UNION)]


class CONSOLE_CURSOR_INFO(Structure):
    _fields_ = [
        ('dwSize', c_int),
        ('bVisible', c_byte)]

funcs = [
    'AllocConsole',
    'CreateConsoleScreenBuffer',
    'FillConsoleOutputAttribute',
    'FillConsoleOutputCharacterW',
    'FreeConsole',
    'GetConsoleCursorInfo',
    'GetConsoleMode',
    'GetConsoleScreenBufferInfo',
    'GetConsoleTitleW',
    'GetProcAddress',
    'GetStdHandle',
    'PeekConsoleInputW',
    'ReadConsoleInputW',
    'ScrollConsoleScreenBufferW',
    'SetConsoleActiveScreenBuffer',
    'SetConsoleCursorInfo',
    'SetConsoleCursorPosition',
    'SetConsoleMode',
    'SetConsoleScreenBufferSize',
    'SetConsoleTextAttribute',
    'SetConsoleTitleW',
    'SetConsoleWindowInfo',
    'WriteConsoleW',
    'WriteConsoleOutputCharacterW',
    'WriteFile']
key_modifiers = {
    91: 1,
    VK_MENU: 1,
    VK_CONTROL: 1,
    VK_SHIFT: 1 }

def split_block(text, size = (1000,)):
    pass
# WARNING: Decompyle incomplete


class Console(object):
    __module__ = __name__
    __qualname__ = 'Console'
    __doc__ = 'Console driver for Windows.'
    
    def __init__(self, newbuffer = (0,)):
        '''Initialize the Console object.

        newbuffer=1 will allocate a new buffer so the old content will be restored
        on exit.
        '''
        if newbuffer:
            self.hout = self.CreateConsoleScreenBuffer(GENERIC_READ | GENERIC_WRITE, 0, None, 1, None)
            self.SetConsoleActiveScreenBuffer(self.hout)
        else:
            self.hout = self.GetStdHandle(STD_OUTPUT_HANDLE)
        self.hin = self.GetStdHandle(STD_INPUT_HANDLE)
        self.inmode = DWORD(0)
        self.GetConsoleMode(self.hin, byref(self.inmode))
        self.SetConsoleMode(self.hin, 15)
        info = CONSOLE_SCREEN_BUFFER_INFO()
        self.GetConsoleScreenBufferInfo(self.hout, byref(info))
        self.attr = info.wAttributes
        self.saveattr = info.wAttributes
        self.defaultstate = AnsiState()
        self.defaultstate.winattr = info.wAttributes
        self.ansiwriter = AnsiWriter(self.defaultstate)
        background = self.attr & 240
    # WARNING: Decompyle incomplete

    
    def __del__(self):
        '''Cleanup the console when finished.'''
        self.SetConsoleTextAttribute(self.hout, self.saveattr)
        self.SetConsoleMode(self.hin, self.inmode)
        self.FreeConsole()

    
    def _get_top_bot(self):
        info = CONSOLE_SCREEN_BUFFER_INFO()
        self.GetConsoleScreenBufferInfo(self.hout, byref(info))
        rect = info.srWindow
        top = rect.Top
        bot = rect.Bottom
        return (top, bot)

    
    def fixcoord(self, x, y):
        '''Return a long with x and y packed inside,
        also handle negative x and y.'''
        if x < 0 or y < 0:
            info = CONSOLE_SCREEN_BUFFER_INFO()
            self.GetConsoleScreenBufferInfo(self.hout, byref(info))
            if x < 0:
                x = info.srWindow.Right - x
                y = info.srWindow.Bottom + y
        return c_int(y << 16 | x)

    
    def pos(self, x, y = (None, None)):
        '''Move or query the window cursor.'''
        pass
    # WARNING: Decompyle incomplete

    
    def home(self):
        '''Move to home.'''
        self.pos(0, 0)

    terminal_escape = re.compile('(\x01?\x1b\\[[0-9;]+m\x02?)')
    escape_parts = re.compile('\x01?\x1b\\[([0-9;]+)m\x02?')
# WARNING: Decompyle incomplete

for func in funcs:
    setattr(Console, func, getattr(windll.kernel32, func))
    _strncpy = ctypes.windll.kernel32.lstrcpynA
    _strncpy.restype = c_char_p
    _strncpy.argtypes = [
        c_char_p,
        c_char_p,
        c_size_t]
    LPVOID = c_void_p
    LPCVOID = c_void_p
    FARPROC = c_void_p
    LPDWORD = POINTER(DWORD)
    Console.AllocConsole.restype = BOOL
    Console.AllocConsole.argtypes = []
    Console.CreateConsoleScreenBuffer.restype = HANDLE
    Console.CreateConsoleScreenBuffer.argtypes = [
        DWORD,
        DWORD,
        c_void_p,
        DWORD,
        LPVOID]
    Console.FillConsoleOutputAttribute.restype = BOOL
    Console.FillConsoleOutputAttribute.argtypes = [
        HANDLE,
        WORD,
        DWORD,
        c_int,
        LPDWORD]
    Console.FillConsoleOutputCharacterW.restype = BOOL
    Console.FillConsoleOutputCharacterW.argtypes = [
        HANDLE,
        c_ushort,
        DWORD,
        c_int,
        LPDWORD]
    Console.FreeConsole.restype = BOOL
    Console.FreeConsole.argtypes = []
    Console.GetConsoleCursorInfo.restype = BOOL
    Console.GetConsoleCursorInfo.argtypes = [
        HANDLE,
        c_void_p]
    Console.GetConsoleMode.restype = BOOL
    Console.GetConsoleMode.argtypes = [
        HANDLE,
        LPDWORD]
    Console.GetConsoleScreenBufferInfo.restype = BOOL
    Console.GetConsoleScreenBufferInfo.argtypes = [
        HANDLE,
        c_void_p]
    Console.GetConsoleTitleW.restype = DWORD
    Console.GetConsoleTitleW.argtypes = [
        c_wchar_p,
        DWORD]
    Console.GetProcAddress.restype = FARPROC
    Console.GetProcAddress.argtypes = [
        HMODULE,
        c_char_p]
    Console.GetStdHandle.restype = HANDLE
    Console.GetStdHandle.argtypes = [
        DWORD]
    Console.PeekConsoleInputW.restype = BOOL
    Console.PeekConsoleInputW.argtypes = [
        HANDLE,
        c_void_p,
        DWORD,
        LPDWORD]
    Console.ReadConsoleInputW.restype = BOOL
    Console.ReadConsoleInputW.argtypes = [
        HANDLE,
        c_void_p,
        DWORD,
        LPDWORD]
    Console.ScrollConsoleScreenBufferW.restype = BOOL
    Console.ScrollConsoleScreenBufferW.argtypes = [
        HANDLE,
        c_void_p,
        c_void_p,
        c_int,
        c_void_p]
    Console.SetConsoleActiveScreenBuffer.restype = BOOL
    Console.SetConsoleActiveScreenBuffer.argtypes = [
        HANDLE]
    Console.SetConsoleCursorInfo.restype = BOOL
    Console.SetConsoleCursorInfo.argtypes = [
        HANDLE,
        c_void_p]
    Console.SetConsoleCursorPosition.restype = BOOL
    Console.SetConsoleCursorPosition.argtypes = [
        HANDLE,
        c_int]
    Console.SetConsoleMode.restype = BOOL
    Console.SetConsoleMode.argtypes = [
        HANDLE,
        DWORD]
    Console.SetConsoleScreenBufferSize.restype = BOOL
    Console.SetConsoleScreenBufferSize.argtypes = [
        HANDLE,
        c_int]
    Console.SetConsoleTextAttribute.restype = BOOL
    Console.SetConsoleTextAttribute.argtypes = [
        HANDLE,
        WORD]
    Console.SetConsoleTitleW.restype = BOOL
    Console.SetConsoleTitleW.argtypes = [
        c_wchar_p]
    Console.SetConsoleWindowInfo.restype = BOOL
    Console.SetConsoleWindowInfo.argtypes = [
        HANDLE,
        BOOL,
        c_void_p]
    Console.WriteConsoleW.restype = BOOL
    Console.WriteConsoleW.argtypes = [
        HANDLE,
        c_void_p,
        DWORD,
        LPDWORD,
        LPVOID]
    Console.WriteConsoleOutputCharacterW.restype = BOOL
    Console.WriteConsoleOutputCharacterW.argtypes = [
        HANDLE,
        c_wchar_p,
        DWORD,
        c_int,
        LPDWORD]
    Console.WriteFile.restype = BOOL
    Console.WriteFile.argtypes = [
        HANDLE,
        LPCVOID,
        DWORD,
        LPDWORD,
        c_void_p]
    VkKeyScan = windll.user32.VkKeyScanA
    
    class event(Event):
        '''Represent events from the console.'''
        
        def __init__(self, console, input):
            '''Initialize an event from the Windows input structure.'''
            self.type = '??'
            self.serial = console.next_serial()
            self.width = 0
            self.height = 0
            self.x = 0
            self.y = 0
            self.char = ''
            self.keycode = 0
            self.keysym = '??'
            self.keyinfo = None
            self.width = None
            if input.EventType == KEY_EVENT:
                if input.Event.KeyEvent.bKeyDown:
                    self.type = 'KeyPress'
                else:
                    self.type = 'KeyRelease'
                self.char = input.Event.KeyEvent.uChar.UnicodeChar
                self.keycode = input.Event.KeyEvent.wVirtualKeyCode
                self.state = input.Event.KeyEvent.dwControlKeyState
                self.keyinfo = make_KeyPress(self.char, self.state, self.keycode)
                return None
            if None.EventType == MOUSE_EVENT:
                if input.Event.MouseEvent.dwEventFlags & MOUSE_MOVED:
                    self.type = 'Motion'
                else:
                    self.type = 'Button'
                self.x = input.Event.MouseEvent.dwMousePosition.X
                self.y = input.Event.MouseEvent.dwMousePosition.Y
                self.state = input.Event.MouseEvent.dwButtonState
                return None
            if None.EventType == WINDOW_BUFFER_SIZE_EVENT:
                self.type = 'Configure'
                self.width = input.Event.WindowBufferSizeEvent.dwSize.X
                self.height = input.Event.WindowBufferSizeEvent.dwSize.Y
                return None
            if None.EventType == FOCUS_EVENT:
                if input.Event.FocusEvent.bSetFocus:
                    self.type = 'FocusIn'
                    return None
                self.type = None
                return None
            if None.EventType == MENU_EVENT:
                self.type = 'Menu'
                self.state = input.Event.MenuEvent.dwCommandId
                return None


    
    def getconsole(buffer = (1,)):
        '''Get a console handle.

    If buffer is non-zero, a new console buffer is allocated and
    installed.  Otherwise, this returns a handle to the current
    console buffer'''
        c = Console(buffer)
        return c

    HOOKFUNC23 = CFUNCTYPE(c_char_p, c_void_p, c_void_p, c_char_p)
    readline_hook = None
    readline_ref = None
    
    def hook_wrapper_23(stdin, stdout, prompt):
        '''Wrap a Python readline so it behaves like GNU readline.'''
        
        try:
            res = ensure_str(readline_hook(prompt))
            if not res and isinstance(res, bytes):
                raise TypeError('readline must return a string.')
        except KeyboardInterrupt:
            return 0
            except EOFError:
                res = ensure_str('')
            except BaseException:
                print('Readline internal error', file = sys.stderr)
                traceback.print_exc()
                res = ensure_str('\n')
            n = len(res)
            p = Console.PyMem_Malloc(n + 1)
            _strncpy(cast(p, c_char_p), res, n + 1)
            return p


    
    def install_readline(hook):
        '''Set up things for the interpreter to call
    our function like GNU readline.'''
        global readline_hook, readline_ref
        readline_hook = hook
        PyOS_RFP = c_void_p.from_address(Console.GetProcAddress(sys.dllhandle, 'PyOS_ReadlineFunctionPointer'.encode('ascii')))
        readline_ref = HOOKFUNC23(hook_wrapper_23)
        func_start = c_void_p.from_address(addressof(readline_ref)).value
        PyOS_RFP.value = func_start

    if __name__ == '__main__':
        import sys
        import time
        
        def p(char):
            return chr(VkKeyScan(ord(char)) & 255)

        c = Console(0)
        sys.stdout = c
        sys.stderr = c
        c.page()
        print(p('d'), p('D'))
        c.pos(5, 10)
        c.write('hi there')
        print('some printed output')
        for i in range(10):
            q = c.getkeypress()
            print(q)
            del c
            return None
            return None
