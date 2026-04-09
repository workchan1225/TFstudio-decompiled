# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: bytecode.pyc (Python 3.11)

'''Bytecode analysis for coverage.py'''
from __future__ import annotations
import collections
import dis
from types import CodeType
from typing import Iterable, Mapping, Optional
from coverage.types import TArc, TLineNo, TOffset

def code_objects(code = None):
    '''Iterate over all the code objects in `code`.'''
    pass
# WARNING: Decompyle incomplete


def op_set(*op_names):
    '''Make a set of opcodes from instruction names.

    The names might not exist in this version of Python, skip those if not.
    '''
    pass
# WARNING: Decompyle incomplete

ALWAYS_JUMPS = op_set('JUMP_BACKWARD', 'JUMP_BACKWARD_NO_INTERRUPT', 'JUMP_FORWARD')
RETURNS = op_set('RETURN_VALUE', 'RETURN_GENERATOR')
NOPS = op_set('NOP', 'NOT_TAKEN')

class InstructionWalker:
    '''Utility to step through trails of instructions.

    We have two reasons to need sequences of instructions from a code object:
    First, in strict sequence to visit all the instructions in the object.
    This is `walk(follow_jumps=False)`.  Second, we want to follow jumps to
    understand how execution will flow: `walk(follow_jumps=True)`.
    '''
    
    def __init__(self = None, code = None):
        self.code = code
        self.insts = { }
        inst = None
    # WARNING: Decompyle incomplete

    
    def walk(self = None, *, start_at, follow_jumps):
        '''
        Yield instructions starting from `start_at`.  Follow unconditional
        jumps if `follow_jumps` is true.
        '''
        pass
    # WARNING: Decompyle incomplete


TBranchTrailsOneSource = dict[(Optional[TArc], set[TOffset])]
TBranchTrails = dict[(TOffset, TBranchTrailsOneSource)]

def branch_trails(code = None, multiline_map = None):
    """
    Calculate branch trails for `code`.

    `multiline_map` maps line numbers to the first line number of a
    multi-line statement.

    Instructions can have a jump_target, where they might jump to next.  Some
    instructions with a jump_target are unconditional jumps (ALWAYS_JUMPS), so
    they aren't interesting to us, since they aren't the start of a branch
    possibility.

    Instructions that might or might not jump somewhere else are branch
    possibilities.  For each of those, we track a trail of instructions.  These
    are lists of instruction offsets, the next instructions that can execute.
    We follow the trail until we get to a new source line.  That gives us the
    arc from the original instruction's line to the new source line.

    """
    pass
# WARNING: Decompyle incomplete


def always_jumps(code = None):
    '''Make a map of unconditional bytecodes jumping to others.

    Only include bytecodes that do no work and go to another bytecode.
    '''
    jumps = { }
    iwalker = InstructionWalker(code)
    for inst in iwalker.walk(follow_jumps = False):
        if inst.opcode in ALWAYS_JUMPS:
            jumps[inst.offset] = inst.jump_target
            continue
        if inst.opcode in NOPS:
            jumps[inst.offset] = inst.offset + 2
        return jumps
