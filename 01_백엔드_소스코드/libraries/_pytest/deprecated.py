# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: deprecated.pyc (Python 3.11)

'''Deprecation messages and bits of code used elsewhere in the codebase that
is planned to be removed in the next pytest release.

Keeping it in a central location makes it easy to track what is deprecated and should
be removed when the time comes.

All constants defined in this module should be either instances of
:class:`PytestWarning`, or :class:`UnformattedWarning`
in case of warnings which need to format their messages.
'''
from __future__ import annotations
from warnings import warn
from _pytest.warning_types import PytestDeprecationWarning
from _pytest.warning_types import PytestRemovedIn9Warning
from _pytest.warning_types import PytestRemovedIn10Warning
from _pytest.warning_types import UnformattedWarning
DEPRECATED_EXTERNAL_PLUGINS = {
    'pytest_catchlog',
    'pytest_subtests',
    'pytest_capturelog',
    'pytest_faulthandler'}
YIELD_FIXTURE = PytestDeprecationWarning('@pytest.yield_fixture is deprecated.\nUse @pytest.fixture instead; they are the same.')
PRIVATE = PytestDeprecationWarning('A private pytest class or function was used.')
HOOK_LEGACY_PATH_ARG = UnformattedWarning(PytestRemovedIn9Warning, 'The ({pylib_path_arg}: py.path.local) argument is deprecated, please use ({pathlib_path_arg}: pathlib.Path)\nsee https://docs.pytest.org/en/latest/deprecations.html#py-path-local-arguments-for-hooks-replaced-with-pathlib-path')
NODE_CTOR_FSPATH_ARG = UnformattedWarning(PytestRemovedIn9Warning, 'The (fspath: py.path.local) argument to {node_type_name} is deprecated. Please use the (path: pathlib.Path) argument instead.\nSee https://docs.pytest.org/en/latest/deprecations.html#fspath-argument-for-node-constructors-replaced-with-pathlib-path')
HOOK_LEGACY_MARKING = UnformattedWarning(PytestDeprecationWarning, 'The hook{type} {fullname} uses old-style configuration options (marks or attributes).\nPlease use the pytest.hook{type}({hook_opts}) decorator instead\n to configure the hooks.\n See https://docs.pytest.org/en/latest/deprecations.html#configuring-hook-specs-impls-using-markers')
MARKED_FIXTURE = PytestRemovedIn9Warning('Marks applied to fixtures have no effect\nSee docs: https://docs.pytest.org/en/stable/deprecations.html#applying-a-mark-to-a-fixture-function')
MONKEYPATCH_LEGACY_NAMESPACE_PACKAGES = PytestRemovedIn10Warning('monkeypatch.syspath_prepend() called with pkg_resources legacy namespace packages detected.\nLegacy namespace packages (using pkg_resources.declare_namespace) are deprecated.\nPlease use native namespace packages (PEP 420) instead.\nSee https://docs.pytest.org/en/stable/deprecations.html#monkeypatch-fixup-namespace-packages')

def check_ispytest(ispytest = None):
    if not ispytest:
        warn(PRIVATE, stacklevel = 3)
        return None
