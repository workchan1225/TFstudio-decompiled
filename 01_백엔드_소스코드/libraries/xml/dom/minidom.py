# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: minidom.pyc (Python 3.11)

'''Simple implementation of the Level 1 DOM.

Namespaces and other minor Level 2 features are also supported.

parse("foo.xml")

parseString("<foo><bar/></foo>")

Todo:
=====
 * convenience methods for getting elements and text.
 * more testing
 * bring some of the writer and linearizer code into conformance with this
        interface
 * SAX 2 namespaces
'''
import io
import xml.dom as xml
from xml.dom import EMPTY_NAMESPACE, EMPTY_PREFIX, XMLNS_NAMESPACE, domreg
from xml.dom.minicompat import *
from xml.dom.xmlbuilder import DOMImplementationLS, DocumentLS
_nodeTypes_with_children = (xml.dom.Node.ELEMENT_NODE, xml.dom.Node.ENTITY_REFERENCE_NODE)

class Node(xml.dom.Node):
    namespaceURI = None
    parentNode = None
    ownerDocument = None
    nextSibling = None
    previousSibling = None
    prefix = EMPTY_PREFIX
    
    def __bool__(self):
        return True

    
    def toxml(self, encoding, standalone = (None, None)):
        return self.toprettyxml('', '', encoding, standalone)

    
    def toprettyxml(self, indent, newl, encoding, standalone = ('\t', '\n', None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def hasChildNodes(self):
        return bool(self.childNodes)

    
    def _get_childNodes(self):
        return self.childNodes

    
    def _get_firstChild(self):
        if self.childNodes:
            return self.childNodes[0]

    
    def _get_lastChild(self):
        if self.childNodes:
            return self.childNodes[-1]

    
    def insertBefore(self, newChild, refChild):
        pass
    # WARNING: Decompyle incomplete

    
    def appendChild(self, node):
        if node.nodeType == self.DOCUMENT_FRAGMENT_NODE:
            for c in tuple(node.childNodes):
                self.appendChild(c)
                return node
                if node.nodeType not in self._child_node_types:
                    raise xml.dom.HierarchyRequestErr(f'''{repr(node)!s} cannot be child of {repr(self)!s}''')
                if node.nodeType in _nodeTypes_with_children:
                    _clear_id_cache(self)
    # WARNING: Decompyle incomplete

    
    def replaceChild(self, newChild, oldChild):
        if newChild.nodeType == self.DOCUMENT_FRAGMENT_NODE:
            refChild = oldChild.nextSibling
            self.removeChild(oldChild)
            return self.insertBefore(newChild, refChild)
        if None.nodeType not in self._child_node_types:
            raise xml.dom.HierarchyRequestErr(f'''{repr(newChild)!s} cannot be child of {repr(self)!s}''')
        if newChild is oldChild:
            return None
    # WARNING: Decompyle incomplete

    
    def removeChild(self, oldChild):
        
        try:
            self.childNodes.remove(oldChild)
        except ValueError:
            raise xml.dom.NotFoundErr()

    # WARNING: Decompyle incomplete

    
    def normalize(self):
        L = []
        for child in self.childNodes:
            if child.nodeType == Node.TEXT_NODE:
                if not child.data:
                    if L:
                        L[-1].nextSibling = child.nextSibling
                    if child.nextSibling:
                        child.nextSibling.previousSibling = child.previousSibling
                    child.unlink()
                    continue
                if L and L[-1].nodeType == child.nodeType:
                    node = L[-1]
                    node.data = node.data + child.data
                    node.nextSibling = child.nextSibling
                    if child.nextSibling:
                        child.nextSibling.previousSibling = node
                    child.unlink()
                    continue
                L.append(child)
                continue
            L.append(child)
            if child.nodeType == Node.ELEMENT_NODE:
                child.normalize()
            self.childNodes[:] = L
            return None

    
    def cloneNode(self, deep):
