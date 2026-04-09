# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: unicode_utils.pyc (Python 3.11)

import unicodedata
import sys

def decompose(path):
    if isinstance(path, str):
        return unicodedata.normalize('NFD', path)
    
    try:
        path = path.decode('utf-8')
        path = unicodedata.normalize('NFD', path)
        path = path.encode('utf-8')
    except UnicodeError:
        pass

    return path


def filesys_decode(path):
    '''
    Ensure that the given path is decoded,
    NONE when no expected encoding works
    '''
    if isinstance(path, str):
        return path
    if not None.getfilesystemencoding():
        fs_enc = 'utf-8'
        candidates = (fs_enc, 'utf-8')
        for enc in candidates:
            
            return None, path.decode(enc)
            except UnicodeDecodeError:
                continue
            return None


def try_encode(string, enc):
    '''turn unicode encoding into a functional routine'''
    
    try:
        return string.encode(enc)
    except UnicodeEncodeError:
        return None
