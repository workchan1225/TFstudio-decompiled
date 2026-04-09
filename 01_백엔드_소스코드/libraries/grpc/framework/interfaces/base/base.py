# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

'''The base interface of RPC Framework.

Implementations of this interface support the conduct of "operations":
exchanges between two distinct ends of an arbitrary number of data payloads
and metadata such as a name for the operation, initial and terminal metadata
in each direction, and flow control. These operations may be used for transfers
of data, remote procedure calls, status indication, or anything else
applications choose.
'''
import abc
import enum
import threading

class NoSuchMethodError(Exception):
    pass
# WARNING: Decompyle incomplete


class Outcome(object):
    '''The outcome of an operation.

    Attributes:
      kind: A Kind value coarsely identifying how the operation terminated.
      code: An application-specific code value or None if no such value was
        provided.
      details: An application-specific details value or None if no such value was
        provided.
    '''
    Kind = <NODE:12>()


class Completion(abc.ABC):
    '''An aggregate of the values exchanged upon operation completion.

    Attributes:
      terminal_metadata: A terminal metadata value for the operation.
      code: A code value for the operation.
      message: A message value for the operation.
    '''
    pass


class OperationContext(abc.ABC):
    '''Provides operation-related information and action.'''
    outcome = (lambda self: raise NotImplementedError())()
    add_termination_callback = (lambda self, callback: raise NotImplementedError())()
    time_remaining = (lambda self: raise NotImplementedError())()
    cancel = (lambda self: raise NotImplementedError())()
    fail = (lambda self, exception: raise NotImplementedError())()


class Operator(abc.ABC):
    '''An interface through which to participate in an operation.'''
    advance = (lambda self, initial_metadata, payload, completion, allowance = (None, None, None, None): raise NotImplementedError())()


class ProtocolReceiver(abc.ABC):
    '''A means of receiving protocol values during an operation.'''
    context = (lambda self, protocol_context: raise NotImplementedError())()


class Subscription(abc.ABC):
    """Describes customer code's interest in values from the other side.

    Attributes:
      kind: A Kind value describing the overall kind of this value.
      termination_callback: A callable to be passed the Outcome associated with
        the operation after it has terminated. Must be non-None if kind is
        Kind.TERMINATION_ONLY. Must be None otherwise.
      allowance: A callable behavior that accepts positive integers representing
        the number of additional payloads allowed to be passed to the other side
        of the operation. Must be None if kind is Kind.FULL. Must not be None
        otherwise.
      operator: An Operator to be passed values from the other side of the
        operation. Must be non-None if kind is Kind.FULL. Must be None otherwise.
      protocol_receiver: A ProtocolReceiver to be passed protocol objects as they
        become available during the operation. Must be non-None if kind is
        Kind.FULL.
    """
    Kind = <NODE:12>()


class Servicer(abc.ABC):
    '''Interface for service implementations.'''
    service = (lambda self, group, method, context, output_operator: raise NotImplementedError())()


class End(abc.ABC):
    '''Common type for entry-point objects on both sides of an operation.'''
    start = (lambda self: raise NotImplementedError())()
    stop = (lambda self, grace: raise NotImplementedError())()
    operate = (lambda self, group, method, subscription, timeout, initial_metadata, payload, completion, protocol_options = (None, None, None, None): raise NotImplementedError())()
    operation_stats = (lambda self: raise NotImplementedError())()
    add_idle_action = (lambda self, action: raise NotImplementedError())()
