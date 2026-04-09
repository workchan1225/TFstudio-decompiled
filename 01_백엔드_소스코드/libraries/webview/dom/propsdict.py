# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: propsdict.pyc (Python 3.11)

import json
from enum import Enum
from typing import Any, Dict, Optional, Union
from webview.util import css_to_camel, escape_string

class DOMPropType(Enum):
    Style = 1
    Attribute = 2


class PropsDict:
    
    def __init__(self = None, element = None, type = None, props = (None,)):
        self._PropsDict__element = element
        self._PropsDict__type = type
        if not props:
            return None
        if None == DOMPropType.Style:
            converted_style = (lambda .0: pass# WARNING: Decompyle incomplete
)(props.items()())
            self._PropsDict__element._window.evaluate_js(f'''\n                {self._PropsDict__element._query_command};\n                var styles = JSON.parse(\'{escape_string(converted_style)}\');\n\n                for (var key in styles) {{\n                    element.style[key] = styles[key];\n                }}\n            ''')
            return None
        if None == DOMPropType.Attribute:
            converted_attributes = (lambda .0: pass# WARNING: Decompyle incomplete
)(props.items()())
            self._PropsDict__element._window.evaluate_js(f'''\n                {self._PropsDict__element._query_command};\n                var attributes = JSON.parse(\'{converted_attributes}\');\n\n                for (var key in attributes) {{\n                    if (key === \'data-pywebview-id\') {{\n                        continue;\n                    }} else if (attributes[key] === null || attributes[key] === undefined) {{\n                        element.removeAttribute(key);\n                    }} else {{\n                        element.setAttribute(key, attributes[key]);\n                    }}\n                }};\n            ''')
            return None

    
    def __getitem__(self, key):
        data = self.__get_data()
        return data.get(key)

    
    def __setitem__(self, key, value):
        if self._PropsDict__type == DOMPropType.Style:
            self.__set_style({
                key: value })
            return None
        if None._PropsDict__type == DOMPropType.Attribute:
            self.__set_attribute({
                key: value })
            return None

    
    def __delitem__(self, key):
        if self._PropsDict__type == DOMPropType.Style:
            self.__set_style({
                key: '' })
            return None
        if None._PropsDict__type == DOMPropType.Attribute:
            self.__set_attribute({
                key: None })
            return None

    
    def __contains__(self, key):
        data = self.__get_data()
        return key in data

    
    def keys(self):
        data = self.__get_data()
        return data.keys()

    
    def values(self):
        data = self.__get_data()
        return data.values()

    
    def items(self):
        data = self.__get_data()
        return data.items()

    
    def get(self, key, default = (None,)):
        data = self.__get_data()
        return data.get(key, default)

    
    def clear(self):
        data = self.__get_data()
        for key in data.keys():
            data[key] = '' if self._PropsDict__type == DOMPropType.Style else None
            if self._PropsDict__type == DOMPropType.Style:
                self.__set_style(data)
                return None
            if None._PropsDict__type == DOMPropType.Attribute:
                self.__set_attribute(data)
                return None
            return None

    
    def copy(self):
        return self.__get_data()

    
    def update(self = None, other_dict = None):
        if self._PropsDict__type == DOMPropType.Style:
            self.__set_style(other_dict)
            return None
        if None._PropsDict__type == DOMPropType.Attribute:
            self.__set_attribute(other_dict)
            return None

    
    def pop(self, key, default = (None,)):
        data = self.__get_data()
        return data.pop(key, default)

    
    def popitem(self):
        data = self.__get_data()
        return data.popitem()

    
    def __str__(self):
        data = self.__get_data()
        return str(data)

    
    def __repr__(self):
        data = self.__get_data()
        return repr(data)

    
    def __get_data(self = None):
        if self._PropsDict__type == DOMPropType.Style:
            return self.__get_style()
        if None._PropsDict__type == DOMPropType.Attribute:
            return self.__get_attributes()

    
    def __get_attributes(self = None):
        return self._PropsDict__element._window.evaluate_js(f'''\n            {self._PropsDict__element._query_command};\n            var attributes = element.attributes;\n            var result = {{}};\n            for (var i = 0; i < attributes.length; i++) {{\n                if (attributes[i].name === \'data-pywebview-id\') {{\n                    continue;\n                }}\n                result[attributes[i].name] = attributes[i].value;\n            }}\n            result\n        ''')

    
    def __set_attribute(self = None, props = None):
        self._PropsDict__element._window.evaluate_js(f'''\n            {self._PropsDict__element._query_command};\n            var values = JSON.parse(\'{escape_string(json.dumps(props))}\');\n\n            for (var key in values) {{\n                var value = values[key];\n                if (value === null || value === undefined) {{\n                    element.removeAttribute(key);\n                }} else {{\n                    element.setAttribute(key, value);\n                }}\n            }}\n        ''')

    
    def __get_style(self = None):
        return self._PropsDict__element._window.evaluate_js(f'''\n            {self._PropsDict__element._query_command};\n            var styles = window.getComputedStyle(element);\n            var computedStyles = {{}};\n\n            for (var i = 0; i < styles.length; i++) {{\n                var propertyName = styles[i];\n                var propertyValue = styles.getPropertyValue(propertyName);\n\n                if (propertyValue !== \'\') {{\n                    computedStyles[propertyName] = propertyValue;\n                }}\n            }}\n\n            computedStyles;\n        ''')

    
    def __set_style(self = None, style = None):
        converted_style = (lambda .0: pass# WARNING: Decompyle incomplete
)(style.items()())
        self._PropsDict__element._window.evaluate_js(f'''\n            {self._PropsDict__element._query_command};\n            var styles = JSON.parse(\'{escape_string(converted_style)}\');\n\n            for (var key in styles) {{\n                var value = styles[key];\n                element.style[key] = value;\n            }}\n        ''')
