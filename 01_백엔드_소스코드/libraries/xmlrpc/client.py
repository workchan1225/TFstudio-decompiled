# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: client.pyc (Python 3.11)

'''
An XML-RPC client interface for Python.

The marshalling and response parser code can also be used to
implement XML-RPC servers.

Exported exceptions:

  Error          Base class for client errors
  ProtocolError  Indicates an HTTP protocol error
  ResponseError  Indicates a broken response package
  Fault          Indicates an XML-RPC fault package

Exported classes:

  ServerProxy    Represents a logical connection to an XML-RPC server

  MultiCall      Executor of boxcared xmlrpc requests
  DateTime       dateTime wrapper for an ISO 8601 string or time tuple or
                 localtime integer value to generate a "dateTime.iso8601"
                 XML-RPC value
  Binary         binary data wrapper

  Marshaller     Generate an XML-RPC params chunk from a Python data structure
  Unmarshaller   Unmarshal an XML-RPC response from incoming XML event message
  Transport      Handles an HTTP transaction to an XML-RPC server
  SafeTransport  Handles an HTTPS transaction to an XML-RPC server

Exported constants:

  (none)

Exported functions:

  getparser      Create instance of the fastest available parser & attach
                 to an unmarshalling object
  dumps          Convert an argument tuple or a Fault instance to an XML-RPC
                 request (or response, if the methodresponse option is used).
  loads          Convert an XML-RPC packet to unmarshalled data plus a method
                 name (None if not present).
'''
import base64
import sys
import time
from datetime import datetime
from decimal import Decimal
import http.client as http
import urllib.parse as urllib
from xml.parsers import expat
import errno
from io import BytesIO

try:
    import gzip
except ImportError:
    gzip = None


def escape(s):
    s = s.replace('&', '&amp;')
    s = s.replace('<', '&lt;')
    return s.replace('>', '&gt;')

__version__ = '%d.%d' % sys.version_info[:2]
MAXINT = 2147483647
MININT = -2147483648
PARSE_ERROR = -32700
SERVER_ERROR = -32600
APPLICATION_ERROR = -32500
SYSTEM_ERROR = -32400
TRANSPORT_ERROR = -32300
NOT_WELLFORMED_ERROR = -32700
UNSUPPORTED_ENCODING = -32701
INVALID_ENCODING_CHAR = -32702
INVALID_XMLRPC = -32600
METHOD_NOT_FOUND = -32601
INVALID_METHOD_PARAMS = -32602
INTERNAL_ERROR = -32603

class Error(Exception):
    '''Base class for client errors.'''
    __str__ = object.__str__


class ProtocolError(Error):
    '''Indicates an HTTP protocol error.'''
    
    def __init__(self, url, errcode, errmsg, headers):
        Error.__init__(self)
        self.url = url
        self.errcode = errcode
        self.errmsg = errmsg
        self.headers = headers

    
    def __repr__(self):
        return f'''<{self.__class__.__name__!s} for {self.url!s}: {self.errcode!s} {self.errmsg!s}>'''



class ResponseError(Error):
    '''Indicates a broken response package.'''
    pass


class Fault(Error):
    '''Indicates an XML-RPC fault package.'''
    
    def __init__(self, faultCode, faultString, **extra):
        Error.__init__(self)
        self.faultCode = faultCode
        self.faultString = faultString

    
    def __repr__(self):
        return f'''<{self.__class__.__name__!s} {self.faultCode!s}: {self.faultString!r}>'''


boolean = bool
Boolean = bool
_day0 = datetime(1, 1, 1)

def _try(fmt):
    
    try:
        return _day0.strftime(fmt) == '0001'
    except ValueError:
        return False


if _try('%Y'):
    
    def _iso8601_format(value):
        return value.strftime('%Y%m%dT%H:%M:%S')

elif _try('%4Y'):
    
    def _iso8601_format(value):
        return value.strftime('%4Y%m%dT%H:%M:%S')

else:
    
    def _iso8601_format(value):
        return value.strftime('%Y%m%dT%H:%M:%S').zfill(17)

del _day0
del _try

def _strftime(value):
    if isinstance(value, datetime):
        return _iso8601_format(value)
    if not None(value, (tuple, time.struct_time)):
        if value == 0:
            value = time.time()
        value = time.localtime(value)
    return '%04d%02d%02dT%02d:%02d:%02d' % value[:6]


class DateTime:
    """DateTime wrapper for an ISO 8601 string or time tuple or
    localtime integer value to generate 'dateTime.iso8601' XML-RPC
    value.
    """
    
    def __init__(self, value = (0,)):
        if isinstance(value, str):
            self.value = value
            return None
        self.value = None(value)

    
    def make_comparable(self, other):
        if isinstance(other, DateTime):
            s = self.value
            o = other.value
        elif isinstance(other, datetime):
            s = self.value
            o = _iso8601_format(other)
        elif isinstance(other, str):
            s = self.value
            o = other
        elif hasattr(other, 'timetuple'):
            s = self.timetuple()
            o = other.timetuple()
        else:
            s = self
            o = NotImplemented
        return (s, o)

    
    def __lt__(self, other):
        (s, o) = self.make_comparable(other)
        if o is NotImplemented:
            return NotImplemented
        return None < o

    
    def __le__(self, other):
        (s, o) = self.make_comparable(other)
        if o is NotImplemented:
            return NotImplemented
        return None <= o

    
    def __gt__(self, other):
        (s, o) = self.make_comparable(other)
        if o is NotImplemented:
            return NotImplemented
        return None > o

    
    def __ge__(self, other):
        (s, o) = self.make_comparable(other)
        if o is NotImplemented:
            return NotImplemented
        return None >= o

    
    def __eq__(self, other):
        (s, o) = self.make_comparable(other)
        if o is NotImplemented:
            return NotImplemented
        return None == o

    
    def timetuple(self):
        return time.strptime(self.value, '%Y%m%dT%H:%M:%S')

    
    def __str__(self):
        return self.value

    
    def __repr__(self):
        return '<%s %r at %#x>' % (self.__class__.__name__, self.value, id(self))

    
    def decode(self, data):
        self.value = str(data).strip()

    
    def encode(self, out):
        out.write('<value><dateTime.iso8601>')
        out.write(self.value)
        out.write('</dateTime.iso8601></value>\n')



def _datetime(data):
    value = DateTime()
    value.decode(data)
    return value


def _datetime_type(data):
    return datetime.strptime(data, '%Y%m%dT%H:%M:%S')


class Binary:
    '''Wrapper for binary data.'''
    
    def __init__(self, data = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self):
        return str(self.data, 'latin-1')

    
    def __eq__(self, other):
        if isinstance(other, Binary):
            other = other.data
        return self.data == other

    
    def decode(self, data):
        self.data = base64.decodebytes(data)

    
    def encode(self, out):
        out.write('<value><base64>\n')
        encoded = base64.encodebytes(self.data)
        out.write(encoded.decode('ascii'))
        out.write('</base64></value>\n')



def _binary(data):
    value = Binary()
    value.decode(data)
    return value

WRAPPERS = (DateTime, Binary)

class ExpatParser:
    
    def __init__(self, target):
        self._parser = expat.ParserCreate(None, None)
        parser = expat.ParserCreate(None, None)
        self._target = target
        parser.StartElementHandler = target.start
        parser.EndElementHandler = target.end
        parser.CharacterDataHandler = target.data
        encoding = None
        target.xml(encoding, None)

    
    def feed(self, data):
        self._parser.Parse(data, False)

    
    def close(self):
        
        try:
            parser = self._parser
            del self._target
            del self._parser
            parser.Parse(b'', True)
            return None
        except AttributeError:
            return None




class Marshaller:
    '''Generate an XML-RPC params chunk from a Python data structure.

    Create a Marshaller instance for each set of parameters, and use
    the "dumps" method to convert your data (represented as a tuple)
    to an XML-RPC params chunk.  To write a fault response, pass a
    Fault instance instead.  You may prefer to use the "dumps" module
    function for this purpose.
    '''
    
    def __init__(self, encoding, allow_none = (None, False)):
        self.memo = { }
        self.data = None
        self.encoding = encoding
        self.allow_none = allow_none

    dispatch = { }
    
    def dumps(self, values):
        out = []
        write = out.append
        dump = self.__dump
        if isinstance(values, Fault):
            write('<fault>\n')
            dump({
                'faultCode': values.faultCode,
                'faultString': values.faultString }, write)
            write('</fault>\n')
        else:
            write('<params>\n')
            for v in values:
                write('<param>\n')
                dump(v, write)
                write('</param>\n')
                write('</params>\n')
                result = ''.join(out)
                return result

    
    def __dump(self, value, write):
        
        try:
            f = self.dispatch[type(value)]
        except KeyError:
            if not hasattr(value, '__dict__'):
                raise TypeError('cannot marshal %s objects' % type(value))
            for type_ in type(value).__mro__:
                if type_ in self.dispatch.keys():
                    raise TypeError('cannot marshal %s objects' % type(value))
                f = self.dispatch['_arbitrary_instance']

        f(self, value, write)

    
    def dump_nil(self, value, write):
        if not self.allow_none:
            raise TypeError('cannot marshal None unless allow_none is enabled')
        write('<value><nil/></value>')

    dispatch[type(None)] = dump_nil
    
    def dump_bool(self, value, write):
