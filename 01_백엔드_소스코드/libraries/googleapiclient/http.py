# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: http.pyc (Python 3.11)

'''Classes to encapsulate a single HTTP request.

The classes implement a command pattern, with every
object supporting an execute() method that does the
actual HTTP request.
'''
from __future__ import absolute_import
__author__ = 'jcgregorio@google.com (Joe Gregorio)'
import copy
from http.client import client as http_client
import io
import json
import logging
import mimetypes
import os
import random
import socket
import time
import urllib
import uuid
import httplib2

try:
    import ssl
    _ssl_SSLError = ssl.SSLError
except ImportError:
    _ssl_SSLError = object()

from email.generator import Generator
from email.mime.multipart import MIMEMultipart
from email.mime.nonmultipart import MIMENonMultipart
from email.parser import FeedParser
from googleapiclient import _auth
from googleapiclient import _helpers as util
from googleapiclient.errors import BatchError, HttpError, InvalidChunkSizeError, ResumableUploadError, UnexpectedBodyError, UnexpectedMethodError
from googleapiclient.model import JsonModel
LOGGER = logging.getLogger(__name__)
DEFAULT_CHUNK_SIZE = 104857600
MAX_URI_LENGTH = 2048
MAX_BATCH_LIMIT = 1000
_TOO_MANY_REQUESTS = 429
DEFAULT_HTTP_TIMEOUT_SEC = 60
_LEGACY_BATCH_URI = 'https://www.googleapis.com/batch'

def _should_retry_response(resp_status, content):
    '''Determines whether a response should be retried.

    Args:
      resp_status: The response status received.
      content: The response content body.

    Returns:
      True if the response should be retried, otherwise False.
    '''
    pass
# WARNING: Decompyle incomplete


def _retry_request(http, num_retries, req_type, sleep, rand, uri, method, *args, **kwargs):
    '''Retries an HTTP request multiple times while handling errors.

    If after all retries the request still fails, last error is either returned as
    return value (for HTTP 5xx errors) or thrown (for ssl.SSLError).

    Args:
      http: Http object to be used to execute request.
      num_retries: Maximum number of retries.
      req_type: Type of the request (used for logging retries).
      sleep, rand: Functions to sleep for random time between retries.
      uri: URI to be requested.
      method: HTTP method to be used.
      args, kwargs: Additional arguments passed to http.request.

    Returns:
      resp, content - Response from the http request (may be HTTP 5xx).
    '''
    resp = None
    content = None
    exception = None
# WARNING: Decompyle incomplete


class MediaUploadProgress(object):
    '''Status of a resumable upload.'''
    
    def __init__(self, resumable_progress, total_size):
        """Constructor.

        Args:
          resumable_progress: int, bytes sent so far.
          total_size: int, total bytes in complete upload, or None if the total
            upload size isn't known ahead of time.
        """
        self.resumable_progress = resumable_progress
        self.total_size = total_size

    
    def progress(self):
        '''Percent of upload completed, as a float.

        Returns:
          the percentage complete as a float, returning 0.0 if the total size of
          the upload is unknown.
        '''
        pass
    # WARNING: Decompyle incomplete



class MediaDownloadProgress(object):
    '''Status of a resumable download.'''
    
    def __init__(self, resumable_progress, total_size):
        '''Constructor.

        Args:
          resumable_progress: int, bytes received so far.
          total_size: int, total bytes in complete download.
        '''
        self.resumable_progress = resumable_progress
        self.total_size = total_size

    
    def progress(self):
        '''Percent of download completed, as a float.

        Returns:
          the percentage complete as a float, returning 0.0 if the total size of
          the download is unknown.
        '''
        pass
    # WARNING: Decompyle incomplete



class MediaUpload(object):
    """Describes a media object to upload.

    Base class that defines the interface of MediaUpload subclasses.

    Note that subclasses of MediaUpload may allow you to control the chunksize
    when uploading a media object. It is important to keep the size of the chunk
    as large as possible to keep the upload efficient. Other factors may influence
    the size of the chunk you use, particularly if you are working in an
    environment where individual HTTP requests may have a hardcoded time limit,
    such as under certain classes of requests under Google App Engine.

    Streams are io.Base compatible objects that support seek(). Some MediaUpload
    subclasses support using streams directly to upload data. Support for
    streaming may be indicated by a MediaUpload sub-class and if appropriate for a
    platform that stream will be used for uploading the media object. The support
    for streaming is indicated by has_stream() returning True. The stream() method
    should return an io.Base object that supports seek(). On platforms where the
    underlying httplib module supports streaming, for example Python 2.6 and
    later, the stream will be passed into the http library which will result in
    less memory being used and possibly faster uploads.

    If you need to upload media that can't be uploaded using any of the existing
    MediaUpload sub-class then you can sub-class MediaUpload for your particular
    needs.
    """
    
    def chunksize(self):
        '''Chunk size for resumable uploads.

        Returns:
          Chunk size in bytes.
        '''
        raise NotImplementedError()

    
    def mimetype(self):
        '''Mime type of the body.

        Returns:
          Mime type.
        '''
        return 'application/octet-stream'

    
    def size(self):
        '''Size of upload.

        Returns:
          Size of the body, or None of the size is unknown.
        '''
        pass

    
    def resumable(self):
        '''Whether this upload is resumable.

        Returns:
          True if resumable upload or False.
        '''
        return False

    
    def getbytes(self, begin, end):
        '''Get bytes from the media.

        Args:
          begin: int, offset from beginning of file.
          length: int, number of bytes to read, starting at begin.

        Returns:
          A string of bytes read. May be shorter than length if EOF was reached
          first.
        '''
        raise NotImplementedError()

    
    def has_stream(self):
        '''Does the underlying upload support a streaming interface.

        Streaming means it is an io.IOBase subclass that supports seek, i.e.
        seekable() returns True.

        Returns:
          True if the call to stream() will return an instance of a seekable io.Base
          subclass.
        '''
        return False

    
    def stream(self):
        '''A stream interface to the data being uploaded.

        Returns:
          The returned value is an io.IOBase subclass that supports seek, i.e.
          seekable() returns True.
        '''
        raise NotImplementedError()

    _to_json = (lambda self, strip = (None,): t = type(self)d = copy.copy(self.__dict__)# WARNING: Decompyle incomplete
)()
    
    def to_json(self):
        '''Create a JSON representation of an instance of MediaUpload.

        Returns:
           string, a JSON representation of this instance, suitable to pass to
           from_json().
        '''
        return self._to_json()

    new_from_json = (lambda cls, s: data = json.loads(s)module = data['_module']m = __import__(module, fromlist = module.split('.')[:-1])kls = getattr(m, data['_class'])from_json = getattr(kls, 'from_json')from_json(s))()


class MediaIoBaseUpload(MediaUpload):
    pass
# WARNING: Decompyle incomplete


class MediaFileUpload(MediaIoBaseUpload):
    pass
# WARNING: Decompyle incomplete


class MediaInMemoryUpload(MediaIoBaseUpload):
    pass
# WARNING: Decompyle incomplete


class MediaIoBaseDownload(object):
    ''' "Download media resources.

    Note that the Python file object is compatible with io.Base and can be used
    with this class also.


    Example:
      request = farms.animals().get_media(id=\'cow\')
      fh = io.FileIO(\'cow.png\', mode=\'wb\')
      downloader = MediaIoBaseDownload(fh, request, chunksize=1024*1024)

      done = False
      while done is False:
        status, done = downloader.next_chunk()
        if status:
          print "Download %d%%." % int(status.progress() * 100)
      print "Download Complete!"
    '''
    __init__ = (lambda self, fd, request, chunksize = (DEFAULT_CHUNK_SIZE,): self._fd = fdself._request = requestself._uri = request.uriself._chunksize = chunksizeself._progress = 0self._total_size = Noneself._done = Falseself._sleep = time.sleepself._rand = random.randomself._headers = { }for k, v in request.headers.items():
if k.lower() not in ('accept', 'accept-encoding', 'user-agent'):
self._headers[k] = vNone)()
    next_chunk = (lambda self, num_retries = (0,): headers = self._headers.copy()headers['range'] = 'bytes=%d-%d' % (self._progress, self._progress + self._chunksize - 1)http = self._request.http(resp, content) = _retry_request(http, num_retries, 'media download', self._sleep, self._rand, self._uri, 'GET', headers = headers)# WARNING: Decompyle incomplete
)()


class _StreamSlice(object):
    '''Truncated stream.

    Takes a stream and presents a stream that is a slice of the original stream.
    This is used when uploading media in chunks. In later versions of Python a
    stream can be passed to httplib in place of the string of data to send. The
    problem is that httplib just blindly reads to the end of the stream. This
    wrapper presents a virtual stream that only reads to the end of the chunk.
    '''
    
    def __init__(self, stream, begin, chunksize):
        '''Constructor.

        Args:
          stream: (io.Base, file object), the stream to wrap.
          begin: int, the seek position the chunk begins at.
          chunksize: int, the size of the chunk.
        '''
        self._stream = stream
        self._begin = begin
        self._chunksize = chunksize
        self._stream.seek(begin)

    
    def read(self, n = (-1,)):
        """Read n bytes.

        Args:
          n, int, the number of bytes to read.

        Returns:
          A string of length 'n', or less if EOF is reached.
        """
        cur = self._stream.tell()
        end = self._begin + self._chunksize
        if n == -1 or cur + n > end:
            n = end - cur
        return self._stream.read(n)



class HttpRequest(object):
    '''Encapsulates a single HTTP request.'''
    __init__ = (lambda self, http, postproc, uri, method, body, headers, methodId, resumable = ('GET', None, None, None, None):
