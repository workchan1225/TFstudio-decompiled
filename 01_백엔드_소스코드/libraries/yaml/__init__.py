# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from error import *
from tokens import *
from events import *
from nodes import *
from loader import *
from dumper import *
__version__ = '6.0.3'

try:
    from cyaml import *
    __with_libyaml__ = True
except ImportError:
    __with_libyaml__ = False

import io

def warnings(settings = (None,)):
    pass
# WARNING: Decompyle incomplete


def scan(stream, Loader = (Loader,)):
    '''
    Scan a YAML stream and produce scanning tokens.
    '''
    pass
# WARNING: Decompyle incomplete


def parse(stream, Loader = (Loader,)):
    '''
    Parse a YAML stream and produce parsing events.
    '''
    pass
# WARNING: Decompyle incomplete


def compose(stream, Loader = (Loader,)):
    '''
    Parse the first YAML document in a stream
    and produce the corresponding representation tree.
    '''
    loader = Loader(stream)
    
    try:
        loader.dispose()
        return loader.get_single_node()
    except:
        loader.dispose()



def compose_all(stream, Loader = (Loader,)):
    '''
    Parse all YAML documents in a stream
    and produce corresponding representation trees.
    '''
    pass
# WARNING: Decompyle incomplete


def load(stream, Loader):
    '''
    Parse the first YAML document in a stream
    and produce the corresponding Python object.
    '''
    loader = Loader(stream)
    
    try:
        loader.dispose()
        return loader.get_single_data()
    except:
        loader.dispose()



def load_all(stream, Loader):
    '''
    Parse all YAML documents in a stream
    and produce corresponding Python objects.
    '''
    pass
# WARNING: Decompyle incomplete


def full_load(stream):
    '''
    Parse the first YAML document in a stream
    and produce the corresponding Python object.

    Resolve all tags except those known to be
    unsafe on untrusted input.
    '''
    return load(stream, FullLoader)


def full_load_all(stream):
    '''
    Parse all YAML documents in a stream
    and produce corresponding Python objects.

    Resolve all tags except those known to be
    unsafe on untrusted input.
    '''
    return load_all(stream, FullLoader)


def safe_load(stream):
    '''
    Parse the first YAML document in a stream
    and produce the corresponding Python object.

    Resolve only basic YAML tags. This is known
    to be safe for untrusted input.
    '''
    return load(stream, SafeLoader)


def safe_load_all(stream):
    '''
    Parse all YAML documents in a stream
    and produce corresponding Python objects.

    Resolve only basic YAML tags. This is known
    to be safe for untrusted input.
    '''
    return load_all(stream, SafeLoader)


def unsafe_load(stream):
    '''
    Parse the first YAML document in a stream
    and produce the corresponding Python object.

    Resolve all tags, even those known to be
    unsafe on untrusted input.
    '''
    return load(stream, UnsafeLoader)


def unsafe_load_all(stream):
    '''
    Parse all YAML documents in a stream
    and produce corresponding Python objects.

    Resolve all tags, even those known to be
    unsafe on untrusted input.
    '''
    return load_all(stream, UnsafeLoader)


def emit(events, stream, Dumper, canonical, indent, width, allow_unicode, line_break = (None, Dumper, None, None, None, None, None)):
    '''
    Emit YAML parsing events into a stream.
    If stream is None, return the produced string instead.
    '''
    getvalue = None
# WARNING: Decompyle incomplete


def serialize_all(nodes, stream, Dumper, canonical, indent, width, allow_unicode, line_break, encoding, explicit_start, explicit_end, version, tags = (None, Dumper, None, None, None, None, None, None, None, None, None, None)):
    '''
    Serialize a sequence of representation trees into a YAML stream.
    If stream is None, return the produced string instead.
    '''
    getvalue = None
# WARNING: Decompyle incomplete


def serialize(node, stream, Dumper = (None, Dumper), **kwds):
    '''
    Serialize a representation tree into a YAML stream.
    If stream is None, return the produced string instead.
    '''
    pass
# WARNING: Decompyle incomplete


def dump_all(documents, stream, Dumper, default_style, default_flow_style, canonical, indent, width, allow_unicode, line_break, encoding, explicit_start, explicit_end, version, tags, sort_keys = (None, Dumper, None, False, None, None, None, None, None, None, None, None, None, None, True)):
    '''
    Serialize a sequence of Python objects into a YAML stream.
    If stream is None, return the produced string instead.
    '''
    getvalue = None
# WARNING: Decompyle incomplete


def dump(data, stream, Dumper = (None, Dumper), **kwds):
    '''
    Serialize a Python object into a YAML stream.
    If stream is None, return the produced string instead.
    '''
    pass
# WARNING: Decompyle incomplete


def safe_dump_all(documents, stream = (None,), **kwds):
    '''
    Serialize a sequence of Python objects into a YAML stream.
    Produce only basic YAML tags.
    If stream is None, return the produced string instead.
    '''
    pass
# WARNING: Decompyle incomplete


def safe_dump(data, stream = (None,), **kwds):
    '''
    Serialize a Python object into a YAML stream.
    Produce only basic YAML tags.
    If stream is None, return the produced string instead.
    '''
    pass
# WARNING: Decompyle incomplete


def add_implicit_resolver(tag, regexp, first, Loader, Dumper = (None, None, Dumper)):
    '''
    Add an implicit scalar detector.
    If an implicit scalar value matches the given regexp,
    the corresponding tag is assigned to the scalar.
    first is a sequence of possible initial characters or None.
    '''
    pass
# WARNING: Decompyle incomplete


def add_path_resolver(tag, path, kind, Loader, Dumper = (None, None, Dumper)):
    '''
    Add a path based resolver for the given tag.
    A path is a list of keys that forms a path
    to a node in the representation tree.
    Keys can be string values, integers, or None.
    '''
    pass
# WARNING: Decompyle incomplete


def add_constructor(tag, constructor, Loader = (None,)):
    '''
    Add a constructor for the given tag.
    Constructor is a function that accepts a Loader instance
    and a node object and produces the corresponding Python object.
    '''
    pass
# WARNING: Decompyle incomplete


def add_multi_constructor(tag_prefix, multi_constructor, Loader = (None,)):
    '''
    Add a multi-constructor for the given tag prefix.
    Multi-constructor is called for a node if its tag starts with tag_prefix.
    Multi-constructor accepts a Loader instance, a tag suffix,
    and a node object and produces the corresponding Python object.
    '''
    pass
# WARNING: Decompyle incomplete


def add_representer(data_type, representer, Dumper = (Dumper,)):
    '''
    Add a representer for the given type.
    Representer is a function accepting a Dumper instance
    and an instance of the given data type
    and producing the corresponding representation node.
    '''
    Dumper.add_representer(data_type, representer)


def add_multi_representer(data_type, multi_representer, Dumper = (Dumper,)):
    '''
    Add a representer for the given type.
    Multi-representer is a function accepting a Dumper instance
    and an instance of the given data type or subtype
    and producing the corresponding representation node.
    '''
    Dumper.add_multi_representer(data_type, multi_representer)


class YAMLObjectMetaclass(type):
    pass
# WARNING: Decompyle incomplete


def YAMLObject():
    '''YAMLObject'''
    __doc__ = '\n    An object that can dump itself to a YAML stream\n    and load itself from a YAML stream.\n    '
    __slots__ = ()
    yaml_loader = [
        Loader,
        FullLoader,
        UnsafeLoader]
    yaml_dumper = Dumper
    yaml_tag = None
    yaml_flow_style = None
    from_yaml = (lambda cls, loader, node: loader.construct_yaml_object(node, cls))()
    to_yaml = (lambda cls, dumper, data: dumper.represent_yaml_object(cls.yaml_tag, data, cls, flow_style = cls.yaml_flow_style))()

YAMLObject = <NODE:27>(YAMLObject, 'YAMLObject', metaclass = YAMLObjectMetaclass)
