# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: managers.pyc (Python 3.11)

__all__ = [
    'BaseManager',
    'SyncManager',
    'BaseProxy',
    'Token']
import sys
import threading
import signal
import array
import queue
import time
import types
import os
from os import getpid
from traceback import format_exc
from  import connection
from context import reduction, get_spawning_popen, ProcessError
from  import pool
from  import process
from  import util
from  import get_context

try:
    from  import shared_memory
    HAS_SHMEM = True
    __all__.append('SharedMemoryManager')
except ImportError:
    HAS_SHMEM = False


def reduce_array(a):
    return (array.array, (a.typecode, a.tobytes()))

reduction.register(array.array, reduce_array)
view_types = ('items', 'keys', 'values')()

def rebuild_as_list(obj):
    return (list, (list(obj),))

for view_type in view_types:
    reduction.register(view_type, rebuild_as_list)
    del view_type
    del view_types
    
    class Token(object):
        '''
    Type to uniquely identify a shared object
    '''
        __slots__ = ('typeid', 'address', 'id')
        
        def __init__(self, typeid, address, id):
            self.typeid, self.address, self.id = typeid, address, id

        
        def __getstate__(self):
            return (self.typeid, self.address, self.id)

        
        def __setstate__(self, state):
            (self.typeid, self.address, self.id) = state

        
        def __repr__(self):
            return f'''{self.__class__.__name__!s}(typeid={self.typeid!r}, address={self.address!r}, id={self.id!r})'''


    
    def dispatch(c, id, methodname, args, kwds = ((), { })):
        '''
    Send a message to manager using connection `c` and return response
    '''
        c.send((id, methodname, args, kwds))
        (kind, result) = c.recv()
        if kind == '#RETURN':
            return result
        raise None(kind, result)

    
    def convert_to_error(kind, result):
        if kind == '#ERROR':
            return result
        if None in ('#TRACEBACK', '#UNSERIALIZABLE'):
            if not isinstance(result, str):
                raise TypeError("Result {0!r} (kind '{1}') type is {2}, not str".format(result, kind, type(result)))
            if kind == '#UNSERIALIZABLE':
                return RemoteError('Unserializable message: %s\n' % result)
            return None(result)
        return None('Unrecognized message type {!r}'.format(kind))

    
    class RemoteError(Exception):
        
        def __str__(self):
            return '\n---------------------------------------------------------------------------\n' + str(self.args[0]) + '---------------------------------------------------------------------------'


    
    def all_methods(obj):
        '''
    Return a list of names of methods of `obj`
    '''
        temp = []
        for name in dir(obj):
            func = getattr(obj, name)
            if callable(func):
                temp.append(name)
            return temp

    
    def public_methods(obj):
        """
    Return a list of names of methods of `obj` which do not start with '_'
    """
        return all_methods(obj)()

    
    class Server(object):
        '''
    Server class which runs in a process controlled by a manager object
    '''
        public = [
            'shutdown',
            'create',
            'accept_connection',
            'get_methods',
            'debug_info',
            'number_of_objects',
            'dummy',
            'incref',
            'decref']
        
        def __init__(self, registry, address, authkey, serializer):
            if not isinstance(authkey, bytes):
                raise TypeError('Authkey {0!r} is type {1!s}, not bytes'.format(authkey, type(authkey)))
            self.registry = registry
            self.authkey = process.AuthenticationString(authkey)
            (Listener, Client) = listener_client[serializer]
            self.listener = Listener(address = address, backlog = 128)
            self.address = self.listener.address
            self.id_to_obj = {
                '0': (None, ()) }
            self.id_to_refcount = { }
            self.id_to_local_proxy_obj = { }
            self.mutex = threading.Lock()

        
        def serve_forever(self):
            '''
        Run the server forever
        '''
            self.stop_event = threading.Event()
            process.current_process()._manager_server = self
        # WARNING: Decompyle incomplete

        
        def accepter(self):
            
            try:
                c = self.listener.accept()
            except OSError:
                continue

            t = threading.Thread(target = self.handle_request, args = (c,))
            t.daemon = True
            t.start()
            continue

        
        def _handle_request(self, c):
            request = None
        # WARNING: Decompyle incomplete

        
        def handle_request(self, conn):
            '''
        Handle a new connection
        '''
            
            try:
                self._handle_request(conn)
                
                try:
                    pass
                except SystemExit:
                    
                    try:
                        pass
                    try:
                        conn.close()
                        return None
                    except:
                        conn.close()




        
        def serve_client(self, conn):
            '''
        Handle requests from the proxies in a particular process/thread
        '''
            util.debug('starting server thread to service %r', threading.current_thread().name)
            recv = conn.recv
            send = conn.send
            id_to_obj = self.id_to_obj
        # WARNING: Decompyle incomplete

        
        def fallback_getvalue(self, conn, ident, obj):
            return obj

        
        def fallback_str(self, conn, ident, obj):
            return str(obj)

        
        def fallback_repr(self, conn, ident, obj):
            return repr(obj)

        fallback_mapping = {
            '__str__': fallback_str,
            '__repr__': fallback_repr,
            '#GETVALUE': fallback_getvalue }
        
        def dummy(self, c):
            pass

        
        def debug_info(self, c):
            '''
        Return some info --- useful to spot problems with refcounting
        '''
            self.mutex
            result = []
            keys = list(self.id_to_refcount.keys())
            keys.sort()
            for ident in keys:
                if ident != '0':
                    result.append(f'''  {ident!s}:       refcount={self.id_to_refcount[ident]!s}\n    {str(self.id_to_obj[ident][0])[:75]!s}''')
                None(None, None)
                return 
                with None:
                    if not None, '\n'.join(result):
                        pass

        
        def number_of_objects(self, c):
            '''
        Number of shared objects
        '''
            return len(self.id_to_refcount)

        
        def shutdown(self, c):
            '''
        Shutdown this process
        '''
            
            try:
                util.debug('manager received shutdown message')
                c.send(('#RETURN', None))
                
                try:
                    pass
                import traceback
                traceback.print_exc()
                try:
                    pass
                self.stop_event.set()
                return None
                self.stop_event.set()



        
        def create(self, c, typeid, *args, **kwds):
            '''
        Create a new shared object and return its id
        '''
            self.mutex
            (callable, exposed, method_to_typeid, proxytype) = self.registry[typeid]
        # WARNING: Decompyle incomplete

        
        def get_methods(self, c, token):
            '''
        Return the methods of the shared object indicated by token
        '''
            return tuple(self.id_to_obj[token.id][1])

        
        def accept_connection(self, c, name):
            '''
        Spawn a new thread to serve this connection
        '''
            threading.current_thread().name = name
            c.send(('#RETURN', None))
            self.serve_client(c)

        
        def incref(self, c, ident):
            self.mutex

        
        def decref(self, c, ident):
