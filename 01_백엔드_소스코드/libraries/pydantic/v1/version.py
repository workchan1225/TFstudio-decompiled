# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: version.pyc (Python 3.11)

__all__ = ('compiled', 'VERSION', 'version_info')
VERSION = '1.10.21'

try:
    import cython
    
    try:
        compiled = cython.compiled
    except AttributeError:
        compiled = False
    except ImportError:
        compiled: bool = False

    
    def version_info():
        import platform
        import sys
        import_module = import_module
        import importlib
        Path = Path
        import pathlib
        optional_deps = []
        for p in ('devtools', 'dotenv', 'email-validator', 'typing-extensions'):
            import_module(p.replace('-', '_'))
        except ImportError:
            continue
        optional_deps.append(p)
        continue
        info = {
            'pydantic version': VERSION,
            'pydantic compiled': compiled,
            'install path': Path(__file__).resolve().parent,
            'python version': sys.version,
            'platform': platform.platform(),
            'optional deps. installed': optional_deps }
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(info.items()())

    return None
