# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ruler.pyc (Python 3.11)

'''
class Ruler

Helper class, used by [[MarkdownIt#core]], [[MarkdownIt#block]] and
[[MarkdownIt#inline]] to manage sequences of functions (rules):

- keep rules in defined order
- assign the name to each rule
- enable/disable rules
- add/replace rules
- allow assign rules to additional named chains (in the same)
- caching lists of active rules

You will not need use this class directly until write plugins. For simple
rules control use [[MarkdownIt.disable]], [[MarkdownIt.enable]] and
[[MarkdownIt.use]].
'''
from __future__ import annotations
from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Generic, TypedDict, TypeVar
import warnings
from utils import EnvType
if TYPE_CHECKING:
    from markdown_it import MarkdownIt

class StateBase:
    
    def __init__(self = None, src = None, md = None, env = ('src', 'str', 'md', 'MarkdownIt', 'env', 'EnvType')):
        self.src = src
        self.env = env
        self.md = md

    src = (lambda self = None: self._src)()
    src = (lambda self = None, value = None: self._src = valueself._srcCharCode = None)()
    srcCharCode = (lambda self = None: warnings.warn('StateBase.srcCharCode is deprecated. Use StateBase.src instead.', DeprecationWarning, stacklevel = 2)# WARNING: Decompyle incomplete
)()


def RuleOptionsType():
    '''RuleOptionsType'''
    alt: 'list[str]' = 'RuleOptionsType'

RuleOptionsType = <NODE:27>(RuleOptionsType, 'RuleOptionsType', TypedDict, total = False)
RuleFuncTv = TypeVar('RuleFuncTv')

def Rule():
    '''Rule'''
    enabled: 'bool' = 'Rule'
    alt: 'list[str]' = field(repr = False)

Rule = <NODE:27>(Rule, 'Rule', Generic[RuleFuncTv])()

def Ruler():
    '''Ruler'''
    
    def __init__(self = None):
        self.__rules__ = []
        self.__cache__ = None

    
    def __find__(self = None, name = None):
        '''Find rule index by name'''
        for i, rule in enumerate(self.__rules__):
            if rule.name == name:
                
                return None, i
            return -1

    
    def __compile__(self = None):
        '''Build rules lookup cache'''
        chains = {
            ''}
        for rule in self.__rules__:
            if not rule.enabled:
                continue
            for name in rule.alt:
                chains.add(name)
                self.__cache__ = { }
                for chain in chains:
                    self.__cache__[chain] = []
                    for rule in self.__rules__:
                        if not rule.enabled:
                            continue
                        if chain and chain not in rule.alt:
                            continue
                        self.__cache__[chain].append(rule.fn)
                        return None

    
    def at(self = None, ruleName = None, fn = None, options = (None,)):
