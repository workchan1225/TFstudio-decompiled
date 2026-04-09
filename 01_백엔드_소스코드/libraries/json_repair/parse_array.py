# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parse_array.pyc (Python 3.11)

from typing import TYPE_CHECKING, Any
from utils.constants import STRING_DELIMITERS, JSONReturnType
from utils.json_context import ContextValues
from utils.object_comparer import ObjectComparer
if TYPE_CHECKING:
    from json_parser import JSONParser
    from schema_repair import SchemaRepairer

def parse_array(self = None, schema = None, path = None):
    schema_repairer = None
    items_schema = None
    additional_items = None
# WARNING: Decompyle incomplete
