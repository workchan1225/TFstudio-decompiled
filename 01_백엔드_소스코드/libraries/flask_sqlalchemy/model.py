# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: model.pyc (Python 3.11)

from __future__ import annotations
import re
import typing as t
import sqlalchemy as sa
from sqlalchemy.orm import orm as sa_orm
from query import Query
if t.TYPE_CHECKING:
    from extension import SQLAlchemy

class _QueryProperty:
    '''A class property that creates a query object for a model.

    :meta private:
    '''
    
    def __get__(self = None, obj = None, cls = None):
        return cls.query_class(cls, session = cls.__fsa__.session())



class Model:
    __fsa__: 't.ClassVar[SQLAlchemy]' = 'The base class of the :attr:`.SQLAlchemy.Model` declarative model class.\n\n    To define models, subclass :attr:`db.Model <.SQLAlchemy.Model>`, not this. To\n    customize ``db.Model``, subclass this and pass it as ``model_class`` to\n    :class:`.SQLAlchemy`. To customize ``db.Model`` at the metaclass level, pass an\n    already created declarative model class as ``model_class``.\n    '
    query_class: 't.ClassVar[type[Query]]' = Query
    query: 't.ClassVar[Query]' = _QueryProperty()
    
    def __repr__(self = None):
        state = sa.inspect(self)
    # WARNING: Decompyle incomplete



class BindMetaMixin(type):
    pass
# WARNING: Decompyle incomplete


class BindMixin:
    pass
# WARNING: Decompyle incomplete


class NameMetaMixin(type):
    pass
# WARNING: Decompyle incomplete


class NameMixin:
    pass
# WARNING: Decompyle incomplete


def should_set_tablename(cls = None):
