# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: py38compat.pyc (Python 3.11)


def aix_platform(osname, version, release):
    
    try:
        import _aix_support
        return _aix_support.aix_platform()
    except ImportError:
        pass

    return '{}-{}.{}'.format(osname, version, release)
