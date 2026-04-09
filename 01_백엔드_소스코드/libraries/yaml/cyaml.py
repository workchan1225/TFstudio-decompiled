# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cyaml.pyc (Python 3.11)

__all__ = [
    'CBaseLoader',
    'CSafeLoader',
    'CFullLoader',
    'CUnsafeLoader',
    'CLoader',
    'CBaseDumper',
    'CSafeDumper',
    'CDumper']
from yaml._yaml import CParser, CEmitter
from constructor import *
from serializer import *
from representer import *
from resolver import *

class CBaseLoader(BaseResolver, BaseConstructor, CParser):
    
    def __init__(self, stream):
        CParser.__init__(self, stream)
        BaseConstructor.__init__(self)
        BaseResolver.__init__(self)



class CSafeLoader(Resolver, SafeConstructor, CParser):
    
    def __init__(self, stream):
        CParser.__init__(self, stream)
        SafeConstructor.__init__(self)
        Resolver.__init__(self)



class CFullLoader(Resolver, FullConstructor, CParser):
    
    def __init__(self, stream):
        CParser.__init__(self, stream)
        FullConstructor.__init__(self)
        Resolver.__init__(self)



class CUnsafeLoader(Resolver, UnsafeConstructor, CParser):
    
    def __init__(self, stream):
        CParser.__init__(self, stream)
        UnsafeConstructor.__init__(self)
        Resolver.__init__(self)



class CLoader(Resolver, Constructor, CParser):
    
    def __init__(self, stream):
        CParser.__init__(self, stream)
        Constructor.__init__(self)
        Resolver.__init__(self)



class CBaseDumper(BaseResolver, BaseRepresenter, CEmitter):
    
    def __init__(self, stream, default_style, default_flow_style, canonical, indent, width, allow_unicode, line_break, encoding, explicit_start, explicit_end, version, tags, sort_keys = (None, False, None, None, None, None, None, None, None, None, None, None, True)):
        CEmitter.__init__(self, stream, canonical = canonical, indent = indent, width = width, encoding = encoding, allow_unicode = allow_unicode, line_break = line_break, explicit_start = explicit_start, explicit_end = explicit_end, version = version, tags = tags)
        Representer.__init__(self, default_style = default_style, default_flow_style = default_flow_style, sort_keys = sort_keys)
        Resolver.__init__(self)



class CSafeDumper(Resolver, SafeRepresenter, CEmitter):
    
    def __init__(self, stream, default_style, default_flow_style, canonical, indent, width, allow_unicode, line_break, encoding, explicit_start, explicit_end, version, tags, sort_keys = (None, False, None, None, None, None, None, None, None, None, None, None, True)):
        CEmitter.__init__(self, stream, canonical = canonical, indent = indent, width = width, encoding = encoding, allow_unicode = allow_unicode, line_break = line_break, explicit_start = explicit_start, explicit_end = explicit_end, version = version, tags = tags)
        SafeRepresenter.__init__(self, default_style = default_style, default_flow_style = default_flow_style, sort_keys = sort_keys)
        Resolver.__init__(self)



class CDumper(Resolver, Representer, Serializer, CEmitter):
    
    def __init__(self, stream, default_style, default_flow_style, canonical, indent, width, allow_unicode, line_break, encoding, explicit_start, explicit_end, version, tags, sort_keys = (None, False, None, None, None, None, None, None, None, None, None, None, True)):
        CEmitter.__init__(self, stream, canonical = canonical, indent = indent, width = width, encoding = encoding, allow_unicode = allow_unicode, line_break = line_break, explicit_start = explicit_start, explicit_end = explicit_end, version = version, tags = tags)
        Representer.__init__(self, default_style = default_style, default_flow_style = default_flow_style, sort_keys = sort_keys)
        Resolver.__init__(self)
