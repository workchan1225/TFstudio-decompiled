# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: constructor.pyc (Python 3.11)

__all__ = [
    'BaseConstructor',
    'SafeConstructor',
    'FullConstructor',
    'UnsafeConstructor',
    'Constructor',
    'ConstructorError']
from error import *
from nodes import *
import collections.abc as collections
import datetime
import base64
import binascii
import re
import sys
import types

class ConstructorError(MarkedYAMLError):
    pass


class BaseConstructor:
    yaml_constructors = { }
    yaml_multi_constructors = { }
    
    def __init__(self):
        self.constructed_objects = { }
        self.recursive_objects = { }
        self.state_generators = []
        self.deep_construct = False

    
    def check_data(self):
        return self.check_node()

    
    def check_state_key(self, key):
        '''Block special attributes/methods from being set in a newly created
        object, to prevent user-controlled methods from being called during
        deserialization'''
        if self.get_state_keys_blacklist_regexp().match(key):
            raise ConstructorError(None, None, f'''blacklisted key \'{key!s}\' in instance state found''', None)

    
    def get_data(self):
        if self.check_node():
            return self.construct_document(self.get_node())

    
    def get_single_data(self):
        node = self.get_single_node()
    # WARNING: Decompyle incomplete

    
    def construct_document(self, node):
        data = self.construct_object(node)
    # WARNING: Decompyle incomplete

    
    def construct_object(self, node, deep = (False,)):
        if node in self.constructed_objects:
            return self.constructed_objects[node]
        if None:
            old_deep = self.deep_construct
            self.deep_construct = True
        if node in self.recursive_objects:
            raise ConstructorError(None, None, 'found unconstructable recursive node', node.start_mark)
        self.recursive_objects[node] = None
        constructor = None
        tag_suffix = None
        if node.tag in self.yaml_constructors:
            constructor = self.yaml_constructors[node.tag]
    # WARNING: Decompyle incomplete

    
    def construct_scalar(self, node):
        if not isinstance(node, ScalarNode):
            raise ConstructorError(None, None, 'expected a scalar node, but found %s' % node.id, node.start_mark)
        return node.value

    
    def construct_sequence(self, node, deep = (False,)):
        pass
    # WARNING: Decompyle incomplete

    
    def construct_mapping(self, node, deep = (False,)):
        if not isinstance(node, MappingNode):
            raise ConstructorError(None, None, 'expected a mapping node, but found %s' % node.id, node.start_mark)
        mapping = { }
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep = deep)
            if not isinstance(key, collections.abc.Hashable):
                raise ConstructorError('while constructing a mapping', node.start_mark, 'found unhashable key', key_node.start_mark)
            value = self.construct_object(value_node, deep = deep)
            mapping[key] = value
            return mapping

    
    def construct_pairs(self, node, deep = (False,)):
        if not isinstance(node, MappingNode):
            raise ConstructorError(None, None, 'expected a mapping node, but found %s' % node.id, node.start_mark)
        pairs = []
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep = deep)
            value = self.construct_object(value_node, deep = deep)
            pairs.append((key, value))
            return pairs

    add_constructor = (lambda cls, tag, constructor: if 'yaml_constructors' not in cls.__dict__:
cls.yaml_constructors = cls.yaml_constructors.copy()cls.yaml_constructors[tag] = constructor)()
    add_multi_constructor = (lambda cls, tag_prefix, multi_constructor: if 'yaml_multi_constructors' not in cls.__dict__:
cls.yaml_multi_constructors = cls.yaml_multi_constructors.copy()cls.yaml_multi_constructors[tag_prefix] = multi_constructor)()


class SafeConstructor(BaseConstructor):
    pass
# WARNING: Decompyle incomplete

SafeConstructor.add_constructor('tag:yaml.org,2002:null', SafeConstructor.construct_yaml_null)
SafeConstructor.add_constructor('tag:yaml.org,2002:bool', SafeConstructor.construct_yaml_bool)
SafeConstructor.add_constructor('tag:yaml.org,2002:int', SafeConstructor.construct_yaml_int)
SafeConstructor.add_constructor('tag:yaml.org,2002:float', SafeConstructor.construct_yaml_float)
SafeConstructor.add_constructor('tag:yaml.org,2002:binary', SafeConstructor.construct_yaml_binary)
SafeConstructor.add_constructor('tag:yaml.org,2002:timestamp', SafeConstructor.construct_yaml_timestamp)
SafeConstructor.add_constructor('tag:yaml.org,2002:omap', SafeConstructor.construct_yaml_omap)
SafeConstructor.add_constructor('tag:yaml.org,2002:pairs', SafeConstructor.construct_yaml_pairs)
SafeConstructor.add_constructor('tag:yaml.org,2002:set', SafeConstructor.construct_yaml_set)
SafeConstructor.add_constructor('tag:yaml.org,2002:str', SafeConstructor.construct_yaml_str)
SafeConstructor.add_constructor('tag:yaml.org,2002:seq', SafeConstructor.construct_yaml_seq)
SafeConstructor.add_constructor('tag:yaml.org,2002:map', SafeConstructor.construct_yaml_map)
SafeConstructor.add_constructor(None, SafeConstructor.construct_undefined)

class FullConstructor(SafeConstructor):
    
    def get_state_keys_blacklist(self):
        return [
            '^extend$',
            '^__.*__$']

    
    def get_state_keys_blacklist_regexp(self):
        if not hasattr(self, 'state_keys_blacklist_regexp'):
            self.state_keys_blacklist_regexp = re.compile('(' + '|'.join(self.get_state_keys_blacklist()) + ')')
        return self.state_keys_blacklist_regexp

    
    def construct_python_str(self, node):
        return self.construct_scalar(node)

    
    def construct_python_unicode(self, node):
        return self.construct_scalar(node)

    
    def construct_python_bytes(self, node):
        
        try:
            value = self.construct_scalar(node).encode('ascii')
        except UnicodeEncodeError:
            exc = None
            raise ConstructorError(None, None, 'failed to convert base64 data into ascii: %s' % exc, node.start_mark)
            exc = None
            del exc

        
        try:
            if hasattr(base64, 'decodebytes'):
                return base64.decodebytes(value)
            return None.decodestring(value)
        except binascii.Error:
            exc = None
            raise ConstructorError(None, None, 'failed to decode base64 data: %s' % exc, node.start_mark)
            exc = None
            del exc


    
    def construct_python_long(self, node):
        return self.construct_yaml_int(node)

    
    def construct_python_complex(self, node):
        return complex(self.construct_scalar(node))

    
    def construct_python_tuple(self, node):
        return tuple(self.construct_sequence(node))

    
    def find_python_module(self, name, mark, unsafe = (False,)):
        if not name:
            raise ConstructorError('while constructing a Python module', mark, 'expected non-empty name appended to the tag', mark)
        if unsafe:
            
            try:
                __import__(name)
            except ImportError:
                exc = None
                raise ConstructorError('while constructing a Python module', mark, f'''cannot find module {name!r} ({exc!s})''', mark)
                exc = None
                del exc

            if name not in sys.modules:
                raise ConstructorError('while constructing a Python module', mark, 'module %r is not imported' % name, mark)
            return sys.modules[name]

    
    def find_python_name(self, name, mark, unsafe = (False,)):
        if not name:
            raise ConstructorError('while constructing a Python object', mark, 'expected non-empty name appended to the tag', mark)
        if '.' in name:
            (module_name, object_name) = name.rsplit('.', 1)
        else:
            module_name = 'builtins'
            object_name = name
        if unsafe:
            
            try:
                __import__(module_name)
            except ImportError:
                exc = None
                raise ConstructorError('while constructing a Python object', mark, f'''cannot find module {module_name!r} ({exc!s})''', mark)
                exc = None
                del exc

            if module_name not in sys.modules:
                raise ConstructorError('while constructing a Python object', mark, 'module %r is not imported' % module_name, mark)
            module = sys.modules[module_name]
            if not hasattr(module, object_name):
                raise ConstructorError('while constructing a Python object', mark, f'''cannot find {object_name!r} in the module {module.__name__!r}''', mark)
            return getattr(module, object_name)

    
    def construct_python_name(self, suffix, node):
        value = self.construct_scalar(node)
        if value:
            raise ConstructorError('while constructing a Python name', node.start_mark, 'expected the empty value, but found %r' % value, node.start_mark)
        return self.find_python_name(suffix, node.start_mark)

    
    def construct_python_module(self, suffix, node):
        value = self.construct_scalar(node)
        if value:
            raise ConstructorError('while constructing a Python module', node.start_mark, 'expected the empty value, but found %r' % value, node.start_mark)
        return self.find_python_module(suffix, node.start_mark)

    
    def make_python_instance(self, suffix, node, args, kwds, newobj, unsafe = (None, None, False, False)):
        if not args:
            args = []
        if not kwds:
            kwds = { }
        cls = self.find_python_name(suffix, node.start_mark)
        if not unsafe and isinstance(cls, type):
            raise ConstructorError('while constructing a Python instance', node.start_mark, 'expected a class, but found %r' % type(cls), node.start_mark)
    # WARNING: Decompyle incomplete

    
    def set_python_instance_state(self, instance, state, unsafe = (False,)):
        if hasattr(instance, '__setstate__'):
            instance.__setstate__(state)
            return None
        slotstate = None
        if isinstance(state, tuple) and len(state) == 2:
            (state, slotstate) = state
        if hasattr(instance, '__dict__'):
            if unsafe and state:
                for key in state.keys():
                    self.check_state_key(key)
                    instance.__dict__.update(state)
                if state:
                    slotstate.update(state)
        for key, value in slotstate.items():
            if not unsafe:
                self.check_state_key(key)
            setattr(instance, key, value)
            return None

    
    def construct_python_object(self, suffix, node):
        pass
    # WARNING: Decompyle incomplete

    
    def construct_python_object_apply(self, suffix, node, newobj = (False,)):
        if isinstance(node, SequenceNode):
            args = self.construct_sequence(node, deep = True)
            kwds = { }
            state = { }
            listitems = []
            dictitems = { }
        else:
            value = self.construct_mapping(node, deep = True)
            args = value.get('args', [])
            kwds = value.get('kwds', { })
            state = value.get('state', { })
            listitems = value.get('listitems', [])
            dictitems = value.get('dictitems', { })
        instance = self.make_python_instance(suffix, node, args, kwds, newobj)
        if state:
            self.set_python_instance_state(instance, state)
        if listitems:
            instance.extend(listitems)
        if dictitems:
            for key in dictitems:
                instance[key] = dictitems[key]
                return instance

    
    def construct_python_object_new(self, suffix, node):
        return self.construct_python_object_apply(suffix, node, newobj = True)


FullConstructor.add_constructor('tag:yaml.org,2002:python/none', FullConstructor.construct_yaml_null)
FullConstructor.add_constructor('tag:yaml.org,2002:python/bool', FullConstructor.construct_yaml_bool)
FullConstructor.add_constructor('tag:yaml.org,2002:python/str', FullConstructor.construct_python_str)
FullConstructor.add_constructor('tag:yaml.org,2002:python/unicode', FullConstructor.construct_python_unicode)
FullConstructor.add_constructor('tag:yaml.org,2002:python/bytes', FullConstructor.construct_python_bytes)
FullConstructor.add_constructor('tag:yaml.org,2002:python/int', FullConstructor.construct_yaml_int)
FullConstructor.add_constructor('tag:yaml.org,2002:python/long', FullConstructor.construct_python_long)
FullConstructor.add_constructor('tag:yaml.org,2002:python/float', FullConstructor.construct_yaml_float)
FullConstructor.add_constructor('tag:yaml.org,2002:python/complex', FullConstructor.construct_python_complex)
FullConstructor.add_constructor('tag:yaml.org,2002:python/list', FullConstructor.construct_yaml_seq)
FullConstructor.add_constructor('tag:yaml.org,2002:python/tuple', FullConstructor.construct_python_tuple)
FullConstructor.add_constructor('tag:yaml.org,2002:python/dict', FullConstructor.construct_yaml_map)
FullConstructor.add_multi_constructor('tag:yaml.org,2002:python/name:', FullConstructor.construct_python_name)

class UnsafeConstructor(FullConstructor):
    pass
# WARNING: Decompyle incomplete

UnsafeConstructor.add_multi_constructor('tag:yaml.org,2002:python/module:', UnsafeConstructor.construct_python_module)
UnsafeConstructor.add_multi_constructor('tag:yaml.org,2002:python/object:', UnsafeConstructor.construct_python_object)
UnsafeConstructor.add_multi_constructor('tag:yaml.org,2002:python/object/new:', UnsafeConstructor.construct_python_object_new)
UnsafeConstructor.add_multi_constructor('tag:yaml.org,2002:python/object/apply:', UnsafeConstructor.construct_python_object_apply)

class Constructor(UnsafeConstructor):
    pass
