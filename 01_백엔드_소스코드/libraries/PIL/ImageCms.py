# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ImageCms.pyc (Python 3.11)

from __future__ import annotations
import operator
import sys
from enum import IntEnum, IntFlag
from functools import reduce
from typing import Any, Literal, SupportsFloat, SupportsInt, Union
from  import Image
from _deprecate import deprecate
from _typing import SupportsRead

try:
    from  import _imagingcms as core
    _CmsProfileCompatible = Union[(str, SupportsRead[bytes], core.CmsProfile, 'ImageCmsProfile')]
except ImportError:
    ex = None
    from _util import DeferredError
    core = DeferredError.new(ex)
    ex = None
    del ex
except:
    ex = None
    del ex

_DESCRIPTION = '\npyCMS\n\n    a Python / PIL interface to the littleCMS ICC Color Management System\n    Copyright (C) 2002-2003 Kevin Cazabon\n    kevin@cazabon.com\n    https://www.cazabon.com\n\n    pyCMS home page:  https://www.cazabon.com/pyCMS\n    littleCMS home page:  https://www.littlecms.com\n    (littleCMS is Copyright (C) 1998-2001 Marti Maria)\n\n    Originally released under LGPL.  Graciously donated to PIL in\n    March 2009, for distribution under the standard PIL license\n\n    The pyCMS.py module provides a "clean" interface between Python/PIL and\n    pyCMSdll, taking care of some of the more complex handling of the direct\n    pyCMSdll functions, as well as error-checking and making sure that all\n    relevant data is kept together.\n\n    While it is possible to call pyCMSdll functions directly, it\'s not highly\n    recommended.\n\n    Version History:\n\n        1.0.0 pil       Oct 2013 Port to LCMS 2.\n\n        0.1.0 pil mod   March 10, 2009\n\n                        Renamed display profile to proof profile. The proof\n                        profile is the profile of the device that is being\n                        simulated, not the profile of the device which is\n                        actually used to display/print the final simulation\n                        (that\'d be the output profile) - also see LCMSAPI.txt\n                        input colorspace -> using \'renderingIntent\' -> proof\n                        colorspace -> using \'proofRenderingIntent\' -> output\n                        colorspace\n\n                        Added LCMS FLAGS support.\n                        Added FLAGS["SOFTPROOFING"] as default flag for\n                        buildProofTransform (otherwise the proof profile/intent\n                        would be ignored).\n\n        0.1.0 pil       March 2009 - added to PIL, as PIL.ImageCms\n\n        0.0.2 alpha     Jan 6, 2002\n\n                        Added try/except statements around type() checks of\n                        potential CObjects... Python won\'t let you use type()\n                        on them, and raises a TypeError (stupid, if you ask\n                        me!)\n\n                        Added buildProofTransformFromOpenProfiles() function.\n                        Additional fixes in DLL, see DLL code for details.\n\n        0.0.1 alpha     first public release, Dec. 26, 2002\n\n    Known to-do list with current version (of Python interface, not pyCMSdll):\n\n        none\n\n'
_VERSION = '1.0.0 pil'

class Intent(IntEnum):
    PERCEPTUAL = 0
    RELATIVE_COLORIMETRIC = 1
    SATURATION = 2
    ABSOLUTE_COLORIMETRIC = 3


class Direction(IntEnum):
    INPUT = 0
    OUTPUT = 1
    PROOF = 2


class Flags(IntFlag):
    '''Flags and documentation are taken from ``lcms2.h``.'''
    NONE = 0
    NOCACHE = 64
    NOOPTIMIZE = 256
    NULLTRANSFORM = 512
    GAMUTCHECK = 4096
    SOFTPROOFING = 16384
    BLACKPOINTCOMPENSATION = 8192
    NOWHITEONWHITEFIXUP = 4
    HIGHRESPRECALC = 1024
    LOWRESPRECALC = 2048
    USE_8BITS_DEVICELINK = 8
    GUESSDEVICECLASS = 32
    KEEP_SEQUENCE = 128
    FORCE_CLUT = 2
    CLUT_POST_LINEARIZATION = 1
    CLUT_PRE_LINEARIZATION = 16
    NONEGATIVES = 32768
    COPY_ALPHA = 67108864
    NODEFAULTRESOURCEDEF = 16777216
    _GRIDPOINTS_1 = 65536
    _GRIDPOINTS_2 = 131072
    _GRIDPOINTS_4 = 262144
    _GRIDPOINTS_8 = 524288
    _GRIDPOINTS_16 = 1048576
    _GRIDPOINTS_32 = 2097152
    _GRIDPOINTS_64 = 4194304
    _GRIDPOINTS_128 = 8388608
    GRIDPOINTS = (lambda n = None: Flags.NONE | (n & 255) << 16)()

_MAX_FLAG = reduce(operator.or_, Flags)
# WARNING: Decompyle incomplete
