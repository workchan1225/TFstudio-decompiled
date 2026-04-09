# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''Mutagen aims to be an all purpose multimedia tagging library.

::

    import mutagen.[format]
    metadata = mutagen.[format].Open(filename)

``metadata`` acts like a dictionary of tags in the file. Tags are generally a
list of string-like values, but may have additional methods available
depending on tag or format. They may also be entirely different objects
for certain keys, again depending on format.
'''
from mutagen._util import MutagenError
from mutagen._file import FileType, StreamInfo, File
from mutagen._tags import Tags, Metadata, PaddingInfo
version = (1, 47, 0)
version_string = '.'.join(map(str, version))
MutagenError
FileType
StreamInfo
File
Tags
Metadata
PaddingInfo
