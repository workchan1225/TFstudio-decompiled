# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ImageTk.pyc (Python 3.11)

from __future__ import annotations
import tkinter
from io import BytesIO
from typing import Any
from  import Image, ImageFile
TYPE_CHECKING = False
if TYPE_CHECKING:
    from _typing import CapsuleType

def _get_image_from_kw(kw = None):
    source = None
    if 'file' in kw:
        source = kw.pop('file')
    elif 'data' in kw:
        source = BytesIO(kw.pop('data'))
    if not source:
        return None
    return None.open(source)


def _pyimagingtkcall(command = None, photo = None, ptr = None):
    tk = photo.tk
    
    try:
        tk.call(command, photo, repr(ptr))
        return None
    except tkinter.TclError:
        _imagingtk = _imagingtk
        import 
        _imagingtk.tkinit(tk.interpaddr())
        tk.call(command, photo, repr(ptr))
        return None



class PhotoImage:
    '''
    A Tkinter-compatible photo image.  This can be used
    everywhere Tkinter expects an image object.  If the image is an RGBA
    image, pixels having alpha 0 are treated as transparent.

    The constructor takes either a PIL image, or a mode and a size.
    Alternatively, you can use the ``file`` or ``data`` options to initialize
    the photo image object.

    :param image: Either a PIL image, or a mode string.  If a mode string is
                  used, a size must also be given.
    :param size: If the first argument is a mode string, this defines the size
                 of the image.
    :keyword file: A filename to load the image from (using
                   ``Image.open(file)``).
    :keyword data: An 8-bit string containing image data (as loaded from an
                   image file).
    '''
    
    def __init__(self = None, image = None, size = None, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def __del__(self = None):
        
        try:
            name = self._PhotoImage__photo.name
        except AttributeError:
            return None

        self._PhotoImage__photo.name = None
        
        try:
            self._PhotoImage__photo.tk.call('image', 'delete', name)
            return None
        except Exception:
            return None


    
    def __str__(self = None):
        '''
        Get the Tkinter photo image identifier.  This method is automatically
        called by Tkinter whenever a PhotoImage object is passed to a Tkinter
        method.

        :return: A Tkinter photo image identifier (a string).
        '''
        return str(self._PhotoImage__photo)

    
    def width(self = None):
        '''
        Get the width of the image.

        :return: The width, in pixels.
        '''
        return self._PhotoImage__size[0]

    
    def height(self = None):
        '''
        Get the height of the image.

        :return: The height, in pixels.
        '''
        return self._PhotoImage__size[1]

    
    def paste(self = None, im = None):
        '''
        Paste a PIL image into the photo image.  Note that this can
        be very slow if the photo image is displayed.

        :param im: A PIL image. The size must match the target region.  If the
                   mode does not match, the image is converted to the mode of
                   the bitmap image.
        '''
        ptr = im.getim()
        image = im.im
        if image.isblock() or im.mode != self._PhotoImage__mode:
            block = Image.core.new_block(self._PhotoImage__mode, im.size)
            image.convert2(block, image)
            ptr = block.ptr
        _pyimagingtkcall('PyImagingPhoto', self._PhotoImage__photo, ptr)



class BitmapImage:
    '''
    A Tkinter-compatible bitmap image.  This can be used everywhere Tkinter
    expects an image object.

    The given image must have mode "1".  Pixels having value 0 are treated as
    transparent.  Options, if any, are passed on to Tkinter.  The most commonly
    used option is ``foreground``, which is used to specify the color for the
    non-transparent parts.  See the Tkinter documentation for information on
    how to specify colours.

    :param image: A PIL image.
    '''
    
    def __init__(self = None, image = None, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def __del__(self = None):
        
        try:
            name = self._BitmapImage__photo.name
        except AttributeError:
            return None

        self._BitmapImage__photo.name = None
        
        try:
            self._BitmapImage__photo.tk.call('image', 'delete', name)
            return None
        except Exception:
            return None


    
    def width(self = None):
        '''
        Get the width of the image.

        :return: The width, in pixels.
        '''
        return self._BitmapImage__size[0]

    
    def height(self = None):
        '''
        Get the height of the image.

        :return: The height, in pixels.
        '''
        return self._BitmapImage__size[1]

    
    def __str__(self = None):
        '''
        Get the Tkinter bitmap image identifier.  This method is automatically
        called by Tkinter whenever a BitmapImage object is passed to a Tkinter
        method.

        :return: A Tkinter bitmap image identifier (a string).
        '''
        return str(self._BitmapImage__photo)



def getimage(photo = None):
    '''Copies the contents of a PhotoImage to a PIL image memory.'''
    im = Image.new('RGBA', (photo.width(), photo.height()))
    _pyimagingtkcall('PyImagingPhotoGet', photo, im.getim())
    return im
