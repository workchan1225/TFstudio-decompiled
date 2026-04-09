# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: formdata.pyc (Python 3.11)

import io
import warnings
from typing import Any, Iterable, List, Optional
from urllib.parse import urlencode
from multidict import MultiDict, MultiDictProxy
from  import hdrs, multipart, payload
from helpers import guess_filename
from payload import Payload
__all__ = ('FormData',)

class FormData:
    '''Helper class for form body generation.

    Supports multipart/form-data and application/x-www-form-urlencoded.
    '''
    
    def __init__(self = None, fields = None, quote_fields = None, charset = None, *, default_to_multipart):
        self._writer = multipart.MultipartWriter('form-data')
        self._fields = []
        self._is_multipart = default_to_multipart
        self._quote_fields = quote_fields
        self._charset = charset
        if isinstance(fields, dict):
            fields = list(fields.items())
        elif not isinstance(fields, (list, tuple)):
            fields = (fields,)
    # WARNING: Decompyle incomplete

    is_multipart = (lambda self = None: self._is_multipart)()
    
    def add_field(self = None, name = None, value = None, *, content_type, filename, content_transfer_encoding):
        if isinstance(value, io.IOBase):
            self._is_multipart = True
    # WARNING: Decompyle incomplete

    
    def add_fields(self = None, *fields):
        to_add = list(fields)
    # WARNING: Decompyle incomplete

    
    def _gen_form_urlencoded(self = None):
        data = []
    # WARNING: Decompyle incomplete

    
    def _gen_form_data(self = None):
        '''Encode a list of fields using the multipart/form-data MIME format'''
        for dispparams, headers, value in self._fields:
            if hdrs.CONTENT_TYPE in headers:
                part = payload.get_payload(value, content_type = headers[hdrs.CONTENT_TYPE], headers = headers, encoding = self._charset)
            else:
                part = payload.get_payload(value, headers = headers, encoding = self._charset)
        except Exception:
            exc = None
            raise TypeError(f'''Can not serialize value type: {type(value)!r}\n headers: {headers!r}\n value: {value!r}'''), exc
            exc = None
            del exc
    # WARNING: Decompyle incomplete

    
    def __call__(self = None):
        if self._is_multipart:
            return self._gen_form_data()
        return None._gen_form_urlencoded()
