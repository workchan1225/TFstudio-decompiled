# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: zipfile.pyc (Python 3.11)

__doc__ = '\nRead and write ZIP files.\n\nXXX references to utf-8 need further investigation.\n'
import binascii
import importlib.util as importlib
import io
import itertools
import os
import posixpath
import shutil
import stat
import struct
import sys
import threading
import time
import contextlib
import pathlib

try:
    import zlib
    crc32 = zlib.crc32
except ImportError:
    zlib = None
    crc32 = binascii.crc32


try:
    import bz2
except ImportError:
    bz2 = None


try:
    import lzma
except ImportError:
    lzma = None

__all__ = [
    'BadZipFile',
    'BadZipfile',
    'error',
    'ZIP_STORED',
    'ZIP_DEFLATED',
    'ZIP_BZIP2',
    'ZIP_LZMA',
    'is_zipfile',
    'ZipInfo',
    'ZipFile',
    'PyZipFile',
    'LargeZipFile',
    'Path']

class BadZipFile(Exception):
    pass


class LargeZipFile(Exception):
    '''
    Raised when writing a zipfile, the zipfile requires ZIP64 extensions
    and those extensions are disabled.
    '''
    pass

error = BadZipFile
BadZipfile = BadZipFile
ZIP64_LIMIT = 2147483647
ZIP_FILECOUNT_LIMIT = 65535
ZIP_MAX_COMMENT = 65535
ZIP_STORED = 0
ZIP_DEFLATED = 8
ZIP_BZIP2 = 12
ZIP_LZMA = 14
DEFAULT_VERSION = 20
ZIP64_VERSION = 45
BZIP2_VERSION = 46
LZMA_VERSION = 63
MAX_EXTRACT_VERSION = 63
structEndArchive = b'<4s4H2LH'
stringEndArchive = b'PK\x05\x06'
sizeEndCentDir = struct.calcsize(structEndArchive)
_ECD_SIGNATURE = 0
_ECD_DISK_NUMBER = 1
_ECD_DISK_START = 2
_ECD_ENTRIES_THIS_DISK = 3
_ECD_ENTRIES_TOTAL = 4
_ECD_SIZE = 5
_ECD_OFFSET = 6
_ECD_COMMENT_SIZE = 7
_ECD_COMMENT = 8
_ECD_LOCATION = 9
structCentralDir = '<4s4B4HL2L5H2L'
stringCentralDir = b'PK\x01\x02'
sizeCentralDir = struct.calcsize(structCentralDir)
_CD_SIGNATURE = 0
_CD_CREATE_VERSION = 1
_CD_CREATE_SYSTEM = 2
_CD_EXTRACT_VERSION = 3
_CD_EXTRACT_SYSTEM = 4
_CD_FLAG_BITS = 5
_CD_COMPRESS_TYPE = 6
_CD_TIME = 7
_CD_DATE = 8
_CD_CRC = 9
_CD_COMPRESSED_SIZE = 10
_CD_UNCOMPRESSED_SIZE = 11
_CD_FILENAME_LENGTH = 12
_CD_EXTRA_FIELD_LENGTH = 13
_CD_COMMENT_LENGTH = 14
_CD_DISK_NUMBER_START = 15
_CD_INTERNAL_FILE_ATTRIBUTES = 16
_CD_EXTERNAL_FILE_ATTRIBUTES = 17
_CD_LOCAL_HEADER_OFFSET = 18
_MASK_ENCRYPTED = 1
_MASK_COMPRESS_OPTION_1 = 2
_MASK_USE_DATA_DESCRIPTOR = 8
_MASK_COMPRESSED_PATCH = 32
_MASK_STRONG_ENCRYPTION = 64
_MASK_UTF_FILENAME = 2048
structFileHeader = '<4s2B4HL2L2H'
stringFileHeader = b'PK\x03\x04'
sizeFileHeader = struct.calcsize(structFileHeader)
_FH_SIGNATURE = 0
_FH_EXTRACT_VERSION = 1
_FH_EXTRACT_SYSTEM = 2
_FH_GENERAL_PURPOSE_FLAG_BITS = 3
_FH_COMPRESSION_METHOD = 4
_FH_LAST_MOD_TIME = 5
_FH_LAST_MOD_DATE = 6
_FH_CRC = 7
_FH_COMPRESSED_SIZE = 8
_FH_UNCOMPRESSED_SIZE = 9
_FH_FILENAME_LENGTH = 10
_FH_EXTRA_FIELD_LENGTH = 11
structEndArchive64Locator = '<4sLQL'
stringEndArchive64Locator = b'PK\x06\x07'
sizeEndCentDir64Locator = struct.calcsize(structEndArchive64Locator)
structEndArchive64 = '<4sQ2H2L4Q'
stringEndArchive64 = b'PK\x06\x06'
sizeEndCentDir64 = struct.calcsize(structEndArchive64)
_CD64_SIGNATURE = 0
_CD64_DIRECTORY_RECSIZE = 1
_CD64_CREATE_VERSION = 2
_CD64_EXTRACT_VERSION = 3
_CD64_DISK_NUMBER = 4
_CD64_DISK_NUMBER_START = 5
_CD64_NUMBER_ENTRIES_THIS_DISK = 6
_CD64_NUMBER_ENTRIES_TOTAL = 7
_CD64_DIRECTORY_SIZE = 8
_CD64_OFFSET_START_CENTDIR = 9
_DD_SIGNATURE = 134695760
_EXTRA_FIELD_STRUCT = struct.Struct('<HH')

def _strip_extra(extra, xids):
    unpack = _EXTRA_FIELD_STRUCT.unpack
    modified = False
    buffer = []
    start = 0
    i = 0
# WARNING: Decompyle incomplete


def _check_zipfile(fp):
    
    try:
        if _EndRecData(fp):
            return True
    except OSError:
        pass

    return False


def is_zipfile(filename):
    '''Quickly see if a file is a ZIP file by checking the magic number.

    The filename argument may be a file or file-like object too.
    '''
    result = False
    
    try:
        if hasattr(filename, 'read'):
            result = _check_zipfile(fp = filename)
        else:
            fp = open(filename, 'rb')
            result = _check_zipfile(fp)
            
            try:
                None(None, None)
            with None:
                if not None:
                    
                    try:
                        
                        try:
                            pass
                        except OSError:
                            pass

                        return result





def _EndRecData64(fpin, offset, endrec):
    '''
    Read the ZIP64 end-of-archive records and use that to update endrec
    '''
    
    try:
        fpin.seek(offset - sizeEndCentDir64Locator, 2)
    except OSError:
        return 

    if len(data) != sizeEndCentDir64Locator:
        return endrec
    (sig, diskno, reloff, disks) = fpin.read(sizeEndCentDir64Locator).unpack(structEndArchive64Locator, data)
    if sig != stringEndArchive64Locator:
        return endrec
    if None != 0 or disks > 1:
        raise BadZipFile('zipfiles that span multiple disks are not supported')
    fpin.seek(offset - sizeEndCentDir64Locator - sizeEndCentDir64, 2)
    data = fpin.read(sizeEndCentDir64)
    if len(data) != sizeEndCentDir64:
        return endrec
    (sig, sz, create_version, read_version, disk_num, disk_dir, dircount, dircount2, dirsize, diroffset) = None.unpack(structEndArchive64, data)
    if sig != stringEndArchive64:
        return endrec
    endrec[_ECD_SIGNATURE] = None
    endrec[_ECD_DISK_NUMBER] = disk_num
    endrec[_ECD_DISK_START] = disk_dir
    endrec[_ECD_ENTRIES_THIS_DISK] = dircount
    endrec[_ECD_ENTRIES_TOTAL] = dircount2
    endrec[_ECD_SIZE] = dirsize
    endrec[_ECD_OFFSET] = diroffset
    return endrec


def _EndRecData(fpin):
    '''Return data from the "End of Central Directory" record, or None.

    The data is a list of the nine items in the ZIP "End of central dir"
    record followed by a tenth item, the file seek offset of this record.'''
    fpin.seek(0, 2)
    filesize = fpin.tell()
    
    try:
        fpin.seek(-sizeEndCentDir, 2)
    except OSError:
        return None

    data = fpin.read()
    if len(data) == sizeEndCentDir and data[0:4] == stringEndArchive and data[-2:] == b'\x00\x00':
        endrec = struct.unpack(structEndArchive, data)
        endrec = list(endrec)
        endrec.append(b'')
        endrec.append(filesize - sizeEndCentDir)
        return _EndRecData64(fpin, -sizeEndCentDir, endrec)
    maxCommentStart = None(filesize - 65536 - sizeEndCentDir, 0)
    fpin.seek(maxCommentStart, 0)
    data = fpin.read()
    start = data.rfind(stringEndArchive)
    if start >= 0:
        recData = data[start:start + sizeEndCentDir]
        if len(recData) != sizeEndCentDir:
            return None
        endrec = None(struct.unpack(structEndArchive, recData))
        commentSize = endrec[_ECD_COMMENT_SIZE]
        comment = data[start + sizeEndCentDir:start + sizeEndCentDir + commentSize]
        endrec.append(comment)
        endrec.append(maxCommentStart + start)
        return _EndRecData64(fpin, maxCommentStart + start - filesize, endrec)


class ZipInfo(object):
    '''Class with attributes describing each file in the ZIP archive.'''
    __slots__ = ('orig_filename', 'filename', 'date_time', 'compress_type', '_compresslevel', 'comment', 'extra', 'create_system', 'create_version', 'extract_version', 'reserved', 'flag_bits', 'volume', 'internal_attr', 'external_attr', 'header_offset', 'CRC', 'compress_size', 'file_size', '_raw_time', '_end_offset')
    
    def __init__(self, filename, date_time = ('NoName', (1980, 1, 1, 0, 0, 0))):
        self.orig_filename = filename
        null_byte = filename.find(chr(0))
        if null_byte >= 0:
            filename = filename[0:null_byte]
        if os.sep != '/' and os.sep in filename:
            filename = filename.replace(os.sep, '/')
        self.filename = filename
        self.date_time = date_time
        if date_time[0] < 1980:
            raise ValueError('ZIP does not support timestamps before 1980')
        self.compress_type = ZIP_STORED
        self._compresslevel = None
        self.comment = b''
        self.extra = b''
        if sys.platform == 'win32':
            self.create_system = 0
        else:
            self.create_system = 3
        self.create_version = DEFAULT_VERSION
        self.extract_version = DEFAULT_VERSION
        self.reserved = 0
        self.flag_bits = 0
        self.volume = 0
        self.internal_attr = 0
        self.external_attr = 0
        self.compress_size = 0
        self.file_size = 0
        self._end_offset = None

    
    def __repr__(self):
        result = [
            f'''<{self.__class__.__name__!s} filename={self.filename!r}''']
        if self.compress_type != ZIP_STORED:
            result.append(' compress_type=%s' % compressor_names.get(self.compress_type, self.compress_type))
        hi = self.external_attr >> 16
        lo = self.external_attr & 65535
        if hi:
            result.append(' filemode=%r' % stat.filemode(hi))
        if lo:
            result.append(' external_attr=%#x' % lo)
        isdir = self.is_dir()
        if isdir or self.file_size:
            result.append(' file_size=%r' % self.file_size)
        if isdir or self.compress_size:
            if self.compress_type != ZIP_STORED or self.file_size != self.compress_size:
                result.append(' compress_size=%r' % self.compress_size)
        result.append('>')
        return ''.join(result)

    
    def FileHeader(self, zip64 = (None,)):
        '''Return the per-file header as a bytes object.

        When the optional zip64 arg is None rather than a bool, we will
        decide based upon the file_size and compress_size, if known,
        False otherwise.
        '''
        dt = self.date_time
        dosdate = dt[0] - 1980 << 9 | dt[1] << 5 | dt[2]
        dostime = dt[3] << 11 | dt[4] << 5 | dt[5] // 2
        if self.flag_bits & _MASK_USE_DATA_DESCRIPTOR:
            CRC = 0
            compress_size = 0
            file_size = 0
        else:
            CRC = self.CRC
            compress_size = self.compress_size
            file_size = self.file_size
        extra = self.extra
        min_version = 0
    # WARNING: Decompyle incomplete

    
    def _encodeFilenameFlags(self):
        
        try:
            return (self.filename.encode('ascii'), self.flag_bits)
        except UnicodeEncodeError:
            return 


    
    def _decodeExtra(self):
        extra = self.extra
        unpack = struct.unpack
    # WARNING: Decompyle incomplete

    from_file = (lambda cls = classmethod, filename = (None,), arcname = {
        'strict_timestamps': True }, *, strict_timestamps, st = None, isdir = None: if isinstance(filename, os.PathLike):
filename = os.fspath(filename)st = os.stat(filename)isdir = stat.S_ISDIR(st.st_mode)mtime = time.localtime(st.st_mtime)date_time = mtime[0:6]if strict_timestamps and date_time[0] < 1980:
date_time = (1980, 1, 1, 0, 0, 0)elif strict_timestamps and date_time[0] > 2107:
date_time = (2107, 12, 31, 23, 59, 59)# WARNING: Decompyle incomplete
)()
    
    def is_dir(self):
        '''Return True if this archive member is a directory.'''
        return self.filename[-1] == '/'


_crctable = None

def _gen_crc(crc):
    for j in range(8):
        if crc & 1:
            crc = crc >> 1 ^ 0xEDB88320
            continue
        crc >>= 1
        return crc


def _ZipDecrypter(pwd):
    pass
# WARNING: Decompyle incomplete


class LZMACompressor:
    
    def __init__(self):
        self._comp = None

    
    def _init(self):
        props = lzma._encode_filter_properties({
            'id': lzma.FILTER_LZMA1 })
        self._comp = lzma.LZMACompressor(lzma.FORMAT_RAW, filters = [
            lzma._decode_filter_properties(lzma.FILTER_LZMA1, props)])
        return struct.pack('<BBH', 9, 4, len(props)) + props

    
    def compress(self, data):
        pass
    # WARNING: Decompyle incomplete

    
    def flush(self):
        pass
    # WARNING: Decompyle incomplete



class LZMADecompressor:
    
    def __init__(self):
        self._decomp = None
        self._unconsumed = b''
        self.eof = False

    
    def decompress(self, data):
        pass
    # WARNING: Decompyle incomplete


# WARNING: Decompyle incomplete
