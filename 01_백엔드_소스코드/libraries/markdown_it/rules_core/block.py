# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: block.pyc (Python 3.11)

from token import Token
from state_core import StateCore

def block(state = None):
    if state.inlineMode:
        token = Token('inline', '', 0)
        token.content = state.src
        token.map = [
            0,
            1]
        token.children = []
        state.tokens.append(token)
        return None
    None.md.block.parse(state.src, state.md, state.env, state.tokens)
