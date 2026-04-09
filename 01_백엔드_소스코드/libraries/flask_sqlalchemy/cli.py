# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cli.pyc (Python 3.11)

from __future__ import annotations
import typing as t
from flask import current_app

def add_models_to_shell():
    '''Registered with :meth:`~flask.Flask.shell_context_processor` if
    ``add_models_to_shell`` is enabled. Adds the ``db`` instance and all model classes
    to ``flask shell``.
    '''
    db = current_app.extensions['sqlalchemy']
    out = db.Model._sa_registry.mappers()
    out['db'] = db
    return out
