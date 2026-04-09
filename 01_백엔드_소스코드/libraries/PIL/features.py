# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: features.pyc (Python 3.11)

from __future__ import annotations
import collections
import os
import sys
import warnings
from typing import IO
import PIL
from  import Image
modules = {
    'pil': ('PIL._imaging', 'PILLOW_VERSION'),
    'tkinter': ('PIL._tkinter_finder', 'tk_version'),
    'freetype2': ('PIL._imagingft', 'freetype2_version'),
    'littlecms2': ('PIL._imagingcms', 'littlecms_version'),
    'webp': ('PIL._webp', 'webpdecoder_version'),
    'avif': ('PIL._avif', 'libavif_version') }

def check_module(feature = None):
    '''
    Checks if a module is available.

    :param feature: The module to check for.
    :returns: ``True`` if available, ``False`` otherwise.
    :raises ValueError: If the module is not defined in this version of Pillow.
    '''
    if feature not in modules:
        msg = f'''Unknown module {feature}'''
        raise ValueError(msg)
    (module, ver) = modules[feature]
    
    try:
        __import__(module)
        return True
    except ModuleNotFoundError:
        return False
        except ImportError:
            ex = None
            warnings.warn(str(ex))
            ex = None
            del ex
            return False
            ex = None
            del ex



def version_module(feature = None):
    '''
    :param feature: The module to check for.
    :returns:
        The loaded version number as a string, or ``None`` if unknown or not available.
    :raises ValueError: If the module is not defined in this version of Pillow.
    '''
    if not check_module(feature):
        return None
    (module, ver) = None[feature]
    return getattr(__import__(module, fromlist = [
        ver]), ver)


def get_supported_modules():
    '''
    :returns: A list of all supported modules.
    '''
    return modules()

codecs = {
    'jpg': ('jpeg', 'jpeglib'),
    'jpg_2000': ('jpeg2k', 'jp2klib'),
    'zlib': ('zip', 'zlib'),
    'libtiff': ('libtiff', 'libtiff') }

def check_codec(feature = None):
    '''
    Checks if a codec is available.

    :param feature: The codec to check for.
    :returns: ``True`` if available, ``False`` otherwise.
    :raises ValueError: If the codec is not defined in this version of Pillow.
    '''
    if feature not in codecs:
        msg = f'''Unknown codec {feature}'''
        raise ValueError(msg)
    (codec, lib) = codecs[feature]
    return f'''{codec}_encoder''' in dir(Image.core)


def version_codec(feature = None):
    '''
    :param feature: The codec to check for.
    :returns:
        The version number as a string, or ``None`` if not available.
        Checked at compile time for ``jpg``, run-time otherwise.
    :raises ValueError: If the codec is not defined in this version of Pillow.
    '''
    if not check_codec(feature):
        return None
    (codec, lib) = None[feature]
    version = getattr(Image.core, f'''{lib}_version''')
    if feature == 'libtiff':
        return version.split('\n')[0].split('Version ')[1]


def get_supported_codecs():
    '''
    :returns: A list of all supported codecs.
    '''
    return codecs()

features: 'dict[str, tuple[str, str, str | None]]' = {
    'raqm': ('PIL._imagingft', 'HAVE_RAQM', 'raqm_version'),
    'fribidi': ('PIL._imagingft', 'HAVE_FRIBIDI', 'fribidi_version'),
    'harfbuzz': ('PIL._imagingft', 'HAVE_HARFBUZZ', 'harfbuzz_version'),
    'libjpeg_turbo': ('PIL._imaging', 'HAVE_LIBJPEGTURBO', 'libjpeg_turbo_version'),
    'mozjpeg': ('PIL._imaging', 'HAVE_MOZJPEG', 'libjpeg_turbo_version'),
    'zlib_ng': ('PIL._imaging', 'HAVE_ZLIBNG', 'zlib_ng_version'),
    'libimagequant': ('PIL._imaging', 'HAVE_LIBIMAGEQUANT', 'imagequant_version'),
    'xcb': ('PIL._imaging', 'HAVE_XCB', None) }

def check_feature(feature = None):
    '''
    Checks if a feature is available.

    :param feature: The feature to check for.
    :returns: ``True`` if available, ``False`` if unavailable, ``None`` if unknown.
    :raises ValueError: If the feature is not defined in this version of Pillow.
    '''
    if feature not in features:
        msg = f'''Unknown feature {feature}'''
        raise ValueError(msg)
    (module, flag, ver) = features[feature]
    
    try:
        imported_module = __import__(module, fromlist = [
            'PIL'])
        return getattr(imported_module, flag)
    except ModuleNotFoundError:
        return None
        except ImportError:
            ex = None
            warnings.warn(str(ex))
            ex = None
            del ex
            return None
            ex = None
            del ex



def version_feature(feature = None):
    '''
    :param feature: The feature to check for.
    :returns: The version number as a string, or ``None`` if not available.
    :raises ValueError: If the feature is not defined in this version of Pillow.
    '''
    if not check_feature(feature):
        return None
    (module, flag, ver) = None[feature]
# WARNING: Decompyle incomplete


def get_supported_features():
    '''
    :returns: A list of all supported features.
    '''
    return features()


def check(feature = None):
    '''
    :param feature: A module, codec, or feature name.
    :returns:
        ``True`` if the module, codec, or feature is available,
        ``False`` or ``None`` otherwise.
    '''
    if feature in modules:
        return check_module(feature)
    if None in codecs:
        return check_codec(feature)
    if None in features:
        return check_feature(feature)
    None.warn(f'''Unknown feature \'{feature}\'.''', stacklevel = 2)
    return False


def version(feature = None):
    '''
    :param feature:
        The module, codec, or feature to check for.
    :returns:
        The version number as a string, or ``None`` if unknown or not available.
    '''
    if feature in modules:
        return version_module(feature)
    if None in codecs:
        return version_codec(feature)
    if None in features:
        return version_feature(feature)


def get_supported():
    '''
    :returns: A list of all supported modules, features, and codecs.
    '''
    ret = get_supported_modules()
    ret.extend(get_supported_features())
    ret.extend(get_supported_codecs())
    return ret


def pilinfo(out = None, supported_formats = None):
    '''
    Prints information about this installation of Pillow.
    This function can be called with ``python3 -m PIL``.
    It can also be called with ``python3 -m PIL.report`` or ``python3 -m PIL --report``
    to have "supported_formats" set to ``False``, omitting the list of all supported
    image file formats.

    :param out:
        The output stream to print to. Defaults to ``sys.stdout`` if ``None``.
    :param supported_formats:
        If ``True``, a list of all supported image file formats will be printed.
    '''
    pass
# WARNING: Decompyle incomplete
