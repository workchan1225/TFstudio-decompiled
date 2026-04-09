# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: localization.pyc (Python 3.11)

'''
Helpers for configuring locale settings.

Name `localization` is chosen to avoid overlap with builtin `locale` module.
'''
from __future__ import annotations
from contextlib import contextmanager
import locale
import platform
import re
import subprocess
from typing import TYPE_CHECKING, cast
from pandas._config.config import options
if TYPE_CHECKING:
    from collections.abc import Generator
set_locale = (lambda new_locale = None, lc_var = None: pass# WARNING: Decompyle incomplete
)()

def can_set_locale(lc = None, lc_var = None):
    '''
    Check to see if we can set a locale, and subsequently get the locale,
    without raising an Exception.

    Parameters
    ----------
    lc : str
        The locale to attempt to set.
    lc_var : int, default `locale.LC_ALL`
        The category of the locale being set.

    Returns
    -------
    bool
        Whether the passed locale can be set
    '''
    
    try:
        set_locale(lc, lc_var = lc_var)
        
        try:
            None(None, None)
        with None:
            if not None:
                
                try:
                    
                    try:
                        return True
                    except (ValueError, locale.Error):
                        return False






def _valid_locales(locales = None, normalize = None):
    '''
    Return a list of normalized locales that do not throw an ``Exception``
    when set.

    Parameters
    ----------
    locales : str
        A string where each locale is separated by a newline.
    normalize : bool
        Whether to call ``locale.normalize`` on each locale.

    Returns
    -------
    valid_locales : list
        A list of valid locales.
    '''
    pass
# WARNING: Decompyle incomplete


def get_locales(prefix = None, normalize = None):
    '''
    Get all the locales that are available on the system.

    Parameters
    ----------
    prefix : str
        If not ``None`` then return only those locales with the prefix
        provided. For example to get all English language locales (those that
        start with ``"en"``), pass ``prefix="en"``.
    normalize : bool
        Call ``locale.normalize`` on the resulting list of available locales.
        If ``True``, only locales that can be set without throwing an
        ``Exception`` are returned.

    Returns
    -------
    locales : list of strings
        A list of locale strings that can be set with ``locale.setlocale()``.
        For example::

            locale.setlocale(locale.LC_ALL, locale_string)

    On error will return an empty list (no locale available, e.g. Windows)

    '''
    if platform.system() in ('Linux', 'Darwin'):
        raw_locales = subprocess.check_output([
            'locale',
            '-a'])
    else:
        return []
# WARNING: Decompyle incomplete
