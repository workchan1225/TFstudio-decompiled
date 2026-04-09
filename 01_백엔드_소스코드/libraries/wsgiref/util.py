# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

'''Miscellaneous WSGI-related Utilities'''
import posixpath
__all__ = [
    'FileWrapper',
    'guess_scheme',
    'application_uri',
    'request_uri',
    'shift_path_info',
    'setup_testing_defaults']

class FileWrapper:
    '''Wrapper to convert file-like objects to iterables'''
    
    def __init__(self, filelike, blksize = (8192,)):
        self.filelike = filelike
        self.blksize = blksize
        if hasattr(filelike, 'close'):
            self.close = filelike.close
            return None

    
    def __iter__(self):
        return self

    
    def __next__(self):
        data = self.filelike.read(self.blksize)
        if data:
            return data
        raise None



def guess_scheme(environ):
    """Return a guess for whether 'wsgi.url_scheme' should be 'http' or 'https'
    """
    if environ.get('HTTPS') in ('yes', 'on', '1'):
        return 'https'


def application_uri(environ):
