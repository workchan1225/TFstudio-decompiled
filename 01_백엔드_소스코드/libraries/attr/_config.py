# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _config.pyc (Python 3.11)

__all__ = [
    'get_run_validators',
    'set_run_validators']
_run_validators = True

def set_run_validators(run):
    '''
    Set whether or not validators are run.  By default, they are run.

    .. deprecated:: 21.3.0 It will not be removed, but it also will not be
        moved to new ``attrs`` namespace. Use `attrs.validators.set_disabled()`
        instead.
    '''
    global _run_validators
    if not isinstance(run, bool):
        msg = "'run' must be bool."
        raise TypeError(msg)
    _run_validators = run


def get_run_validators():
    '''
    Return whether or not validators are run.

    .. deprecated:: 21.3.0 It will not be removed, but it also will not be
        moved to new ``attrs`` namespace. Use `attrs.validators.get_disabled()`
        instead.
    '''
    return _run_validators
