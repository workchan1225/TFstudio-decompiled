# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: hooks.pyc (Python 3.11)

'''
requests.hooks
~~~~~~~~~~~~~~

This module provides the capabilities for the Requests hooks system.

Available hooks:

``response``:
    The response generated from a Request.
'''
HOOKS = [
    'response']

def default_hooks():
    return HOOKS()


def dispatch_hook(key, hooks, hook_data, **kwargs):
    '''Dispatches a hook dictionary on a given piece of data.'''
    pass
# WARNING: Decompyle incomplete
