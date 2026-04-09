# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: extension_dict.pyc (Python 3.11)

'''Contains _ExtensionDict class to represent extensions.
'''
from google.protobuf.internal import type_checkers
from google.protobuf.descriptor import FieldDescriptor

def _VerifyExtensionHandle(message, extension_handle):
    '''Verify that the given extension handle is valid.'''
    if not isinstance(extension_handle, FieldDescriptor):
        raise KeyError('HasExtension() expects an extension handle, got: %s' % extension_handle)
    if not extension_handle.is_extension:
        raise KeyError('"%s" is not an extension.' % extension_handle.full_name)
    if not extension_handle.containing_type:
        raise KeyError('"%s" is missing a containing_type.' % extension_handle.full_name)
    if extension_handle.containing_type is not message.DESCRIPTOR:
        raise KeyError(f'''Extension "{extension_handle.full_name!s}" extends message type "{extension_handle.containing_type.full_name!s}", but this message is of type "{message.DESCRIPTOR.full_name!s}".''')


class _ExtensionDict(object):
    '''Dict-like container for Extension fields on proto instances.

  Note that in all cases we expect extension handles to be
  FieldDescriptors.
  '''
    
    def __init__(self, extended_message):
        '''
    Args:
      extended_message: Message instance for which we are the Extensions dict.
    '''
        self._extended_message = extended_message

    
    def __getitem__(self, extension_handle):
        '''Returns the current value of the given extension handle.'''
        _VerifyExtensionHandle(self._extended_message, extension_handle)
        result = self._extended_message._fields.get(extension_handle)
    # WARNING: Decompyle incomplete

    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        my_fields = None._extended_message.ListFields()
        other_fields = other._extended_message.ListFields()
        my_fields = my_fields()
        other_fields = other_fields()
        return my_fields == other_fields

    
    def __ne__(self, other):
        return not (self == other)

    
    def __len__(self):
        fields = self._extended_message.ListFields()
        extension_fields = fields()
        return len(extension_fields)

    
    def __hash__(self):
        raise TypeError('unhashable object')

    
    def __setitem__(self, extension_handle, value):
        '''If extension_handle specifies a non-repeated, scalar extension
    field, sets the value of that field.
    '''
        _VerifyExtensionHandle(self._extended_message, extension_handle)
        if extension_handle.label == FieldDescriptor.LABEL_REPEATED or extension_handle.cpp_type == FieldDescriptor.CPPTYPE_MESSAGE:
            raise TypeError('Cannot assign to extension "%s" because it is a repeated or composite type.' % extension_handle.full_name)
        type_checker = type_checkers.GetTypeChecker(extension_handle)
        self._extended_message._fields[extension_handle] = type_checker.CheckValue(value)
        self._extended_message._Modified()

    
    def __delitem__(self, extension_handle):
        self._extended_message.ClearExtension(extension_handle)

    
    def _FindExtensionByName(self, name):
        '''Tries to find a known extension with the specified name.

    Args:
      name: Extension full name.

    Returns:
      Extension field descriptor.
    '''
        descriptor = self._extended_message.DESCRIPTOR
        extensions = descriptor.file.pool._extensions_by_name[descriptor]
        return extensions.get(name, None)

    
    def _FindExtensionByNumber(self, number):
        '''Tries to find a known extension with the field number.

    Args:
      number: Extension field number.

    Returns:
      Extension field descriptor.
    '''
        descriptor = self._extended_message.DESCRIPTOR
        extensions = descriptor.file.pool._extensions_by_number[descriptor]
        return extensions.get(number, None)

    
    def __iter__(self):
        return self._extended_message.ListFields()()

    
    def __contains__(self, extension_handle):
