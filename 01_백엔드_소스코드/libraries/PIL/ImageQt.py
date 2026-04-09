# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ImageQt.pyc (Python 3.11)

from __future__ import annotations
import sys
from io import BytesIO
from  import Image
from _util import is_path
TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import Any
    from  import ImageFile
    QBuffer: 'type'
qt_version: 'str | None'
qt_versions = [
    [
        '6',
        'PyQt6'],
    [
        'side6',
        'PySide6']]
qt_versions.sort(key = (lambda version: version[1] in sys.modules), reverse = True)
for version, qt_module in qt_versions:
    qRgba: 'Callable[[int, int, int, int], int]'
    if qt_module == 'PyQt6':
        from PyQt6.QtCore import QBuffer, QByteArray, QIODevice
        from PyQt6.QtGui import QImage, QPixmap, qRgba
    elif qt_module == 'PySide6':
        from PySide6.QtCore import QBuffer, QByteArray, QIODevice
        from PySide6.QtGui import QImage, QPixmap, qRgba
    else:
        except (ImportError, RuntimeError):
            continue
    qt_is_installed = True
    qt_version = version
qt_is_installed = False
qt_version = None

def rgb(r = None, g = None, b = None, a = (255,)):
    '''(Internal) Turns an RGB color into a Qt compatible color integer.'''
    return qRgba(r, g, b, a) & 0xFFFFFFFF


def fromqimage(im = None):
    '''
    :param im: QImage or PIL ImageQt object
    '''
    buffer = QBuffer()
    if qt_version == '6':
        
        try:
            qt_openmode = getattr(QIODevice, 'OpenModeFlag')
        except AttributeError:
            qt_openmode = getattr(QIODevice, 'OpenMode')
        except:
            qt_openmode = QIODevice

        buffer.open(getattr(qt_openmode, 'ReadWrite'))
        if im.hasAlphaChannel():
            im.save(buffer, 'png')
        else:
            im.save(buffer, 'ppm')
    b = BytesIO()
    b.write(buffer.data())
    buffer.close()
    b.seek(0)
    return Image.open(b)


def fromqpixmap(im = None):
    return fromqimage(im)


def align8to32(bytes = None, width = None, mode = None):
    '''
    converts each scanline of data from 8 bit to 32 bit aligned
    '''
    pass
# WARNING: Decompyle incomplete


def _toqclass_helper(im = None):
    pass
# WARNING: Decompyle incomplete

if qt_is_installed:
    
    class ImageQt(QImage):
        pass
    # WARNING: Decompyle incomplete


def toqimage(im = None):
    return ImageQt(im)


def toqpixmap(im = None):
    qimage = toqimage(im)
    pixmap = getattr(QPixmap, 'fromImage')(qimage)
    if qt_version == '6':
        pixmap.detach()
    return pixmap
