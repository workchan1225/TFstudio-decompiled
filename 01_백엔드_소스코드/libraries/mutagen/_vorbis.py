# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _vorbis.pyc (Python 3.11)

'''Read and write Vorbis comment data.

Vorbis comments are freeform key/value pairs; keys are
case-insensitive ASCII and values are Unicode strings. A key may have
multiple values.

The specification is at http://www.xiph.org/vorbis/doc/v-comment.html.
'''
import sys
from io import BytesIO
import mutagen
from mutagen._util import DictMixin, cdata, MutagenError, reraise

def is_valid_key(key = None):
    """Return true if a string is a valid Vorbis comment key.

    Valid Vorbis comment keys are printable ASCII between 0x20 (space)
    and 0x7D ('}'), excluding '='.

    Takes str/unicode in Python 2, unicode in Python 3
    """
    if isinstance(key, bytes):
        raise TypeError('needs to be str not bytes')
    for c in key:
        if c < ' ' and c > '}' or c == '=':
            return False
        return bool(key)

istag = is_valid_key

class error(MutagenError):
    pass


class VorbisUnsetFrameError(error):
    pass


class VorbisEncodingError(error):
    pass


class VComment(list, mutagen.Tags):
    """A Vorbis comment parser, accessor, and renderer.

    All comment ordering is preserved. A VComment is a list of
    key/value pairs, and so any Python list method can be used on it.

    Vorbis comments are always wrapped in something like an Ogg Vorbis
    bitstream or a FLAC metadata block, so this loads string data or a
    file-like object, not a filename.

    Attributes:
        vendor (text): the stream 'vendor' (i.e. writer); default 'Mutagen'
    """
    vendor = 'Mutagen ' + mutagen.version_string
    
    def __init__(self, data = (None,), *args, **kwargs):
        self._size = 0
    # WARNING: Decompyle incomplete

    
    def load(self, fileobj, errors, framing = ('replace', True)):
        """Parse a Vorbis comment from a file-like object.

        Arguments:
            errors (str): 'strict', 'replace', or 'ignore'.
                This affects Unicode decoding and how other malformed content
                is interpreted.
            framing (bool): if true, fail if a framing bit is not present

        Framing bits are required by the Vorbis comment specification,
        but are not used in FLAC Vorbis comment blocks.
        """
        
        try:
            vendor_length = cdata.uint_le(fileobj.read(4))
            self.vendor = fileobj.read(vendor_length).decode('utf-8', errors)
            count = cdata.uint_le(fileobj.read(4))
            for i in range(count):
                length = cdata.uint_le(fileobj.read(4))
                string = fileobj.read(length).decode('utf-8', errors)
                
                try:
                    pass
                except (OverflowError, MemoryError):
                    raise error('cannot read %d bytes, too large' % length)

                
                try:
                    (tag, value) = string.split('=', 1)
                    
                    try:
                        pass
                    except ValueError:
                        err = None
                        if errors == 'ignore':
                            
                            try:
                                err = None
                                del err
                                continue
                                if errors == 'replace':
                                    value = string
                                    tag = 'unknown%d' % i
                                else:
                                    reraise(VorbisEncodingError, err, sys.exc_info()[2])
                                    
                                    try:
                                        err = None
                                        del err
                                    err = None
                                    del err
                                    try:
                                        tag = tag.encode('ascii', errors)
                                        
                                        try:
                                            tag = tag.decode('ascii')
                                            if is_valid_key(tag):
                                                self.append((tag, value))
                                            continue
                                            except UnicodeEncodeError:
                                                raise VorbisEncodingError('invalid tag name %r' % tag)
                                            
                                            try:
                                                if not framing or bytearray(fileobj.read(1))[0] & 1:
                                                    raise VorbisUnsetFrameError('framing bit was unset')
                                                return None
                                                return None
                                            except (cdata.error, TypeError):
                                                raise error('file is not a valid Vorbis comment')








    
    def validate(self):
        '''Validate keys and values.

        Check to make sure every key used is a valid Vorbis key, and
        that every value used is a valid Unicode or UTF-8 string. If
        any invalid keys or values are found, a ValueError is raised.

        In Python 3 all keys and values have to be a string.
        '''
        if not isinstance(self.vendor, str):
            raise ValueError('vendor needs to be str')
        for key, value in self:
            if not is_valid_key(key):
                raise ValueError('%r is not a valid key' % key)
        except TypeError:
            raise ValueError('%r is not a valid key' % key)
        if not isinstance(value, str):
            err = f'''{value!r} needs to be str for key {key!r}'''
            raise ValueError(err)
        continue
        return True

    
    def clear(self = None):
        '''Clear all keys from the comment.'''
        for i in list(self):
            self.remove(i)
            return None

    
    def write(self, framing = (True,)):
        '''Return a string representation of the data.

        Validation is always performed, so calling this function on
        invalid data may raise a ValueError.

        Arguments:
            framing (bool): if true, append a framing bit (see load)
        '''
        self.validate()
        
        def _encode(value):
            if not isinstance(value, bytes):
                return value.encode('utf-8')

        f = BytesIO()
        vendor = _encode(self.vendor)
        f.write(cdata.to_uint_le(len(vendor)))
        f.write(vendor)
        f.write(cdata.to_uint_le(len(self)))
        for tag, value in self:
            tag = _encode(tag)
            value = _encode(value)
            comment = tag + b'=' + value
            f.write(cdata.to_uint_le(len(comment)))
            f.write(comment)
            if framing:
                f.write(b'\x01')
        return f.getvalue()

    
    def pprint(self = None):
        pass
    # WARNING: Decompyle incomplete



class VCommentDict(DictMixin, VComment):
    '''A VComment that looks like a dictionary.

    This object differs from a dictionary in two ways. First,
    len(comment) will still return the number of values, not the
    number of keys. Secondly, iterating through the object will
    iterate over (key, value) pairs, not keys. Since a key may have
    multiple values, the same value may appear multiple times while
    iterating.

    Since Vorbis comment keys are case-insensitive, all keys are
    normalized to lowercase ASCII.
    '''
    
    def __getitem__(self, key):
        """A list of values for the key.

        This is a copy, so comment['title'].append('a title') will not
        work.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def __delitem__(self, key):
        '''Delete all values associated with the key.'''
        pass
    # WARNING: Decompyle incomplete

    
    def __contains__(self, key):
        '''Return true if the key has any values.'''
        if not is_valid_key(key):
            raise ValueError
        key = key.lower()
        for k, value in self:
            if k.lower() == key:
                return True
            return False

    
    def __setitem__(self, key, values):
        """Set a key's value or values.

        Setting a value overwrites all old ones. The value may be a
        list of Unicode or UTF-8 strings, or a single Unicode or UTF-8
        string.
        """
        if isinstance(key, slice):
            return VComment.__setitem__(self, key, values)
        if not None(key):
            raise ValueError
        if not isinstance(values, list):
            values = [
                values]
        
        try:
            del self[key]
        except KeyError:
            pass

        for value in values:
            self.append((key, value))
            return None

    
    def keys(self):
        '''Return all keys in the comment.'''
        return set((lambda .0: [ k.lower() for k, v in .0 ])(self()))

    
    def as_dict(self):
        '''Return a copy of the comment data in a real dict.'''
        pass
    # WARNING: Decompyle incomplete
