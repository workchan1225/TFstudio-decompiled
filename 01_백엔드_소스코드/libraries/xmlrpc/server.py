# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: server.pyc (Python 3.11)

'''XML-RPC Servers.

This module can be used to create simple XML-RPC servers
by creating a server and either installing functions, a
class instance, or by extending the SimpleXMLRPCServer
class.

It can also be used to handle XML-RPC requests in a CGI
environment using CGIXMLRPCRequestHandler.

The Doc* classes can be used to create XML-RPC servers that
serve pydoc-style documentation in response to HTTP
GET requests. This documentation is dynamically generated
based on the functions and methods registered with the
server.

A list of possible usage patterns follows:

1. Install functions:

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(pow)
server.register_function(lambda x,y: x+y, \'add\')
server.serve_forever()

2. Install an instance:

class MyFuncs:
    def __init__(self):
        # make all of the sys functions available through sys.func_name
        import sys
        self.sys = sys
    def _listMethods(self):
        # implement this method so that system.listMethods
        # knows to advertise the sys methods
        return list_public_methods(self) + \\
                [\'sys.\' + method for method in list_public_methods(self.sys)]
    def pow(self, x, y): return pow(x, y)
    def add(self, x, y) : return x + y

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_introspection_functions()
server.register_instance(MyFuncs())
server.serve_forever()

3. Install an instance with custom dispatch method:

class Math:
    def _listMethods(self):
        # this method must be present for system.listMethods
        # to work
        return [\'add\', \'pow\']
    def _methodHelp(self, method):
        # this method must be present for system.methodHelp
        # to work
        if method == \'add\':
            return "add(2,3) => 5"
        elif method == \'pow\':
            return "pow(x, y[, z]) => number"
        else:
            # By convention, return empty
            # string if no help is available
            return ""
    def _dispatch(self, method, params):
        if method == \'pow\':
            return pow(*params)
        elif method == \'add\':
            return params[0] + params[1]
        else:
            raise ValueError(\'bad method\')

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_introspection_functions()
server.register_instance(Math())
server.serve_forever()

4. Subclass SimpleXMLRPCServer:

class MathServer(SimpleXMLRPCServer):
    def _dispatch(self, method, params):
        try:
            # We are forcing the \'export_\' prefix on methods that are
            # callable through XML-RPC to prevent potential security
            # problems
            func = getattr(self, \'export_\' + method)
        except AttributeError:
            raise Exception(\'method "%s" is not supported\' % method)
        else:
            return func(*params)

    def export_add(self, x, y):
        return x + y

server = MathServer(("localhost", 8000))
server.serve_forever()

5. CGI script:

server = CGIXMLRPCRequestHandler()
server.register_function(pow)
server.handle_request()
'''
from xmlrpc.client import Fault, dumps, loads, gzip_encode, gzip_decode
from http.server import BaseHTTPRequestHandler
from functools import partial
from inspect import signature
import html
import http.server as http
import socketserver
import sys
import os
import re
import pydoc
import traceback

try:
    import fcntl
except ImportError:
    fcntl = None


def resolve_dotted_attribute(obj, attr, allow_dotted_names = (True,)):
    """resolve_dotted_attribute(a, 'b.c.d') => a.b.c.d

    Resolves a dotted attribute name to an object.  Raises
    an AttributeError if any attribute in the chain starts with a '_'.

    If the optional allow_dotted_names argument is false, dots are not
    supported and this function operates similar to getattr(obj, attr).
    """
    if allow_dotted_names:
        attrs = attr.split('.')
    else:
        attrs = [
            attr]
    for i in attrs:
        if i.startswith('_'):
            raise AttributeError('attempt to access private attribute "%s"' % i)
        obj = getattr(obj, i)
        return obj


def list_public_methods(obj):
    '''Returns a list of attribute strings, found in the specified
    object, which represent callable attributes'''
    pass
# WARNING: Decompyle incomplete


class SimpleXMLRPCDispatcher:
    """Mix-in class that dispatches XML-RPC requests.

    This class is used to register XML-RPC method handlers
    and then to dispatch them. This class doesn't need to be
    instanced directly when used by SimpleXMLRPCServer but it
    can be instanced when used by the MultiPathXMLRPCServer
    """
    
    def __init__(self, allow_none, encoding, use_builtin_types = (False, None, False)):
