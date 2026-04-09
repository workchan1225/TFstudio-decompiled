# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ogg.pyc (Python 3.11)

'''Read and write Ogg bitstreams and pages.

This module reads and writes a subset of the Ogg bitstream format
version 0. It does *not* read or write Ogg Vorbis files! For that,
you should use mutagen.oggvorbis.

This implementation is based on the RFC 3533 standard found at
http://www.xiph.org/ogg/doc/rfc3533.txt.
'''
import struct
import sys
import zlib
from io import BytesIO
from typing import Type
from mutagen import FileType
from mutagen._util import cdata, resize_bytes, MutagenError, loadfile, seek_end, bchr, reraise
from mutagen._file import StreamInfo
from mutagen._tags import Tags

class error(MutagenError):
    '''Ogg stream parsing errors.'''
    pass


class OggPage(object):
    """A single Ogg page (not necessarily a single encoded packet).

    A page is a header of 26 bytes, followed by the length of the
    data, followed by the data.

    The constructor is given a file-like object pointing to the start
    of an Ogg page. After the constructor is finished it is pointing
    to the start of the next page.

    Attributes:
        version (`int`): stream structure version (currently always 0)
        position (`int`): absolute stream position (default -1)
        serial (`int`): logical stream serial number (default 0)
        sequence (`int`): page sequence number within logical stream
            (default 0)
        offset (`int` or `None`): offset this page was read from (default None)
        complete (`bool`): if the last packet on this page is complete
            (default True)
        packets (list[bytes]): list of raw packet data (default [])

    Note that if 'complete' is false, the next page's 'continued'
    property must be true (so set both when constructing pages).

    If a file-like object is supplied to the constructor, the above
    attributes will be filled in based on it.
    """
    version = 0
    __type_flags = 0
    position = 0
    serial = 0
    sequence = 0
    offset = None
    complete = True
    
    def __init__(self, fileobj = (None,)):
        '''Raises error, IOError, EOFError'''
        pass
    # WARNING: Decompyle incomplete

    
    def __eq__(self, other):
        '''Two Ogg pages are the same if they write the same data.'''
        
        try:
            return self.write() == other.write()
        except AttributeError:
            return False


    __hash__ = object.__hash__
    
    def __repr__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def write(self):
        '''Return a string encoding of the page header and data.

        A ValueError is raised if the data is too big to fit in a
        single page.
        '''
        data = [
            struct.pack('<4sBBqIIi', b'OggS', self.version, self.__type_flags, self.position, self.serial, self.sequence, 0)]
        lacing_data = []
        for datum in self.packets:
            (quot, rem) = divmod(len(datum), 255)
            lacing_data.append(b'\xff' * quot + bchr(rem))
            lacing_data = b''.join(lacing_data)
            if self.complete and lacing_data.endswith(b'\x00'):
                lacing_data = lacing_data[:-1]
        data.append(bchr(len(lacing_data)))
        data.append(lacing_data)
        data.extend(self.packets)
        data = b''.join(data)
        crc = ~zlib.crc32(data.translate(cdata.bitswap), -1) & 0xFFFFFFFF
        crc = cdata.to_uint_be(crc).translate(cdata.bitswap)
        data = data[:22] + crc + data[26:]
        return data

    size = (lambda self = None: size = 27for datum in self.packets:
(quot, rem) = divmod(len(datum), 255)size += quot + 1if self.complete and rem == 0:
size -= 1size += sum(map(len, self.packets))size)()
    
    def __set_flag(self, bit, val):
        mask = 1 << bit
        if val:
            return None

    continued = property((lambda self: cdata.test_bit(self.__type_flags, 0)), (lambda self, v: self.__set_flag(0, v)), doc = 'The first packet is continued from the previous page.')
    first = property((lambda self: cdata.test_bit(self.__type_flags, 1)), (lambda self, v: self.__set_flag(1, v)), doc = 'This is the first page of a logical bitstream.')
    last = property((lambda self: cdata.test_bit(self.__type_flags, 2)), (lambda self, v: self.__set_flag(2, v)), doc = 'This is the last page of a logical bitstream.')
    renumber = (lambda fileobj, serial, start: number = starttry:
page = OggPage(fileobj)if page.serial != serial:
continuefileobj.seek(-(page.size), 1)except EOFError:
Nonepage.sequence = numberfileobj.write(page.write())fileobj.seek(page.offset + page.size, 0)number += 1continue)()
    to_packets = (lambda pages, strict = (False,): serial = pages[0].serialsequence = pages[0].sequencepackets = []if strict:
if pages[0].continued:
raise ValueError('first packet is continued')if not pages[-1].complete:
raise ValueError('last packet does not complete')elif pages and pages[0].continued:
packets.append([
b''])for page in pages:
if serial != page.serial:
raise ValueError('invalid serial number in %r' % page)if sequence != page.sequence:
raise ValueError('bad sequence number in %r' % page)sequence += 1if page.packets:
if page.continued:
packets[-1].append(page.packets[0])else:
packets.append([
page.packets[0]])(lambda .0: pass# WARNING: Decompyle incomplete
)(page.packets[1:]())
            return packets()
)()
    _from_packets_try_preserve = (lambda cls, packets, old_pages: old_packets = cls.to_packets(old_pages)if (lambda .0: [ len(p) for p in .0 ]) != old_packets():
            return cls.from_packets(packets, old_pages[0].sequence)
        new_data = packets().join(packets)
        new_pages = []
    # WARNING: Decompyle incomplete
)()
    from_packets = (lambda packets, sequence, default_size, wiggle_room = (0, 4096, 2048): chunk_size = (default_size // 255) * 255pages = []page = OggPage()page.sequence = sequence# WARNING: Decompyle incomplete
)()
    replace = (lambda cls, fileobj, old_pages, new_pages: pass# WARNING: Decompyle incomplete
)()
    find_last = (lambda fileobj, serial, finishing = (False,): pass# WARNING: Decompyle incomplete
)()


class OggFileType(FileType):
    _Error: Type[error] = 'OggFileType(filething)\n\n    An generic Ogg file.\n\n    Arguments:\n        filething (filething)\n    '
    _mimes = [
        'application/ogg',
        'application/x-ogg']
    load = (lambda self, filething: fileobj = filething.fileobjtry:
self.info = self._Info(fileobj)self.tags = self._Tags(fileobj, self.info)self.info._post_tags(fileobj)Noneexcept (error, IOError):
e = Nonereraise(self._Error, e, sys.exc_info()[2])e = Nonedel eNonee = Nonedel eexcept EOFError:
raise self._Error('no appropriate stream found'))()
    delete = (lambda self, filething = (None,): fileobj = filething.fileobjself.tags.clear()try:
self.tags._inject(fileobj, (lambda x: 0))
            return None
        except error:
            e = None
            reraise(self._Error, e, sys.exc_info()[2])
            
            try:
                e = None
                del e
                return None
                e = None
                del e
                except EOFError:
                    raise self._Error('no appropriate stream found')
                
                try:
                    pass
                except IOError:
                    e = None
                    reraise(self._Error, e, sys.exc_info()[2])
                    e = None
                    del e
                    return None
                    e = None
                    del e



)()
    
    def add_tags(self):
        raise self._Error

    save = (lambda self, filething, padding = (None, None): try:
self.tags._inject(filething.fileobj, padding)Noneexcept (IOError, error):
e = Nonereraise(self._Error, e, sys.exc_info()[2])e = Nonedel eNonee = Nonedel eexcept EOFError:
raise self._Error('no appropriate stream found'))()
