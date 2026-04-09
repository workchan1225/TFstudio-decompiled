# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: version.pyc (Python 3.11)

"""`tqdm` version detector. Precedence: installed dist, git, 'UNKNOWN'."""

try:
    from _dist_ver import __version__
    return None
except ImportError:
    from setuptools_scm import get_version
    __version__ = get_version(root = '..', relative_to = __file__)
    return None
    except (ImportError, LookupError):
        __version__ = 'UNKNOWN'
        return None
