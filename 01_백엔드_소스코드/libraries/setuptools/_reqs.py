# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _reqs.pyc (Python 3.11)



text
from pkg_resources import Requirement
import setuptools.extern.jaraco.text, extern, jaraco

def parse_strings(strs):
    '''
    Yield requirement strings for each specification in `strs`.

    `strs` must be a string, or a (possibly-nested) iterable thereof.
    '''
    return text.join_continuation(map(text.drop_comment, text.yield_lines(strs)))


def parse(strs):
    '''
    Deprecated drop-in replacement for pkg_resources.parse_requirements.
    '''
    return map(Requirement, parse_strings(strs))
