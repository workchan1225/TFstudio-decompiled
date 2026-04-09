# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ImageSequence.pyc (Python 3.11)

from __future__ import annotations
from  import Image
TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Callable

class Iterator:
    '''
    This class implements an iterator object that can be used to loop
    over an image sequence.

    You can use the ``[]`` operator to access elements by index. This operator
    will raise an :py:exc:`IndexError` if you try to access a nonexistent
    frame.

    :param im: An image object.
    '''
    
    def __init__(self = None, im = None):
        if not hasattr(im, 'seek'):
            msg = 'im must have seek method'
            raise AttributeError(msg)
        self.im = im
        self.position = getattr(self.im, '_min_frame', 0)

    
    def __getitem__(self = None, ix = None):
        
        try:
            self.im.seek(ix)
            return self.im
        except EOFError:
            e = None
            msg = 'end of sequence'
            raise IndexError(msg), e
            e = None
            del e


    
    def __iter__(self = None):
        return self

    
    def __next__(self = None):
        
        try:
            self.im.seek(self.position)
            return self.im
        except EOFError:
            None = None
            msg = 'end of sequence'
            raise StopIteration(msg), e
            e = None
            del e




def all_frames(im = None, func = None):
    '''
    Applies a given function to all frames in an image or a list of images.
    The frames are returned as a list of separate images.

    :param im: An image, or a list of images.
    :param func: The function to apply to all of the image frames.
    :returns: A list of images.
    '''
    pass
# WARNING: Decompyle incomplete
