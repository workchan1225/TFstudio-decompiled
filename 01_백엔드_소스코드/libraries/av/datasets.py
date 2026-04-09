# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: datasets.pyc (Python 3.11)

import errno
import logging
import os
import sys
from typing import Iterator
from urllib.request import urlopen
log = logging.getLogger(__name__)

def iter_data_dirs(check_writable = None):
    pass
# WARNING: Decompyle incomplete


def cached_download(url = None, name = None):
    """Download the data at a URL, and cache it under the given name.

    The file is stored under `pyav/test` with the given name in the directory
    :envvar:`PYAV_TESTDATA_DIR`, or the first that is writeable of:

    - the current virtualenv
    - ``/usr/local/share``
    - ``/usr/local/lib``
    - ``/usr/share``
    - ``/usr/lib``
    - the user's home

    """
    clean_name = os.path.normpath(name)
    if clean_name != name:
        raise ValueError(f'''{name} is not normalized.''')
    for dir_ in iter_data_dirs():
        path = os.path.join(dir_, name)
        if os.path.exists(path):
            
            return None, path
        os.path.join(dir_, name) = next(iter_data_dirs(True))
        log.info(f'''Downloading {url} to {path}''')
        response = urlopen(url)
        if response.getcode() != 200:
            raise ValueError(f'''HTTP {response.getcode()}''')
        dir_ = os.path.dirname(path)
        
        try:
            os.makedirs(dir_)
        except OSError:
            e = None
            if e.errno != errno.EEXIST:
                raise 
            e = None
            del e
        except:
            e = None
            del e

        tmp_path = path + '.tmp'
        fh = open(tmp_path, 'wb')
        chunk = response.read(8196)
        if chunk:
            fh.write(chunk)
        
    continue
    None(None, None)


def fate(name = None):
    '''Download and return a path to a sample from the FFmpeg test suite.

    Data is handled by :func:`cached_download`.

    See the `FFmpeg Automated Test Environment <https://www.ffmpeg.org/fate.html>`_

    '''
    return cached_download('http://fate.ffmpeg.org/fate-suite/' + name, os.path.join('fate-suite', name.replace('/', os.path.sep)))


def curated(name = None):
    '''Download and return a path to a sample that is curated by the PyAV developers.

    Data is handled by :func:`cached_download`.

    '''
    return cached_download('https://pyav.org/datasets/' + name, os.path.join('pyav-curated', name.replace('/', os.path.sep)))
