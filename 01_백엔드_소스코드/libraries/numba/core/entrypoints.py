# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: entrypoints.pyc (Python 3.11)

import logging
import warnings
from importlib import metadata as importlib_metadata
_already_initialized = False
logger = logging.getLogger(__name__)

def init_all():
    '''Execute all `numba_extensions` entry points with the name `init`

    If extensions have already been initialized, this function does nothing.
    '''
    global _already_initialized
    if _already_initialized:
        return None
    _already_initialized = None
    
    def load_ep(entry_point):
        '''Loads a given entry point. Warns and logs on failure.
        '''
        logger.debug('Loading extension: %s', entry_point)
        
        try:
            func = entry_point.load()
            func()
            return None
        except Exception:
            e = None
            msg = f'''Numba extension module \'{entry_point.module}\' failed to load due to \'{type(e).__name__}({str(e)})\'.'''
            warnings.warn(msg, stacklevel = 3)
            logger.debug('Extension loading failed for: %s', entry_point)
            e = None
            del e
            return None
            e = None
            del e


    eps = importlib_metadata.entry_points()
    if hasattr(eps, 'select'):
        for entry_point in eps.select(group = 'numba_extensions', name = 'init'):
            load_ep(entry_point)
            return None
            for entry_point in eps.get('numba_extensions', ()):
                if entry_point.name == 'init':
                    load_ep(entry_point)
                return None
