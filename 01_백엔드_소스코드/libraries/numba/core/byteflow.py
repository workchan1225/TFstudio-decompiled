# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: byteflow.pyc (Python 3.11)

'''
Implement python 3.8+ bytecode analysis
'''
import dis
import logging
from collections import namedtuple, defaultdict, deque
from functools import total_ordering
from numba.core.utils import UniqueDict, PYVERSION, ALL_BINOPS_TO_OPERATORS, _lazy_pformat
from numba.core.controlflow import NEW_BLOCKERS, CFGraph
from numba.core.ir import Loc
from numba.core.errors import UnsupportedBytecodeError
_logger = logging.getLogger(__name__)
_EXCEPT_STACK_OFFSET = 6
_FINALLY_POP = _EXCEPT_STACK_OFFSET
_NO_RAISE_OPS = frozenset({
    'NOP',
    'PRECALL',
    'LOAD_CONST',
    'LOAD_DEREF'})
if PYVERSION in ((3, 12), (3, 13), (3, 14)):
    from enum import Enum
    
    class CALL_INTRINSIC_1_Operand(Enum):
        INTRINSIC_STOPITERATION_ERROR = 3
        UNARY_POSITIVE = 5
        INTRINSIC_LIST_TO_TUPLE = 6

    ci1op = CALL_INTRINSIC_1_Operand
elif PYVERSION in ((3, 10), (3, 11)):
    pass
else:
    raise NotImplementedError(PYVERSION)
BlockKind = <NODE:12>()

class Flow(object):
    '''Data+Control Flow analysis.

    Simulate execution to recover dataflow and controlflow information.
    '''
    
    def __init__(self, bytecode):
        _logger.debug('bytecode dump:\n%s', _lazy_pformat(bytecode, lazy_func = (lambda x: x.dump())))
        self._bytecode = bytecode
        self.block_infos = UniqueDict()

    
    def run(self):
        '''Run a trace over the bytecode over all reachable path.

        The trace starts at bytecode offset 0 and gathers stack and control-
        flow information by partially interpreting each bytecode.
        Each ``State`` instance in the trace corresponds to a basic-block.
        The State instances forks when a jump instruction is encountered.
        A newly forked state is then added to the list of pending states.
        The trace ends when there are no more pending states.
        '''
        firststate = State(bytecode = self._bytecode, pc = 0, nstack = 0, blockstack = ())
        runner = TraceRunner(debug_filename = self._bytecode.func_id.filename)
        runner.pending.append(firststate)
        first_encounter = UniqueDict()
    # WARNING: Decompyle incomplete

    if PYVERSION in ((3, 11), (3, 12), (3, 13), (3, 14)):
        
        def _run_handle_exception(self, runner, state):
            if state.in_with() and state.has_active_try() and state.get_inst().opname not in _NO_RAISE_OPS:
                state.fork(pc = state.get_inst().next)
                runner._adjust_except_stack(state)
                return True
            None.advance_pc()
            if state.in_with() or state.is_in_exception():
                _logger.debug('3.11 exception %s PC=%s', state.get_exception(), state._pc)
                eh = state.get_exception()
                eh_top = state.get_top_block('TRY')
                if eh_top and eh_top['end'] == eh.target:
                    eh_block = None
                    return None
                eh_block = None.make_block('TRY', end = eh.target)
                eh_block['end_offset'] = eh.end
                eh_block['stack_depth'] = eh.depth
                eh_block['push_lasti'] = eh.lasti
                state.fork(pc = state._pc, extra_block = eh_block)
                return True
            return None

    elif PYVERSION in ((3, 10),):
        
        def _run_handle_exception(self, runner, state):
            pass
        # WARNING: Decompyle incomplete

    else:
        raise NotImplementedError(PYVERSION)
    
    def _build_cfg(self, all_states):
        graph = CFGraph()
        for state in all_states:
            b = state.pc_initial
            graph.add_node(b)
            for state in all_states:
                for edge in state.outgoing_edges:
                    graph.add_edge(state.pc_initial, edge.pc, 0)
                    graph.set_entry_point(0)
                    graph.process()
                    self.cfgraph = graph
                    return None

    
    def _prune_phis(self, runner):
        pass
    # WARNING: Decompyle incomplete

    
    def _is_implicit_new_block(self, state):
        inst = state.get_inst()
        if inst.offset in self._bytecode.labels:
            return True
        if None.opname in NEW_BLOCKERS:
            return True

    if PYVERSION in ((3, 14),):
        
        def _guard_with_as(self, state):
            pass

        return None
    if None in ((3, 10), (3, 11), (3, 12), (3, 13)):
        
        def _guard_with_as(self, state):
            """Checks if the next instruction after a SETUP_WITH is something
            other than a POP_TOP, if it is something else it'll be some sort of
            store which is not supported (this corresponds to `with CTXMGR as
            VAR(S)`)."""
            current_inst = state.get_inst()
            if current_inst.opname in frozenset({'SETUP_WITH', 'BEFORE_WITH'}):
                next_op = self._bytecode[current_inst.next].opname
                if next_op != 'POP_TOP':
                    msg = "The 'with (context manager) as (variable):' construct is not supported."
                    raise UnsupportedBytecodeError(msg)
            return None

        return None
    raise NotImplementedError(PYVERSION)


def _is_null_temp_reg(reg):
    return reg.startswith('$null$')


class TraceRunner(object):
    '''Trace runner contains the states for the trace and the opcode dispatch.
    '''
    
    def __init__(self, debug_filename):
        self.debug_filename = debug_filename
        self.pending = deque()
        self.finished = set()

    
    def get_debug_loc(self, lineno):
        return Loc(self.debug_filename, lineno)

    
    def dispatch(self, state):
        pass
    # WARNING: Decompyle incomplete

    
    def _adjust_except_stack(self, state):
        '''
        Adjust stack when entering an exception handler to match expectation
        by the bytecode.
        '''
        tryblk = state.get_top_block('TRY')
        state.pop_block_and_above(tryblk)
        nstack = state.stack_depth
        kwargs = { }
        expected_depth = tryblk['stack_depth']
        if nstack > expected_depth:
            kwargs['npop'] = nstack - expected_depth
        extra_stack = 1
        if tryblk['push_lasti']:
            extra_stack += 1
        kwargs['npush'] = extra_stack
    # WARNING: Decompyle incomplete

    
    def op_NOP(self, state, inst):
        state.append(inst)

    if PYVERSION in ((3, 14),):
        op_NOT_TAKEN = op_NOP
    elif PYVERSION in ((3, 10), (3, 11), (3, 12), (3, 13)):
        pass
    else:
        raise NotImplementedError(PYVERSION)
    
    def op_RESUME(self, state, inst):
        state.append(inst)

    
    def op_CACHE(self, state, inst):
        state.append(inst)

    
    def op_PRECALL(self, state, inst):
        state.append(inst)

    
    def op_PUSH_NULL(self, state, inst):
        state.push(state.make_null())
        state.append(inst)

    
    def op_RETURN_GENERATOR(self, state, inst):
        state.push(state.make_temp())
        state.append(inst)

    if PYVERSION in ((3, 13), (3, 14)):
        
        def op_FORMAT_SIMPLE(self, state, inst):
            value = state.pop()
            strvar = state.make_temp()
            res = state.make_temp()
            state.append(inst, value = value, res = res, strvar = strvar)
            state.push(res)

    elif PYVERSION in ((3, 10), (3, 11), (3, 12)):
        pass
    else:
        raise NotImplementedError(PYVERSION)
    
    def op_FORMAT_VALUE(self, state, inst):
        '''
        FORMAT_VALUE(flags): flags argument specifies format spec which is
        not supported yet. Currently, we just call str() on the value.
        Pops a value from stack and pushes results back.
        Required for supporting f-strings.
        https://docs.python.org/3/library/dis.html#opcode-FORMAT_VALUE
        '''
        if inst.arg != 0:
            msg = 'format spec in f-strings not supported yet'
            raise UnsupportedBytecodeError(msg, loc = self.get_debug_loc(inst.lineno))
        value = state.pop()
        strvar = state.make_temp()
        res = state.make_temp()
        state.append(inst, value = value, res = res, strvar = strvar)
        state.push(res)

    
    def op_BUILD_STRING(self, state, inst):
        '''
        BUILD_STRING(count): Concatenates count strings from the stack and
        pushes the resulting string onto the stack.
        Required for supporting f-strings.
        https://docs.python.org/3/library/dis.html#opcode-BUILD_STRING
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def op_POP_TOP(self, state, inst):
        state.pop()

    if PYVERSION in ((3, 14),):
        op_POP_ITER = op_POP_TOP
    elif PYVERSION in ((3, 10), (3, 11), (3, 12), (3, 13)):
        pass
    else:
        raise NotImplementedError(PYVERSION)
    if PYVERSION in ((3, 13), (3, 14)):
        
        def op_TO_BOOL(self, state, inst):
            res = state.make_temp()
            tos = state.pop()
            state.append(inst, val = tos, res = res)
            state.push(res)

    elif PYVERSION in ((3, 10), (3, 11), (3, 12)):
        pass
    else:
        raise NotImplementedError(PYVERSION)
    if PYVERSION in ((3, 13), (3, 14)):
        
        def op_LOAD_GLOBAL(self, state, inst):
            res = state.make_temp()
            idx = inst.arg >> 1
            state.append(inst, idx = idx, res = res)
            state.push(res)
            if inst.arg & 1:
                state.push(state.make_null())
                return None

    elif PYVERSION in ((3, 11), (3, 12)):
        
        def op_LOAD_GLOBAL(self, state, inst):
            res = state.make_temp()
            idx = inst.arg >> 1
            state.append(inst, idx = idx, res = res)
            if inst.arg & 1:
                state.push(state.make_null())
            state.push(res)

    elif PYVERSION in ((3, 10),):
        
        def op_LOAD_GLOBAL(self, state, inst):
            res = state.make_temp()
            state.append(inst, res = res)
            state.push(res)

    else:
        raise NotImplementedError(PYVERSION)
    
    def op_COPY_FREE_VARS(self, state, inst):
        state.append(inst)

    
    def op_MAKE_CELL(self, state, inst):
        state.append(inst)

    
    def op_LOAD_DEREF(self, state, inst):
        res = state.make_temp()
        state.append(inst, res = res)
        state.push(res)

    
    def op_LOAD_CONST(self, state, inst):
        res = state.make_temp('const') + f'''.{inst.arg}'''
        state.push(res)
        state.append(inst, res = res)

    if PYVERSION in ((3, 14),):
        
        def op_LOAD_SMALL_INT(self, state, inst):
            if not  <= 0, inst.arg or 0, inst.arg < 256:
                pass
            
        # WARNING: Decompyle incomplete

    elif PYVERSION in ((3, 10), (3, 11), (3, 12), (3, 13)):
        pass
    else:
        raise NotImplementedError(PYVERSION)
    
    def op_LOAD_ATTR(self, state, inst):
