# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: error_reporting.pyc (Python 3.11)

import io
import json
import logging
import os
import re
from contextlib import contextmanager
from textwrap import indent, wrap
from typing import Any, Dict, Iterator, List, Optional, Sequence, Union, cast
from fastjsonschema_exceptions import JsonSchemaValueException
_logger = logging.getLogger(__name__)
_MESSAGE_REPLACEMENTS = {
    'must be named by propertyName definition': 'keys must be named by',
    'one of contains definition': 'at least one item that matches',
    ' same as const definition:': '',
    'only specified items': 'only items matching the definition' }
_SKIP_DETAILS = ('must not be empty', 'is always invalid', 'must not be there')
_NEED_DETAILS = {
    'not',
    'anyOf',
    'items',
    'oneOf',
    'contains',
    'propertyNames'}
_CAMEL_CASE_SPLITTER = re.compile('\\W+|([A-Z][^A-Z\\W]*)')
_IDENTIFIER = re.compile('^[\\w_]+$', re.I)
_TOML_JARGON = {
    'object': 'table',
    'property': 'key',
    'properties': 'keys',
    'property names': 'keys' }

class ValidationError(JsonSchemaValueException):
    '''Report violations of a given JSON schema.

    This class extends :exc:`~fastjsonschema.JsonSchemaValueException`
    by adding the following properties:

    - ``summary``: an improved version of the ``JsonSchemaValueException`` error message
      with only the necessary information)

    - ``details``: more contextual information about the error like the failing schema
      itself and the value that violates the schema.

    Depending on the level of the verbosity of the ``logging`` configuration
    the exception message will be only ``summary`` (default) or a combination of
    ``summary`` and ``details`` (when the logging level is set to :obj:`logging.DEBUG`).
    '''
    summary = ''
    details = ''
    _original_message = ''
    _from_jsonschema = (lambda cls = None, ex = None: formatter = _ErrorFormatting(ex)obj = cls(str(formatter), ex.value, formatter.name, ex.definition, ex.rule)debug_code = os.getenv('JSONSCHEMA_DEBUG_CODE_GENERATION', 'false').lower()if debug_code != 'false':
obj.__cause__, obj.__traceback__ = ex.__cause__, ex.__traceback__obj._original_message = ex.messageobj.summary = formatter.summaryobj.details = formatter.detailsobj)()

detailed_errors = (lambda : pass# WARNING: Decompyle incomplete
)()

class _ErrorFormatting:
    
    def __init__(self = None, ex = None):
        self.ex = ex
        self.name = f'''`{self._simplify_name(ex.name)}`'''
        self._original_message = self.ex.message.replace(ex.name, self.name)
        self._summary = ''
        self._details = ''

    
    def __str__(self = None):
        if _logger.getEffectiveLevel() <= logging.DEBUG and self.details:
            return f'''{self.summary}\n\n{self.details}'''
        return None.summary

    summary = (lambda self = None: if not self._summary:
self._summary = self._expand_summary()self._summary)()
    details = (lambda self = None: if not self._details:
self._details = self._expand_details()self._details)()
    
    def _simplify_name(self, name):
        x = len('data.')
        return name[x:] if name.startswith('data.') else name

    
    def _expand_summary(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _expand_details(self = None):
        optional = []
        desc_lines = self.ex.definition.pop('$$description', [])
        if not self.ex.definition.pop('description', None):
            desc = ' '.join(desc_lines)
            if desc:
                description = '\n'.join(wrap(desc, width = 80, initial_indent = '    ', subsequent_indent = '    ', break_long_words = False))
                optional.append(f'''DESCRIPTION:\n{description}''')
        schema = json.dumps(self.ex.definition, indent = 4)
        value = json.dumps(self.ex.value, indent = 4)
        defaults = [
            f'''GIVEN VALUE:\n{indent(value, '    ')}''',
            f'''OFFENDING RULE: {self.ex.rule!r}''',
            f'''DEFINITION:\n{indent(schema, '    ')}''']
        return '\n\n'.join(optional + defaults)



class _SummaryWriter:
    _IGNORE = {
        'title',
        'default',
        'examples',
        'description'}
    
    def __init__(self = None, jargon = None):
