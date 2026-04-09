# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dumper.pyc (Python 3.11)

__all__ = [
    'BaseDumper',
    'SafeDumper',
    'Dumper']
from emitter import *
from serializer import *
from representer import *
from resolver import *

class BaseDumper(BaseResolver, BaseRepresenter, Serializer, Emitter):
    
    def __init__(self, stream, default_style, default_flow_style, canonical, indent, width, allow_unicode, line_break, encoding, explicit_start, explicit_end, version, tags, sort_keys = (None, False, None, None, None, None, None, None, None, None, None, None, True)):
        Emitter.__init__(self, stream, canonical = canonical, indent = indent, width = width, allow_unicode = allow_unicode, line_break = line_break)
        Serializer.__init__(self, encoding = encoding, explicit_start = explicit_start, explicit_end = explicit_end, version = version, tags = tags)
        Representer.__init__(self, default_style = default_style, default_flow_style = default_flow_style, sort_keys = sort_keys)
        Resolver.__init__(self)



class SafeDumper(Resolver, SafeRepresenter, Serializer, Emitter):
    
    def __init__(self, stream, default_style, default_flow_style, canonical, indent, width, allow_unicode, line_break, encoding, explicit_start, explicit_end, version, tags, sort_keys = (None, False, None, None, None, None, None, None, None, None, None, None, True)):
        Emitter.__init__(self, stream, canonical = canonical, indent = indent, width = width, allow_unicode = allow_unicode, line_break = line_break)
        Serializer.__init__(self, encoding = encoding, explicit_start = explicit_start, explicit_end = explicit_end, version = version, tags = tags)
        SafeRepresenter.__init__(self, default_style = default_style, default_flow_style = default_flow_style, sort_keys = sort_keys)
        Resolver.__init__(self)



class Dumper(Resolver, Representer, Serializer, Emitter):
    
    def __init__(self, stream, default_style, default_flow_style, canonical, indent, width, allow_unicode, line_break, encoding, explicit_start, explicit_end, version, tags, sort_keys = (None, False, None, None, None, None, None, None, None, None, None, None, True)):
        Emitter.__init__(self, stream, canonical = canonical, indent = indent, width = width, allow_unicode = allow_unicode, line_break = line_break)
        Serializer.__init__(self, encoding = encoding, explicit_start = explicit_start, explicit_end = explicit_end, version = version, tags = tags)
        Representer.__init__(self, default_style = default_style, default_flow_style = default_flow_style, sort_keys = sort_keys)
        Resolver.__init__(self)
