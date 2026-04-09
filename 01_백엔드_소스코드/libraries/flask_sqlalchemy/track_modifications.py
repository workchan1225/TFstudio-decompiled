# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: track_modifications.pyc (Python 3.11)

from __future__ import annotations
import typing as t
import sqlalchemy as sa
from sqlalchemy.event import event as sa_event
from sqlalchemy.orm import orm as sa_orm
from flask import current_app
from flask import has_app_context
from flask.signals import Namespace
if t.TYPE_CHECKING:
    from session import Session
_signals = Namespace()
models_committed = _signals.signal('models-committed')
before_models_committed = _signals.signal('before-models-committed')

def _listen(session = None):
    sa_event.listen(session, 'before_flush', _record_ops, named = True)
    sa_event.listen(session, 'before_commit', _record_ops, named = True)
    sa_event.listen(session, 'before_commit', _before_commit)
    sa_event.listen(session, 'after_commit', _after_commit)
    sa_event.listen(session, 'after_rollback', _after_rollback)


def _record_ops(session = None, **kwargs):
    if not has_app_context():
        return None
    if not None.config['SQLALCHEMY_TRACK_MODIFICATIONS']:
        return None
    for targets, operation in ((None.new, 'insert'), (session.dirty, 'update'), (session.deleted, 'delete')):
        for target in targets:
            state = sa.inspect(target)
            key = state.identity_key if state.has_identity else id(target)
            session._model_changes[key] = (target, operation)
            return None


def _before_commit(session = None):
    if not has_app_context():
        return None
    app = None._get_current_object()
    if not app.config['SQLALCHEMY_TRACK_MODIFICATIONS']:
        return None
    if None._model_changes:
        changes = list(session._model_changes.values())
        before_models_committed.send(app, changes = changes)
        return None


def _after_commit(session = None):
    if not has_app_context():
        return None
    app = None._get_current_object()
    if not app.config['SQLALCHEMY_TRACK_MODIFICATIONS']:
        return None
    if None._model_changes:
        changes = list(session._model_changes.values())
        models_committed.send(app, changes = changes)
        session._model_changes.clear()
        return None


def _after_rollback(session = None):
    session._model_changes.clear()
