# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: profile.pyc (Python 3.11)

'''Class for profiling Python code.'''
import io
import sys
import time
import marshal
__all__ = [
    'run',
    'runctx',
    'Profile']

class _Utils:
    '''Support class for utility functions which are shared by
    profile.py and cProfile.py modules.
    Not supposed to be used directly.
    '''
    
    def __init__(self, profiler):
        self.profiler = profiler

    
    def run(self, statement, filename, sort):
        prof = self.profiler()
        
        try:
            prof.run(statement)
            
            try:
                pass
            except SystemExit:
                
                try:
                    pass
                try:
                    self._show(prof, filename, sort)
                    return None
                except:
                    self._show(prof, filename, sort)




    
    def runctx(self, statement, globals, locals, filename, sort):
        prof = self.profiler()
        
        try:
            prof.runctx(statement, globals, locals)
            
            try:
                pass
            except SystemExit:
                
                try:
                    pass
                try:
                    self._show(prof, filename, sort)
                    return None
                except:
                    self._show(prof, filename, sort)




    
    def _show(self, prof, filename, sort):
        pass
    # WARNING: Decompyle incomplete



def run(statement, filename, sort = (None, -1)):
    '''Run statement under profiler optionally saving results in filename

    This function takes a single argument that can be passed to the
    "exec" statement, and an optional file name.  In all cases this
    routine attempts to "exec" its first argument and gather profiling
    statistics from the execution. If no file name is present, then this
    function automatically prints a simple profiling report, sorted by the
    standard name string (file/line/function-name) that is presented in
    each line.
    '''
    return _Utils(Profile).run(statement, filename, sort)


def runctx(statement, globals, locals, filename, sort = (None, -1)):
    '''Run statement under profiler, supplying your own globals and locals,
    optionally saving results in filename.

    statement and filename have the same semantics as profile.run
    '''
    return _Utils(Profile).runctx(statement, globals, locals, filename, sort)


class Profile:
    '''Profiler class.

    self.cur is always a tuple.  Each such tuple corresponds to a stack
    frame that is currently active (self.cur[-2]).  The following are the
    definitions of its members.  We use this external "parallel stack" to
    avoid contaminating the program that we are profiling. (old profiler
    used to write into the frames local dictionary!!) Derived classes
    can change the definition of some entries, as long as they leave
    [-2:] intact (frame and previous tuple).  In case an internal error is
    detected, the -3 element is used as the function name.

    [ 0] = Time that needs to be charged to the parent frame\'s function.
           It is used so that a function call will not have to access the
           timing data for the parent frame.
    [ 1] = Total time spent in this frame\'s function, excluding time in
           subfunctions (this latter is tallied in cur[2]).
    [ 2] = Total time spent in subfunctions, excluding time executing the
           frame\'s function (this latter is tallied in cur[1]).
    [-3] = Name of the function that corresponds to this frame.
    [-2] = Actual frame that we correspond to (used to sync exception handling).
    [-1] = Our parent 6-tuple (corresponds to frame.f_back).

    Timing data for each function is stored as a 5-tuple in the dictionary
    self.timings[].  The index is always the name stored in self.cur[-3].
    The following are the definitions of the members:

    [0] = The number of times this function was called, not counting direct
          or indirect recursion,
    [1] = Number of times this function appears on the stack, minus one
    [2] = Total time spent internal to this function
    [3] = Cumulative time that this function was present on the stack.  In
          non-recursive functions, this is the total execution time from start
          to finish of each invocation of a function, including time spent in
          all subfunctions.
    [4] = A dictionary indicating for each function name, the number of times
          it was called by us.
    '''
    bias = 0
    
    def __init__(self, timer, bias = (None, None)):
        self.timings = { }
        self.cur = None
        self.cmd = ''
        self.c_func_name = ''
    # WARNING: Decompyle incomplete

    
    def trace_dispatch(self, frame, event, arg):
        timer = self.timer
        t = timer()
        t = t[0] + t[1] - self.t - self.bias
        if event == 'c_call':
            self.c_func_name = arg.__name__
        if self.dispatch[event](self, frame, t):
            t = timer()
            self.t = t[0] + t[1]
            return None
        r = timer()
        self.t = r[0] + r[1] - t

    
    def trace_dispatch_i(self, frame, event, arg):
        timer = self.timer
        t = timer() - self.t - self.bias
        if event == 'c_call':
            self.c_func_name = arg.__name__
        if self.dispatch[event](self, frame, t):
            self.t = timer()
            return None
        self.t = timer() - t

    
    def trace_dispatch_mac(self, frame, event, arg):
        timer = self.timer
        t = timer() / 60 - self.t - self.bias
        if event == 'c_call':
            self.c_func_name = arg.__name__
        if self.dispatch[event](self, frame, t):
            self.t = timer() / 60
            return None
        self.t = timer() / 60 - t

    
    def trace_dispatch_l(self, frame, event, arg):
        get_time = self.get_time
        t = get_time() - self.t - self.bias
        if event == 'c_call':
            self.c_func_name = arg.__name__
        if self.dispatch[event](self, frame, t):
            self.t = get_time()
            return None
        self.t = get_time() - t

    
    def trace_dispatch_exception(self, frame, t):
        (rpt, rit, ret, rfn, rframe, rcur) = self.cur
        if rframe is not frame and rcur:
            return self.trace_dispatch_return(rframe, t)
        self.cur = (None, rit + t, ret, rfn, rframe, rcur)
        return 1

    
    def trace_dispatch_call(self, frame, t):
        pass
    # WARNING: Decompyle incomplete

    
    def trace_dispatch_c_call(self, frame, t):
        fn = ('', 0, self.c_func_name)
        self.cur = (t, 0, 0, fn, frame, self.cur)
        timings = self.timings
        if fn in timings:
            (cc, ns, tt, ct, callers) = timings[fn]
            timings[fn] = (cc, ns + 1, tt, ct, callers)
        else:
            timings[fn] = (0, 0, 0, 0, { })
        return 1

    
    def trace_dispatch_return(self, frame, t):
        pass
    # WARNING: Decompyle incomplete

    dispatch = {
        'call': trace_dispatch_call,
        'exception': trace_dispatch_exception,
        'return': trace_dispatch_return,
        'c_call': trace_dispatch_c_call,
        'c_exception': trace_dispatch_return,
        'c_return': trace_dispatch_return }
    
    def set_cmd(self, cmd):
        if self.cur[-1]:
            return None
        self.cmd = None
        self.simulate_call(cmd)

    
    class fake_code:
        
        def __init__(self, filename, line, name):
            self.co_filename = filename
            self.co_line = line
            self.co_name = name
            self.co_firstlineno = 0

        
        def __repr__(self):
            return repr((self.co_filename, self.co_line, self.co_name))


    
    class fake_frame:
        
        def __init__(self, code, prior):
            self.f_code = code
            self.f_back = prior


    
    def simulate_call(self, name):
        code = self.fake_code('profile', 0, name)
        if self.cur:
            pframe = self.cur[-2]
        else:
            pframe = None
        frame = self.fake_frame(code, pframe)
        self.dispatch['call'](self, frame, 0)

    
    def simulate_cmd_complete(self):
        get_time = self.get_time
        t = get_time() - self.t
    # WARNING: Decompyle incomplete

    
    def print_stats(self, sort = (-1,)):
        import pstats
        pstats.Stats(self).strip_dirs().sort_stats(sort).print_stats()

    
    def dump_stats(self, file):
        f = open(file, 'wb')
        self.create_stats()
        marshal.dump(self.stats, f)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def create_stats(self):
        self.simulate_cmd_complete()
        self.snapshot_stats()

    
    def snapshot_stats(self):
        self.stats = { }
        for cc, ns, tt, ct, callers in self.timings.items():
            callers = callers.copy()
            nc = 0
            for callcnt in callers.values():
                nc += callcnt
                self.stats[func] = (cc, nc, tt, ct, callers)
                return None

    
    def run(self, cmd):
        import __main__
        dict = __main__.__dict__
        return self.runctx(cmd, dict, dict)

    
    def runctx(self, cmd, globals, locals):
        self.set_cmd(cmd)
        sys.setprofile(self.dispatcher)
        
        try:
            exec(cmd, globals, locals)
            sys.setprofile(None)
        except:
            sys.setprofile(None)

        return self

    
    def runcall(self, func, *args, **kw):
        self.set_cmd(repr(func))
        sys.setprofile(self.dispatcher)
    # WARNING: Decompyle incomplete

    
    def calibrate(self, m, verbose = (0,)):
        if self.__class__ is not Profile:
            raise TypeError('Subclasses must override .calibrate().')
        saved_bias = self.bias
        self.bias = 0
        
        try:
            self.bias = saved_bias
            return self._calibrate_inner(m, verbose)
        except:
            self.bias = saved_bias


    
    def _calibrate_inner(self, m, verbose):
        get_time = self.get_time
        
        def f1(n):
            for i in range(n):
                x = 1
                return None

        
        def f(m, f1 = (f1,)):
            for i in range(m):
                f1(100)
                return None

        f(m)
        t0 = get_time()
        f(m)
        t1 = get_time()
        elapsed_noprofile = t1 - t0
        if verbose:
            print('elapsed time without profiling =', elapsed_noprofile)
        p = Profile()
        t0 = get_time()
        p.runctx('f(m)', globals(), locals())
        t1 = get_time()
        elapsed_profile = t1 - t0
        if verbose:
            print('elapsed time with profiling =', elapsed_profile)
        total_calls = 0
        reported_time = 0
        for filename, line, funcname in p.timings.items():
            (cc, ns, tt, ct, callers) = None
            if funcname in ('f', 'f1'):
                total_calls += cc
                reported_time += tt
            if verbose:
                print("'CPU seconds' profiler reported =", reported_time)
                print('total # calls =', total_calls)
        if total_calls != m + 1:
            raise ValueError('internal error: total calls = %d' % total_calls)
        mean = (reported_time - elapsed_noprofile) / 2 / total_calls
        if verbose:
            print('mean stopwatch overhead per profile event =', mean)
        return mean



def main():
    import os
    OptionParser = OptionParser
    import optparse
    usage = 'profile.py [-o output_file_path] [-s sort] [-m module | scriptfile] [arg] ...'
    parser = OptionParser(usage = usage)
    parser.allow_interspersed_args = False
    parser.add_option('-o', '--outfile', dest = 'outfile', help = 'Save stats to <outfile>', default = None)
    parser.add_option('-m', dest = 'module', action = 'store_true', help = 'Profile a library module.', default = False)
    parser.add_option('-s', '--sort', dest = 'sort', help = 'Sort order when printing to stdout, based on pstats.Stats class', default = -1)
    if not sys.argv[1:]:
        parser.print_usage()
        sys.exit(2)
    (options, args) = parser.parse_args()
    sys.argv[:] = args
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    main()
    return None
