# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import annotations
import typing as t
from extension import SQLAlchemy
__all__ = [
    'SQLAlchemy']

def __getattr__(name = None):
    if name == '__version__':
        import importlib.metadata as importlib
        import warnings
        warnings.warn('The \'__version__\' attribute is deprecated and will be removed in Flask-SQLAlchemy 3.2. Use feature detection or \'importlib.metadata.version("flask-sqlalchemy")\' instead.', DeprecationWarning, stacklevel = 2)
        return importlib.metadata.version('flask-sqlalchemy')
    raise None(name)
