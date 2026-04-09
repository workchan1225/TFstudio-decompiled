# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: iso8601.pyc (Python 3.11)

import re
import time
_iso8601_tmpl = [
    'YYYY-?MM-?DD',
    'YYYY-0MM?-?DD',
    'YYYY-MM',
    'YYYY-?OOO',
    'YY-?MM-?DD',
    'YY-?OOO',
    'YYYY',
    '-YY-?MM',
    '-OOO',
    '-YY',
    '--MM-?DD',
    '--MM',
    '---DD',
    'CC',
    '']
_iso8601_re = _iso8601_tmpl()

try:
    del tmpl
except NameError:
    pass

_iso8601_matches = _iso8601_re()

try:
    del regex
except NameError:
    (lambda .0: [ tmpl.replace('YYYY', '(?P<year>\\d{4})').replace('YY', '(?P<year>\\d\\d)').replace('MM', '(?P<month>[01]\\d)').replace('DD', '(?P<day>[0123]\\d)').replace('OOO', '(?P<ordinal>[0123]\\d\\d)').replace('CC', '(?P<century>\\d\\d$)') + '(T?(?P<hour>\\d{2}):(?P<minute>\\d{2})' + '(:(?P<second>\\d{2}))?' + '(\\.(?P<fracsecond>\\d+))?' + '(?P<tz>[+-](?P<tzhour>\\d{2})(:(?P<tzmin>\\d{2}))?|Z)?)?' for tmpl in .0 ])


def _parse_date_iso8601(date_string):
