# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: serializer.pyc (Python 3.11)

__all__ = [
    'Serializer',
    'SerializerError']
from error import YAMLError
from events import *
from nodes import *

class SerializerError(YAMLError):
    pass


class Serializer:
    ANCHOR_TEMPLATE = 'id%03d'
    
    def __init__(self, encoding, explicit_start, explicit_end, version, tags = (None, None, None, None, None)):
        self.use_encoding = encoding
        self.use_explicit_start = explicit_start
        self.use_explicit_end = explicit_end
        self.use_version = version
        self.use_tags = tags
        self.serialized_nodes = { }
        self.anchors = { }
        self.last_anchor_id = 0
        self.closed = None

    
    def open(self):
        pass
    # WARNING: Decompyle incomplete

    
    def close(self):
        pass
    # WARNING: Decompyle incomplete

    
    def serialize(self, node):
        pass
    # WARNING: Decompyle incomplete

    
    def anchor_node(self, node):
        pass
    # WARNING: Decompyle incomplete

    
    def generate_anchor(self, node):
        return self.ANCHOR_TEMPLATE % self.last_anchor_id

    
    def serialize_node(self, node, parent, index):
        alias = self.anchors[node]
        if node in self.serialized_nodes:
            self.emit(AliasEvent(alias))
            return None
        self.serialized_nodes[node] = None
        self.descend_resolver(parent, index)
        if isinstance(node, ScalarNode):
            detected_tag = self.resolve(ScalarNode, node.value, (True, False))
            default_tag = self.resolve(ScalarNode, node.value, (False, True))
            implicit = (node.tag == detected_tag, node.tag == default_tag)
            self.emit(ScalarEvent(alias, node.tag, implicit, node.value, style = node.style))
        elif isinstance(node, SequenceNode):
            implicit = node.tag == self.resolve(SequenceNode, node.value, True)
            self.emit(SequenceStartEvent(alias, node.tag, implicit, flow_style = node.flow_style))
            index = 0
            for item in node.value:
                self.serialize_node(item, node, index)
                index += 1
                self.emit(SequenceEndEvent())
        if isinstance(node, MappingNode):
            implicit = node.tag == self.resolve(MappingNode, node.value, True)
            self.emit(MappingStartEvent(alias, node.tag, implicit, flow_style = node.flow_style))
            for key, value in node.value:
                self.serialize_node(key, node, None)
                self.serialize_node(value, node, key)
                self.emit(MappingEndEvent())
                self.ascend_resolver()
                return None
