# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: timeit.pyc (Python 3.11)

"""Tool for measuring execution time of small code snippets.

This module avoids a number of common traps for measuring execution
times.  See also Tim Peters' introduction to the Algorithms chapter in
the Python Cookbook, published by O'Reilly.

Library usage: see the Timer class.

Command line usage:
    python timeit.py [-n N] [-r N] [-s S] [-p] [-h] [--] [statement]

Options:
  -n/--number N: how many times to execute 'statement' (default: see below)
  -r/--repeat N: how many times to repeat the timer (default 5)
  -s/--setup S: statement to be executed once initially (default 'pass').
                Execution time of this setup statement is NOT timed.
  -p/--process: use time.process_time() (default is time.perf_counter())
  -v/--verbose: print raw timing results; repeat for more digits precision
  -u/--unit: set the output time unit (nsec, usec, msec, or sec)
  -h/--help: print this usage message and exit
  --: separate options from statement, use when statement starts with -
  statement: statement to be timed (default 'pass')

A multi-line statement may be given by specifying each line as a
separate argument; indented lines are possible by enclosing an
argument in quotes and using leading spaces.  Multiple -s options are
treated similarly.

If -n is not given, a suitable number of loops is calculated by trying
increasing numbers from the sequence 1, 2, 5, 10, 20, 50, ... until the
total time is at least 0.2 seconds.

Note: there is a certain baseline overhead associated with executing a
pass statement.  It differs between versions.  The code here doesn't try
to hide it, but you should be aware of it.  The baseline overhead can be
measured by invoking the program without arguments.

Classes:

    Timer

Functions:

    timeit(string, string) -> float
    repeat(string, string) -> list
    default_timer() -> float

"""
import gc
import itertools
import sys
import time
__all__ = [
    'Timer',
    'timeit',
    'repeat',
    'default_timer']
dummy_src_name = '<timeit-src>'
default_number = 1000000
default_repeat = 5
default_timer = time.perf_counter
_globals = globals
template = '\ndef inner(_it, _timer{init}):\n    {setup}\n    _t0 = _timer()\n    for _i in _it:\n        {stmt}\n        pass\n    _t1 = _timer()\n    return _t1 - _t0\n'

def reindent(src, indent):
    '''Helper to reindent a multi-line statement.'''
    return src.replace('\n', '\n' + ' ' * indent)


class Timer:
    """Class for timing execution speed of small code snippets.

    The constructor takes a statement to be timed, an additional
    statement used for setup, and a timer function.  Both statements
    default to 'pass'; the timer function is platform-dependent (see
    module doc string).  If 'globals' is specified, the code will be
    executed within that namespace (as opposed to inside timeit's
    namespace).

    To measure the execution time of the first statement, use the
    timeit() method.  The repeat() method is a convenience to call
    timeit() multiple times and return a list of results.

    The statements may contain newlines, as long as they don't contain
    multi-line string literals.
    """
    
    def __init__(self, stmt, setup, timer, globals = ('pass', 'pass', default_timer, None)):
        '''Constructor.  See class doc string.'''
        self.timer = timer
        local_ns = { }
    # WARNING: Decompyle incomplete

    
    def print_exc(self, file = (None,)):
        '''Helper to print a traceback from the timed code.

        Typical use:

            t = Timer(...)       # outside the try/except
            try:
                t.timeit(...)    # or t.repeat(...)
            except:
                t.print_exc()

        The advantage over the standard traceback is that source lines
        in the compiled template will be displayed.

        The optional file argument directs where the traceback is
        sent; it defaults to sys.stderr.
        '''
        import linecache
        import traceback
    # WARNING: Decompyle incomplete

    
    def timeit(self, number = (default_number,)):
        """Time 'number' executions of the main statement.

        To be precise, this executes the setup statement once, and
        then returns the time it takes to execute the main statement
        a number of times, as float seconds if using the default timer.   The
        argument is the number of times through the loop, defaulting
        to one million.  The main statement, the setup statement and
        the timer function to be used are passed to the constructor.
        """
        it = itertools.repeat(None, number)
        gcold = gc.isenabled()
        gc.disable()
        
        try:
            timing = self.inner(it, self.timer)
            if gcold:
                gc.enable()
            elif gcold:
                gc.enable()

        return timing

    
    def repeat(self, repeat, number = (default_repeat, default_number)):
        """Call timeit() a few times.

        This is a convenience function that calls the timeit()
        repeatedly, returning a list of results.  The first argument
        specifies how many times to call timeit(), defaulting to 5;
        the second argument specifies the timer argument, defaulting
        to one million.

        Note: it's tempting to calculate mean and standard deviation
        from the result vector and report these.  However, this is not
        very useful.  In a typical case, the lowest value gives a
        lower bound for how fast your machine can run the given code
        snippet; higher values in the result vector are typically not
        caused by variability in Python's speed, but by other
        processes interfering with your timing accuracy.  So the min()
        of the result is probably the only number you should be
        interested in.  After that, you should look at the entire
        vector and apply common sense rather than statistics.
        """
        r = []
        for i in range(repeat):
            t = self.timeit(number)
            r.append(t)
            return r

    
    def autorange(self, callback = (None,)):
        '''Return the number of loops and time taken so that total time >= 0.2.

        Calls the timeit method with increasing numbers from the sequence
        1, 2, 5, 10, 20, 50, ... until the time taken is at least 0.2
        second.  Returns (number, time_taken).

        If *callback* is given and is not None, it will be called after
        each trial with two arguments: ``callback(number, time_taken)``.
        '''
        i = 1
        for j in (1, 2, 5):
            number = i * j
            time_taken = self.timeit(number)
            if callback:
                callback(number, time_taken)
            if time_taken >= 0.2:
                
                return None, (number, time_taken)



def timeit(stmt, setup, timer, number, globals = ('pass', 'pass', default_timer, default_number, None)):
    '''Convenience function to create Timer object and call timeit method.'''
    return Timer(stmt, setup, timer, globals).timeit(number)


def repeat(stmt, setup, timer, repeat, number, globals = ('pass', 'pass', default_timer, default_repeat, default_number, None)):
    '''Convenience function to create Timer object and call repeat method.'''
    return Timer(stmt, setup, timer, globals).repeat(repeat, number)


def main(args = None, *, _wrap_timer):
    """Main program, used when run as a script.

    The optional 'args' argument specifies the command line to be parsed,
    defaulting to sys.argv[1:].

    The return value is an exit code to be passed to sys.exit(); it
    may be None to indicate success.

    When an exception happens during timing, a traceback is printed to
    stderr and the return value is 1.  Exceptions at other times
    (including the template compilation) are not caught.

    '_wrap_timer' is an internal interface used for unit testing.  If it
    is not None, it must be a callable that accepts a timer function
    and returns another timer function (used for unit testing).
    """
    pass
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    sys.exit(main())
    return None
