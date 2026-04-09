# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

__doc__ = '\nNumPy\n=====\n\nProvides\n  1. An array object of arbitrary homogeneous items\n  2. Fast mathematical operations over arrays\n  3. Linear Algebra, Fourier Transforms, Random Number Generation\n\nHow to use the documentation\n----------------------------\nDocumentation is available in two forms: docstrings provided\nwith the code, and a loose standing reference guide, available from\n`the NumPy homepage <https://numpy.org>`_.\n\nWe recommend exploring the docstrings using\n`IPython <https://ipython.org>`_, an advanced Python shell with\nTAB-completion and introspection capabilities.  See below for further\ninstructions.\n\nThe docstring examples assume that `numpy` has been imported as ``np``::\n\n  >>> import numpy as np\n\nCode snippets are indicated by three greater-than signs::\n\n  >>> x = 42\n  >>> x = x + 1\n\nUse the built-in ``help`` function to view a function\'s docstring::\n\n  >>> help(np.sort)\n  ... # doctest: +SKIP\n\nFor some objects, ``np.info(obj)`` may provide additional help.  This is\nparticularly true if you see the line "Help on ufunc object:" at the top\nof the help() page.  Ufuncs are implemented in C, not Python, for speed.\nThe native Python help() does not know how to view their help, but our\nnp.info() function does.\n\nTo search for documents containing a keyword, do::\n\n  >>> np.lookfor(\'keyword\')\n  ... # doctest: +SKIP\n\nGeneral-purpose documents like a glossary and help on the basic concepts\nof numpy are available under the ``doc`` sub-module::\n\n  >>> from numpy import doc\n  >>> help(doc)\n  ... # doctest: +SKIP\n\nAvailable subpackages\n---------------------\nlib\n    Basic functions used by several sub-packages.\nrandom\n    Core Random Tools\nlinalg\n    Core Linear Algebra Tools\nfft\n    Core FFT routines\npolynomial\n    Polynomial tools\ntesting\n    NumPy testing tools\ndistutils\n    Enhancements to distutils with support for\n    Fortran compilers support and more  (for Python <= 3.11).\n\nUtilities\n---------\ntest\n    Run numpy unittests\nshow_config\n    Show numpy build configuration\nmatlib\n    Make everything matrices.\n__version__\n    NumPy version string\n\nViewing documentation using IPython\n-----------------------------------\n\nStart IPython and import `numpy` usually under the alias ``np``: `import\nnumpy as np`.  Then, directly past or use the ``%cpaste`` magic to paste\nexamples into the shell.  To see which functions are available in `numpy`,\ntype ``np.<TAB>`` (where ``<TAB>`` refers to the TAB key), or use\n``np.*cos*?<ENTER>`` (where ``<ENTER>`` refers to the ENTER key) to narrow\ndown the list.  To view the docstring for a function, use\n``np.cos?<ENTER>`` (to view the docstring) and ``np.cos??<ENTER>`` (to view\nthe source code).\n\nCopies vs. in-place operation\n-----------------------------\nMost of the functions in `numpy` return a copy of the array argument\n(e.g., `np.sort`).  In-place versions of these functions are often\navailable as array methods, i.e. ``x = np.array([1,2,3]); x.sort()``.\nExceptions to this rule are documented.\n\n'

def _delvewheel_patch_1_5_2():
    import os
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'numpy.libs'))
    if os.path.isdir(libs_dir):
        os.add_dll_directory(libs_dir)
        return None

_delvewheel_patch_1_5_2()
del _delvewheel_patch_1_5_2
import sys
import warnings
from _globals import _NoValue, _CopyMode
from exceptions import ComplexWarning, ModuleDeprecationWarning, VisibleDeprecationWarning, TooHardError, AxisError
from  import version
from version import __version__

try:
    __NUMPY_SETUP__
except NameError:
    __NUMPY_SETUP__ = False

if __NUMPY_SETUP__:
    sys.stderr.write('Running from numpy source directory.\n')
# WARNING: Decompyle incomplete
