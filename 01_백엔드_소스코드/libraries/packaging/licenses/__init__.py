# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import annotations
import re
from typing import NewType, cast
from packaging.licenses._spdx import EXCEPTIONS, LICENSES
__all__ = [
    'InvalidLicenseExpression',
    'NormalizedLicenseExpression',
    'canonicalize_license_expression']
license_ref_allowed = re.compile('^[A-Za-z0-9.-]*$')
NormalizedLicenseExpression = NewType('NormalizedLicenseExpression', str)

class InvalidLicenseExpression(ValueError):
    '''Raised when a license-expression string is invalid

    >>> canonicalize_license_expression("invalid")
    Traceback (most recent call last):
        ...
    packaging.licenses.InvalidLicenseExpression: Invalid license expression: \'invalid\'
    '''
    pass


def canonicalize_license_expression(raw_license_expression = None):
    pass
# WARNING: Decompyle incomplete
