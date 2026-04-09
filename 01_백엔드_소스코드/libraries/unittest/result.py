# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: result.pyc (Python 3.11)

'''Test result object'''
import io
import sys
import traceback
from  import util
from functools import wraps
__unittest = True

def failfast(method):
    pass
# WARNING: Decompyle incomplete

STDOUT_LINE = '\nStdout:\n%s'
STDERR_LINE = '\nStderr:\n%s'

class TestResult(object):
    '''Holder for test result information.

    Test results are automatically managed by the TestCase and TestSuite
    classes, and do not need to be explicitly manipulated by writers of tests.

    Each instance holds the total number of tests run, and collections of
    failures and errors that occurred among those test runs. The collections
    contain tuples of (testcase, exceptioninfo), where exceptioninfo is the
    formatted traceback of the error that occurred.
    '''
    _previousTestClass = None
    _testRunEntered = False
    _moduleSetUpFailed = False
    
    def __init__(self, stream, descriptions, verbosity = (None, None, None)):
        self.failfast = False
        self.failures = []
        self.errors = []
        self.testsRun = 0
        self.skipped = []
        self.expectedFailures = []
        self.unexpectedSuccesses = []
        self.shouldStop = False
        self.buffer = False
        self.tb_locals = False
        self._stdout_buffer = None
        self._stderr_buffer = None
        self._original_stdout = sys.stdout
        self._original_stderr = sys.stderr
        self._mirrorOutput = False

    
    def printErrors(self):
        '''Called by TestRunner after test run'''
        pass

    
    def startTest(self, test):
        '''Called when the given test is about to be run'''
        False = self, self.testsRun += 1, .testsRun
        self._setupStdout()

    
    def _setupStdout(self):
        pass
    # WARNING: Decompyle incomplete

    
    def startTestRun(self):
        '''Called once before any tests are executed.

        See startTest for a method called before each test.
        '''
        pass

    
    def stopTest(self, test):
        '''Called when the given test has been run'''
        self._restoreStdout()
        self._mirrorOutput = False

    
    def _restoreStdout(self):
        if self.buffer:
            if self._mirrorOutput:
                output = sys.stdout.getvalue()
                error = sys.stderr.getvalue()
                if output:
                    if not output.endswith('\n'):
                        output += '\n'
                    self._original_stdout.write(STDOUT_LINE % output)
                if error:
                    if not error.endswith('\n'):
                        error += '\n'
                    self._original_stderr.write(STDERR_LINE % error)
            sys.stdout = self._original_stdout
            sys.stderr = self._original_stderr
            self._stdout_buffer.seek(0)
            self._stdout_buffer.truncate()
            self._stderr_buffer.seek(0)
            self._stderr_buffer.truncate()
            return None

    
    def stopTestRun(self):
        '''Called once after all tests are executed.

        See stopTest for a method called after each test.
        '''
        pass

    addError = (lambda self, test, err: self.errors.append((test, self._exc_info_to_string(err, test)))self._mirrorOutput = True)()
    addFailure = (lambda self, test, err: self.failures.append((test, self._exc_info_to_string(err, test)))self._mirrorOutput = True)()
    
    def addSubTest(self, test, subtest, err):
        """Called at the end of a subtest.
        'err' is None if the subtest ended successfully, otherwise it's a
        tuple of values as returned by sys.exc_info().
        """
        pass
    # WARNING: Decompyle incomplete

    
    def addSuccess(self, test):
        '''Called when a test has completed successfully'''
        pass

    
    def addSkip(self, test, reason):
        '''Called when a test is skipped.'''
        self.skipped.append((test, reason))

    
    def addExpectedFailure(self, test, err):
        '''Called when an expected failure/error occurred.'''
        self.expectedFailures.append((test, self._exc_info_to_string(err, test)))

    addUnexpectedSuccess = (lambda self, test: self.unexpectedSuccesses.append(test))()
    
    def wasSuccessful(self):
