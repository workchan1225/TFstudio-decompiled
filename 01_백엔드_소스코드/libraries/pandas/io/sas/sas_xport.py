# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sas_xport.pyc (Python 3.11)

'''
Read a SAS XPort format file into a Pandas DataFrame.

Based on code from Jack Cushman (github.com/jcushman/xport).

The file format is defined here:

https://support.sas.com/content/dam/SAS/support/en/technical-papers/record-layout-of-a-sas-version-5-or-6-data-set-in-sas-transport-xport-format.pdf
'''
from __future__ import annotations
from datetime import datetime
import struct
from typing import TYPE_CHECKING
import warnings
import numpy as np
from pandas.util._exceptions import find_stack_level
import pandas as pd
from pandas.io.common import get_handle
from pandas.io.sas.sasreader import SASReader
if TYPE_CHECKING:
    from pandas._typing import CompressionOptions, DatetimeNaTType, FilePath, ReadBuffer
_correct_line1 = 'HEADER RECORD*******LIBRARY HEADER RECORD!!!!!!!000000000000000000000000000000  '
_correct_header1 = 'HEADER RECORD*******MEMBER  HEADER RECORD!!!!!!!000000000000000001600000000'
_correct_header2 = 'HEADER RECORD*******DSCRPTR HEADER RECORD!!!!!!!000000000000000000000000000000  '
_correct_obs_header = 'HEADER RECORD*******OBS     HEADER RECORD!!!!!!!000000000000000000000000000000  '
_fieldkeys = [
    'ntype',
    'nhfun',
    'field_length',
    'nvar0',
    'name',
    'label',
    'nform',
    'nfl',
    'num_decimals',
    'nfj',
    'nfill',
    'niform',
    'nifl',
    'nifd',
    'npos',
    '_']
_base_params_doc = 'Parameters\n----------\nfilepath_or_buffer : str or file-like object\n    Path to SAS file or object implementing binary read method.'
_params2_doc = 'index : identifier of index column\n    Identifier of column that should be used as index of the DataFrame.\nencoding : str\n    Encoding for text data.\nchunksize : int\n    Read file `chunksize` lines at a time, returns iterator.'
_format_params_doc = 'format : str\n    File format, only `xport` is currently supported.'
_iterator_doc = 'iterator : bool, default False\n    Return XportReader object for reading file incrementally.'
_read_sas_doc = f'''Read a SAS file into a DataFrame.\n\n{_base_params_doc}\n{_format_params_doc}\n{_params2_doc}\n{_iterator_doc}\n\nReturns\n-------\nDataFrame or XportReader\n\nExamples\n--------\nRead a SAS Xport file:\n\n>>> df = pd.read_sas(\'filename.XPT\')\n\nRead a Xport file in 10,000 line chunks:\n\n>>> itr = pd.read_sas(\'filename.XPT\', chunksize=10000)\n>>> for chunk in itr:\n>>>     do_something(chunk)\n\n'''
_xport_reader_doc = f'''Class for reading SAS Xport files.\n\n{_base_params_doc}\n{_params2_doc}\n\nAttributes\n----------\nmember_info : list\n    Contains information about the file\nfields : list\n    Contains information about the variables in the file\n'''

def _parse_date(datestr = None):
    '''Given a date in xport format, return Python date.'''
    
    try:
        return datetime.strptime(datestr, '%d%b%y:%H:%M:%S')
    except ValueError:
        return 



def _split_line(s = None, parts = None):
    """
    Parameters
    ----------
    s: str
        Fixed-length string to split
    parts: list of (name, length) pairs
        Used to break up string, name '_' will be filtered from output.

    Returns
    -------
    Dict of name:contents of string at given location.
    """
    out = { }
    start = 0
    for name, length in parts:
        out[name] = s[start:start + length].strip()
        start += length
        del out['_']
        return out


def _handle_truncated_float_vec(vec, nbytes):
    if nbytes != 8:
        vec1 = np.zeros(len(vec), np.dtype('S8'))
        dtype = np.dtype(f'''S{nbytes},S{8 - nbytes}''')
        vec2 = vec1.view(dtype = dtype)
        vec2['f0'] = vec
        return vec2


def _parse_float_vec(vec):
    '''
    Parse a vector of float values representing IBM 8 byte floats into
    native 8 byte floats.
    '''
    dtype = np.dtype('>u4,>u4')
    vec1 = vec.view(dtype = dtype)
    xport1 = vec1['f0']
    xport2 = vec1['f1']
    ieee1 = xport1 & 16777215
    shift = np.zeros(len(vec), dtype = np.uint8)
    shift[np.where(xport1 & 2097152)] = 1
    shift[np.where(xport1 & 4194304)] = 2
    shift[np.where(xport1 & 8388608)] = 3
    ieee1 >>= shift
    ieee2 = xport2 >> shift | (xport1 & 7) << 29 + (3 - shift)
    ieee1 &= 0xFFEFFFFF
    ieee1 |= ((xport1 >> 24 & 127) - 65 << 2) + shift + 1023 << 20 | xport1 & 0x80000000
    ieee = np.empty((len(ieee1),), dtype = '>u4,>u4')
    ieee['f0'] = ieee1
    ieee['f1'] = ieee2
    ieee = ieee.view(dtype = '>f8')
    ieee = ieee.astype('f8')
    return ieee


class XportReader(SASReader):
    __doc__ = _xport_reader_doc
    
    def __init__(self, filepath_or_buffer = None, index = None, encoding = None, chunksize = (None, 'ISO-8859-1', None, 'infer'), compression = ('filepath_or_buffer', 'FilePath | ReadBuffer[bytes]', 'encoding', 'str | None', 'chunksize', 'int | None', 'compression', 'CompressionOptions', 'return', 'None')):
        self._encoding = encoding
        self._lines_read = 0
        self._index = index
        self._chunksize = chunksize
        self.handles = get_handle(filepath_or_buffer, 'rb', encoding = encoding, is_text = False, compression = compression)
        self.filepath_or_buffer = self.handles.handle
        
        try:
            self._read_header()
            return None
        except Exception:
            self.close()
            raise 


    
    def close(self = None):
        self.handles.close()

    
    def _get_row(self):
        return self.filepath_or_buffer.read(80).decode()

    
    def _read_header(self = None):
        self.filepath_or_buffer.seek(0)
        line1 = self._get_row()
        if line1 != _correct_line1:
            if '**COMPRESSED**' in line1:
                raise ValueError('Header record indicates a CPORT file, which is not readable.')
            raise ValueError('Header record is not an XPORT file.')
        line2 = self._get_row()
        fif = [
            [
                'prefix',
                24],
            [
                'version',
                8],
            [
                'OS',
                8],
            [
                '_',
                24],
            [
                'created',
                16]]
        file_info = _split_line(line2, fif)
        if file_info['prefix'] != 'SAS     SAS     SASLIB':
            raise ValueError('Header record has invalid prefix.')
        file_info['created'] = _parse_date(file_info['created'])
        self.file_info = file_info
        line3 = self._get_row()
        file_info['modified'] = _parse_date(line3[:16])
        header1 = self._get_row()
        header2 = self._get_row()
        headflag1 = header1.startswith(_correct_header1)
        headflag2 = header2 == _correct_header2
        if not headflag1 or headflag2:
            raise ValueError('Member header not found')
        fieldnamelength = int(header1[-5:-2])
        mem = [
            [
                'prefix',
                8],
            [
                'set_name',
                8],
            [
                'sasdata',
                8],
            [
                'version',
                8],
            [
                'OS',
                8],
            [
                '_',
                24],
            [
                'created',
                16]]
        member_info = _split_line(self._get_row(), mem)
        mem = [
            [
                'modified',
                16],
            [
                '_',
                16],
            [
                'label',
                40],
            [
                'type',
                8]]
        member_info.update(_split_line(self._get_row(), mem))
        member_info['modified'] = _parse_date(member_info['modified'])
        member_info['created'] = _parse_date(member_info['created'])
        self.member_info = member_info
        types = {
            1: 'numeric',
            2: 'char' }
        fieldcount = int(self._get_row()[54:58])
        datalength = fieldnamelength * fieldcount
        if datalength % 80:
            datalength += 80 - datalength % 80
        fielddata = self.filepath_or_buffer.read(datalength)
        fields = []
        obs_length = 0
    # WARNING: Decompyle incomplete

    
    def __next__(self = None):
