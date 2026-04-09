# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: http.pyc (Python 3.11)

import base64
import datetime
import gzip
import io
import re
import struct
import urllib.parse as urllib
import urllib.request as urllib
import zlib
from datetimes import _parse_date
from urls import convert_to_idn
ACCEPT_HEADER = 'application/atom+xml,application/rdf+xml,application/rss+xml,application/x-netcdf,application/xml;q=0.9,text/xml;q=0.2,*/*;q=0.1'

class _FeedURLHandler(urllib.request.HTTPDefaultErrorHandler, urllib.request.HTTPRedirectHandler, urllib.request.HTTPDigestAuthHandler):
    
    def http_error_default(self, req, fp, code, msg, headers):
        fp.status = code
        return fp

    
    def http_error_301(self, req, fp, code, msg, hdrs):
        result = urllib.request.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, hdrs)
        if not result:
            return fp
        result.status = None
        result.newurl = result.geturl()
        return result

    http_error_300 = http_error_301
    http_error_302 = http_error_301
    http_error_303 = http_error_301
    http_error_307 = http_error_301
    
    def http_error_401(self, req, fp, code, msg, headers):
        host = urllib.parse.urlparse(req.get_full_url())[1]
        if 'Authorization' not in req.headers or 'WWW-Authenticate' not in headers:
            return self.http_error_default(req, fp, code, msg, headers)
        auth = None.decodebytes(req.headers['Authorization'].split(' ')[1].encode()).decode()
        (user, passw) = auth.split(':')
        realm = re.findall('realm="([^"]*)"', headers['WWW-Authenticate'])[0]
        self.add_password(realm, host, user, passw)
        retry = self.http_error_auth_reqed('www-authenticate', host, req, headers)
        self.reset_retry_count()
        return retry



def _build_urllib2_request(url, agent, accept_header, etag, modified, referrer, auth, request_headers):
    request = urllib.request.Request(url)
    request.add_header('User-Agent', agent)
    if etag:
        request.add_header('If-None-Match', etag)
    if isinstance(modified, str):
        modified = _parse_date(modified)
    elif isinstance(modified, datetime.datetime):
        modified = modified.utctimetuple()
    if modified:
        short_weekdays = [
            'Mon',
            'Tue',
            'Wed',
            'Thu',
            'Fri',
            'Sat',
            'Sun']
        months = [
            'Jan',
            'Feb',
            'Mar',
            'Apr',
            'May',
            'Jun',
            'Jul',
            'Aug',
            'Sep',
            'Oct',
            'Nov',
            'Dec']
        request.add_header('If-Modified-Since', '%s, %02d %s %04d %02d:%02d:%02d GMT' % (short_weekdays[modified[6]], modified[2], months[modified[1] - 1], modified[0], modified[3], modified[4], modified[5]))
    if referrer:
        request.add_header('Referer', referrer)
    request.add_header('Accept-encoding', 'gzip, deflate')
    if auth:
        request.add_header('Authorization', 'Basic %s' % auth)
    if accept_header:
        request.add_header('Accept', accept_header)
    for header_name, header_value in request_headers.items():
        request.add_header(header_name, header_value)
        request.add_header('A-IM', 'feed')
        return request


def get(url, etag, modified, agent, referrer, handlers, request_headers, result = (None, None, None, None, None, None, None)):
    pass
# WARNING: Decompyle incomplete
