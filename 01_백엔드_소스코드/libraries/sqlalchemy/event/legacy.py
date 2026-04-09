# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: legacy.pyc (Python 3.11)

'''Routines to handle adaption of legacy call signatures,
generation of deprecation notes and docstrings.

'''
from __future__ import annotations
import typing
from typing import Any
from typing import Callable
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type
from typing import TypeVar
from registry import _ET
from registry import _ListenerFnType
from  import util
from util.compat import FullArgSpec
if typing.TYPE_CHECKING:
    from attr import _ClsLevelDispatch
    from base import _HasEventsDispatch
_F = TypeVar('_F', bound = Callable[(..., Any)])
_LegacySignatureType = Tuple[(str, List[str], Callable[(..., Any)])]

def _legacy_signature(since = None, argnames = None, converter = None):
    '''legacy sig decorator


    :param since: string version for deprecation warning
    :param argnames: list of strings, which is *all* arguments that the legacy
     version accepted, including arguments that are still there
    :param converter: lambda that will accept tuple of this full arg signature
     and return tuple of new arg signature.

    '''
    pass
# WARNING: Decompyle incomplete


def _omit_standard_example(fn = None):
    fn._omit_standard_example = True
    return fn


def _wrap_fn_for_legacy(dispatch_collection = None, fn = None, argspec = None):
    pass
# WARNING: Decompyle incomplete


def _indent(text = None, indent = None):
    pass
# WARNING: Decompyle incomplete


def _standard_listen_example(dispatch_collection = None, sample_target = None, fn = None):
    example_kw_arg = '\n'.join((lambda .0: pass# WARNING: Decompyle incomplete
)(dispatch_collection.arg_names[0:2]()), '    ')
    text = 'from sqlalchemy import event\n\n\n@event.listens_for(%(sample_target)s, \'%(event_name)s\')\ndef receive_%(event_name)s(%(named_event_arguments)s%(has_kw_arguments)s):\n    "listen for the \'%(event_name)s\' event"\n\n    # ... (event handling logic) ...\n'
    text %= {
        'current_since': ' (arguments as of %s)' % current_since if current_since else '',
        'event_name': fn.__name__,
        'has_kw_arguments': ', **kw' if dispatch_collection.has_kw else '',
        'named_event_arguments': ', '.join(dispatch_collection.arg_names),
        'example_kw_arg': example_kw_arg,
        'sample_target': sample_target }
    return text


def _legacy_listen_examples(dispatch_collection = None, sample_target = None, fn = None):
    text = ''
    for since, args, conv in dispatch_collection.legacy_signatures:
        text += '\n# DEPRECATED calling style (pre-%(since)s, will be removed in a future release)\n@event.listens_for(%(sample_target)s, \'%(event_name)s\')\ndef receive_%(event_name)s(%(named_event_arguments)s%(has_kw_arguments)s):\n    "listen for the \'%(event_name)s\' event"\n\n    # ... (event handling logic) ...\n' % {
            'since': since,
            'event_name': fn.__name__,
            'has_kw_arguments': ' **kw' if dispatch_collection.has_kw else '',
            'named_event_arguments': ', '.join(args),
            'sample_target': sample_target }
        return text


def _version_signature_changes(parent_dispatch_cls = None, dispatch_collection = None):
    pass
# WARNING: Decompyle incomplete


def _augment_fn_docs(dispatch_collection = None, parent_dispatch_cls = None, fn = None):
    pass
# WARNING: Decompyle incomplete
