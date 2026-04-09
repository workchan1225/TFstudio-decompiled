# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: runner.pyc (Python 3.11)

'''Running tests'''
import sys
import time
import warnings
from  import result
from case import _SubTest
from signals import registerResult
__unittest = True

class _WritelnDecorator(object):
    """Used to decorate file-like objects with a handy 'writeln' method"""
    
    def __init__(self, stream):
        self.stream = stream

    
    def __getattr__(self, attr):
        if attr in ('stream', '__getstate__'):
            raise AttributeError(attr)
        return getattr(self.stream, attr)

    
    def writeln(self, arg = (None,)):
        if arg:
            self.write(arg)
        self.write('\n')



class TextTestResult(result.TestResult):
    pass
# WARNING: Decompyle incomplete


class TextTestRunner(object):
    '''A test runner class that displays results in textual form.

    It prints out the names of tests as they are run, errors as they
    occur, and a summary of the results at the end of the test run.
    '''
    resultclass = TextTestResult
    
    def __init__(self, stream, descriptions, verbosity, failfast, buffer = None, resultclass = (None, True, 1, False, False, None, None), warnings = {
        'tb_locals': False }, *, tb_locals):
        '''Construct a TextTestRunner.

        Subclasses should accept **kwargs to ensure compatibility as the
        interface changes.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _makeResult(self):
        return self.resultclass(self.stream, self.descriptions, self.verbosity)

    
    def run(self, test):
        '''Run the given test case or test suite.'''
        result = self._makeResult()
        registerResult(result)
        result.failfast = self.failfast
        result.buffer = self.buffer
        result.tb_locals = self.tb_locals
        warnings.catch_warnings()
        if self.warnings:
            warnings.simplefilter(self.warnings)
            if self.warnings in ('default', 'always'):
                warnings.filterwarnings('module', category = DeprecationWarning, message = 'Please use assert\\w+ instead.')
        startTime = time.perf_counter()
        startTestRun = getattr(result, 'startTestRun', None)
    # WARNING: Decompyle incomplete
