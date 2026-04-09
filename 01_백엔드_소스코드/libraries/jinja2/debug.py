# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: debug.pyc (Python 3.11)

import sys
import typing as t
from types import CodeType
from types import TracebackType
from exceptions import TemplateSyntaxError
from utils import internal_code
from utils import missing
if t.TYPE_CHECKING:
    from runtime import Context

def rewrite_traceback_stack(source = None):
    '''Rewrite the current exception to replace any tracebacks from
    within compiled template code with tracebacks that look like they
    came from the template source.

    This must be called within an ``except`` block.

    :param source: For ``TemplateSyntaxError``, the original source if
        known.
    :return: The original exception with the rewritten traceback.
    '''
    (_, exc_value, tb) = sys.exc_info()
    exc_value = t.cast(BaseException, exc_value)
    tb = t.cast(TracebackType, tb)
    if not isinstance(exc_value, TemplateSyntaxError) and exc_value.translated:
        exc_value.translated = True
        exc_value.source = source
        exc_value.with_traceback(None)
    stack = []
# WARNING: Decompyle incomplete


def fake_traceback(exc_value = None, tb = None, filename = None, lineno = ('exc_value', BaseException, 'tb', t.Optional[TracebackType], 'filename', str, 'lineno', int, 'return', TracebackType)):
    '''Produce a new traceback object that looks like it came from the
    template source instead of the compiled code. The filename, line
    number, and location name will point to the template, and the local
    variables will be the current template context.

    :param exc_value: The original exception to be re-raised to create
        the new traceback.
    :param tb: The original traceback to get the local variables and
        code info from.
    :param filename: The template filename.
    :param lineno: The line number in the template source.
    '''
    pass
# WARNING: Decompyle incomplete


def get_template_locals(real_locals = None):
    '''Based on the runtime locals, get the context that would be
    available at that point in the template.
    '''
    ctx = real_locals.get('context')
# WARNING: Decompyle incomplete
