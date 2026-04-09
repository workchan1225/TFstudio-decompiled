# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: winterm.pyc (Python 3.11)


try:
    from msvcrt import get_osfhandle
except ImportError:
    
    def get_osfhandle(_):
        raise OSError("This isn't windows!")


from  import win32

class WinColor(object):
    BLACK = 0
    BLUE = 1
    GREEN = 2
    CYAN = 3
    RED = 4
    MAGENTA = 5
    YELLOW = 6
    GREY = 7


class WinStyle(object):
    NORMAL = 0
    BRIGHT = 8
    BRIGHT_BACKGROUND = 128


class WinTerm(object):
    
    def __init__(self):
        self._default = win32.GetConsoleScreenBufferInfo(win32.STDOUT).wAttributes
        self.set_attrs(self._default)
        self._default_fore = self._fore
        self._default_back = self._back
        self._default_style = self._style
        self._light = 0

    
    def get_attrs(self):
        return self._fore + self._back * 16 + (self._style | self._light)

    
    def set_attrs(self, value):
        self._fore = value & 7
        self._back = value >> 4 & 7
        self._style = value & (WinStyle.BRIGHT | WinStyle.BRIGHT_BACKGROUND)

    
    def reset_all(self, on_stderr = (None,)):
        self.set_attrs(self._default)
        self.set_console(attrs = self._default)
        self._light = 0

    
    def fore(self, fore, light, on_stderr = (None, False, False)):
        pass
    # WARNING: Decompyle incomplete

    
    def back(self, back, light, on_stderr = (None, False, False)):
        pass
    # WARNING: Decompyle incomplete

    
    def style(self, style, on_stderr = (None, False)):
        pass
    # WARNING: Decompyle incomplete

    
    def set_console(self, attrs, on_stderr = (None, False)):
        pass
    # WARNING: Decompyle incomplete

    
    def get_position(self, handle):
        position = win32.GetConsoleScreenBufferInfo(handle).dwCursorPosition
        return position

    
    def set_cursor_position(self, position, on_stderr = (None, False)):
        pass
    # WARNING: Decompyle incomplete

    
    def cursor_adjust(self, x, y, on_stderr = (False,)):
        handle = win32.STDOUT
        if on_stderr:
            handle = win32.STDERR
        position = self.get_position(handle)
        adjusted_position = (position.Y + y, position.X + x)
        win32.SetConsoleCursorPosition(handle, adjusted_position, adjust = False)

    
    def erase_screen(self, mode, on_stderr = (0, False)):
        handle = win32.STDOUT
        if on_stderr:
            handle = win32.STDERR
        csbi = win32.GetConsoleScreenBufferInfo(handle)
        cells_in_screen = csbi.dwSize.X * csbi.dwSize.Y
        cells_before_cursor = csbi.dwSize.X * csbi.dwCursorPosition.Y + csbi.dwCursorPosition.X
        if mode == 0:
            from_coord = csbi.dwCursorPosition
            cells_to_erase = cells_in_screen - cells_before_cursor
        elif mode == 1:
            from_coord = win32.COORD(0, 0)
            cells_to_erase = cells_before_cursor
        elif mode == 2:
            from_coord = win32.COORD(0, 0)
            cells_to_erase = cells_in_screen
        else:
            return None
        None.FillConsoleOutputCharacter(handle, ' ', cells_to_erase, from_coord)
        win32.FillConsoleOutputAttribute(handle, self.get_attrs(), cells_to_erase, from_coord)
        if mode == 2:
            win32.SetConsoleCursorPosition(handle, (1, 1))
            return None

    
    def erase_line(self, mode, on_stderr = (0, False)):
        handle = win32.STDOUT
        if on_stderr:
            handle = win32.STDERR
        csbi = win32.GetConsoleScreenBufferInfo(handle)
        if mode == 0:
            from_coord = csbi.dwCursorPosition
            cells_to_erase = csbi.dwSize.X - csbi.dwCursorPosition.X
        elif mode == 1:
            from_coord = win32.COORD(0, csbi.dwCursorPosition.Y)
            cells_to_erase = csbi.dwCursorPosition.X
        elif mode == 2:
            from_coord = win32.COORD(0, csbi.dwCursorPosition.Y)
            cells_to_erase = csbi.dwSize.X
        else:
            return None
        None.FillConsoleOutputCharacter(handle, ' ', cells_to_erase, from_coord)
        win32.FillConsoleOutputAttribute(handle, self.get_attrs(), cells_to_erase, from_coord)

    
    def set_title(self, title):
        win32.SetConsoleTitle(title)



def enable_vt_processing(fd):
    pass
# WARNING: Decompyle incomplete
