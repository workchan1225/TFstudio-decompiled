# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parse_link_label.pyc (Python 3.11)

'''
Parse link label

this function assumes that first character ("[") already matches
returns the end of the label

'''
from markdown_it.rules_inline import StateInline

def parseLinkLabel(state = None, start = None, disableNested = None):
    labelEnd = -1
    oldPos = state.pos
    found = False
    state.pos = start + 1
    level = 1
# WARNING: Decompyle incomplete
