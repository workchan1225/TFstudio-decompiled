# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: errors.pyc (Python 3.11)

'''Errors for the library.

All exceptions defined by the library
should be defined in this file.
'''
from __future__ import absolute_import
__author__ = 'jcgregorio@google.com (Joe Gregorio)'
import json
from googleapiclient import _helpers as util

class Error(Exception):
    '''Base error for this module.'''
    pass


class HttpError(Error):
    '''HTTP data was invalid or unexpected.'''
    __init__ = (lambda self, resp, content, uri = (None,): self.resp = respif not isinstance(content, bytes):
raise TypeError('HTTP content should be bytes')self.content = contentself.uri = uriself.error_details = ''self.reason = self._get_reason())()
    status_code = (lambda self: self.resp.status)()
    
    def _get_reason(self):
        '''Calculate the reason for the error from the response content.'''
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        if self.error_details:
            return f'''<HttpError {self.resp.status!s} when requesting {self.uri!s} returned "{self.reason!s}". Details: "{self.error_details!s}">'''
        if None.uri:
            return f'''<HttpError {self.resp.status!s} when requesting {self.uri!s} returned "{self.reason!s}">'''
        return f'''{self.resp.status!s} "{self.reason!s}">'''

    __str__ = __repr__


class InvalidJsonError(Error):
    '''The JSON returned could not be parsed.'''
    pass


class UnknownFileType(Error):
    '''File type unknown or unexpected.'''
    pass


class UnknownLinkType(Error):
    '''Link type unknown or unexpected.'''
    pass


class UnknownApiNameOrVersion(Error):
    '''No API with that name and version exists.'''
    pass


class UnacceptableMimeTypeError(Error):
    '''That is an unacceptable mimetype for this operation.'''
    pass


class MediaUploadSizeError(Error):
    '''Media is larger than the method can accept.'''
    pass


class ResumableUploadError(HttpError):
    '''Error occurred during resumable upload.'''
    pass


class InvalidChunkSizeError(Error):
    '''The given chunksize is not valid.'''
    pass


class InvalidNotificationError(Error):
    '''The channel Notification is invalid.'''
    pass


class BatchError(HttpError):
    '''Error occurred during batch operations.'''
    __init__ = (lambda self, reason, resp, content = (None, None): self.resp = respself.content = contentself.reason = reason)()
    
    def __repr__(self):
        pass
    # WARNING: Decompyle incomplete

    __str__ = __repr__


class UnexpectedMethodError(Error):
    pass
# WARNING: Decompyle incomplete


class UnexpectedBodyError(Error):
    pass
# WARNING: Decompyle incomplete
