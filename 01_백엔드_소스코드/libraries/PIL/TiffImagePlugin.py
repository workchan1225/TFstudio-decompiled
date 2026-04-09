# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: TiffImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import io
import itertools
import logging
import math
import os
import struct
import warnings
from collections.abc import Callable, MutableMapping
from fractions import Fraction
from numbers import Number, Rational
from typing import IO, Any, cast
from  import ExifTags, Image, ImageFile, ImageOps, ImagePalette, TiffTags
from _binary import i16be as i16
from _binary import i32be as i32
from _binary import o8
from _util import DeferredError, is_path
from TiffTags import TYPES
TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterator
    from typing import NoReturn
    from _typing import Buffer, IntegralLike, StrOrBytesPath
logger = logging.getLogger(__name__)
READ_LIBTIFF = False
WRITE_LIBTIFF = False
STRIP_SIZE = 65536
II = b'II'
MM = b'MM'
OSUBFILETYPE = 255
IMAGEWIDTH = 256
IMAGELENGTH = 257
BITSPERSAMPLE = 258
COMPRESSION = 259
PHOTOMETRIC_INTERPRETATION = 262
FILLORDER = 266
IMAGEDESCRIPTION = 270
STRIPOFFSETS = 273
SAMPLESPERPIXEL = 277
ROWSPERSTRIP = 278
STRIPBYTECOUNTS = 279
X_RESOLUTION = 282
Y_RESOLUTION = 283
PLANAR_CONFIGURATION = 284
RESOLUTION_UNIT = 296
TRANSFERFUNCTION = 301
SOFTWARE = 305
DATE_TIME = 306
ARTIST = 315
PREDICTOR = 317
COLORMAP = 320
TILEWIDTH = 322
TILELENGTH = 323
TILEOFFSETS = 324
TILEBYTECOUNTS = 325
SUBIFD = 330
EXTRASAMPLES = 338
SAMPLEFORMAT = 339
JPEGTABLES = 347
YCBCRSUBSAMPLING = 530
REFERENCEBLACKWHITE = 532
COPYRIGHT = 33432
IPTC_NAA_CHUNK = 33723
PHOTOSHOP_CHUNK = 34377
ICCPROFILE = 34675
EXIFIFD = 34665
XMP = 700
JPEGQUALITY = 65537
IMAGEJ_META_DATA_BYTE_COUNTS = 50838
IMAGEJ_META_DATA = 50839
# WARNING: Decompyle incomplete
