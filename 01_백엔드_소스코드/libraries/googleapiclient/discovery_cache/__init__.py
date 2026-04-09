# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''Caching utility for the discovery document.'''
from __future__ import absolute_import
import logging
import os
LOGGER = logging.getLogger(__name__)
DISCOVERY_DOC_MAX_AGE = 86400
DISCOVERY_DOC_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'documents')

def autodetect():
    '''Detects an appropriate cache module and returns it.

    Returns:
      googleapiclient.discovery_cache.base.Cache, a cache object which
      is auto detected, or None if no cache object is available.
    '''
    if 'GAE_ENV' in os.environ:
        
        try:
            appengine_memcache = appengine_memcache
            import 
            return appengine_memcache.cache
        except Exception:
            pass

        
        try:
            file_cache = file_cache
            import 
            return file_cache.cache
        except Exception:
            LOGGER.info('file_cache is only supported with oauth2client<4.0.0', exc_info = False)
            return None



def get_static_doc(serviceName, version):
    '''Retrieves the discovery document from the directory defined in
    DISCOVERY_DOC_DIR corresponding to the serviceName and version provided.

    Args:
        serviceName: string, name of the service.
        version: string, the version of the service.

    Returns:
        A string containing the contents of the JSON discovery document,
        otherwise None if the JSON discovery document was not found.
    '''
    content = None
    doc_name = '{}.{}.json'.format(serviceName, version)
    
    try:
        f = open(os.path.join(DISCOVERY_DOC_DIR, doc_name), 'r')
        content = f.read()
        
        try:
            None(None, None)
        with None:
            if not None:
                
                try:
                    
                    try:
                        pass
                    except FileNotFoundError:
                        pass

                    return content
