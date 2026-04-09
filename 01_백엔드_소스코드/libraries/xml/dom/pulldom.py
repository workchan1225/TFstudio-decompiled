# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pulldom.pyc (Python 3.11)

import xml.sax as xml
import xml.sax.handler as xml
START_ELEMENT = 'START_ELEMENT'
END_ELEMENT = 'END_ELEMENT'
COMMENT = 'COMMENT'
START_DOCUMENT = 'START_DOCUMENT'
END_DOCUMENT = 'END_DOCUMENT'
PROCESSING_INSTRUCTION = 'PROCESSING_INSTRUCTION'
IGNORABLE_WHITESPACE = 'IGNORABLE_WHITESPACE'
CHARACTERS = 'CHARACTERS'

class PullDOM(xml.sax.ContentHandler):
    _locator = None
    document = None
    
    def __init__(self, documentFactory = (None,)):
        XML_NAMESPACE = XML_NAMESPACE
        import xml.dom
        self.documentFactory = documentFactory
        self.firstEvent = [
            None,
            None]
        self.lastEvent = self.firstEvent
        self.elementStack = []
        self.push = self.elementStack.append
        
        try:
            self.pop = self.elementStack.pop
        except AttributeError:
            pass

        self._ns_contexts = [
            {
                XML_NAMESPACE: 'xml' }]
        self._current_context = self._ns_contexts[-1]
        self.pending_events = []

    
    def pop(self):
        result = self.elementStack[-1]
        del self.elementStack[-1]
        return result

    
    def setDocumentLocator(self, locator):
        self._locator = locator

    
    def startPrefixMapping(self, prefix, uri):
