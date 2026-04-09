# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ansi.pyc (Python 3.11)

import os
import re
import sys
terminal_escape = re.compile('(\x01?\x1b\\[[0-9;]*m\x02?)')
escape_parts = re.compile('\x01?\x1b\\[([0-9;]*)m\x02?')

class AnsiState(object):
    
    def __init__(self, bold, inverse, color, background, backgroundbold = (False, False, 'white', 'black', False)):
        self.bold = bold
        self.inverse = inverse
        self.color = color
        self.background = background
        self.backgroundbold = backgroundbold

    trtable = {
        'black': 0,
        'red': 4,
        'green': 2,
        'yellow': 6,
        'blue': 1,
        'magenta': 5,
        'cyan': 3,
        'white': 7 }
    revtable = dict(zip(trtable.values(), trtable.keys()))
    
    def get_winattr(self):
        attr = 0
        if self.bold:
            attr |= 8
        if self.backgroundbold:
            attr |= 128
        if self.inverse:
            attr |= 16384
        attr |= self.trtable[self.color]
        attr |= self.trtable[self.background] << 4
        return attr

    
    def set_winattr(self, attr):
        self.bold = bool(attr & 8)
        self.backgroundbold = bool(attr & 128)
        self.inverse = bool(attr & 16384)
        self.color = self.revtable[attr & 7]
        self.background = self.revtable[(attr & 112) >> 4]

    winattr = property(get_winattr, set_winattr)
    
    def __repr__(self):
        return 'AnsiState(bold=%s,inverse=%s,color=%9s,background=%9s,backgroundbold=%s)# 0x%x' % (self.bold, self.inverse, '"%s"' % self.color, '"%s"' % self.background, self.backgroundbold, self.winattr)

    
    def copy(self):
        x = AnsiState()
        x.bold = self.bold
        x.inverse = self.inverse
        x.color = self.color
        x.background = self.background
        x.backgroundbold = self.backgroundbold
        return x


defaultstate = AnsiState(False, False, 'white')
trtable = {
    0: 'black',
    1: 'red',
    2: 'green',
    3: 'yellow',
    4: 'blue',
    5: 'magenta',
    6: 'cyan',
    7: 'white' }

class AnsiWriter(object):
    
    def __init__(self, default = (defaultstate,)):
        if isinstance(defaultstate, AnsiState):
            self.defaultstate = default
            return None
        self.defaultstate = None()
        self.defaultstate.winattr = defaultstate

    
    def write_color(self, text, attr = (None,)):
        '''write text at current cursor position and interpret color escapes.

        return the number of characters written.
        '''
        if isinstance(attr, AnsiState):
            defaultstate = attr
    # WARNING: Decompyle incomplete

    
    def parse_color(self, text, attr = (None,)):
        (n, res) = self.write_color(text, attr)
        return ((lambda .0: [ attr.winattr for attr, text in .0 ]), res())



def write_color(text, attr = (None,)):
    a = AnsiWriter(defaultstate)
    return a.write_color(text, attr)


def write_color_old(text, attr = (None,)):
    '''write text at current cursor position and interpret color escapes.

    return the number of characters written.
    '''
    res = []
    chunks = terminal_escape.split(text)
    n = 0
# WARNING: Decompyle incomplete

if __name__ == '__main__x':
    import pprint
    pprint = pprint.pprint
    s = '\x1b[0;31mred\x1b[0;32mgreen\x1b[0;33myellow\x1b[0;34mblue\x1b[0;35mmagenta\x1b[0;36mcyan\x1b[0;37mwhite\x1b[0m'
    pprint(write_color(s))
    pprint(write_color_old(s))
    s = '\x1b[1;31mred\x1b[1;32mgreen\x1b[1;33myellow\x1b[1;34mblue\x1b[1;35mmagenta\x1b[1;36mcyan\x1b[1;37mwhite\x1b[0m'
    pprint(write_color(s))
    pprint(write_color_old(s))
    s = '\x1b[0;7;31mred\x1b[0;7;32mgreen\x1b[0;7;33myellow\x1b[0;7;34mblue\x1b[0;7;35mmagenta\x1b[0;7;36mcyan\x1b[0;7;37mwhite\x1b[0m'
    pprint(write_color(s))
    pprint(write_color_old(s))
    s = '\x1b[1;7;31mred\x1b[1;7;32mgreen\x1b[1;7;33myellow\x1b[1;7;34mblue\x1b[1;7;35mmagenta\x1b[1;7;36mcyan\x1b[1;7;37mwhite\x1b[0m'
    pprint(write_color(s))
    pprint(write_color_old(s))
if __name__ == '__main__':
    import pprint
    import console
    pprint = pprint.pprint
    c = console.Console()
    c.write_color('dhsjdhs')
    c.write_color('\x1b[0;32mIn [\x1b[1;32m1\x1b[0;32m]:')
    print
    pprint(write_color('\x1b[0;32mIn [\x1b[1;32m1\x1b[0;32m]:'))
if __name__ == '__main__x':
    import pprint
    pprint = pprint.pprint
    s = '\x1b[0;31mred\x1b[0;32mgreen\x1b[0;33myellow\x1b[0;34mblue\x1b[0;35mmagenta\x1b[0;36mcyan\x1b[0;37mwhite\x1b[0m'
    pprint(write_color(s))
    return None
