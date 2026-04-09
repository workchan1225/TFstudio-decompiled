# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _atom.pyc (Python 3.11)

import struct
from mutagen._util import convert_error
_CONTAINERS = [
    b'moov',
    b'udta',
    b'trak',
    b'mdia',
    b'meta',
    b'ilst',
    b'stbl',
    b'minf',
    b'moof',
    b'traf']
_SKIP_SIZE = {
    b'meta': 4 }

class AtomError(Exception):
    pass


class Atom(object):
    '''An individual atom.

    Attributes:
    children -- list child atoms (or None for non-container atoms)
    length -- length of this atom, including length and name
    datalength = -- length of this atom without length, name
    name -- four byte name of the atom, as a str
    offset -- location in the constructor-given fileobj of this atom

    This structure should only be used internally by Mutagen.
    '''
    children = None
    __init__ = (lambda self, fileobj, level = (0,): self.offset = fileobj.tell()try:
(self.length, self.name) = struct.unpack('>I4s', fileobj.read(8))except struct.error:
raise AtomError('truncated data')self._dataoffset = self.offset + 8if self.length == 1:
try:
(self.length,) = struct.unpack('>Q', fileobj.read(8))except struct.error:
raise AtomError('truncated data')if self.length < 16:
raise AtomError('64 bit atom length can only be 16 and higher')elif self.length == 0:
if level != 0:
raise AtomError('only a top-level atom can have zero length')fileobj.seek(0, 2)fileobj.tell() - self.offset = self, self._dataoffset += 8, ._dataoffsetfileobj.seek(self.offset + 8, 0)elif self.length < 8:
raise AtomError('atom length can only be 0, 1 or 8 and higher')# WARNING: Decompyle incomplete
)()
    datalength = (lambda self: self.length - self._dataoffset - self.offset)()
    
    def read(self, fileobj):
        '''Return if all data could be read and the atom payload'''
        fileobj.seek(self._dataoffset, 0)
        data = fileobj.read(self.datalength)
        return (len(data) == self.datalength, data)

    render = (lambda name, data: size = len(data) + 8if size <= 0xFFFFFFFF:
struct.pack('>I4s', size, name) + dataNone.pack('>I4sQ', 1, name, size + 8) + data)()
    
    def findall(self, name, recursive = (False,)):
        '''Recursively find all child atoms by specified name.'''
        pass
    # WARNING: Decompyle incomplete

    
    def __getitem__(self, remaining):
        """Look up a child atom, potentially recursively.

        e.g. atom['udta', 'meta'] => <Atom name='meta' ...>
        """
        if not remaining:
            return self
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        cls = self.__class__.__name__
    # WARNING: Decompyle incomplete



class Atoms(object):
    '''Root atoms in a given file.

    Attributes:
    atoms -- a list of top-level atoms as Atom objects

    This structure should only be used internally by Mutagen.
    '''
    __init__ = (lambda self, fileobj: self.atoms = []fileobj.seek(0, 2)end = fileobj.tell()fileobj.seek(0)# WARNING: Decompyle incomplete
)()
    
    def path(self, *names):
        """Look up and return the complete path of an atom.

        For example, atoms.path('moov', 'udta', 'meta') will return a
        list of three atoms, corresponding to the moov, udta, and meta
        atoms.
        """
        path = [
            self]
        for name in names:
            path.append(path[-1][(name,)])
            return path[1:]

    
    def __contains__(self, names):
        
        try:
            self[names]
        except KeyError:
            return False

        return True

    
    def __getitem__(self, names):
        """Look up a child atom.

        'names' may be a list of atoms (['moov', 'udta']) or a string
        specifying the complete path ('moov.udta').
        """
        if isinstance(names, bytes):
            names = names.split(b'.')
        for child in self.atoms:
            if child.name == names[0]:
                
                return None, child[names[1:]]
            raise KeyError('%r not found' % names[0])

    
    def __repr__(self):
        return (lambda .0: [ repr(child) for child in .0 ])(self.atoms())
