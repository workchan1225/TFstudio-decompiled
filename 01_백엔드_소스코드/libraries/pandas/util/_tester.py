# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _tester.pyc (Python 3.11)

'''
Entrypoint for testing from the top-level namespace.
'''
from __future__ import annotations
import os
import sys
from pandas.compat._optional import import_optional_dependency
from pandas.util._decorators import set_module
PKG = os.path.dirname(os.path.dirname(__file__))
test = (lambda extra_args = None, run_doctests = None: pytest = import_optional_dependency('pytest')import_optional_dependency('hypothesis')cmd = [
'-m not slow and not network and not db']if extra_args:
if not isinstance(extra_args, list):
extra_args = [
extra_args]cmd = extra_argsif run_doctests:
cmd = [
'--doctest-modules',
'--doctest-cython',
f'''--ignore={os.path.join(PKG, 'tests')}''']cmd += [
PKG]joined = ' '.join(cmd)print(f'''running: pytest {joined}''')sys.exit(pytest.main(cmd)))()
__all__ = [
    'test']
