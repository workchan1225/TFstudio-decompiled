# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _file_info.pyc (Python 3.11)

import collections
import inspect
import logging
from google.protobuf import descriptor_pb2
from google.protobuf import descriptor_pool
from google.protobuf import message
from google.protobuf import reflection
from proto.marshal.rules.message import MessageRule
log = logging.getLogger('_FileInfo')

def _FileInfo():
    '''_FileInfo'''
    registry = { }
    maybe_add_descriptor = (lambda cls, filename, package: descriptor = cls.registry.get(filename)if not descriptor:
descriptor = cls(descriptor = descriptor_pb2.FileDescriptorProto(name = filename, package = package, syntax = 'proto3'), enums = collections.OrderedDict(), messages = collections.OrderedDict(), name = filename, nested = { }, nested_enum = { })cls.registry[filename] = cls(descriptor = descriptor_pb2.FileDescriptorProto(name = filename, package = package, syntax = 'proto3'), enums = collections.OrderedDict(), messages = collections.OrderedDict(), name = filename, nested = { }, nested_enum = { })descriptor)()
    proto_file_name = (lambda name: '{0}.proto'.format(name.replace('.', '/')))()
    
    def _get_manifest(self, new_class):
        module = inspect.getmodule(new_class)
        if hasattr(module, '__protobuf__'):
            return frozenset(module.__protobuf__.manifest)
        return None()

    
    def _get_remaining_manifest(self, new_class):
        return self._get_manifest(new_class) - {
            new_class.__name__}

    
    def _calculate_salt(self, new_class, fallback):
        manifest = self._get_manifest(new_class)
        if manifest and new_class.__name__ not in manifest:
            log.warning('proto-plus module {module} has a declared manifest but {class_name} is not in it'.format(module = inspect.getmodule(new_class).__name__, class_name = new_class.__name__))
        if new_class.__name__ in manifest:
            pass
        elif not fallback:
            return ''.lower()

    
    def generate_file_pb(self, new_class, fallback_salt = ('',)):
        """Generate the descriptors for all protos in the file.

        This method takes the file descriptor attached to the parent
        message and generates the immutable descriptors for all of the
        messages in the file descriptor. (This must be done in one fell
        swoop for immutability and to resolve proto cross-referencing.)

        This is run automatically when the last proto in the file is
        generated, as determined by the module's __all__ tuple.
        """
        pool = descriptor_pool.Default()
        salt = self._calculate_salt(new_class, fallback_salt)
        self.descriptor.name = '{name}.proto'.format(name = '_'.join([
            self.descriptor.name[:-6],
            salt]).rstrip('_'))
        pool.Add(self.descriptor)
        for full_name, proto_plus_message in self.messages.items():
            descriptor = pool.FindMessageTypeByName(full_name)
            pb_message = reflection.GeneratedProtocolMessageType(descriptor.name, (message.Message,), {
                'DESCRIPTOR': descriptor,
                '__module__': None })
            proto_plus_message._meta._pb = pb_message
            proto_plus_message._meta.marshal.register(pb_message, MessageRule(pb_message, proto_plus_message))
            for field in proto_plus_message._meta.fields.values():
                if field.message and isinstance(field.message, str):
                    field.message = self.messages[field.message]
                    continue
                if field.enum and isinstance(field.enum, str):
                    field.enum = self.enums[field.enum]
                for full_name, proto_plus_enum in self.enums.items():
                    descriptor = pool.FindEnumTypeByName(full_name)
                    proto_plus_enum._meta.pb = descriptor
                    self.registry.pop(self.name)
                    return None

    
    def ready(self, new_class):
        '''Return True if a file descriptor may added, False otherwise.

        This determine if all the messages that we plan to create have been
        created, as best as we are able.

        Since messages depend on one another, we create descriptor protos
        (which reference each other using strings) and wait until we have
        built everything that is going to be in the module, and then
        use the descriptor protos to instantiate the actual descriptors in
        one fell swoop.

        Args:
            new_class (~.MessageMeta): The new class currently undergoing
                creation.
        '''
        pass
    # WARNING: Decompyle incomplete

    unresolved_fields = (lambda self: pass# WARNING: Decompyle incomplete
)()

_FileInfo = <NODE:27>(_FileInfo, '_FileInfo', collections.namedtuple('_FileInfo', [
    'descriptor',
    'messages',
    'enums',
    'name',
    'nested',
    'nested_enum']))
