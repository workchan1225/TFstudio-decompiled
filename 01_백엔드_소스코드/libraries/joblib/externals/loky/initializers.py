# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: initializers.pyc (Python 3.11)

import warnings

def _viztracer_init(init_kwargs):
    """Initialize viztracer's profiler in worker processes"""
    VizTracer = VizTracer
    import viztracer
# WARNING: Decompyle incomplete


def _make_viztracer_initializer_and_initargs():
    pass
# WARNING: Decompyle incomplete


class _ChainedInitializer:
    '''Compound worker initializer

    This is meant to be used in conjunction with _chain_initializers to
    produce  the necessary chained_args list to be passed to __call__.
    '''
    
    def __init__(self, initializers):
        self._initializers = initializers

    
    def __call__(self, *chained_args):
        pass
    # WARNING: Decompyle incomplete



def _chain_initializers(initializer_and_args):
    '''Convenience helper to combine a sequence of initializers.

    If some initializers are None, they are filtered out.
    '''
    filtered_initializers = []
    filtered_initargs = []
# WARNING: Decompyle incomplete


def _prepare_initializer(initializer, initargs):
    pass
# WARNING: Decompyle incomplete
