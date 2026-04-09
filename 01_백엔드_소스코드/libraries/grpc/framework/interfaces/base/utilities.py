# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utilities.pyc (Python 3.11)

'''Utilities for use with the base interface of RPC Framework.'''
import collections
from grpc.framework.interfaces.base import base

def _Completion():
    '''_Completion'''
    __doc__ = 'A trivial implementation of base.Completion.'

_Completion = <NODE:27>(_Completion, '_Completion', base.Completion, collections.namedtuple('_Completion', ('terminal_metadata', 'code', 'message')))

def _Subscription():
    '''_Subscription'''
    __doc__ = 'A trivial implementation of base.Subscription.'

_Subscription = <NODE:27>(_Subscription, '_Subscription', base.Subscription, collections.namedtuple('_Subscription', ('kind', 'termination_callback', 'allowance', 'operator', 'protocol_receiver')))
_NONE_SUBSCRIPTION = _Subscription(base.Subscription.Kind.NONE, None, None, None, None)

def completion(terminal_metadata, code, message):
    '''Creates a base.Completion aggregating the given operation values.

    Args:
      terminal_metadata: A terminal metadata value for an operation.
      code: A code value for an operation.
      message: A message value for an operation.

    Returns:
      A base.Completion aggregating the given operation values.
    '''
    return _Completion(terminal_metadata, code, message)


def full_subscription(operator, protocol_receiver):
    '''Creates a "full" base.Subscription for the given base.Operator.

    Args:
      operator: A base.Operator to be used in an operation.
      protocol_receiver: A base.ProtocolReceiver to be used in an operation.

    Returns:
      A base.Subscription of kind base.Subscription.Kind.FULL wrapping the given
        base.Operator and base.ProtocolReceiver.
    '''
    return _Subscription(base.Subscription.Kind.FULL, None, None, operator, protocol_receiver)
