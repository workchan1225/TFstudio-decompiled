# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: handlers.pyc (Python 3.11)

"""
Additional handlers for the logging package for Python. The core package is
based on PEP 282 and comments thereto in comp.lang.python.

Copyright (C) 2001-2021 Vinay Sajip. All Rights Reserved.

To use, simply 'import logging.handlers' and log away!
"""
import io
import logging
import socket
import os
import pickle
import struct
import time
import re
from stat import ST_DEV, ST_INO, ST_MTIME
import queue
import threading
import copy
DEFAULT_TCP_LOGGING_PORT = 9020
DEFAULT_UDP_LOGGING_PORT = 9021
DEFAULT_HTTP_LOGGING_PORT = 9022
DEFAULT_SOAP_LOGGING_PORT = 9023
SYSLOG_UDP_PORT = 514
SYSLOG_TCP_PORT = 514
_MIDNIGHT = 86400

class BaseRotatingHandler(logging.FileHandler):
    '''
    Base class for handlers that rotate log files at a certain point.
    Not meant to be instantiated directly.  Instead, use RotatingFileHandler
    or TimedRotatingFileHandler.
    '''
    namer = None
    rotator = None
    
    def __init__(self, filename, mode, encoding, delay, errors = (None, False, None)):
        '''
        Use the specified filename for streamed logging
        '''
        logging.FileHandler.__init__(self, filename, mode = mode, encoding = encoding, delay = delay, errors = errors)
        self.mode = mode
        self.encoding = encoding
        self.errors = errors

    
    def emit(self, record):
        '''
        Emit a record.

        Output the record to the file, catering for rollover as described
        in doRollover().
        '''
        
        try:
            if self.shouldRollover(record):
                self.doRollover()
            logging.FileHandler.emit(self, record)
            return None
        except Exception:
            self.handleError(record)
            return None


    
    def rotation_filename(self, default_name):
        """
        Modify the filename of a log file when rotating.

        This is provided so that a custom filename can be provided.

        The default implementation calls the 'namer' attribute of the
        handler, if it's callable, passing the default name to
        it. If the attribute isn't callable (the default is None), the name
        is returned unchanged.

        :param default_name: The default name for the log file.
        """
        if not callable(self.namer):
            result = default_name
        else:
            result = self.namer(default_name)
        return result

    
    def rotate(self, source, dest):
        """
        When rotating, rotate the current log.

        The default implementation calls the 'rotator' attribute of the
        handler, if it's callable, passing the source and dest arguments to
        it. If the attribute isn't callable (the default is None), the source
        is simply renamed to the destination.

        :param source: The source filename. This is normally the base
                       filename, e.g. 'test.log'
        :param dest:   The destination filename. This is normally
                       what the source is rotated to, e.g. 'test.log.1'.
        """
        if not callable(self.rotator):
            if os.path.exists(source):
                os.rename(source, dest)
                return None
            return None
        None.rotator(source, dest)



class RotatingFileHandler(BaseRotatingHandler):
    '''
    Handler for logging to a set of files, which switches from one file
    to the next when the current file reaches a certain size.
    '''
    
    def __init__(self, filename, mode, maxBytes, backupCount, encoding, delay, errors = ('a', 0, 0, None, False, None)):
        '''
        Open the specified file and use it as the stream for logging.

        By default, the file grows indefinitely. You can specify particular
        values of maxBytes and backupCount to allow the file to rollover at
        a predetermined size.

        Rollover occurs whenever the current log file is nearly maxBytes in
        length. If backupCount is >= 1, the system will successively create
        new files with the same pathname as the base file, but with extensions
        ".1", ".2" etc. appended to it. For example, with a backupCount of 5
        and a base file name of "app.log", you would get "app.log",
        "app.log.1", "app.log.2", ... through to "app.log.5". The file being
        written to is always "app.log" - when it gets filled up, it is closed
        and renamed to "app.log.1", and if files "app.log.1", "app.log.2" etc.
        exist, then they are renamed to "app.log.2", "app.log.3" etc.
        respectively.

        If maxBytes is zero, rollover never occurs.
        '''
        if maxBytes > 0:
            mode = 'a'
        if 'b' not in mode:
            encoding = io.text_encoding(encoding)
        BaseRotatingHandler.__init__(self, filename, mode, encoding = encoding, delay = delay, errors = errors)
        self.maxBytes = maxBytes
        self.backupCount = backupCount

    
    def doRollover(self):
        '''
        Do a rollover, as described in __init__().
        '''
        if self.stream:
            self.stream.close()
            self.stream = None
        if self.backupCount > 0:
            for i in range(self.backupCount - 1, 0, -1):
                sfn = self.rotation_filename('%s.%d' % (self.baseFilename, i))
                dfn = self.rotation_filename('%s.%d' % (self.baseFilename, i + 1))
                if os.path.exists(sfn):
                    if os.path.exists(dfn):
                        os.remove(dfn)
                    os.rename(sfn, dfn)
                dfn = self.rotation_filename(self.baseFilename + '.1')
                if os.path.exists(dfn):
                    os.remove(dfn)
            self.rotate(self.baseFilename, dfn)
        if not self.delay:
            self.stream = self._open()
            return None

    
    def shouldRollover(self, record):
        '''
        Determine if rollover should occur.

        Basically, see if the supplied record would cause the file to exceed
        the size limit we have.
        '''
        if not os.path.exists(self.baseFilename) and os.path.isfile(self.baseFilename):
            return False
    # WARNING: Decompyle incomplete



class TimedRotatingFileHandler(BaseRotatingHandler):
    '''
    Handler for logging to a file, rotating the log file at certain timed
    intervals.

    If backupCount is > 0, when rollover is done, no more than backupCount
    files are kept - the oldest ones are deleted.
    '''
    
    def __init__(self, filename, when, interval, backupCount, encoding, delay, utc, atTime, errors = ('h', 1, 0, None, False, False, None, None)):
        encoding = io.text_encoding(encoding)
        BaseRotatingHandler.__init__(self, filename, 'a', encoding = encoding, delay = delay, errors = errors)
        self.when = when.upper()
        self.backupCount = backupCount
        self.utc = utc
        self.atTime = atTime
        if self.when == 'S':
            self.interval = 1
            self.suffix = '%Y-%m-%d_%H-%M-%S'
            self.extMatch = '^\\d{4}-\\d{2}-\\d{2}_\\d{2}-\\d{2}-\\d{2}(\\.\\w+)?$'
        elif self.when == 'M':
            self.interval = 60
            self.suffix = '%Y-%m-%d_%H-%M'
            self.extMatch = '^\\d{4}-\\d{2}-\\d{2}_\\d{2}-\\d{2}(\\.\\w+)?$'
        elif self.when == 'H':
            self.interval = 3600
            self.suffix = '%Y-%m-%d_%H'
            self.extMatch = '^\\d{4}-\\d{2}-\\d{2}_\\d{2}(\\.\\w+)?$'
        elif self.when == 'D' or self.when == 'MIDNIGHT':
            self.interval = 86400
            self.suffix = '%Y-%m-%d'
            self.extMatch = '^\\d{4}-\\d{2}-\\d{2}(\\.\\w+)?$'
        elif self.when.startswith('W'):
            self.interval = 604800
            if len(self.when) != 2:
                raise ValueError('You must specify a day for weekly rollover from 0 to 6 (0 is Monday): %s' % self.when)
            if self.when[1] < '0' or self.when[1] > '6':
                raise ValueError('Invalid day specified for weekly rollover: %s' % self.when)
            self.dayOfWeek = int(self.when[1])
            self.suffix = '%Y-%m-%d'
            self.extMatch = '^\\d{4}-\\d{2}-\\d{2}(\\.\\w+)?$'
        else:
            raise ValueError('Invalid rollover interval specified: %s' % self.when)
        self.extMatch = re.compile(self.extMatch, re.ASCII)
        self.interval = self.interval * interval
        filename = self.baseFilename
        if os.path.exists(filename):
            t = os.stat(filename)[ST_MTIME]
        else:
            t = int(time.time())
        self.rolloverAt = self.computeRollover(t)

    
    def computeRollover(self, currentTime):
        '''
        Work out the rollover time based on the specified time.
        '''
        result = currentTime + self.interval
    # WARNING: Decompyle incomplete

    
    def shouldRollover(self, record):
        '''
        Determine if rollover should occur.

        record is not used, as we are just comparing times, but it is needed so
        the method signatures are the same
        '''
        t = int(time.time())
        if t >= self.rolloverAt:
            if not os.path.exists(self.baseFilename) and os.path.isfile(self.baseFilename):
                self.rolloverAt = self.computeRollover(t)
                return False
            return None

    
    def getFilesToDelete(self):
        '''
        Determine the files to delete when rolling over.

        More specific than the earlier method, which just used glob.glob().
        '''
        (dirName, baseName) = os.path.split(self.baseFilename)
        fileNames = os.listdir(dirName)
        result = []
        (n, e) = os.path.splitext(baseName)
        prefix = n + '.'
        plen = len(prefix)
    # WARNING: Decompyle incomplete

    
    def doRollover(self):
        '''
        do a rollover; in this case, a date/time stamp is appended to the filename
        when the rollover happens.  However, you want the file to be named for the
        start of the interval, not the current time.  If there is a backup count,
        then we have to get a list of matching filenames, sort them and remove
        the one with the oldest suffix.
        '''
        if self.stream:
            self.stream.close()
            self.stream = None
        currentTime = int(time.time())
        dstNow = time.localtime(currentTime)[-1]
        t = self.rolloverAt - self.interval
        if self.utc:
            timeTuple = time.gmtime(t)
        else:
            timeTuple = time.localtime(t)
            dstThen = timeTuple[-1]
            if dstNow != dstThen:
                if dstNow:
                    addend = 3600
                else:
                    addend = -3600
                timeTuple = time.localtime(t + addend)
        dfn = self.rotation_filename(self.baseFilename + '.' + time.strftime(self.suffix, timeTuple))
        if os.path.exists(dfn):
            os.remove(dfn)
        self.rotate(self.baseFilename, dfn)
        if self.backupCount > 0:
            for s in self.getFilesToDelete():
                os.remove(s)
                if not self.delay:
                    self.stream = self._open()
        newRolloverAt = self.computeRollover(currentTime)
    # WARNING: Decompyle incomplete



class WatchedFileHandler(logging.FileHandler):
    '''
    A handler for logging to a file, which watches the file
    to see if it has changed while in use. This can happen because of
    usage of programs such as newsyslog and logrotate which perform
    log file rotation. This handler, intended for use under Unix,
    watches the file to see if it has changed since the last emit.
    (A file has changed if its device or inode have changed.)
    If it has changed, the old file stream is closed, and the file
    opened to get a new stream.

    This handler is not appropriate for use under Windows, because
    under Windows open files cannot be moved or renamed - logging
    opens the files with exclusive locks - and so there is no need
    for such a handler. Furthermore, ST_INO is not supported under
    Windows; stat always returns zero for this value.

    This handler is based on a suggestion and patch by Chad J.
    Schroeder.
    '''
    
    def __init__(self, filename, mode, encoding, delay, errors = ('a', None, False, None)):
        if 'b' not in mode:
            encoding = io.text_encoding(encoding)
        logging.FileHandler.__init__(self, filename, mode = mode, encoding = encoding, delay = delay, errors = errors)
        (self.dev, self.ino) = (-1, -1)
        self._statstream()

    
    def _statstream(self):
        if self.stream:
            sres = os.fstat(self.stream.fileno())
            self.dev, self.ino = sres[ST_DEV], sres[ST_INO]
            return None

    
    def reopenIfNeeded(self):
        '''
        Reopen log file if needed.

        Checks if the underlying file has changed, and if it
        has, close the old stream and reopen the file to get the
        current stream.
        '''
        
        try:
            sres = os.stat(self.baseFilename)
        except FileNotFoundError:
            sres = None

    # WARNING: Decompyle incomplete

    
    def emit(self, record):
        '''
        Emit a record.

        If underlying file has changed, reopen the file before emitting the
        record to it.
        '''
        self.reopenIfNeeded()
        logging.FileHandler.emit(self, record)



class SocketHandler(logging.Handler):
    """
    A handler class which writes logging records, in pickle format, to
    a streaming socket. The socket is kept open across logging calls.
    If the peer resets it, an attempt is made to reconnect on the next call.
    The pickle which is sent is that of the LogRecord's attribute dictionary
    (__dict__), so that the receiver does not need to have the logging module
    installed in order to process the logging event.

    To unpickle the record at the receiving end into a LogRecord, use the
    makeLogRecord function.
    """
    
    def __init__(self, host, port):
        '''
        Initializes the handler with a specific host address and port.

        When the attribute *closeOnError* is set to True - if a socket error
        occurs, the socket is silently closed and then reopened on the next
        logging call.
        '''
        logging.Handler.__init__(self)
        self.host = host
        self.port = port
    # WARNING: Decompyle incomplete

    
    def makeSocket(self, timeout = (1,)):
        '''
        A factory method which allows subclasses to define the precise
        type of socket they want.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def createSocket(self):
        '''
        Try to create a socket, using an exponential backoff with
        a max retry time. Thanks to Robert Olson for the original patch
        (SF #815911) which has been slightly refactored.
        '''
        now = time.time()
    # WARNING: Decompyle incomplete

    
    def send(self, s):
        '''
        Send a pickled string to the socket.

        This function allows for partial sends which can happen when the
        network is busy.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def makePickle(self, record):
        '''
        Pickles the record in binary format with a length prefix, and
        returns it ready for transmission across the socket.
        '''
        ei = record.exc_info
        if ei:
            dummy = self.format(record)
        d = dict(record.__dict__)
        d['msg'] = record.getMessage()
        d['args'] = None
        d['exc_info'] = None
        d.pop('message', None)
        s = pickle.dumps(d, 1)
        slen = struct.pack('>L', len(s))
        return slen + s

    
    def handleError(self, record):
        '''
        Handle an error during logging.

        An error has occurred during logging. Most likely cause -
        connection lost. Close the socket so that we can retry on the
        next event.
        '''
        if self.closeOnError and self.sock:
            self.sock.close()
            self.sock = None
            return None
        None.Handler.handleError(self, record)

    
    def emit(self, record):
        '''
        Emit a record.

        Pickles the record and writes it to the socket in binary format.
        If there is an error with the socket, silently drop the packet.
        If there was a problem with the socket, re-establishes the
        socket.
        '''
        
        try:
            s = self.makePickle(record)
            self.send(s)
            return None
        except Exception:
            self.handleError(record)
            return None


    
    def close(self):
        '''
        Closes the socket.
        '''
        self.acquire()
        
        try:
            sock = self.sock
            if sock:
                self.sock = None
                sock.close()
            logging.Handler.close(self)
            self.release()
            return None
        except:
            self.release()




class DatagramHandler(SocketHandler):
    """
    A handler class which writes logging records, in pickle format, to
    a datagram socket.  The pickle which is sent is that of the LogRecord's
    attribute dictionary (__dict__), so that the receiver does not need to
    have the logging module installed in order to process the logging event.

    To unpickle the record at the receiving end into a LogRecord, use the
    makeLogRecord function.

    """
    
    def __init__(self, host, port):
        '''
        Initializes the handler with a specific host address and port.
        '''
        SocketHandler.__init__(self, host, port)
        self.closeOnError = False

    
    def makeSocket(self):
        '''
        The factory method of SocketHandler is here overridden to create
        a UDP socket (SOCK_DGRAM).
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def send(self, s):
        '''
        Send a pickled string to a socket.

        This function no longer allows for partial sends which can happen
        when the network is busy - UDP does not guarantee delivery and
        can deliver packets out of sequence.
        '''
        pass
    # WARNING: Decompyle incomplete



class SysLogHandler(logging.Handler):
    __module__ = __name__
    __qualname__ = 'SysLogHandler'
    __doc__ = "\n    A handler class which sends formatted logging records to a syslog\n    server. Based on Sam Rushing's syslog module:\n    http://www.nightmare.com/squirl/python-ext/misc/syslog.py\n    Contributed by Nicolas Untz (after which minor refactoring changes\n    have been made).\n    "
    LOG_EMERG = 0
    LOG_ALERT = 1
    LOG_CRIT = 2
    LOG_ERR = 3
    LOG_WARNING = 4
    LOG_NOTICE = 5
    LOG_INFO = 6
    LOG_DEBUG = 7
    LOG_KERN = 0
    LOG_USER = 1
    LOG_MAIL = 2
    LOG_DAEMON = 3
    LOG_AUTH = 4
    LOG_SYSLOG = 5
    LOG_LPR = 6
    LOG_NEWS = 7
    LOG_UUCP = 8
    LOG_CRON = 9
    LOG_AUTHPRIV = 10
    LOG_FTP = 11
    LOG_NTP = 12
    LOG_SECURITY = 13
    LOG_CONSOLE = 14
    LOG_SOLCRON = 15
    LOG_LOCAL0 = 16
    LOG_LOCAL1 = 17
    LOG_LOCAL2 = 18
    LOG_LOCAL3 = 19
    LOG_LOCAL4 = 20
    LOG_LOCAL5 = 21
    LOG_LOCAL6 = 22
    LOG_LOCAL7 = 23
    priority_names = {
        'alert': LOG_ALERT,
        'crit': LOG_CRIT,
        'critical': LOG_CRIT,
        'debug': LOG_DEBUG,
        'emerg': LOG_EMERG,
        'err': LOG_ERR,
        'error': LOG_ERR,
        'info': LOG_INFO,
        'notice': LOG_NOTICE,
        'panic': LOG_EMERG,
        'warn': LOG_WARNING,
        'warning': LOG_WARNING }
# WARNING: Decompyle incomplete


class SMTPHandler(logging.Handler):
    '''
    A handler class which sends an SMTP email for each logging event.
    '''
    
    def __init__(self, mailhost, fromaddr, toaddrs, subject, credentials, secure, timeout = (None, None, 5)):
        '''
        Initialize the handler.

        Initialize the instance with the from and to addresses and subject
        line of the email. To specify a non-standard SMTP port, use the
        (host, port) tuple format for the mailhost argument. To specify
        authentication credentials, supply a (username, password) tuple
        for the credentials argument. To specify the use of a secure
        protocol (TLS), pass in a tuple for the secure argument. This will
        only be used when authentication credentials are supplied. The tuple
        will be either an empty tuple, or a single-value tuple with the name
        of a keyfile, or a 2-value tuple with the names of the keyfile and
        certificate file. (This tuple is passed to the `starttls` method).
        A timeout in seconds can be specified for the SMTP connection (the
        default is one second).
        '''
        logging.Handler.__init__(self)
        if isinstance(mailhost, (list, tuple)):
            (self.mailhost, self.mailport) = mailhost
        else:
            self.mailhost, self.mailport = mailhost, None
        if isinstance(credentials, (list, tuple)):
            (self.username, self.password) = credentials
        else:
            self.username = None
        self.fromaddr = fromaddr
        if isinstance(toaddrs, str):
            toaddrs = [
                toaddrs]
        self.toaddrs = toaddrs
        self.subject = subject
        self.secure = secure
        self.timeout = timeout

    
    def getSubject(self, record):
        '''
        Determine the subject for the email.

        If you want to specify a subject line which is record-dependent,
        override this method.
        '''
        return self.subject

    
    def emit(self, record):
        '''
        Emit a record.

        Format the record and send it to the specified addressees.
        '''
        pass
    # WARNING: Decompyle incomplete



class NTEventLogHandler(logging.Handler):
    '''
    A handler class which sends events to the NT Event Log. Adds a
    registry entry for the specified application name. If no dllname is
    provided, win32service.pyd (which contains some basic message
    placeholders) is used. Note that use of these placeholders will make
    your event logs big, as the entire message source is held in the log.
    If you want slimmer logs, you have to pass in the name of your own DLL
    which contains the message definitions you want to use in the event log.
    '''
    
    def __init__(self, appname, dllname, logtype = (None, 'Application')):
        logging.Handler.__init__(self)
        
        try:
            import win32evtlogutil
            import win32evtlog
            self.appname = appname
            self._welu = win32evtlogutil
            if not dllname:
                dllname = os.path.split(self._welu.__file__)
                dllname = os.path.split(dllname[0])
                dllname = os.path.join(dllname[0], 'win32service.pyd')
            self.dllname = dllname
            self.logtype = logtype
            
            try:
                self._welu.AddSourceToRegistry(appname, dllname, logtype)
                
                try:
                    pass
                except Exception:
                    e = None
                    if getattr(e, 'winerror', None) != 5:
                        raise 
                    
                    try:
                        e = None
                        del e
                    e = None
                    del e
                    try:
                        self.deftype = win32evtlog.EVENTLOG_ERROR_TYPE
                        self.typemap = {
                            logging.CRITICAL: win32evtlog.EVENTLOG_ERROR_TYPE,
                            logging.ERROR: win32evtlog.EVENTLOG_ERROR_TYPE,
                            logging.WARNING: win32evtlog.EVENTLOG_WARNING_TYPE,
                            logging.INFO: win32evtlog.EVENTLOG_INFORMATION_TYPE,
                            logging.DEBUG: win32evtlog.EVENTLOG_INFORMATION_TYPE }
                        return None
                    except ImportError:
                        print('The Python Win32 extensions for NT (service, event logging) appear not to be available.')
                        self._welu = None
                        return None





    
    def getMessageID(self, record):
        '''
        Return the message ID for the event record. If you are using your
        own messages, you could do this by having the msg passed to the
        logger being an ID rather than a formatting string. Then, in here,
        you could use a dictionary lookup to get the message ID. This
        version returns 1, which is the base message ID in win32service.pyd.
        '''
        return 1

    
    def getEventCategory(self, record):
        '''
        Return the event category for the record.

        Override this if you want to specify your own categories. This version
        returns 0.
        '''
        return 0

    
    def getEventType(self, record):
        """
        Return the event type for the record.

        Override this if you want to specify your own types. This version does
        a mapping using the handler's typemap attribute, which is set up in
        __init__() to a dictionary which contains mappings for DEBUG, INFO,
        WARNING, ERROR and CRITICAL. If you are using your own levels you will
        either need to override this method or place a suitable dictionary in
        the handler's typemap attribute.
        """
        return self.typemap.get(record.levelno, self.deftype)

    
    def emit(self, record):
        '''
        Emit a record.

        Determine the message ID, event category and event type. Then
        log the message in the NT event log.
        '''
        if self._welu:
            
            try:
                id = self.getMessageID(record)
                cat = self.getEventCategory(record)
                type = self.getEventType(record)
                msg = self.format(record)
                self._welu.ReportEvent(self.appname, id, cat, type, [
                    msg])
                return None
            except Exception:
                self.handleError(record)
                return None
                return None


    
    def close(self):
        '''
        Clean up this handler.

        You can remove the application name from the registry as a
        source of event log entries. However, if you do this, you will
        not be able to see the events as you intended in the Event Log
        Viewer - it needs to be able to access the registry to get the
        DLL name.
        '''
        logging.Handler.close(self)



class HTTPHandler(logging.Handler):
    '''
    A class which sends records to a web server, using either GET or
    POST semantics.
    '''
    
    def __init__(self, host, url, method, secure, credentials, context = ('GET', False, None, None)):
        '''
        Initialize the instance with the host, the request URL, and the method
        ("GET" or "POST")
        '''
        logging.Handler.__init__(self)
        method = method.upper()
        if method not in ('GET', 'POST'):
            raise ValueError('method must be GET or POST')
    # WARNING: Decompyle incomplete

    
    def mapLogRecord(self, record):
        '''
        Default implementation of mapping the log record into a dict
        that is sent as the CGI data. Overwrite in your class.
        Contributed by Franz Glasner.
        '''
        return record.__dict__

    
    def getConnection(self, host, secure):
        '''
        get a HTTP[S]Connection.

        Override when a custom connection is required, for example if
        there is a proxy.
        '''
        import http.client as http
        if secure:
            connection = http.client.HTTPSConnection(host, context = self.context)
        else:
            connection = http.client.HTTPConnection(host)
        return connection

    
    def emit(self, record):
        '''
        Emit a record.

        Send the record to the web server as a percent-encoded dictionary
        '''
        
        try:
            import urllib.parse as urllib
            host = self.host
            h = self.getConnection(host, self.secure)
            url = self.url
            data = urllib.parse.urlencode(self.mapLogRecord(record))
            if self.method == 'GET':
                if url.find('?') >= 0:
                    sep = '&'
                else:
                    sep = '?'
                url = url + '%c%s' % (sep, data)
            h.putrequest(self.method, url)
            i = host.find(':')
            if i >= 0:
                host = host[:i]
            if self.method == 'POST':
                h.putheader('Content-type', 'application/x-www-form-urlencoded')
                h.putheader('Content-length', str(len(data)))
            if self.credentials:
                import base64
                s = ('%s:%s' % self.credentials).encode('utf-8')
                s = 'Basic ' + base64.b64encode(s).strip().decode('ascii')
                h.putheader('Authorization', s)
            h.endheaders()
            if self.method == 'POST':
                h.send(data.encode('utf-8'))
            h.getresponse()
            return None
        except Exception:
            self.handleError(record)
            return None




class BufferingHandler(logging.Handler):
    """
  A handler class which buffers logging records in memory. Whenever each
  record is added to the buffer, a check is made to see if the buffer should
  be flushed. If it should, then flush() is expected to do what's needed.
    """
    
    def __init__(self, capacity):
        '''
        Initialize the handler with the buffer size.
        '''
        logging.Handler.__init__(self)
        self.capacity = capacity
        self.buffer = []

    
    def shouldFlush(self, record):
        '''
        Should the handler flush its buffer?

        Returns true if the buffer is up to capacity. This method can be
        overridden to implement custom flushing strategies.
        '''
        return len(self.buffer) >= self.capacity

    
    def emit(self, record):
        '''
        Emit a record.

        Append the record. If shouldFlush() tells us to, call flush() to process
        the buffer.
        '''
        self.buffer.append(record)
        if self.shouldFlush(record):
            self.flush()
            return None

    
    def flush(self):
        '''
        Override to implement custom flushing behaviour.

        This version just zaps the buffer to empty.
        '''
        self.acquire()
        
        try:
            self.buffer.clear()
            self.release()
            return None
        except:
            self.release()


    
    def close(self):
        """
        Close the handler.

        This version just flushes and chains to the parent class' close().
        """
        
        try:
            self.flush()
            logging.Handler.close(self)
            return None
        except:
            logging.Handler.close(self)




class MemoryHandler(BufferingHandler):
    '''
    A handler class which buffers logging records in memory, periodically
    flushing them to a target handler. Flushing occurs whenever the buffer
    is full, or when an event of a certain severity or greater is seen.
    '''
    
    def __init__(self, capacity, flushLevel, target, flushOnClose = (logging.ERROR, None, True)):
        """
        Initialize the handler with the buffer size, the level at which
        flushing should occur and an optional target.

        Note that without a target being set either here or via setTarget(),
        a MemoryHandler is no use to anyone!

        The ``flushOnClose`` argument is ``True`` for backward compatibility
        reasons - the old behaviour is that when the handler is closed, the
        buffer is flushed, even if the flush level hasn't been exceeded nor the
        capacity exceeded. To prevent this, set ``flushOnClose`` to ``False``.
        """
        BufferingHandler.__init__(self, capacity)
        self.flushLevel = flushLevel
        self.target = target
        self.flushOnClose = flushOnClose

    
    def shouldFlush(self, record):
