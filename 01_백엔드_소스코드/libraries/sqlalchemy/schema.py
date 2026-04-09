# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: schema.pyc (Python 3.11)

'''Compatibility namespace for sqlalchemy.sql.schema and related.'''
from __future__ import annotations
from sql.base import SchemaVisitor
from sql.ddl import _CreateDropBase
from sql.ddl import _DropView
from sql.ddl import AddConstraint
from sql.ddl import BaseDDLElement
from sql.ddl import CreateColumn
from sql.ddl import CreateIndex
from sql.ddl import CreateSchema
from sql.ddl import CreateSequence
from sql.ddl import CreateTable
from sql.ddl import DDL
from sql.ddl import DDLElement
from sql.ddl import DropColumnComment
from sql.ddl import DropConstraint
from sql.ddl import DropConstraintComment
from sql.ddl import DropIndex
from sql.ddl import DropSchema
from sql.ddl import DropSequence
from sql.ddl import DropTable
from sql.ddl import DropTableComment
from sql.ddl import ExecutableDDLElement
from sql.ddl import InvokeDDLBase
from sql.ddl import SetColumnComment
from sql.ddl import SetConstraintComment
from sql.ddl import SetTableComment
from sql.ddl import sort_tables
from sql.ddl import sort_tables_and_constraints
from sql.naming import conv
from sql.schema import _get_table_key
from sql.schema import BLANK_SCHEMA
from sql.schema import CheckConstraint
from sql.schema import Column
from sql.schema import ColumnCollectionConstraint
from sql.schema import ColumnCollectionMixin
from sql.schema import ColumnDefault
from sql.schema import Computed
from sql.schema import Constraint
from sql.schema import DefaultClause
from sql.schema import DefaultGenerator
from sql.schema import FetchedValue
from sql.schema import ForeignKey
from sql.schema import ForeignKeyConstraint
from sql.schema import HasConditionalDDL
from sql.schema import Identity
from sql.schema import Index
from sql.schema import insert_sentinel
from sql.schema import MetaData
from sql.schema import PrimaryKeyConstraint
from sql.schema import SchemaConst
from sql.schema import SchemaItem
from sql.schema import SchemaVisitable
from sql.schema import Sequence
from sql.schema import Table
from sql.schema import UniqueConstraint
