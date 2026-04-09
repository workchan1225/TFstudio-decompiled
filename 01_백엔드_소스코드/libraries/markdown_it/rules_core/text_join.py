# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: text_join.pyc (Python 3.11)

"""Join raw text tokens with the rest of the text

This is set as a separate rule to provide an opportunity for plugins
to run text replacements after text join, but before escape join.

For example, `\\:)` shouldn't be replaced with an emoji.
"""
from __future__ import annotations
from token import Token
from state_core import StateCore

def text_join(state = None):
    '''Join raw text for escape sequences (`text_special`) tokens with the rest of the text'''
    for inline_token in state.tokens[:]:
        if inline_token.type != 'inline':
            continue
        new_tokens = []
        if not inline_token.children:
            for child_token in []:
                if child_token.type == 'text_special':
                    child_token.type = 'text'
                if child_token.type == 'text' and new_tokens and new_tokens[-1].type == 'text':
                    continue
                new_tokens.append(child_token)
                new_tokens = new_tokens[-1], new_tokens[-1].content += child_token.content, .content
                return None
