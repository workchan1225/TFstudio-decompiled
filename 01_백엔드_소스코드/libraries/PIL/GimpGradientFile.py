# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: GimpGradientFile.pyc (Python 3.11)

'''
Stuff to translate curve segments to palette values (derived from
the corresponding code in GIMP, written by Federico Mena Quintero.
See the GIMP distribution for more information.)
'''
from __future__ import annotations
from math import log, pi, sin, sqrt
from _binary import o8
TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import IO
EPSILON = 1e-10

def linear(middle = None, pos = None):
    if pos <= middle:
        if middle < EPSILON:
            return 0
        return None * pos / middle
    pos = None - middle
    middle = 1 - middle
    if middle < EPSILON:
        return 1
    return None + 0.5 * pos / middle


def curved(middle = None, pos = None):
    return pos ** (log(0.5) / log(max(middle, EPSILON)))


def sine(middle = None, pos = None):
    return (sin(-pi / 2 + pi * linear(middle, pos)) + 1) / 2


def sphere_increasing(middle = None, pos = None):
    return sqrt(1 - (linear(middle, pos) - 1) ** 2)


def sphere_decreasing(middle = None, pos = None):
    return 1 - sqrt(1 - linear(middle, pos) ** 2)

SEGMENTS = [
    linear,
    curved,
    sine,
    sphere_increasing,
    sphere_decreasing]

class GradientFile:
    gradient: 'list[tuple[float, float, float, list[float], list[float], Callable[[float, float], float]]] | None' = None
    
    def getpalette(self = None, entries = None):
        pass
    # WARNING: Decompyle incomplete



class GimpGradientFile(GradientFile):
    """File handler for GIMP's gradient format."""
    
    def __init__(self = None, fp = None):
        if not fp.readline().startswith(b'GIMP Gradient'):
            msg = 'not a GIMP gradient file'
            raise SyntaxError(msg)
        line = fp.readline()
        if line.startswith(b'Name: '):
            line = fp.readline().strip()
        count = int(line)
        self.gradient = []
        for i in range(count):
            s = fp.readline().split()
            w = s[:11]()
            x1 = w[2]
            x0 = w[0]
            xm = w[1]
            rgb0 = w[3:7]
            rgb1 = w[7:11]
            segment = SEGMENTS[int(s[11])]
            cspace = int(s[12])
            if cspace != 0:
                msg = 'cannot handle HSV colour space'
                raise OSError(msg)
            self.gradient.append((x0, x1, xm, rgb0, rgb1, segment))
            return None
