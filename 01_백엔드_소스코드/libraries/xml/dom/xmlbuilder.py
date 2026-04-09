# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: xmlbuilder.pyc (Python 3.11)

"""Implementation of the DOM Level 3 'LS-Load' feature."""
import copy
import xml.dom as xml
from xml.dom.NodeFilter import NodeFilter
__all__ = [
    'DOMBuilder',
    'DOMEntityResolver',
    'DOMInputSource']

class Options:
    '''Features object that has variables set for each DOMBuilder feature.

    The DOMBuilder class uses an instance of this class to pass settings to
    the ExpatBuilder class.
    '''
    namespaces = 1
    namespace_declarations = True
    validation = False
    external_parameter_entities = True
    external_general_entities = True
    external_dtd_subset = True
    validate_if_schema = False
    validate = False
    datatype_normalization = False
    create_entity_ref_nodes = True
    entities = True
    whitespace_in_element_content = True
    cdata_sections = True
    comments = True
    charset_overrides_xml_encoding = True
    infoset = False
    supported_mediatypes_only = False
    errorHandler = None
    filter = None


class DOMBuilder:
    __module__ = __name__
    __qualname__ = 'DOMBuilder'
    entityResolver = None
    errorHandler = None
    filter = None
    ACTION_REPLACE = 1
    ACTION_APPEND_AS_CHILDREN = 2
    ACTION_INSERT_AFTER = 3
    ACTION_INSERT_BEFORE = 4
    _legal_actions = (ACTION_REPLACE, ACTION_APPEND_AS_CHILDREN, ACTION_INSERT_AFTER, ACTION_INSERT_BEFORE)
    
    def __init__(self):
        self._options = Options()

    
    def _get_entityResolver(self):
        return self.entityResolver

    
    def _set_entityResolver(self, entityResolver):
        self.entityResolver = entityResolver

    
    def _get_errorHandler(self):
        return self.errorHandler

    
    def _set_errorHandler(self, errorHandler):
        self.errorHandler = errorHandler

    
    def _get_filter(self):
        return self.filter

    
    def _set_filter(self, filter):
        self.filter = filter

    
    def setFeature(self, name, state):
        if self.supportsFeature(name):
            if state:
                if not 1:
                    state = 0
                    
                    try:
                        settings = self._settings[(_name_xform(name), state)]
                        for name, value in settings:
                            setattr(self._options, name, value)
                            return None
                            except KeyError:
                                raise xml.dom.NotSupportedErr(f'''unsupported feature: {name!r}'''), None
                            raise xml.dom.NotFoundErr('unknown feature: ' + repr(name))


    
    def supportsFeature(self, name):
        return hasattr(self._options, _name_xform(name))

    
    def canSetFeature(self, name, state):
