# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dom.pyc (Python 3.11)

import json
from typing import List, Optional, Union
from webview.dom import ManipulationMode
from webview.dom.element import Element

class DOM:
    _serializable = False
    
    def __init__(self, window):
        self._DOM__window = window
        { } = window.events, window.events.loaded += self.__on_loaded, .loaded

    
    def __on_loaded(self):
        self._elements = { }

    body = (lambda self = None: self._elements.get('body', Element(self._DOM__window, 'body')))()
    document = (lambda self = None: self._elements.get('document', Element(self._DOM__window, 'document')))()
    window = (lambda self = None: self._elements.get('window', Element(self._DOM__window, 'window')))()
    
    def create_element(self = None, html = None, parent = None, mode = (None, ManipulationMode.LastChild)):
        self._DOM__window.events.loaded.wait()
        if isinstance(parent, Element):
            parent_command = parent._query_command
        elif isinstance(parent, str):
            parent_command = f'''var element = document.querySelector("{parent}");'''
        else:
            parent_command = 'var element = document.body;'
        if not isinstance(html, str):
            html = str(html)
        node_id = self._DOM__window.evaluate_js(f'''\n            {parent_command};\n            var template = document.createElement(\'template\');\n            template.innerHTML = {json.dumps(html)}.trim();\n            var newElement = template.content.firstChild;\n            pywebview._insertNode(newElement, element, \'{mode.value}\')\n            pywebview._getNodeId(newElement);\n        ''')
        return Element(self._DOM__window, node_id)

    
    def get_element(self = None, selector = None):
        node_id = self._DOM__window.evaluate_js(f'''\n            var element = document.querySelector(\'{selector}\');\n            pywebview._getNodeId(element);\n        ''')
        return Element(self._DOM__window, node_id) if node_id else None

    
    def get_elements(self = None, selector = None):
        pass
    # WARNING: Decompyle incomplete
