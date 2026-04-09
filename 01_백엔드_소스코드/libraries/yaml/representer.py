# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: representer.pyc (Python 3.11)

__all__ = [
    'BaseRepresenter',
    'SafeRepresenter',
    'Representer',
    'RepresenterError']
from error import *
from nodes import *
import datetime
import copyreg
import types
import base64
import collections

class RepresenterError(YAMLError):
    pass


class BaseRepresenter:
    yaml_representers = { }
    yaml_multi_representers = { }
    
    def __init__(self, default_style, default_flow_style, sort_keys = (None, False, True)):
        self.default_style = default_style
        self.sort_keys = sort_keys
        self.default_flow_style = default_flow_style
        self.represented_objects = { }
        self.object_keeper = []
        self.alias_key = None

    
    def represent(self, data):
        node = self.represent_data(data)
        self.serialize(node)
        self.represented_objects = { }
        self.object_keeper = []
        self.alias_key = None

    
    def represent_data(self, data):
        if self.ignore_aliases(data):
            self.alias_key = None
        else:
            self.alias_key = id(data)
    # WARNING: Decompyle incomplete

    add_representer = (lambda cls, data_type, representer: if 'yaml_representers' not in cls.__dict__:
cls.yaml_representers = cls.yaml_representers.copy()cls.yaml_representers[data_type] = representer)()
    add_multi_representer = (lambda cls, data_type, representer: if 'yaml_multi_representers' not in cls.__dict__:
cls.yaml_multi_representers = cls.yaml_multi_representers.copy()cls.yaml_multi_representers[data_type] = representer)()
    
    def represent_scalar(self, tag, value, style = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def represent_sequence(self, tag, sequence, flow_style = (None,)):
        value = []
        node = SequenceNode(tag, value, flow_style = flow_style)
    # WARNING: Decompyle incomplete

    
    def represent_mapping(self, tag, mapping, flow_style = (None,)):
        value = []
        node = MappingNode(tag, value, flow_style = flow_style)
    # WARNING: Decompyle incomplete

    
    def ignore_aliases(self, data):
        return False



class SafeRepresenter(BaseRepresenter):
    __module__ = __name__
    __qualname__ = 'SafeRepresenter'
    
    def ignore_aliases(self, data):
        pass
    # WARNING: Decompyle incomplete

    
    def represent_none(self, data):
        return self.represent_scalar('tag:yaml.org,2002:null', 'null')

    
    def represent_str(self, data):
        return self.represent_scalar('tag:yaml.org,2002:str', data)

    
    def represent_binary(self, data):
        if hasattr(base64, 'encodebytes'):
            data = base64.encodebytes(data).decode('ascii')
        else:
            data = base64.encodestring(data).decode('ascii')
        return self.represent_scalar('tag:yaml.org,2002:binary', data, style = '|')

    
    def represent_bool(self, data):
        if data:
            value = 'true'
        else:
            value = 'false'
        return self.represent_scalar('tag:yaml.org,2002:bool', value)

    
    def represent_int(self, data):
        return self.represent_scalar('tag:yaml.org,2002:int', str(data))

    inf_value = 1e+300
# WARNING: Decompyle incomplete

SafeRepresenter.add_representer(type(None), SafeRepresenter.represent_none)
SafeRepresenter.add_representer(str, SafeRepresenter.represent_str)
SafeRepresenter.add_representer(bytes, SafeRepresenter.represent_binary)
SafeRepresenter.add_representer(bool, SafeRepresenter.represent_bool)
SafeRepresenter.add_representer(int, SafeRepresenter.represent_int)
SafeRepresenter.add_representer(float, SafeRepresenter.represent_float)
SafeRepresenter.add_representer(list, SafeRepresenter.represent_list)
SafeRepresenter.add_representer(tuple, SafeRepresenter.represent_list)
SafeRepresenter.add_representer(dict, SafeRepresenter.represent_dict)
SafeRepresenter.add_representer(set, SafeRepresenter.represent_set)
SafeRepresenter.add_representer(datetime.date, SafeRepresenter.represent_date)
SafeRepresenter.add_representer(datetime.datetime, SafeRepresenter.represent_datetime)
SafeRepresenter.add_representer(None, SafeRepresenter.represent_undefined)

class Representer(SafeRepresenter):
    
    def represent_complex(self, data):
        if data.imag == 0:
            data = '%r' % data.real
        elif data.real == 0:
            data = '%rj' % data.imag
        elif data.imag > 0:
            data = f'''{data.real!r}+{data.imag!r}j'''
        else:
            data = f'''{data.real!r}{data.imag!r}j'''
        return self.represent_scalar('tag:yaml.org,2002:python/complex', data)

    
    def represent_tuple(self, data):
        return self.represent_sequence('tag:yaml.org,2002:python/tuple', data)

    
    def represent_name(self, data):
        name = f'''{data.__module__!s}.{data.__name__!s}'''
        return self.represent_scalar('tag:yaml.org,2002:python/name:' + name, '')

    
    def represent_module(self, data):
        return self.represent_scalar('tag:yaml.org,2002:python/module:' + data.__name__, '')

    
    def represent_object(self, data):
        cls = type(data)
        if cls in copyreg.dispatch_table:
            reduce = copyreg.dispatch_table[cls](data)
        elif hasattr(data, '__reduce_ex__'):
            reduce = data.__reduce_ex__(2)
        elif hasattr(data, '__reduce__'):
            reduce = data.__reduce__()
        else:
            raise RepresenterError('cannot represent an object', data)
        reduce = list(reduce) + [
            None] * 5[:5]
        (function, args, state, listitems, dictitems) = reduce
        args = list(args)
    # WARNING: Decompyle incomplete

    
    def represent_ordered_dict(self, data):
        data_type = type(data)
        tag = f'''tag:yaml.org,2002:python/object/apply:{data_type.__module__!s}.{data_type.__name__!s}'''
        items = data.items()()
        return self.represent_sequence(tag, [
            items])


Representer.add_representer(complex, Representer.represent_complex)
Representer.add_representer(tuple, Representer.represent_tuple)
Representer.add_multi_representer(type, Representer.represent_name)
Representer.add_representer(collections.OrderedDict, Representer.represent_ordered_dict)
Representer.add_representer(types.FunctionType, Representer.represent_name)
Representer.add_representer(types.BuiltinFunctionType, Representer.represent_name)
Representer.add_representer(types.ModuleType, Representer.represent_module)
Representer.add_multi_representer(object, Representer.represent_object)
