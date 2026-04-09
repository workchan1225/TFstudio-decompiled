# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __config__.pyc (Python 3.11)

from enum import Enum
from numpy.core._multiarray_umath import __cpu_features__, __cpu_baseline__, __cpu_dispatch__
__all__ = [
    'show']
_built_with_meson = True

class DisplayModes(Enum):
    stdout = 'stdout'
    dicts = 'dicts'


def _cleanup(d):
    '''
    Removes empty values in a `dict` recursively
    This ensures we remove values that Meson could not provide to CONFIG
    '''
    if isinstance(d, dict):
        return d.items()()

CONFIG = {
    'host': {
        'cpu': 'x86_64',
        'family': 'x86_64',
        'endian': 'little',
        'system': 'windows' },
    'build': {
        'cpu': 'x86_64',
        'family': 'x86_64',
        'endian': 'little',
        'system': 'windows' },
    'cross-compiled': bool('False'.lower().replace('false', '')) }({
    'Compilers': {
        'blas': {
            'name': 'openblas64',
            'found': bool('True'.lower().replace('false', '')),
            'version': '0.3.23.dev',
            'detection method': 'pkgconfig',
            'include directory': '/c/opt/64/include',
            'lib directory': '/c/opt/64/lib',
            'openblas configuration': 'USE_64BITINT=1 DYNAMIC_ARCH=1 DYNAMIC_OLDER= NO_CBLAS= NO_LAPACK= NO_LAPACKE= NO_AFFINITY=1 USE_OPENMP= SKYLAKEX MAX_THREADS=2',
            'pc file directory': 'C:/opt/64/lib/pkgconfig' },
        'lapack': {
            'name': 'dep2270588361616',
            'found': bool('True'.lower().replace('false', '')),
            'version': '1.26.4',
            'detection method': 'internal',
            'include directory': 'unknown',
            'lib directory': 'unknown',
            'openblas configuration': 'unknown',
            'pc file directory': 'unknown' } },
    'Machine Information': {
        'path': 'C:\\Users\\runneradmin\\AppData\\Local\\Temp\\cibw-run-j442zwj6\\cp311-win_amd64\\build\\venv\\Scripts\\python.exe',
        'version': '3.11' },
    'Build Dependencies': __cpu_baseline__,
    'Python Information': (lambda .0: pass# WARNING: Decompyle incomplete
),
    'SIMD Extensions': {
        'baseline': __cpu_dispatch__(),
        'found': (lambda .0: pass# WARNING: Decompyle incomplete
),
        'not found': __cpu_dispatch__() } })

def _check_pyyaml():
    import yaml
    return yaml


def show(mode = (DisplayModes.stdout.value,)):
    """
    Show libraries and system information on which NumPy was built
    and is being used

    Parameters
    ----------
    mode : {`'stdout'`, `'dicts'`}, optional.
        Indicates how to display the config information.
        `'stdout'` prints to console, `'dicts'` returns a dictionary
        of the configuration.

    Returns
    -------
    out : {`dict`, `None`}
        If mode is `'dicts'`, a dict is returned, else None

    See Also
    --------
    get_include : Returns the directory containing NumPy C
                  header files.

    Notes
    -----
    1. The `'stdout'` mode will give more readable
       output if ``pyyaml`` is installed

    """
    if mode == DisplayModes.stdout.value:
        
        try:
            yaml = _check_pyyaml()
            print(yaml.dump(CONFIG))
            return None
        except ModuleNotFoundError:
            import warnings
            import json
            warnings.warn('Install `pyyaml` for better output', stacklevel = 1)
            print(json.dumps(CONFIG, indent = 2))
            return None
            if mode == DisplayModes.dicts.value:
                return CONFIG
            raise 'Invalid `mode`, use one of: '(f'''{(lambda .0: [ e.value for e in .0 ])(DisplayModes())}''')
