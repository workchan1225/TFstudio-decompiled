# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: models.pyc (Python 3.11)

from copy import copy

class Request:
    
    def __init__(self = None, url = None, method = None, headers = ('url', str, 'method', str, 'headers', dict, 'return', None)):
        self.url = url
        self.method = method
        self.headers = copy(headers)

    
    def __repr__(self = None):
        return f'''Request to {self.url} - {self.method}'''



class Response:
    
    def __init__(self = None, url = None, status_code = None, headers = ('url', str, 'status_code', int, 'headers', dict, 'return', None)):
        self.url = url
        self.status_code = status_code
        self.headers = headers

    
    def __repr__(self = None):
        return f'''Response from {self.url} - {self.status_code}'''
