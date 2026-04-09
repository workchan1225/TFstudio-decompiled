# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: PaletteFile.pyc (Python 3.11)

from __future__ import annotations
from typing import IO
from _binary import o8

class PaletteFile:
    '''File handler for Teragon-style palette files.'''
    rawmode = 'RGB'
    
    def __init__(self = None, fp = None):
        palette = range(256)()
        s = fp.readline()
        if not s:
            pass
        elif s.startswith(b'#'):
            continue
        if len(s) > 100:
            msg = 'bad palette file'
            raise SyntaxError(msg)
        v = s.split()()
        
        try:
            (i, r, g, b) = v
        except ValueError:
            (lambda .0: [ o8(i) * 3 for i in .0 ])
            (i, r) = v
            g = r
            b = r

        if  <= 0, i or 0, i <= 255:
            pass
        else:
            (lambda .0: [ int(x) for x in .0 ])
        continue
        b''.join(palette) = o8(r) + o8(g) + o8(b)

    
    def getpalette(self = None):
        return (self.palette, self.rawmode)
