# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: message_factory.pyc (Python 3.11)

"""Provides a factory class for generating dynamic messages.

The easiest way to use this class is if you have access to the FileDescriptor
protos containing the messages you want to create you can just do the following:

message_classes = message_factory.GetMessages(iterable_of_file_descriptors)
my_proto_instance = message_classes['some.proto.package.MessageName']()
"""
__author__ = 'matthewtoia@google.com (Matt Toia)'
import warnings
from google.protobuf.internal import api_implementation
from google.protobuf import descriptor_pool
from google.protobuf import message
if api_implementation.Type() == 'python':
    from google.protobuf.internal import python_message as message_impl
else:
    from google.protobuf.pyext import cpp_message as message_impl
_GENERATED_PROTOCOL_MESSAGE_TYPE = message_impl.GeneratedProtocolMessageType

def GetMessageClass(descriptor):
    '''Obtains a proto2 message class based on the passed in descriptor.

  Passing a descriptor with a fully qualified name matching a previous
  invocation will cause the same class to be returned.

  Args:
    descriptor: The descriptor to build from.

  Returns:
    A class describing the passed in descriptor.
  '''
    concrete_class = getattr(descriptor, '_concrete_class', None)
    if concrete_class:
        return concrete_class
    return None(descriptor)


def GetMessageClassesForFiles(files, pool):
    '''Gets all the messages from specified files.

  This will find and resolve dependencies, failing if the descriptor
  pool cannot satisfy them.

  Args:
    files: The file names to extract messages from.
    pool: The descriptor pool to find the files including the dependent
      files.

  Returns:
    A dictionary mapping proto names to the message classes.
  '''
    result = { }
    for file_name in files:
        file_desc = pool.FindFileByName(file_name)
        for desc in file_desc.message_types_by_name.values():
            result[desc.full_name] = GetMessageClass(desc)
            for extension in file_desc.extensions_by_name.values():
                extended_class = GetMessageClass(extension.containing_type)
                if api_implementation.Type() != 'python' and extension is not pool.FindExtensionByNumber(extension.containing_type, extension.number):
                    raise ValueError('Double registration of Extensions')
                if extension.message_type:
                    GetMessageClass(extension.message_type)
                return result


def _InternalCreateMessageClass(descriptor):
    '''Builds a proto2 message class based on the passed in descriptor.

  Args:
    descriptor: The descriptor to build from.

  Returns:
    A class describing the passed in descriptor.
  '''
    descriptor_name = descriptor.name
    result_class = _GENERATED_PROTOCOL_MESSAGE_TYPE(descriptor_name, (message.Message,), {
        'DESCRIPTOR': descriptor,
        '__module__': None })
    for field in descriptor.fields:
        if field.message_type:
            GetMessageClass(field.message_type)
        for extension in result_class.DESCRIPTOR.extensions:
            extended_class = GetMessageClass(extension.containing_type)
            if api_implementation.Type() != 'python':
                pool = extension.containing_type.file.pool
                if extension is not pool.FindExtensionByNumber(extension.containing_type, extension.number):
                    raise ValueError('Double registration of Extensions')
            if extension.message_type:
                GetMessageClass(extension.message_type)
            return result_class


class MessageFactory(object):
    '''Factory for creating Proto2 messages from descriptors in a pool.'''
    
    def __init__(self, pool = (None,)):
        '''Initializes a new factory.'''
        if not pool:
            pass
        self.pool = descriptor_pool.DescriptorPool()

    
    def GetPrototype(self, descriptor):
        '''Obtains a proto2 message class based on the passed in descriptor.

    Passing a descriptor with a fully qualified name matching a previous
    invocation will cause the same class to be returned.

    Args:
      descriptor: The descriptor to build from.

    Returns:
      A class describing the passed in descriptor.
    '''
        warnings.warn('MessageFactory class is deprecated. Please use GetMessageClass() instead of MessageFactory.GetPrototype. MessageFactory class will be removed after 2024.', stacklevel = 2)
        return GetMessageClass(descriptor)

    
    def CreatePrototype(self, descriptor):
        """Builds a proto2 message class based on the passed in descriptor.

    Don't call this function directly, it always creates a new class. Call
    GetMessageClass() instead.

    Args:
      descriptor: The descriptor to build from.

    Returns:
      A class describing the passed in descriptor.
    """
        warnings.warn('Directly call CreatePrototype is wrong. Please use GetMessageClass() method instead. Directly use CreatePrototype will raise error after July 2023.', stacklevel = 2)
        return _InternalCreateMessageClass(descriptor)

    
    def GetMessages(self, files):
        '''Gets all the messages from a specified file.

    This will find and resolve dependencies, failing if the descriptor
    pool cannot satisfy them.

    Args:
      files: The file names to extract messages from.

    Returns:
      A dictionary mapping proto names to the message classes. This will include
      any dependent messages as well as any messages defined in the same file as
      a specified message.
    '''
        warnings.warn('MessageFactory class is deprecated. Please use GetMessageClassesForFiles() instead of MessageFactory.GetMessages(). MessageFactory class will be removed after 2024.', stacklevel = 2)
        return GetMessageClassesForFiles(files, self.pool)



def GetMessages(file_protos, pool = (None,)):
    '''Builds a dictionary of all the messages available in a set of files.

  Args:
    file_protos: Iterable of FileDescriptorProto to build messages out of.
    pool: The descriptor pool to add the file protos.

  Returns:
    A dictionary mapping proto names to the message classes. This will include
    any dependent messages as well as any messages defined in the same file as
    a specified message.
  '''
    pass
# WARNING: Decompyle incomplete
