# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: events.pyc (Python 3.11)


class Event(object):
    
    def __init__(self, start_mark, end_mark = (None, None)):
        self.start_mark = start_mark
        self.end_mark = end_mark

    
    def __repr__(self):
        pass
    # WARNING: Decompyle incomplete



class NodeEvent(Event):
    
    def __init__(self, anchor, start_mark, end_mark = (None, None)):
        self.anchor = anchor
        self.start_mark = start_mark
        self.end_mark = end_mark



class CollectionStartEvent(NodeEvent):
    
    def __init__(self, anchor, tag, implicit, start_mark, end_mark, flow_style = (None, None, None)):
        self.anchor = anchor
        self.tag = tag
        self.implicit = implicit
        self.start_mark = start_mark
        self.end_mark = end_mark
        self.flow_style = flow_style



class CollectionEndEvent(Event):
    pass


class StreamStartEvent(Event):
    
    def __init__(self, start_mark, end_mark, encoding = (None, None, None)):
        self.start_mark = start_mark
        self.end_mark = end_mark
        self.encoding = encoding



class StreamEndEvent(Event):
    pass


class DocumentStartEvent(Event):
    
    def __init__(self, start_mark, end_mark, explicit, version, tags = (None, None, None, None, None)):
        self.start_mark = start_mark
        self.end_mark = end_mark
        self.explicit = explicit
        self.version = version
        self.tags = tags



class DocumentEndEvent(Event):
    
    def __init__(self, start_mark, end_mark, explicit = (None, None, None)):
        self.start_mark = start_mark
        self.end_mark = end_mark
        self.explicit = explicit



class AliasEvent(NodeEvent):
    pass


class ScalarEvent(NodeEvent):
    
    def __init__(self, anchor, tag, implicit, value, start_mark, end_mark, style = (None, None, None)):
        self.anchor = anchor
        self.tag = tag
        self.implicit = implicit
        self.value = value
        self.start_mark = start_mark
        self.end_mark = end_mark
        self.style = style



class SequenceStartEvent(CollectionStartEvent):
    pass


class SequenceEndEvent(CollectionEndEvent):
    pass


class MappingStartEvent(CollectionStartEvent):
    pass


class MappingEndEvent(CollectionEndEvent):
    pass
