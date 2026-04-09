# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fragments_join.pyc (Python 3.11)

from state_inline import StateInline

def fragments_join(state = None):
    '''
    Clean up tokens after emphasis and strikethrough postprocessing:
    merge adjacent text nodes into one and re-calculate all token levels

    This is necessary because initially emphasis delimiter markers (``*, _, ~``)
    are treated as their own separate text tokens. Then emphasis rule either
    leaves them as text (needed to merge with adjacent text) or turns them
    into opening/closing tags (which messes up levels inside).
    '''
    level = 0
    maximum = len(state.tokens)
    curr = 0
    last = 0
# WARNING: Decompyle incomplete
