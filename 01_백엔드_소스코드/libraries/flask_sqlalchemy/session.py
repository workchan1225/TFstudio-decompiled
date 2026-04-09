# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: session.pyc (Python 3.11)

from __future__ import annotations
import typing as t
import sqlalchemy as sa
from sqlalchemy.exc import exc as sa_exc
from sqlalchemy.orm import orm as sa_orm
from flask.globals import app_ctx
if t.TYPE_CHECKING:
    from extension import SQLAlchemy

class Session(sa_orm.Session):
    pass
# WARNING: Decompyle incomplete


def _clause_to_engine(clause = None, engines = None):
    """If the clause is a table, return the engine associated with the table's
    metadata's bind key.
    """
    table = None
# WARNING: Decompyle incomplete


def _app_ctx_id():
    '''Get the id of the current Flask application context for the session scope.'''
    return id(app_ctx._get_current_object())
