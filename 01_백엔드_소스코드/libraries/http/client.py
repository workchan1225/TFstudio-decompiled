# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: client.pyc (Python 3.11)

'''HTTP/1.1 client library

<intro stuff goes here>
<other stuff, too>

HTTPConnection goes through a number of "states", which define when a client
may legally make another request or fetch the response for a particular
request. This diagram details these state transitions:

    (null)
      |
      | HTTPConnection()
      v
    Idle
      |
      | putrequest()
      v
    Request-started
      |
      | ( putheader() )*  endheaders()
      v
    Request-sent
      |\\_____________________________
      |                              | getresponse() raises
      | response = getresponse()     | ConnectionError
      v                              v
    Unread-response                Idle
    [Response-headers-read]
      |\\____________________
      |                     |
      | response.read()     | putrequest()
      v                     v
    Idle                  Req-started-unread-response
                     ______/|
                   /        |
   response.read() |        | ( putheader() )*  endheaders()
                   v        v
       Request-started    Req-sent-unread-response
                            |
                            | response.read()
                            v
                          Request-sent

This diagram presents the following rules:
  -- a second request may not be started until {response-headers-read}
  -- a response [object] cannot be retrieved until {request-sent}
  -- there is no differentiation between an unread response body and a
     partially read response body

Note: this enforcement is applied by the HTTPConnection class. The
      HTTPResponse class does not enforce this state machine, which
      implies sophisticated clients may accelerate the request/response
      pipeline. Caution should be taken, though: accelerating the states
      beyond the above pattern may imply knowledge of the server\'s
      connection-close behavior for certain requests. For example, it
      is impossible to tell whether the server will close the connection
      UNTIL the response headers have been read; this means that further
      requests cannot be placed into the pipeline until it is known that
      the server will NOT be closing the connection.

Logical State                  __state            __response
-------------                  -------            ----------
Idle                           _CS_IDLE           None
Request-started                _CS_REQ_STARTED    None
Request-sent                   _CS_REQ_SENT       None
Unread-response                _CS_IDLE           <response_class>
Req-started-unread-response    _CS_REQ_STARTED    <response_class>
Req-sent-unread-response       _CS_REQ_SENT       <response_class>
'''
import email.parser as email
import email.message as email
import errno
import http
import io
import re
import socket
import sys
import collections.abc as collections
from urllib.parse import urlsplit
__all__ = [
    'HTTPResponse',
    'HTTPConnection',
    'HTTPException',
    'NotConnected',
    'UnknownProtocol',
    'UnknownTransferEncoding',
    'UnimplementedFileMode',
    'IncompleteRead',
    'InvalidURL',
    'ImproperConnectionState',
    'CannotSendRequest',
    'CannotSendHeader',
    'ResponseNotReady',
    'BadStatusLine',
    'LineTooLong',
    'RemoteDisconnected',
    'error',
    'responses']
HTTP_PORT = 80
HTTPS_PORT = 443
_UNKNOWN = 'UNKNOWN'
_CS_IDLE = 'Idle'
_CS_REQ_STARTED = 'Request-started'
_CS_REQ_SENT = 'Request-sent'
globals().update(http.HTTPStatus.__members__)
responses = http.HTTPStatus.__members__.values()()
_MAXLINE = 65536
_MAXHEADERS = 100
_is_legal_header_name = re.compile(b'[^:\\s][^:\\r\\n]*').fullmatch
_is_illegal_header_value = re.compile(b'\\n(?![ \\t])|\\r(?![ \\t\\n])').search
_contains_disallowed_url_pchar_re = re.compile('[\x00- \x7f]')
_contains_disallowed_method_pchar_re = re.compile('[\x00-\x1f]')
_METHODS_EXPECTING_BODY = {
    'PUT',
    'POST',
    'PATCH'}

def _encode(data, name = ('data',)):
    '''Call data.encode("latin-1") but show a better error message.'''
    
    try:
        return data.encode('latin-1')
    except UnicodeEncodeError:
        err = None
        raise UnicodeEncodeError(err.encoding, err.object, err.start, err.end, f'''{name.title()!s} ({data[err.start:err.end]!r:.20}) is not valid Latin-1. Use {name!s}.encode(\'utf-8\') if you want to send it encoded in UTF-8.'''), None
        err = None
        del err



def _strip_ipv6_iface(enc_name = None):
    '''Remove interface scope from IPv6 address.'''
    (enc_name, percent, _) = enc_name.partition(b'%')
# WARNING: Decompyle incomplete


class HTTPMessage(email.message.Message):
    
    def getallmatchingheaders(self, name):
        '''Find all header lines matching a given header name.

        Look through the list of headers and find all lines matching a given
        header name (and their continuation lines).  A list of the lines is
        returned, without interpretation.  If the header does not occur, an
        empty list is returned.  If the header occurs multiple times, all
        occurrences are returned.  Case is not important in the header name.

        '''
        name = name.lower() + ':'
        n = len(name)
        lst = []
        hit = 0
        for line in self.keys():
            if line[:n].lower() == name:
                hit = 1
            elif not line[:1].isspace():
                hit = 0
            if hit:
                lst.append(line)
            return lst



def _read_headers(fp):
    '''Reads potential header lines into a list from a file pointer.

    Length of line is limited by _MAXLINE, and number of
    headers is limited by _MAXHEADERS.
    '''
    headers = []
    line = fp.readline(_MAXLINE + 1)
    if len(line) > _MAXLINE:
        raise LineTooLong('header line')
    headers.append(line)
    if len(headers) > _MAXHEADERS:
        raise HTTPException('got more than %d headers' % _MAXHEADERS)
    if line in (b'\r\n', b'\n', b''):
        pass
    
    return headers


def parse_headers(fp, _class = (HTTPMessage,)):
    '''Parses only RFC2822 headers from a file pointer.

    email Parser wants to see strings rather than bytes.
    But a TextIOWrapper around self.rfile would buffer too many bytes
    from the stream, bytes which we later need to read as bytes.
    So we read the correct bytes here, as bytes, for email Parser
    to parse.

    '''
    headers = _read_headers(fp)
    hstring = b''.join(headers).decode('iso-8859-1')
    return email.parser.Parser(_class = _class).parsestr(hstring)


class HTTPResponse(io.BufferedIOBase):
    pass
# WARNING: Decompyle incomplete


class HTTPConnection:
    _http_vsn = 11
    _http_vsn_str = 'HTTP/1.1'
    response_class = HTTPResponse
    default_port = HTTP_PORT
    auto_open = 1
    debuglevel = 0
    _is_textIO = (lambda stream: isinstance(stream, io.TextIOBase))()
    _get_content_length = (lambda body, method: pass# WARNING: Decompyle incomplete
)()
    
    def __init__(self, host, port, timeout, source_address, blocksize = (None, socket._GLOBAL_DEFAULT_TIMEOUT, None, 8192)):
        self.timeout = timeout
        self.source_address = source_address
        self.blocksize = blocksize
        self.sock = None
        self._buffer = []
        self._HTTPConnection__response = None
        self._HTTPConnection__state = _CS_IDLE
        self._method = None
        self._tunnel_host = None
        self._tunnel_port = None
        self._tunnel_headers = { }
        (self.host, self.port) = self._get_hostport(host, port)
        self._validate_host(self.host)
        self._create_connection = socket.create_connection

    
    def set_tunnel(self, host, port, headers = (None, None)):
        '''Set up host and port for HTTP CONNECT tunnelling.

        In a connection that uses HTTP CONNECT tunneling, the host passed to the
        constructor is used as a proxy server that relays all communication to
        the endpoint passed to `set_tunnel`. This done by sending an HTTP
        CONNECT request to the proxy server when the connection is established.

        This method must be called before the HTTP connection has been
        established.

        The headers argument should be a mapping of extra HTTP headers to send
        with the CONNECT request.
        '''
        if self.sock:
            raise RuntimeError("Can't set up tunnel for established connection")
        (self._tunnel_host, self._tunnel_port) = self._get_hostport(host, port)
        if headers:
            self._tunnel_headers = headers
            return None
        None._tunnel_headers.clear()

    
    def _get_hostport(self, host, port):
        pass
    # WARNING: Decompyle incomplete

    
    def set_debuglevel(self, level):
        self.debuglevel = level

    
    def _tunnel(self):
        connect = b'CONNECT %s:%d HTTP/1.0\r\n' % (self._tunnel_host.encode('ascii'), self._tunnel_port)
        headers = [
            connect]
        for header, value in self._tunnel_headers.items():
            headers.append(f'''{header}: {value}\r\n'''.encode('latin-1'))
            headers.append(b'\r\n')
            self.send(b''.join(headers))
            del headers
            response = self.response_class(self.sock, method = self._method)
            
            try:
                (version, code, message) = response._read_status()
                if code != http.HTTPStatus.OK:
                    self.close()
                    raise OSError(f'''Tunnel connection failed: {code} {message.strip()}''')
                line = response.fp.readline(_MAXLINE + 1)
                if len(line) > _MAXLINE:
                    raise LineTooLong('header line')
                if not line:
                    pass
                elif line in (b'\r\n', b'\n', b''):
                    pass
                elif self.debuglevel > 0:
                    print('header:', line.decode())
                continue
                response.close()
                return None
            except:
                response.close()


    
    def connect(self):
        '''Connect to the host and port specified in __init__.'''
        sys.audit('http.client.connect', self, self.host, self.port)
        self.sock = self._create_connection((self.host, self.port), self.timeout, self.source_address)
        
        try:
            self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        except OSError:
            e = None
            if e.errno != errno.ENOPROTOOPT:
                raise 
            e = None
            del e
        except:
            e = None
            del e

        if self._tunnel_host:
            self._tunnel()
            return None

    
    def close(self):
        '''Close the connection to the HTTP server.'''
        self._HTTPConnection__state = _CS_IDLE
        
        try:
            sock = self.sock
            if sock:
                self.sock = None
                sock.close()
            response = self._HTTPConnection__response
            if response:
                self._HTTPConnection__response = None
                response.close()
                return None
            return None
        except:
            response = self._HTTPConnection__response
            if response:
                self._HTTPConnection__response = None
                response.close()


    
    def send(self, data):
        """Send `data' to the server.
        ``data`` can be a string object, a bytes object, an array object, a
        file-like object that supports a .read() method, or an iterable object.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def _output(self, s):
        '''Add a line of output to the current request buffer.

        Assumes that the line does *not* end with \\r\\n.
        '''
        self._buffer.append(s)

    
    def _read_readable(self, readable):
        pass
    # WARNING: Decompyle incomplete

    
    def _send_output(self, message_body, encode_chunked = (None, False)):
        '''Send the currently buffered request and clear the buffer.

        Appends an extra \\r\\n to the buffer.
        A message_body may be specified, to be appended to the request.
        '''
        self._buffer.extend((b'', b''))
        msg = b'\r\n'.join(self._buffer)
        del self._buffer[:]
        self.send(msg)
    # WARNING: Decompyle incomplete

    
    def putrequest(self, method, url, skip_host, skip_accept_encoding = (False, False)):
        """Send a request to the server.

        `method' specifies an HTTP request method, e.g. 'GET'.
        `url' specifies the object being requested, e.g. '/index.html'.
        `skip_host' if True does not add automatically a 'Host:' header
        `skip_accept_encoding' if True does not add automatically an
           'Accept-Encoding:' header
        """
        if self._HTTPConnection__response and self._HTTPConnection__response.isclosed():
            self._HTTPConnection__response = None
        if self._HTTPConnection__state == _CS_IDLE:
            self._HTTPConnection__state = _CS_REQ_STARTED
        else:
            raise CannotSendRequest(self._HTTPConnection__state)
        self._validate_method(method)
        self._method = method
        if not url:
            url = '/'
            self._validate_path(url)
            request = f'''{method!s} {url!s} {self._http_vsn_str!s}'''
            self._output(self._encode_request(request))
            if self._http_vsn == 11:
                if not skip_host:
                    netloc = ''
                    if url.startswith('http'):
                        (nil, netloc, nil, nil, nil) = urlsplit(url)
                    if netloc:
                        
                        try:
                            netloc_enc = netloc.encode('ascii')
                        except UnicodeEncodeError:
                            netloc_enc = netloc.encode('idna')

                        self.putheader('Host', _strip_ipv6_iface(netloc_enc))
                    elif self._tunnel_host:
                        host = self._tunnel_host
                        port = self._tunnel_port
                    else:
                        host = self.host
                        port = self.port
                    
                    try:
                        host_enc = host.encode('ascii')
                    except UnicodeEncodeError:
                        host_enc = host.encode('idna')

                    if ':' in host:
                        host_enc = b'[' + host_enc + b']'
                        host_enc = _strip_ipv6_iface(host_enc)
                    if port == self.default_port:
                        self.putheader('Host', host_enc)
                    else:
                        host_enc = host_enc.decode('ascii')
                        self.putheader('Host', f'''{host_enc!s}:{port!s}''')
                if not skip_accept_encoding:
                    self.putheader('Accept-Encoding', 'identity')
                    return None
                return None

    
    def _encode_request(self, request):
        return request.encode('ascii')

    
    def _validate_method(self, method):
        '''Validate a method name for putrequest.'''
        match = _contains_disallowed_method_pchar_re.search(method)
        if match:
            raise ValueError(f'''method can\'t contain control characters. {method!r} (found at least {match.group()!r})''')

    
    def _validate_path(self, url):
        '''Validate a url for putrequest.'''
        match = _contains_disallowed_url_pchar_re.search(url)
        if match:
            raise InvalidURL(f'''URL can\'t contain control characters. {url!r} (found at least {match.group()!r})''')

    
    def _validate_host(self, host):
        """Validate a host so it doesn't contain control characters."""
        match = _contains_disallowed_url_pchar_re.search(host)
        if match:
            raise InvalidURL(f'''URL can\'t contain control characters. {host!r} (found at least {match.group()!r})''')

    
    def putheader(self, header, *values):
        """Send a request header line to the server.

        For example: h.putheader('Accept', 'text/html')
        """
        if self._HTTPConnection__state != _CS_REQ_STARTED:
            raise CannotSendHeader()
        if hasattr(header, 'encode'):
            header = header.encode('ascii')
        if not _is_legal_header_name(header):
            raise ValueError(f'''Invalid header name {header!r}''')
        values = list(values)
        for i, one_value in enumerate(values):
            if hasattr(one_value, 'encode'):
                values[i] = one_value.encode('latin-1')
            elif isinstance(one_value, int):
                values[i] = str(one_value).encode('ascii')
            if _is_illegal_header_value(values[i]):
                raise ValueError(f'''Invalid header value {values[i]!r}''')
            value = b'\r\n\t'.join(values)
            header = header + b': ' + value
            self._output(header)
            return None

    
    def endheaders(self = staticmethod, message_body = (None,), *, encode_chunked):
        '''Indicate that the last header line has been sent to the server.

        This method sends the request to the server.  The optional message_body
        argument can be used to pass a message body associated with the
        request.
        '''
        if self._HTTPConnection__state == _CS_REQ_STARTED:
            self._HTTPConnection__state = _CS_REQ_SENT
        else:
            raise CannotSendHeader()
        self._send_output(message_body, encode_chunked = encode_chunked)

    
    def request(self, method, url = staticmethod, body = (None, { }), headers = {
        'encode_chunked': False }, *, encode_chunked):
        '''Send a complete request to the server.'''
        self._send_request(method, url, body, headers, encode_chunked)

    
    def _send_request(self, method, url, body, headers, encode_chunked):
        header_names = (lambda .0: pass# WARNING: Decompyle incomplete
)(headers())
        skips = { }
        if 'host' in header_names:
            skips['skip_host'] = 1
        if 'accept-encoding' in header_names:
            skips['skip_accept_encoding'] = 1
    # WARNING: Decompyle incomplete

    
    def getresponse(self):
        '''Get the response from the server.

        If the HTTPConnection is in the correct state, returns an
        instance of HTTPResponse or of whatever object is returned by
        the response_class variable.

        If a request has not been sent or if a previous response has
        not be handled, ResponseNotReady is raised.  If the HTTP
        response indicates that the connection should be closed, then
        it will be closed before the response is returned.  When the
        connection is closed, the underlying socket is closed.
        '''
        if self._HTTPConnection__response and self._HTTPConnection__response.isclosed():
            self._HTTPConnection__response = None
        if self._HTTPConnection__state != _CS_REQ_SENT or self._HTTPConnection__response:
            raise ResponseNotReady(self._HTTPConnection__state)
        if self.debuglevel > 0:
            response = self.response_class(self.sock, self.debuglevel, method = self._method)
        else:
            response = self.response_class(self.sock, method = self._method)
    # WARNING: Decompyle incomplete



try:
    import ssl
    
    class HTTPSConnection(HTTPConnection):
        pass
    # WARNING: Decompyle incomplete

    __all__.append('HTTPSConnection')
except ImportError:
    pass


class HTTPException(Exception):
    pass


class NotConnected(HTTPException):
    pass


class InvalidURL(HTTPException):
    pass


class UnknownProtocol(HTTPException):
    
    def __init__(self, version):
        self.args = (version,)
        self.version = version



class UnknownTransferEncoding(HTTPException):
    pass


class UnimplementedFileMode(HTTPException):
    pass


class IncompleteRead(HTTPException):
    
    def __init__(self, partial, expected = (None,)):
        self.args = (partial,)
        self.partial = partial
        self.expected = expected

    
    def __repr__(self):
        pass
    # WARNING: Decompyle incomplete

    __str__ = object.__str__


class ImproperConnectionState(HTTPException):
    pass


class CannotSendRequest(ImproperConnectionState):
    pass


class CannotSendHeader(ImproperConnectionState):
    pass


class ResponseNotReady(ImproperConnectionState):
    pass


class BadStatusLine(HTTPException):
    
    def __init__(self, line):
        if not line:
            line = repr(line)
        self.args = (line,)
        self.line = line



class LineTooLong(HTTPException):
    
    def __init__(self, line_type):
        HTTPException.__init__(self, 'got more than %d bytes when reading %s' % (_MAXLINE, line_type))



class RemoteDisconnected(BadStatusLine, ConnectionResetError):
    
    def __init__(self, *pos, **kw):
        BadStatusLine.__init__(self, '')
    # WARNING: Decompyle incomplete


error = HTTPException
