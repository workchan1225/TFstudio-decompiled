# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: builder.pyc (Python 3.11)

'''Builds descriptors, message classes and services for generated _pb2.py.

This file is only called in python generated _pb2.py files. It builds
descriptors, message classes and services that users can directly use
in generated code.
'''
__author__ = 'jieluo@google.com (Jie Luo)'
from google.protobuf.internal import enum_type_wrapper
from google.protobuf.internal import python_message
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()

def BuildMessageAndEnumDescriptors(file_des, module):
    '''Builds message and enum descriptors.

  Args:
    file_des: FileDescriptor of the .proto file
    module: Generated _pb2 module
  '''
    pass
# WARNING: Decompyle incomplete


def BuildTopDescriptorsAndMessages(file_des, module_name, module):
    '''Builds top level descriptors and message classes.

  Args:
    file_des: FileDescriptor of the .proto file
    module_name: str, the name of generated _pb2 module
    module: Generated _pb2 module
  '''
    pass
# WARNING: Decompyle incomplete


def AddHelpersToExtensions(file_des):
    '''no-op to keep old generated code work with new runtime.

  Args:
    file_des: FileDescriptor of the .proto file
  '''
    pass


def BuildServices(file_des, module_name, module):
    '''Builds services classes and services stub class.

  Args:
    file_des: FileDescriptor of the .proto file
    module_name: str, the name of generated _pb2 module
    module: Generated _pb2 module
  '''
    _service = service
    import google.protobuf
    service_reflection = service_reflection
    import google.protobuf
    for name, service in file_des.services_by_name.items():
        module[name] = service_reflection.GeneratedServiceType(name, (_service.Service,), dict(DESCRIPTOR = service, __module__ = module_name))
        stub_name = name + '_Stub'
        module[stub_name] = service_reflection.GeneratedServiceStubType(stub_name, (module[name],), dict(DESCRIPTOR = service, __module__ = module_name))
        return None
