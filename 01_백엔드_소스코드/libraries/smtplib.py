# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: smtplib.pyc (Python 3.11)

'''SMTP/ESMTP client class.

This should follow RFC 821 (SMTP), RFC 1869 (ESMTP), RFC 2554 (SMTP
Authentication) and RFC 2487 (Secure SMTP over TLS).

Notes:

Please remember, when doing ESMTP, that the names of the SMTP service
extensions are NOT the same thing as the option keywords for the RCPT
and MAIL commands!

Example:

  >>> import smtplib
  >>> s=smtplib.SMTP("localhost")
  >>> print(s.help())
  This is Sendmail version 8.8.4
  Topics:
      HELO    EHLO    MAIL    RCPT    DATA
      RSET    NOOP    QUIT    HELP    VRFY
      EXPN    VERB    ETRN    DSN
  For more info use "HELP <topic>".
  To report bugs in the implementation send email to
      sendmail-bugs@sendmail.org.
  For local information send email to Postmaster at your site.
  End of HELP info
  >>> s.putcmd("vrfy","someone@here")
  >>> s.getreply()
  (250, "Somebody OverHere <somebody@here.my.org>")
  >>> s.quit()
'''
import socket
import io
import re
import email.utils as email
import email.message as email
import email.generator as email
import base64
import hmac
import copy
import datetime
import sys
from email.base64mime import body_encode as encode_base64
__all__ = [
    'SMTPException',
    'SMTPNotSupportedError',
    'SMTPServerDisconnected',
    'SMTPResponseException',
    'SMTPSenderRefused',
    'SMTPRecipientsRefused',
    'SMTPDataError',
    'SMTPConnectError',
    'SMTPHeloError',
    'SMTPAuthenticationError',
    'quoteaddr',
    'quotedata',
    'SMTP']
SMTP_PORT = 25
SMTP_SSL_PORT = 465
CRLF = '\r\n'
bCRLF = b'\r\n'
_MAXLINE = 8192
_MAXCHALLENGE = 5
OLDSTYLE_AUTH = re.compile('auth=(.*)', re.I)

class SMTPException(OSError):
    '''Base class for all exceptions raised by this module.'''
    pass


class SMTPNotSupportedError(SMTPException):
    '''The command or option is not supported by the SMTP server.

    This exception is raised when an attempt is made to run a command or a
    command with an option which is not supported by the server.
    '''
    pass


class SMTPServerDisconnected(SMTPException):
    '''Not connected to any SMTP server.

    This exception is raised when the server unexpectedly disconnects,
    or when an attempt is made to use the SMTP instance before
    connecting it to a server.
    '''
    pass


class SMTPResponseException(SMTPException):
    """Base class for all exceptions that include an SMTP error code.

    These exceptions are generated in some instances when the SMTP
    server returns an error code.  The error code is stored in the
    `smtp_code' attribute of the error, and the `smtp_error' attribute
    is set to the error message.
    """
    
    def __init__(self, code, msg):
        self.smtp_code = code
        self.smtp_error = msg
        self.args = (code, msg)



class SMTPSenderRefused(SMTPResponseException):
    """Sender address refused.

    In addition to the attributes set by on all SMTPResponseException
    exceptions, this sets `sender' to the string that the SMTP refused.
    """
    
    def __init__(self, code, msg, sender):
        self.smtp_code = code
        self.smtp_error = msg
        self.sender = sender
        self.args = (code, msg, sender)



class SMTPRecipientsRefused(SMTPException):
    """All recipient addresses refused.

    The errors for each recipient are accessible through the attribute
    'recipients', which is a dictionary of exactly the same sort as
    SMTP.sendmail() returns.
    """
    
    def __init__(self, recipients):
        self.recipients = recipients
        self.args = (recipients,)



class SMTPDataError(SMTPResponseException):
    """The SMTP server didn't accept the data."""
    pass


class SMTPConnectError(SMTPResponseException):
    '''Error during connection establishment.'''
    pass


class SMTPHeloError(SMTPResponseException):
    '''The server refused our HELO reply.'''
    pass


class SMTPAuthenticationError(SMTPResponseException):
    """Authentication error.

    Most probably the server didn't accept the username/password
    combination provided.
    """
    pass


def quoteaddr(addrstring):
    '''Quote a subset of the email addresses defined by RFC 821.

    Should be able to handle anything email.utils.parseaddr can handle.
    '''
    (displayname, addr) = email.utils.parseaddr(addrstring)
    if (displayname, addr) == ('', ''):
        if addrstring.strip().startswith('<'):
            return addrstring
        return None % addrstring
    return None % addr


def _addr_only(addrstring):
    (displayname, addr) = email.utils.parseaddr(addrstring)
    if (displayname, addr) == ('', ''):
        return addrstring


def quotedata(data):
    """Quote data for email.

    Double leading '.', and change Unix newline '\\n', or Mac '\\r' into
    internet CRLF end-of-line.
    """
    return re.sub('(?m)^\\.', '..', re.sub('(?:\\r\\n|\\n|\\r(?!\\n))', CRLF, data))


def _quote_periods(bindata):
    return re.sub(b'(?m)^\\.', b'..', bindata)


def _fix_eols(data):
    return re.sub('(?:\\r\\n|\\n|\\r(?!\\n))', CRLF, data)


try:
    import ssl
    _have_ssl = True
except ImportError:
    _have_ssl = False


class SMTP:
    """This class manages a connection to an SMTP or ESMTP server.
    SMTP Objects:
        SMTP objects have the following attributes:
            helo_resp
                This is the message given by the server in response to the
                most recent HELO command.

            ehlo_resp
                This is the message given by the server in response to the
                most recent EHLO command. This is usually multiline.

            does_esmtp
                This is a True value _after you do an EHLO command_, if the
                server supports ESMTP.

            esmtp_features
                This is a dictionary, which, if the server supports ESMTP,
                will _after you do an EHLO command_, contain the names of the
                SMTP service extensions this server supports, and their
                parameters (if any).

                Note, all extension names are mapped to lower case in the
                dictionary.

        See each method's docstrings for details.  In general, there is a
        method of the same name to perform each SMTP command.  There is also a
        method called 'sendmail' that will do an entire mail transaction.
        """
    debuglevel = 0
    sock = None
    file = None
    helo_resp = None
    ehlo_msg = 'ehlo'
    ehlo_resp = None
    does_esmtp = False
    default_port = SMTP_PORT
    
    def __init__(self, host, port, local_hostname, timeout, source_address = ('', 0, None, socket._GLOBAL_DEFAULT_TIMEOUT, None)):
        """Initialize a new instance.

        If specified, `host` is the name of the remote host to which to
        connect.  If specified, `port` specifies the port to which to connect.
        By default, smtplib.SMTP_PORT is used.  If a host is specified the
        connect method is called, and if it returns anything other than a
        success code an SMTPConnectError is raised.  If specified,
        `local_hostname` is used as the FQDN of the local host in the HELO/EHLO
        command.  Otherwise, the local hostname is found using
        socket.getfqdn(). The `source_address` parameter takes a 2-tuple (host,
        port) for the socket to bind to as its source address before
        connecting. If the host is '' and port is 0, the OS default behavior
        will be used.

        """
        self._host = host
        self.timeout = timeout
        self.esmtp_features = { }
        self.command_encoding = 'ascii'
        self.source_address = source_address
        self._auth_challenge_count = 0
        if host:
            (code, msg) = self.connect(host, port)
            if code != 220:
                self.close()
                raise SMTPConnectError(code, msg)
    # WARNING: Decompyle incomplete

    
    def __enter__(self):
        return self

    
    def __exit__(self, *args):
        
        try:
            (code, message) = self.docmd('QUIT')
            if code != 221:
                raise SMTPResponseException(code, message)
            
            try:
                pass
            except SMTPServerDisconnected:
                
                try:
                    pass
                try:
                    self.close()
                    return None
                except:
                    self.close()




    
    def set_debuglevel(self, debuglevel):
        '''Set the debug output level.

        A non-false value results in debug messages for connection and for all
        messages sent to and received from the server.

        '''
        self.debuglevel = debuglevel

    
    def _print_debug(self, *args):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_socket(self, host, port, timeout):
        pass
    # WARNING: Decompyle incomplete

    
    def connect(self, host, port, source_address = ('localhost', 0, None)):
        """Connect to a host on a given port.

        If the hostname ends with a colon (`:') followed by a number, and
        there is no port specified, that suffix will be stripped off and the
        number interpreted as the port number to use.

        Note: This method is automatically invoked by __init__, if a host is
        specified during instantiation.

        """
        if source_address:
            self.source_address = source_address
        if port and host.find(':') == host.rfind(':'):
            i = host.rfind(':')
            if i >= 0:
                port = host[i + 1:]
                host = host[:i]
                
                try:
                    port = int(port)
                except ValueError:
                    raise OSError('nonnumeric port')

                if not port:
                    port = self.default_port
        sys.audit('smtplib.connect', self, host, port)
        self.sock = self._get_socket(host, port, self.timeout)
        self.file = None
        (code, msg) = self.getreply()
        if self.debuglevel > 0:
            self._print_debug('connect:', repr(msg))
        return (code, msg)

    
    def send(self, s):
        """Send `s' to the server."""
        if self.debuglevel > 0:
            self._print_debug('send:', repr(s))
        if self.sock:
            if isinstance(s, str):
                s = s.encode(self.command_encoding)
            sys.audit('smtplib.send', self, s)
            
            try:
                self.sock.sendall(s)
                return None
            except OSError:
                self.close()
                raise SMTPServerDisconnected('Server not connected')
                raise SMTPServerDisconnected('please run connect() first')


    
    def putcmd(self, cmd, args = ('',)):
        '''Send a command to the server.'''
        if args == '':
            s = cmd
        else:
            s = f'''{cmd} {args}'''
        if '\r' in s or '\n' in s:
            s = s.replace('\n', '\\n').replace('\r', '\\r')
            raise ValueError(f'''command and arguments contain prohibited newline characters: {s}''')
        self.send(f'''{s}{CRLF}''')

    
    def getreply(self):
        """Get a reply from the server.

        Returns a tuple consisting of:

          - server response code (e.g. '250', or such, if all goes well)
            Note: returns -1 if it can't read response code.

          - server response string corresponding to response code (multiline
            responses are converted to a single, multiline string).

        Raises SMTPServerDisconnected if end-of-file is reached.
        """
        resp = []
    # WARNING: Decompyle incomplete

    
    def docmd(self, cmd, args = ('',)):
        '''Send a command, and return its response code.'''
        self.putcmd(cmd, args)
        return self.getreply()

    
    def helo(self, name = ('',)):
