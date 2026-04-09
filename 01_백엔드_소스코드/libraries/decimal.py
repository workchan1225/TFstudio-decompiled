# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: decimal.pyc (Python 3.11)


try:
    from _decimal import *
    from _decimal import __doc__
    from _decimal import __version__
    from _decimal import __libmpdec_version__
    return None
except ImportError:
    from _pydecimal import *
    from _pydecimal import __doc__
    from _pydecimal import __version__
    from _pydecimal import __libmpdec_version__
    return None
