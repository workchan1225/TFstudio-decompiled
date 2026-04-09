# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: json.pyc (Python 3.11)

from __future__ import annotations
from typing import Any
from typing import TYPE_CHECKING
from  import types as sqltypes
if TYPE_CHECKING:
    from engine.interfaces import Dialect
    from sql.type_api import _BindProcessorType
    from sql.type_api import _LiteralProcessorType

class JSON(sqltypes.JSON):
    '''MySQL JSON type.

    MySQL supports JSON as of version 5.7.
    MariaDB supports JSON (as an alias for LONGTEXT) as of version 10.2.

    :class:`_mysql.JSON` is used automatically whenever the base
    :class:`_types.JSON` datatype is used against a MySQL or MariaDB backend.

    .. seealso::

        :class:`_types.JSON` - main documentation for the generic
        cross-platform JSON datatype.

    The :class:`.mysql.JSON` type supports persistence of JSON values
    as well as the core index operations provided by :class:`_types.JSON`
    datatype, by adapting the operations to render the ``JSON_EXTRACT``
    function at the database level.

    '''
    pass


class _FormatTypeMixin:
    
    def _format_value(self = None, value = None):
        raise NotImplementedError()

    
    def bind_processor(self = None, dialect = None):
        pass
    # WARNING: Decompyle incomplete

    
    def literal_processor(self = None, dialect = None):
        pass
    # WARNING: Decompyle incomplete



class JSONIndexType(sqltypes.JSON.JSONIndexType, _FormatTypeMixin):
    
    def _format_value(self = None, value = None):
        if isinstance(value, int):
            formatted_value = '$[%s]' % value
        else:
            formatted_value = '$."%s"' % value
        return formatted_value



class JSONPathType(sqltypes.JSON.JSONPathType, _FormatTypeMixin):
    
    def _format_value(self = None, value = None):
        return ''.join % (lambda .0: for elem in .0:
passcontinue'[%s]' % elem['."%s"' % elem])(value())
