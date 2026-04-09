# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fastjsonschema_validations.pyc (Python 3.11)

VERSION = '2.15.3'
import re
from fastjsonschema_exceptions import JsonSchemaValueException
REGEX_PATTERNS = {
    '^.*$': re.compile('^.*$'),
    '.+': re.compile('.+'),
    '^.+$': re.compile('^.+$'),
    'idn-email_re_pattern': re.compile('^[^@]+@[^@]+\\.[^@]+\\Z') }
NoneType = type(None)

def validate(data, custom_formats, name_prefix = ({ }, None)):
