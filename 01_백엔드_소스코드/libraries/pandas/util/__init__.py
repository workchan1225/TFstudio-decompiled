# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)


def __getattr__(key = None):
    if key == 'hash_array':
        hash_array = hash_array
        import pandas.core.util.hashing
        return hash_array
    if None == 'hash_pandas_object':
        hash_pandas_object = hash_pandas_object
        import pandas.core.util.hashing
        return hash_pandas_object
    if None == 'Appender':
        Appender = Appender
        import pandas.util._decorators
        return Appender
    if None == 'Substitution':
        Substitution = Substitution
        import pandas.util._decorators
        return Substitution
    if None == 'cache_readonly':
        cache_readonly = cache_readonly
        import pandas.util._decorators
        return cache_readonly
    raise None(f'''module \'pandas.util\' has no attribute \'{key}\'''')


def __dir__():
    return None['hash_array']['hash_pandas_object']
