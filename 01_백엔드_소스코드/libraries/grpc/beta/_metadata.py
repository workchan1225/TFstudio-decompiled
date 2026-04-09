# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _metadata.pyc (Python 3.11)

'''API metadata conversion utilities.'''
import collections
_Metadatum = collections.namedtuple('_Metadatum', ('key', 'value'))

def _beta_metadatum(key, value):
    beta_key = key if isinstance(key, (bytes,)) else key.encode('ascii')
    beta_value = value if isinstance(value, (bytes,)) else value.encode('ascii')
    return _Metadatum(beta_key, beta_value)


def _metadatum(beta_key, beta_value):
    key = beta_key if isinstance(beta_key, (str,)) else beta_key.decode('utf8')
    if isinstance(beta_value, (str,)) or key[-4:] == '-bin':
        value = beta_value
    else:
        value = beta_value.decode('utf8')
    return _Metadatum(key, value)


def beta(metadata):
    pass
# WARNING: Decompyle incomplete


def unbeta(beta_metadata):
    pass
# WARNING: Decompyle incomplete
