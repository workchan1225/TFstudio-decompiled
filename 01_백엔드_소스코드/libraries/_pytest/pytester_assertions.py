# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pytester_assertions.pyc (Python 3.11)

'''Helper plugin for pytester; should not be loaded on its own.'''
from __future__ import annotations
from collections.abc import Sequence
from _pytest.reports import CollectReport
from _pytest.reports import TestReport

def assertoutcome(outcomes = None, passed = None, skipped = None, failed = (0, 0, 0)):
    __tracebackhide__ = True
    (realpassed, realskipped, realfailed) = outcomes
    obtained = {
        'passed': len(realpassed),
        'skipped': len(realskipped),
        'failed': len(realfailed) }
    expected = {
        'passed': passed,
        'skipped': skipped,
        'failed': failed }
# WARNING: Decompyle incomplete


def assert_outcomes(outcomes, passed, skipped, failed, errors = None, xpassed = None, xfailed = None, warnings = (0, 0, 0, 0, 0, 0, None, None), deselected = ('outcomes', 'dict[str, int]', 'passed', 'int', 'skipped', 'int', 'failed', 'int', 'errors', 'int', 'xpassed', 'int', 'xfailed', 'int', 'warnings', 'int | None', 'deselected', 'int | None', 'return', 'None')):
    """Assert that the specified outcomes appear with the respective
    numbers (0 means it didn't occur) in the text output from a test run."""
    __tracebackhide__ = True
    obtained = {
        'passed': outcomes.get('passed', 0),
        'skipped': outcomes.get('skipped', 0),
        'failed': outcomes.get('failed', 0),
        'errors': outcomes.get('errors', 0),
        'xpassed': outcomes.get('xpassed', 0),
        'xfailed': outcomes.get('xfailed', 0) }
    expected = {
        'passed': passed,
        'skipped': skipped,
        'failed': failed,
        'errors': errors,
        'xpassed': xpassed,
        'xfailed': xfailed }
# WARNING: Decompyle incomplete
