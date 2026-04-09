# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: composer.pyc (Python 3.11)

__all__ = [
    'Composer',
    'ComposerError']
from error import MarkedYAMLError
from events import *
from nodes import *

class ComposerError(MarkedYAMLError):
    pass


class Composer:
    
    def __init__(self):
        self.anchors = { }

    
    def check_node(self):
        if self.check_event(StreamStartEvent):
            self.get_event()
        return not self.check_event(StreamEndEvent)

    
    def get_node(self):
        if not self.check_event(StreamEndEvent):
            return self.compose_document()

    
    def get_single_node(self):
        self.get_event()
        document = None
        if not self.check_event(StreamEndEvent):
            document = self.compose_document()
        if not self.check_event(StreamEndEvent):
            event = self.get_event()
            raise ComposerError('expected a single document in the stream', document.start_mark, 'but found another document', event.start_mark)
        self.get_event()
        return document

    
    def compose_document(self):
        self.get_event()
        node = self.compose_node(None, None)
        self.get_event()
        self.anchors = { }
        return node

    
    def compose_node(self, parent, index):
        if self.check_event(AliasEvent):
            event = self.get_event()
            anchor = event.anchor
            if anchor not in self.anchors:
                raise ComposerError(None, None, 'found undefined alias %r' % anchor, event.start_mark)
            return self.anchors[anchor]
        event = None.peek_event()
        anchor = event.anchor
    # WARNING: Decompyle incomplete

    
    def compose_scalar_node(self, anchor):
        event = self.get_event()
        tag = event.tag
    # WARNING: Decompyle incomplete

    
    def compose_sequence_node(self, anchor):
        start_event = self.get_event()
        tag = start_event.tag
    # WARNING: Decompyle incomplete

    
    def compose_mapping_node(self, anchor):
        start_event = self.get_event()
        tag = start_event.tag
    # WARNING: Decompyle incomplete
