# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: WebPImagePlugin.pyc (Python 3.11)

from __future__ import annotations
from io import BytesIO
from  import Image, ImageFile

try:
    from  import _webp
    SUPPORTED = True
except ImportError:
    SUPPORTED = False

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import IO, Any
_VP8_MODES_BY_IDENTIFIER = {
    b'VP8 ': 'RGB',
    b'VP8X': 'RGBA',
    b'VP8L': 'RGBA' }

def _accept(prefix = None):
    is_riff_file_format = prefix.startswith(b'RIFF')
    is_webp_file = prefix[8:12] == b'WEBP'
    is_valid_vp8_mode = prefix[12:16] in _VP8_MODES_BY_IDENTIFIER
    if is_riff_file_format and is_webp_file and is_valid_vp8_mode:
        if not SUPPORTED:
            return 'image file could not be identified because WEBP support not installed'
        return None


class WebPImageFile(ImageFile.ImageFile):
    pass
# WARNING: Decompyle incomplete


def _convert_frame(im = None):
    if im.mode not in ('RGBX', 'RGBA', 'RGB'):
        im = im.convert('RGBA' if im.has_transparency_data else 'RGB')
    return im


def _save_all(im = None, fp = None, filename = None):
    encoderinfo = im.encoderinfo.copy()
    append_images = list(encoderinfo.get('append_images', []))
    total = 0
    for ims in [
        im] + append_images:
        total += getattr(ims, 'n_frames', 1)
        if total == 1:
            _save(im, fp, filename)
            return None
        background = None
        if 'background' in encoderinfo:
            background = encoderinfo['background']
        elif 'background' in im.info:
            background = im.info['background']
            if isinstance(background, int):
                palette = im.getpalette()
                if palette:
                    (r, g, b) = palette[background * 3:(background + 1) * 3]
                    background = (r, g, b, 255)
                else:
                    background = (background, background, background, 255)
    duration = im.encoderinfo.get('duration', im.info.get('duration', 0))
    loop = im.encoderinfo.get('loop', 0)
    minimize_size = im.encoderinfo.get('minimize_size', False)
    kmin = im.encoderinfo.get('kmin', None)
    kmax = im.encoderinfo.get('kmax', None)
    allow_mixed = im.encoderinfo.get('allow_mixed', False)
    verbose = False
    lossless = im.encoderinfo.get('lossless', False)
    quality = im.encoderinfo.get('quality', 80)
    alpha_quality = im.encoderinfo.get('alpha_quality', 100)
    method = im.encoderinfo.get('method', 0)
    if not im.encoderinfo.get('icc_profile'):
        icc_profile = ''
        exif = im.encoderinfo.get('exif', '')
        if isinstance(exif, Image.Exif):
            exif = exif.tobytes()
    xmp = im.encoderinfo.get('xmp', '')
    if allow_mixed:
        lossless = False
# WARNING: Decompyle incomplete


def _save(im = None, fp = None, filename = None):
    lossless = im.encoderinfo.get('lossless', False)
    quality = im.encoderinfo.get('quality', 80)
    alpha_quality = im.encoderinfo.get('alpha_quality', 100)
    if not im.encoderinfo.get('icc_profile'):
        icc_profile = ''
        exif = im.encoderinfo.get('exif', b'')
        if isinstance(exif, Image.Exif):
            exif = exif.tobytes()
    if exif.startswith(b'Exif\x00\x00'):
        exif = exif[6:]
    xmp = im.encoderinfo.get('xmp', '')
    method = im.encoderinfo.get('method', 4)
    exact = 1 if im.encoderinfo.get('exact') else 0
    im = _convert_frame(im)
    data = _webp.WebPEncode(im.getim(), lossless, float(quality), float(alpha_quality), icc_profile, method, exact, exif, xmp)
# WARNING: Decompyle incomplete

Image.register_open(WebPImageFile.format, WebPImageFile, _accept)
if SUPPORTED:
    Image.register_save(WebPImageFile.format, _save)
    Image.register_save_all(WebPImageFile.format, _save_all)
    Image.register_extension(WebPImageFile.format, '.webp')
    Image.register_mime(WebPImageFile.format, 'image/webp')
    return None
