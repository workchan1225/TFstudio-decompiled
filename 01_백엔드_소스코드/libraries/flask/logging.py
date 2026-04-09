# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: logging.pyc (Python 3.11)

from __future__ import annotations
import logging
import sys
import typing as t
from werkzeug.local import LocalProxy
from globals import request
if t.TYPE_CHECKING:
    from sansio.app import App
wsgi_errors_stream = (lambda : request.environ['wsgi.errors'] if request else sys.stderr)()

def has_level_handler(logger = None):
    """Check if there is a handler in the logging chain that will handle the
    given logger's :meth:`effective level <~logging.Logger.getEffectiveLevel>`.
    """
    pass
# WARNING: Decompyle incomplete

default_handler = logging.StreamHandler(wsgi_errors_stream)
default_handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s'))

def create_logger(app = None):
    """Get the Flask app's logger and configure it if needed.

    The logger name will be the same as
    :attr:`app.import_name <flask.Flask.name>`.

    When :attr:`~flask.Flask.debug` is enabled, set the logger level to
    :data:`logging.DEBUG` if it is not set.

    If there is no handler for the logger's effective level, add a
    :class:`~logging.StreamHandler` for
    :func:`~flask.logging.wsgi_errors_stream` with a basic format.
    """
    logger = logging.getLogger(app.name)
    if not app.debug and logger.level:
        logger.setLevel(logging.DEBUG)
    if not has_level_handler(logger):
        logger.addHandler(default_handler)
    return logger
