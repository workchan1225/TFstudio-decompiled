# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: bdb.pyc (Python 3.11)

'''Debugger basics'''
import fnmatch
import sys
import os
from inspect import CO_GENERATOR, CO_COROUTINE, CO_ASYNC_GENERATOR
__all__ = [
    'BdbQuit',
    'Bdb',
    'Breakpoint']
GENERATOR_AND_COROUTINE_FLAGS = CO_GENERATOR | CO_COROUTINE | CO_ASYNC_GENERATOR

class BdbQuit(Exception):
    '''Exception to give up completely.'''
    pass


class Bdb:
    '''Generic Python debugger base class.

    This class takes care of details of the trace facility;
    a derived class should implement user interaction.
    The standard debugger class (pdb.Pdb) is an example.

    The optional skip argument must be an iterable of glob-style
    module name patterns.  The debugger will not step into frames
    that originate in a module that matches one of these patterns.
    Whether a frame is considered to originate in a certain module
    is determined by the __name__ in the frame globals.
    '''
    
    def __init__(self, skip = (None,)):
        self.skip = set(skip) if skip else None
        self.breaks = { }
        self.fncache = { }
        self.frame_returning = None
        self._load_breaks()

    
    def canonic(self, filename):
        '''Return canonical form of filename.

        For real filenames, the canonical form is a case-normalized (on
        case insensitive filesystems) absolute path.  \'Filenames\' with
        angle brackets, such as "<stdin>", generated in interactive
        mode, are returned unchanged.
        '''
        if filename == '<' + filename[1:-1] + '>':
            return filename
        canonic = None.fncache.get(filename)
        if not canonic:
            canonic = os.path.abspath(filename)
            canonic = os.path.normcase(canonic)
            self.fncache[filename] = canonic
        return canonic

    
    def reset(self):
        '''Set values of attributes as ready to start debugging.'''
        import linecache
        linecache.checkcache()
        self.botframe = None
        self._set_stopinfo(None, None)

    
    def trace_dispatch(self, frame, event, arg):
        '''Dispatch a trace function for debugged frames based on the event.

        This function is installed as the trace function for debugged
        frames. Its return value is the new trace function, which is
        usually itself. The default implementation decides how to
        dispatch a frame, depending on the type of event (passed in as a
        string) that is about to be executed.

        The event can be one of the following:
            line: A new line of code is going to be executed.
            call: A function is about to be called or another code block
                  is entered.
            return: A function or other code block is about to return.
            exception: An exception has occurred.
            c_call: A C function is about to be called.
            c_return: A C function has returned.
            c_exception: A C function has raised an exception.

        For the Python events, specialized functions (see the dispatch_*()
        methods) are called.  For the C events, no action is taken.

        The arg parameter depends on the previous event.
        '''
        if self.quitting:
            return None
        if None == 'line':
            return self.dispatch_line(frame)
        if None == 'call':
            return self.dispatch_call(frame, arg)
        if None == 'return':
            return self.dispatch_return(frame, arg)
        if None == 'exception':
            return self.dispatch_exception(frame, arg)
        if None == 'c_call':
            return self.trace_dispatch
        if None == 'c_exception':
            return self.trace_dispatch
        if None == 'c_return':
            return self.trace_dispatch
        None('bdb.Bdb.dispatch: unknown debugging event:', repr(event))
        return self.trace_dispatch

    
    def dispatch_line(self, frame):
        '''Invoke user function and return trace function for line event.

        If the debugger stops on the current line, invoke
        self.user_line(). Raise BdbQuit if self.quitting is set.
        Return self.trace_dispatch to continue tracing in this scope.
        '''
        if self.stop_here(frame) or self.break_here(frame):
            self.user_line(frame)
            if self.quitting:
                raise BdbQuit
        return self.trace_dispatch

    
    def dispatch_call(self, frame, arg):
        '''Invoke user function and return trace function for call event.

        If the debugger stops on this function call, invoke
        self.user_call(). Raise BdbQuit if self.quitting is set.
        Return self.trace_dispatch to continue tracing in this scope.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def dispatch_return(self, frame, arg):
        '''Invoke user function and return trace function for return event.

        If the debugger stops on this function return, invoke
        self.user_return(). Raise BdbQuit if self.quitting is set.
        Return self.trace_dispatch to continue tracing in this scope.
        '''
        if self.stop_here(frame) or frame == self.returnframe:
            if self.stopframe and frame.f_code.co_flags & GENERATOR_AND_COROUTINE_FLAGS:
                return self.trace_dispatch
            
            try:
                self.frame_returning = frame
                self.user_return(frame, arg)
                self.frame_returning = None
            except:
                self.frame_returning = None

            if self.quitting:
                raise BdbQuit
            if self.stopframe is frame and self.stoplineno != -1:
                self._set_stopinfo(None, None)
        return self.trace_dispatch

    
    def dispatch_exception(self, frame, arg):
        '''Invoke user function and return trace function for exception event.

        If the debugger stops on this exception, invoke
        self.user_exception(). Raise BdbQuit if self.quitting is set.
        Return self.trace_dispatch to continue tracing in this scope.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def is_skipped_module(self, module_name):
        '''Return True if module_name matches any skip pattern.'''
        pass
    # WARNING: Decompyle incomplete

    
    def stop_here(self, frame):
        '''Return True if frame is below the starting frame in the stack.'''
        if self.skip and self.is_skipped_module(frame.f_globals.get('__name__')):
            return False
        if None is self.stopframe:
            if self.stoplineno == -1:
                return False
            return None.f_lineno >= self.stoplineno
        if not None.stopframe:
            return True

    
    def break_here(self, frame):
