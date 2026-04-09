# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: nodes.pyc (Python 3.11)


class Node(object):
    
    def __init__(self, tag, value, start_mark, end_mark):
        self.tag = tag
        self.value = value
        self.start_mark = start_mark
        self.end_mark = end_mark

    
    def __repr__(self):
        value = self.value
        value = repr(value)
        return f'''{self.__class__.__name__!s}(tag={self.tag!r}, value={value!s})'''



class ScalarNode(Node):
    id = 'scalar'
    
    def __init__(self, tag, value, start_mark, end_mark, style = (None, None, None)):
        self.tag = tag
        self.value = value
        self.start_mark = start_mark
        self.end_mark = end_mark
        self.style = style



class CollectionNode(Node):
    
    def __init__(self, tag, value, start_mark, end_mark, flow_style = (None, None, None)):
        self.tag = tag
        self.value = value
        self.start_mark = start_mark
        self.end_mark = end_mark
        self.flow_style = flow_style



class SequenceNode(CollectionNode):
    id = 'sequence'


class MappingNode(CollectionNode):
    id = 'mapping'
