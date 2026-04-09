# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: errors.pyc (Python 3.11)

'''
Numba-specific errors and warnings.
'''
import abc
import contextlib
import os
import warnings
import numba.core.config as numba
import numpy as np
from collections import defaultdict
from functools import wraps
from abc import abstractmethod
__all__ = []

def _is_numba_core_config_loaded():
    '''
    To detect if numba.core.config has been initialized due to circular imports.
    '''
    
    try:
        numba.core.config
        return True
    except AttributeError:
        return False



class NumbaWarning(Warning):
    pass
# WARNING: Decompyle incomplete


class NumbaPerformanceWarning(NumbaWarning):
    '''
    Warning category for when an operation might not be
    as fast as expected.
    '''
    pass


class NumbaDeprecationWarning(DeprecationWarning, NumbaWarning):
    '''
    Warning category for use of a deprecated feature.
    '''
    pass


class NumbaPendingDeprecationWarning(PendingDeprecationWarning, NumbaWarning):
    '''
    Warning category for use of a feature that is pending deprecation.
    '''
    pass


class NumbaParallelSafetyWarning(NumbaWarning):
    '''
    Warning category for when an operation in a prange
    might not have parallel semantics.
    '''
    pass


class NumbaTypeSafetyWarning(NumbaWarning):
    '''
    Warning category for unsafe casting operations.
    '''
    pass


class NumbaExperimentalFeatureWarning(NumbaWarning):
    '''
    Warning category for using an experimental feature.
    '''
    pass


class NumbaInvalidConfigWarning(NumbaWarning):
    '''
    Warning category for using an invalid configuration.
    '''
    pass


class NumbaPedanticWarning(NumbaWarning):
    pass
# WARNING: Decompyle incomplete


class NumbaIRAssumptionWarning(NumbaPedanticWarning):
    '''
    Warning category for reporting an IR assumption violation.
    '''
    pass


class NumbaDebugInfoWarning(NumbaWarning):
    '''
    Warning category for an issue with the emission of debug information.
    '''
    pass


class NumbaSystemWarning(NumbaWarning):
    '''
    Warning category for an issue with the system configuration.
    '''
    pass


def _ColorScheme():
    '''_ColorScheme'''
    code = (lambda self, msg: pass)()
    errmsg = (lambda self, msg: pass)()
    filename = (lambda self, msg: pass)()
    indicate = (lambda self, msg: pass)()
    highlight = (lambda self, msg: pass)()
    reset = (lambda self, msg: pass)()

_ColorScheme = <NODE:27>(_ColorScheme, '_ColorScheme', metaclass = abc.ABCMeta)

class _DummyColorScheme(_ColorScheme):
    
    def __init__(self, theme = (None,)):
        pass

    
    def code(self, msg):
        pass

    
    def errmsg(self, msg):
        pass

    
    def filename(self, msg):
        pass

    
    def indicate(self, msg):
        pass

    
    def highlight(self, msg):
        pass

    
    def reset(self, msg):
        pass


_termcolor_inst = None

try:
    import colorama
    colorama_version = getattr(colorama, '__version__', '0.0.0')
    if (lambda .0: [ int(x) for x in .0 ])(colorama_version.split('.')()) < (0, 3, 9):
        msg = 'Insufficiently recent colorama version found. Numba requires colorama >= 0.3.9'
        warnings.warn(msg)
        raise ImportError
    if os.environ.get('NUMBA_DISABLE_ERROR_MESSAGE_HIGHLIGHTING', None):
        raise ImportError
    from colorama import init, reinit, deinit, Fore, Style
    
    class ColorShell(object):
        _has_initialized = False
        
        def __init__(self):
            init()
            self._has_initialized = True

        
        def __enter__(self):
            if self._has_initialized:
                reinit()
                return None

        
        def __exit__(self, *exc_detail):
            Style.RESET_ALL
            deinit()


    
    class reset_terminal(object):
        
        def __init__(self):
            self._buf = bytearray(b'')

        
        def __enter__(self):
            return self._buf

        
        def __exit__(self, *exc_detail):
            pass


    themes = { }
    themes['no_color'] = {
        'code': None,
        'errmsg': None,
        'filename': None,
        'indicate': None,
        'highlight': None,
        'reset': None }
    themes['dark_bg'] = {
        'code': Fore.BLUE,
        'errmsg': Fore.YELLOW,
        'filename': Fore.WHITE,
        'indicate': Fore.GREEN,
        'highlight': Fore.RED,
        'reset': Style.RESET_ALL }
    themes['light_bg'] = {
        'code': Fore.BLUE,
        'errmsg': Fore.BLACK,
        'filename': Fore.MAGENTA,
        'indicate': Fore.BLACK,
        'highlight': Fore.RED,
        'reset': Style.RESET_ALL }
    themes['blue_bg'] = {
        'code': Fore.WHITE,
        'errmsg': Fore.YELLOW,
        'filename': Fore.MAGENTA,
        'indicate': Fore.CYAN,
        'highlight': Fore.RED,
        'reset': Style.RESET_ALL }
    themes['jupyter_nb'] = {
        'code': Fore.BLACK,
        'errmsg': Fore.BLACK,
        'filename': Fore.GREEN,
        'indicate': Fore.CYAN,
        'highlight': Fore.RED,
        'reset': Style.RESET_ALL }
    default_theme = themes['no_color']
    
    class HighlightColorScheme(_DummyColorScheme):
        
        def __init__(self, theme = (default_theme,)):
            self._code = theme['code']
            self._errmsg = theme['errmsg']
            self._filename = theme['filename']
            self._indicate = theme['indicate']
            self._highlight = theme['highlight']
            self._reset = theme['reset']
            _DummyColorScheme.__init__(self, theme = theme)

        
        def _markup(self, msg, color, style = (None, Style.BRIGHT)):
            features = ''
            if color:
                features += color
            if style:
                features += style
            ColorShell()
            mu = reset_terminal()
            mu += features.encode('utf-8')
            mu += msg.encode('utf-8')
            None(None, None)

        
        def code(self, msg):
            return self._markup(msg, self._code)

        
        def errmsg(self, msg):
            return self._markup(msg, self._errmsg)

        
        def filename(self, msg):
            return self._markup(msg, self._filename)

        
        def indicate(self, msg):
            return self._markup(msg, self._indicate)

        
        def highlight(self, msg):
            return self._markup(msg, self._highlight)

        
        def reset(self, msg):
            return self._markup(msg, self._reset)


    
    def termcolor():
        pass
    # WARNING: Decompyle incomplete

except ImportError:
    
    class NOPColorScheme(_DummyColorScheme):
        
        def __init__(self, theme = (None,)):
            pass
        # WARNING: Decompyle incomplete

        
        def code(self, msg):
            return msg

        
        def errmsg(self, msg):
            return msg

        
        def filename(self, msg):
            return msg

        
        def indicate(self, msg):
            return msg

        
        def highlight(self, msg):
            return msg

        
        def reset(self, msg):
            return msg


    
    def termcolor():
        pass
    # WARNING: Decompyle incomplete


pedantic_warning_info = '\nThis warning came from an internal pedantic check. Please report the warning\nmessage and traceback, along with a minimal reproducer at:\nhttps://github.com/numba/numba/issues/new?template=bug_report.md\n'
feedback_details = '\nPlease report the error message and traceback, along with a minimal reproducer\nat: https://github.com/numba/numba/issues/new?template=bug_report.md\n\nIf more help is needed please feel free to speak to the Numba core developers\ndirectly at: https://gitter.im/numba/numba\n\nThanks in advance for your help in improving Numba!\n'
unsupported_error_info = '\nUnsupported functionality was found in the code Numba was trying to compile.\n\nIf this functionality is important to you please file a feature request at:\nhttps://github.com/numba/numba/issues/new?template=feature_request.md\n'
interpreter_error_info = '\nUnsupported Python functionality was found in the code Numba was trying to\ncompile. This error could be due to invalid code, does the code work\nwithout Numba? (To temporarily disable Numba JIT, set the `NUMBA_DISABLE_JIT`\nenvironment variable to non-zero, and then rerun the code).\n\nIf the code is valid and the unsupported functionality is important to you\nplease file a feature request at:\nhttps://github.com/numba/numba/issues/new?template=feature_request.md\n\nTo see Python/NumPy features supported by the latest release of Numba visit:\nhttps://numba.readthedocs.io/en/stable/reference/pysupported.html\nand\nhttps://numba.readthedocs.io/en/stable/reference/numpysupported.html\n'
constant_inference_info = "\nNumba could not make a constant out of something that it decided should be\na constant. This could well be a current limitation in Numba's internals,\nhowever please first check that your code is valid for compilation,\nparticularly with respect to string interpolation (not supported!) and\nthe requirement of compile time constants as arguments to exceptions:\nhttps://numba.readthedocs.io/en/stable/reference/pysupported.html?highlight=exceptions#constructs\n\nIf the code is valid and the unsupported functionality is important to you\nplease file a feature request at:\nhttps://github.com/numba/numba/issues/new?template=feature_request.md\n\nIf you think your code should work with Numba. %s\n" % feedback_details
typing_error_info = '\nThis is not usually a problem with Numba itself but instead often caused by\nthe use of unsupported features or an issue in resolving types.\n\nTo see Python/NumPy features supported by the latest release of Numba visit:\nhttps://numba.readthedocs.io/en/stable/reference/pysupported.html\nand\nhttps://numba.readthedocs.io/en/stable/reference/numpysupported.html\n\nFor more information about typing errors and how to debug them visit:\nhttps://numba.readthedocs.io/en/stable/user/troubleshoot.html#my-code-doesn-t-compile\n\nIf you think your code should work with Numba, please report the error message\nand traceback, along with a minimal reproducer at:\nhttps://github.com/numba/numba/issues/new?template=bug_report.md\n'
reportable_issue_info = f'''\n-------------------------------------------------------------------------------\nThis should not have happened, a problem has occurred in Numba\'s internals.\nYou are currently using Numba version {numba.__version__!s}.\n{feedback_details!s}\n'''
error_extras = dict()
error_extras['unsupported_error'] = unsupported_error_info
error_extras['typing'] = typing_error_info
error_extras['reportable'] = reportable_issue_info
error_extras['interpreter'] = interpreter_error_info
error_extras['constant_inference'] = constant_inference_info

def deprecated(arg):
    """Define a deprecation decorator.
    An optional string should refer to the new API to be used instead.

    Example:
      @deprecated
      def old_func(): ...

      @deprecated('new_func')
      def old_func(): ..."""
    pass
# WARNING: Decompyle incomplete


class WarningsFixer(object):
    '''
    An object "fixing" warnings of a given category caught during
    certain phases.  The warnings can have their filename and lineno fixed,
    and they are deduplicated as well.

    When used as a context manager, any warnings caught by `.catch_warnings()`
    will be flushed at the exit of the context manager.
    '''
    
    def __init__(self, category):
        self._category = category
        self._warnings = defaultdict(set)

    catch_warnings = (lambda self, filename, lineno = (None, None): pass# WARNING: Decompyle incomplete
)()
    
    def flush(self):
        '''
        Emit all stored warnings.
        '''
        
        def key(arg):
            return str(arg) + str(id(arg))

        for filename, lineno, category in sorted(self._warnings.items(), key = key):
            messages = None
            for msg in sorted(messages):
                warnings.warn_explicit(msg, category, filename, lineno)
                self._warnings.clear()
                return None

    
    def __enter__(self):
        pass

    
    def __exit__(self, exc_type, exc_value, traceback):
        self.flush()



class NumbaError(Exception):
    pass
# WARNING: Decompyle incomplete


class UnsupportedError(NumbaError):
    '''
    Numba does not have an implementation for this functionality.
    '''
    pass


class UnsupportedBytecodeError(Exception):
    pass
# WARNING: Decompyle incomplete


class UnsupportedRewriteError(UnsupportedError):
    '''UnsupportedError from rewrite passes
    '''
    pass


class IRError(NumbaError):
    '''
    An error occurred during Numba IR generation.
    '''
    pass


class RedefinedError(IRError):
    '''
    An error occurred during interpretation of IR due to variable redefinition.
    '''
    pass


class NotDefinedError(IRError):
    pass
# WARNING: Decompyle incomplete


class VerificationError(IRError):
    """
    An error occurred during IR verification. Once Numba's internal
    representation (IR) is constructed it is then verified to ensure that
    terminators are both present and in the correct places within the IR. If
    it is the case that this condition is not met, a VerificationError is
    raised.
    """
    pass


class DeprecationError(NumbaError):
    '''
    Functionality is deprecated.
    '''
    pass


class LoweringError(NumbaError):
    pass
# WARNING: Decompyle incomplete


class UnsupportedParforsError(NumbaError):
    '''
    An error occurred because parfors is not supported on the platform.
    '''
    pass


class ForbiddenConstruct(LoweringError):
    '''
    A forbidden Python construct was encountered (e.g. use of locals()).
    '''
    pass


class TypingError(NumbaError):
    '''
    A type inference failure.
    '''
    pass


class UntypedAttributeError(TypingError):
    pass
# WARNING: Decompyle incomplete


class ByteCodeSupportError(NumbaError):
    pass
# WARNING: Decompyle incomplete


class CompilerError(NumbaError):
    '''
    Some high-level error in the compiler.
    '''
    pass


class ConstantInferenceError(NumbaError):
    pass
# WARNING: Decompyle incomplete


class InternalError(NumbaError):
    pass
# WARNING: Decompyle incomplete


class InternalTargetMismatchError(InternalError):
    pass
# WARNING: Decompyle incomplete


class NonexistentTargetError(InternalError):
    '''For signalling that a target that does not exist was requested.
    '''
    pass


class RequireLiteralValue(TypingError):
    """
    For signalling that a function's typing requires a constant value for
    some of its arguments.
    """
    pass


class ForceLiteralArg(NumbaError):
    pass
# WARNING: Decompyle incomplete


class LiteralTypingError(TypingError):
    '''
    Failure in typing a Literal type
    '''
    pass


class NumbaValueError(TypingError):
    pass


class NumbaTypeError(TypingError):
    pass


class NumbaAttributeError(TypingError):
    pass


class NumbaAssertionError(TypingError):
    pass


class NumbaNotImplementedError(TypingError):
    pass


class NumbaKeyError(TypingError):
    pass


class NumbaIndexError(TypingError):
    pass


class NumbaRuntimeError(NumbaError):
    pass


def _format_msg(fmt, args, kwargs):
    if not args and kwargs:
        return fmt
# WARNING: Decompyle incomplete

_numba_path = os.path.dirname(__file__)
loc_info = { }
new_error_context = (lambda fmt_: pass# WARNING: Decompyle incomplete
)()
(lambda .0: pass# WARNING: Decompyle incomplete
) += globals().items()()
