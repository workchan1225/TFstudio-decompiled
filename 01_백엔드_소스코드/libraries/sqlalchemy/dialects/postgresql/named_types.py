# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: named_types.pyc (Python 3.11)

from __future__ import annotations
from types import ModuleType
from typing import Any
from typing import Dict
from typing import Optional
from typing import Type
from typing import TYPE_CHECKING
from typing import Union
from  import schema
from  import util
from sql import coercions
from sql import elements
from sql import roles
from sql import sqltypes
from sql import type_api
from sql.base import _NoArg
from sql.ddl import InvokeCreateDDLBase
from sql.ddl import InvokeDropDDLBase
if TYPE_CHECKING:
    from sql._typing import _CreateDropBind
    from sql._typing import _TypeEngineArgument

class NamedType(sqltypes.TypeEngine, schema.SchemaVisitable):
    '''Base for named types.'''
    create_type: 'bool' = True
    
    def create(self = None, bind = None, checkfirst = None, **kw):
        '''Emit ``CREATE`` DDL for this type.

        :param bind: a connectable :class:`_engine.Engine`,
         :class:`_engine.Connection`, or similar object to emit
         SQL.
        :param checkfirst: if ``True``, a query against
         the PG catalog will be first performed to see
         if the type does not exist already before
         creating.

        '''
        bind._run_ddl_visitor(self.DDLGenerator, self, checkfirst = checkfirst)

    
    def drop(self = None, bind = None, checkfirst = None, **kw):
        '''Emit ``DROP`` DDL for this type.

        :param bind: a connectable :class:`_engine.Engine`,
         :class:`_engine.Connection`, or similar object to emit
         SQL.
        :param checkfirst: if ``True``, a query against
         the PG catalog will be first performed to see
         if the type actually exists before dropping.

        '''
        bind._run_ddl_visitor(self.DDLDropper, self, checkfirst = checkfirst)

    
    def _check_for_name_in_memos(self = None, checkfirst = None, kw = None):
        '''Look in the \'ddl runner\' for \'memos\', then
        note our name in that collection.

        This to ensure a particular named type is operated
        upon only once within any kind of create/drop
        sequence without relying upon "checkfirst".

        '''
        if not self.create_type:
            return True
        if None in kw:
            ddl_runner = kw['_ddl_runner']
            type_name = f'''pg_{self.__visit_name__}'''
            if type_name in ddl_runner.memo:
                existing = ddl_runner.memo[type_name]
            else:
                existing = set()
                ddl_runner.memo[type_name] = set()
            present = (self.schema, self.name) in existing
            existing.add((self.schema, self.name))
            return present

    
    def _on_table_create(self = None, target = None, bind = None, checkfirst = (False,), **kw):
        if not checkfirst or self.metadata or kw.get('_is_metadata_operation', False):
            if not self._check_for_name_in_memos(checkfirst, kw):
                self.create(bind = bind, checkfirst = checkfirst)
                return None
            return None
        return None

    
    def _on_table_drop(self = None, target = None, bind = None, checkfirst = (False,), **kw):
        if not self.metadata or kw.get('_is_metadata_operation', False) or self._check_for_name_in_memos(checkfirst, kw):
            self.drop(bind = bind, checkfirst = checkfirst)
            return None
        return None
        return None

    
    def _on_metadata_create(self = None, target = None, bind = None, checkfirst = (False,), **kw):
        if not self._check_for_name_in_memos(checkfirst, kw):
            self.create(bind = bind, checkfirst = checkfirst)
            return None

    
    def _on_metadata_drop(self = None, target = None, bind = None, checkfirst = (False,), **kw):
        if not self._check_for_name_in_memos(checkfirst, kw):
            self.drop(bind = bind, checkfirst = checkfirst)
            return None



class NamedTypeGenerator(InvokeCreateDDLBase):
    pass
# WARNING: Decompyle incomplete


class NamedTypeDropper(InvokeDropDDLBase):
    pass
# WARNING: Decompyle incomplete


class EnumGenerator(NamedTypeGenerator):
    
    def visit_enum(self, enum):
        if not self._can_create_type(enum):
            return None
        None.with_ddl_events(enum)
        self.connection.execute(CreateEnumType(enum))
        None(None, None)
        return None
        with None:
            if not None:
                pass



class EnumDropper(NamedTypeDropper):
    
    def visit_enum(self, enum):
        if not self._can_drop_type(enum):
            return None
        None.with_ddl_events(enum)
        self.connection.execute(DropEnumType(enum))
        None(None, None)
        return None
        with None:
            if not None:
                pass



class ENUM(sqltypes.Enum, type_api.NativeForEmulated, NamedType):
    pass
# WARNING: Decompyle incomplete


class DomainGenerator(NamedTypeGenerator):
    
    def visit_DOMAIN(self, domain):
        if not self._can_create_type(domain):
            return None
        None.with_ddl_events(domain)
        self.connection.execute(CreateDomainType(domain))
        None(None, None)
        return None
        with None:
            if not None:
                pass



class DomainDropper(NamedTypeDropper):
    
    def visit_DOMAIN(self, domain):
        if not self._can_drop_type(domain):
            return None
        None.with_ddl_events(domain)
        self.connection.execute(DropDomainType(domain))
        None(None, None)
        return None
        with None:
            if not None:
                pass



class DOMAIN(sqltypes.SchemaType, NamedType):
    pass
# WARNING: Decompyle incomplete


class CreateEnumType(schema._CreateDropBase):
    __visit_name__ = 'create_enum_type'


class DropEnumType(schema._CreateDropBase):
    __visit_name__ = 'drop_enum_type'


class CreateDomainType(schema._CreateDropBase):
    '''Represent a CREATE DOMAIN statement.'''
    __visit_name__ = 'create_domain_type'


class DropDomainType(schema._CreateDropBase):
    '''Represent a DROP DOMAIN statement.'''
    __visit_name__ = 'drop_domain_type'
