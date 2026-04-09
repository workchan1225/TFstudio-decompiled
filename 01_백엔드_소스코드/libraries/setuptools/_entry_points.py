# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _entry_points.pyc (Python 3.11)

import functools
import operator
import itertools
from extern.jaraco.text import yield_lines
from extern.jaraco.functools import pass_none
from _importlib import metadata
from _itertools import ensure_unique
from extern.more_itertools import consume

def ensure_valid(ep):
    '''
    Exercise one of the dynamic properties to trigger
    the pattern match.
    '''
    ep.extras


def load_group(value, group):
    '''
    Given a value of an entry point or series of entry points,
    return each as an EntryPoint.
    '''
    lines = yield_lines(value)
    text = f'''[{group}]\n''' + '\n'.join(lines)
    return metadata.EntryPoints._from_text(text)


def by_group_and_name(ep):
    return (ep.group, ep.name)


def validate(eps = None):
    '''
    Ensure entry points are unique by group and name and validate each.
    '''
    consume(map(ensure_valid, ensure_unique(eps, key = by_group_and_name)))
    return eps

load = (lambda eps: groups = (lambda .0: pass# WARNING: Decompyle incomplete
)(eps.items()())
    return validate(metadata.EntryPoints(groups))
)()
_ = (lambda eps: validate(metadata.EntryPoints(metadata.EntryPoints._from_text(eps))))()
load.register(type(None), (lambda x: x))
render = (lambda eps = functools.singledispatch: by_group = operator.attrgetter('group')groups = itertools.groupby(sorted(eps, key = by_group), by_group)(lambda .0: pass# WARNING: Decompyle incomplete
)(groups())
)()

def render_items(eps):
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(sorted(eps)())
