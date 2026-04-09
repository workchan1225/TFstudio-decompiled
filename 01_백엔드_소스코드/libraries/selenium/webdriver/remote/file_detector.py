# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: file_detector.pyc (Python 3.11)

from abc import ABCMeta, abstractmethod
from contextlib import suppress
from pathlib import Path
from selenium.webdriver.common.utils import keys_to_typing

def FileDetector():
    '''FileDetector'''
    __doc__ = 'Identify whether a sequence of characters represents a file path.'
    is_local_file = (lambda self = None: raise NotImplementedError)()

FileDetector = <NODE:27>(FileDetector, 'FileDetector', metaclass = ABCMeta)

class UselessFileDetector(FileDetector):
    '''A file detector that never finds anything.'''
    
    def is_local_file(self = None, *keys):
        pass



class LocalFileDetector(FileDetector):
    '''Detects files on the local disk.'''
    
    def is_local_file(self = None, *keys):
        file_path = ''.join(keys_to_typing(keys))
        suppress(OSError)
        if Path(file_path).is_file():
            None(None, None)
            return 
        None(None, None)
