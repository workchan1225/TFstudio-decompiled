# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: matcher.pyc (Python 3.11)

from __future__ import annotations
import re
import typing as t
from dataclasses import dataclass
from dataclasses import field
from converters import ValidationError
from exceptions import NoMatch
from exceptions import RequestAliasRedirect
from exceptions import RequestPath
from rules import Rule
from rules import RulePart

class SlashRequired(Exception):
    pass

State = <NODE:12>()

class StateMachineMatcher:
    
    def __init__(self = None, merge_slashes = None):
        self._root = State()
        self.merge_slashes = merge_slashes

    
    def add(self = None, rule = None):
        state = self._root
        for part in rule._parts:
            if part.static:
                state.static.setdefault(part.content, State())
                state = state.static[part.content]
                continue
            for test_part, new_state in state.dynamic:
                if test_part == part:
                    state = new_state
                
                new_state = State()
                state.dynamic.append((part, new_state))
                state = new_state
                state.rules.append(rule)
                return None

    
    def update(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def match(self, domain = None, path = None, method = None, websocket = ('domain', 'str', 'path', 'str', 'method', 'str', 'websocket', 'bool', 'return', 'tuple[Rule, t.MutableMapping[str, t.Any]]')):
        pass
    # WARNING: Decompyle incomplete
