# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: screen.pyc (Python 3.11)


class Screen:
    
    def __init__(self, x = None, y = None, width = None, height = (None,), frame = ('x', int, 'y', int, 'width', int, 'height', int, 'frame', object, 'return', None)):
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        self.frame = frame

    
    def __str__(self = None):
        return repr(self)

    
    def __repr__(self = None):
        return f'''{self.width}x{self.height} at {self.x},{self.y}'''
