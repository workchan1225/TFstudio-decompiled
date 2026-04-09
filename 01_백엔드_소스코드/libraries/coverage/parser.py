# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parser.pyc (Python 3.11)

'''Code parsing for coverage.py.'''
from __future__ import annotations
import ast
import collections
import functools
import os
import re
import token
import tokenize
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from types import CodeType
from typing import Callable, Optional, Protocol, cast
from coverage import env
from coverage.bytecode import code_objects
from coverage.debug import short_stack
from coverage.exceptions import NoSource, NotPython
from coverage.misc import isolate_module, nice_pair
from coverage.phystokens import generate_tokens
from coverage.types import TArc, TLineNo
os = isolate_module(os)

class PythonParser:
    '''Parse code to find executable lines, excluded lines, etc.

    This information is all based on static analysis: no code execution is
    involved.

    '''
    
    def __init__(self = None, text = None, filename = None, exclude = (None, None, None)):
        '''
        Source can be provided as `text`, the text itself, or `filename`, from
        which the text will be read.  Excluded lines are those that match
        `exclude`, a regex string.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def lines_matching(self = None, regex = None):
        """Find the lines matching a regex.

        Returns a set of line numbers, the lines that contain a match for
        `regex`. The entire line needn't match, just a part of it.
        Handles multiline regex patterns.

        """
        pass
    # WARNING: Decompyle incomplete

    
    def _raw_parse(self = None):
        '''Parse the source to find the interesting facts about its lines.

        A handful of attributes are updated.

        '''
        if self.exclude:
            self.raw_excluded = self.lines_matching(self.exclude)
            self.excluded = set(self.raw_excluded)
        indent = 0
        exclude_indent = 0
        excluding = False
        first_line = 0
        empty = True
        nesting = 0
    # WARNING: Decompyle incomplete

    first_line = (lambda self = None, lineno = None: if lineno < 0:
lineno = -self.multiline_map.get(-lineno, -lineno)else:
lineno = self.multiline_map.get(lineno, lineno)lineno)()
    
    def first_lines(self = None, linenos = None):
        '''Map the line numbers in `linenos` to the correct first line of the
        statement.

        Returns a set of the first lines.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def translate_lines(self = None, lines = None):
        '''Implement `FileReporter.translate_lines`.'''
        return self.first_lines(lines)

    
    def translate_arcs(self = None, arcs = None):
        '''Implement `FileReporter.translate_arcs`.'''
        pass
    # WARNING: Decompyle incomplete

    
    def parse_source(self = None):
        '''Parse source text to find executable lines, excluded lines, etc.

        Sets the .excluded and .statements attributes, normalized to the first
        line of multi-line statements.

        '''
        
        try:
            self._ast_root = ast.parse(self.text)
            self._raw_parse()
        except (tokenize.TokenError, IndentationError, SyntaxError):
            err = None
            if hasattr(err, 'lineno'):
                lineno = err.lineno
            else:
                lineno = err.args[1][0]
            raise NotPython(f'''Couldn\'t parse \'{self.filename}\' as Python source: ''' + f'''{err.args[0]!r} at line {lineno}'''), err
            err = None
            del err

        ignore = self.excluded | self.raw_docstrings
        starts = self.raw_statements - ignore
        self.statements = self.first_lines(starts) - ignore

    
    def arcs(self = None):
        '''Get information about the arcs available in the code.

        Returns a set of line number pairs.  Line numbers have been normalized
        to the first line of multi-line statements.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _analyze_ast(self = None):
        '''Run the AstArcAnalyzer and save its results.

        `_all_arcs` is the set of arcs in the code.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def fix_with_jumps(self = None, arcs = None):
        '''Adjust arcs to fix jumps leaving `with` statements.

        Consider this code:

            with open("/tmp/test", "w") as f1:
                a = 2
                b = 3
            print(4)

        In 3.10+, we get traces for lines 1, 2, 3, 1, 4.  But we want to present
        it to the user as if it had been 1, 2, 3, 4.  The arc 3->1 should be
        replaced with 3->4, and 1->4 should be removed.

        For this code, the fixers dict is {(3, 1): ((1, 4), (3, 4))}.  The key
        is the actual measured arc from the end of the with block back to the
        start of the with-statement.  The values are start_next (the with
        statement to the next statement after the with), and end_next (the end
        of the with-statement to the next statement after the with).

        With nested with-statements, we have to trace through a few levels to
        correct a longer chain of arcs.

        '''
        to_remove = set()
        to_add = set()
    # WARNING: Decompyle incomplete

    exit_counts = (lambda self = None: exit_counts = collections.defaultdict(int)# WARNING: Decompyle incomplete
)()
    
    def _finish_action_msg(self = None, action_msg = None, end = None):
        """Apply some defaulting and formatting to an arc's description."""
        pass
    # WARNING: Decompyle incomplete

    
    def missing_arc_description(self = None, start = None, end = None):
        '''Provide an English sentence describing a missing arc.'''
        pass
    # WARNING: Decompyle incomplete

    
    def arc_description(self = None, start = None, end = None):
        """Provide an English description of an arc's effect."""
        pass
    # WARNING: Decompyle incomplete



class ByteParser:
    '''Parse bytecode to understand the structure of code.'''
    
    def __init__(self = None, text = None, code = None, filename = (None, None)):
        self.text = text
    # WARNING: Decompyle incomplete

    
    def child_parsers(self = None):
        '''Iterate over all the code objects nested within this one.

        The iteration includes `self` as its first value.

        We skip code objects named `__annotate__` since they are deferred
        annotations that usually are never run.  If there are errors in the
        annotations, they will be caught by type checkers or other tools that
        use annotations.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _line_numbers(self = None):
        '''Yield the line numbers possible in this code object.

        Uses co_lines() to produce a sequence: l0, l1, ...
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _find_statements(self = None):
        '''Find the statements in `self.code`.

        Produce a sequence of line numbers that start statements.  Recurses
        into all code objects reachable from `self.code`.

        '''
        pass
    # WARNING: Decompyle incomplete


ArcStart = <NODE:12>()

class TAddArcFn(Protocol):
    '''The type for AstArcAnalyzer.add_arc().'''
    
    def __call__(self = None, start = None, end = None, missing_cause_msg = (None, None), action_msg = ('start', 'TLineNo', 'end', 'TLineNo', 'missing_cause_msg', 'str | None', 'action_msg', 'str | None', 'return', 'None')):
        '''
        Record an arc from `start` to `end`.

        `missing_cause_msg` is a description of the reason the arc wasn\'t
        taken if it wasn\'t taken.  For example, "the condition on line 10 was
        never true."

        `action_msg` is a description of what the arc does, like "jump to line
        10" or "exit from function \'fooey\'."

        '''
        pass


TArcFragments = dict[(TArc, list[tuple[(Optional[str], Optional[str])]])]

class Block:
    '''
    Blocks need to handle various exiting statements in their own ways.

    All of these methods take a list of exits, and a callable `add_arc`
    function that they can use to add arcs if needed.  They return True if the
    exits are handled, or False if the search should continue up the block
    stack.
    '''
    
    def process_break_exits(self = None, exits = None, add_arc = None):
        '''Process break exits.'''
        return False

    
    def process_continue_exits(self = None, exits = None, add_arc = None):
        '''Process continue exits.'''
        return False

    
    def process_raise_exits(self = None, exits = None, add_arc = None):
        '''Process raise exits.'''
        return False

    
    def process_return_exits(self = None, exits = None, add_arc = None):
        '''Process return exits.'''
        return False



class LoopBlock(Block):
    '''A block on the block stack representing a `for` or `while` loop.'''
    
    def __init__(self = None, start = None):
        self.start = start
        self.break_exits = set()

    
    def process_break_exits(self = None, exits = None, add_arc = None):
        self.break_exits.update(exits)
        return True

    
    def process_continue_exits(self = None, exits = None, add_arc = None):
        for xit in exits:
            add_arc(xit.lineno, self.start, xit.cause)
            return True



class FunctionBlock(Block):
    '''A block on the block stack representing a function definition.'''
    
    def __init__(self = None, start = None, name = None):
        self.start = start
        self.name = name

    
    def process_raise_exits(self = None, exits = None, add_arc = None):
        for xit in exits:
            add_arc(xit.lineno, -(self.start), xit.cause, f'''except from function {self.name!r}''')
            return True

    
    def process_return_exits(self = None, exits = None, add_arc = None):
        for xit in exits:
            add_arc(xit.lineno, -(self.start), xit.cause, f'''return from function {self.name!r}''')
            return True



class TryBlock(Block):
    '''A block on the block stack representing a `try` block.'''
    
    def __init__(self = None, handler_start = None, final_start = None):
        self.handler_start = handler_start
        self.final_start = final_start

    
    def process_raise_exits(self = None, exits = None, add_arc = None):
        pass
    # WARNING: Decompyle incomplete



def is_constant_test_expr(node = None):
    """Is this a compile-time constant test expression?

    We don't try to mimic all of CPython's optimizations.  We just have to
    handle the kinds of constant expressions people might actually use.

    """
    pass
# WARNING: Decompyle incomplete


class AstArcAnalyzer:
    '''Analyze source text with an AST to find executable code paths.

    The .analyze() method does the work, and populates these attributes:

    `arcs`: a set of (from, to) pairs of the the arcs possible in the code.

    `missing_arc_fragments`: a dict mapping (from, to) arcs to lists of
    message fragments explaining why the arc is missing from execution::

        { (start, end): [(missing_cause_msg, action_msg), ...], }

    For an arc starting from line 17, they should be usable to form complete
    sentences like: "Line 17 didn\'t {action_msg} because {missing_cause_msg}".

    NOTE: Starting in July 2024, I\'ve been whittling this down to only report
    arc that are part of true branches.  It\'s not clear how far this work will
    go.

    '''
    
    def __init__(self, filename = None, root_node = None, statements = None, multiline = ('filename', 'str', 'root_node', 'ast.AST', 'statements', 'set[TLineNo]', 'multiline', 'dict[TLineNo, TLineNo]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def analyze(self = None):
        '''Examine the AST tree from `self.root_node` to determine possible arcs.'''
        pass
    # WARNING: Decompyle incomplete

    
    def with_jump_fixers(self = None):
        '''Get a dict with data for fixing jumps out of with statements.

        Returns a dict.  The keys are arcs leaving a with-statement by jumping
        back to its start.  The values are pairs: first, the arc from the start
        to the next statement, then the arc that exits the with without going
        to the start.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _code_object__Module(self = None, node = None):
        start = self.line_for_node(node)
        if node.body:
            exits = self.process_body(node.body)
            for xit in exits:
                self.add_arc(xit.lineno, -start, xit.cause, 'exit the module')
                return None
                self.add_arc(start, -start)
                return None

    
    def _code_object__FunctionDef(self = None, node = None):
        start = self.line_for_node(node)
        self.block_stack.append(FunctionBlock(start = start, name = node.name))
        exits = self.process_body(node.body)
        self.process_return_exits(exits)
        self.block_stack.pop()

    _code_object__AsyncFunctionDef = _code_object__FunctionDef
    
    def _code_object__ClassDef(self = None, node = None):
        start = self.line_for_node(node)
        exits = self.process_body(node.body)
        for xit in exits:
            self.add_arc(xit.lineno, -start, xit.cause, f'''exit class {node.name!r}''')
            return None

    
    def add_arc(self = None, start = None, end = None, missing_cause_msg = (None, None), action_msg = ('start', 'TLineNo', 'end', 'TLineNo', 'missing_cause_msg', 'str | None', 'action_msg', 'str | None', 'return', 'None')):
        '''Add an arc, including message fragments to use if it is missing.'''
        if self.debug:
            print(f'''Adding possible arc: ({start}, {end}): {missing_cause_msg!r}, {action_msg!r}''')
            print(short_stack(), end = '\n\n')
        self.arcs.add((start, end))
        if start in self.current_with_starts:
            self.with_entries.add((start, end))
    # WARNING: Decompyle incomplete

    
    def nearest_blocks(self = None):
        '''Yield the blocks in nearest-to-farthest order.'''
        return reversed(self.block_stack)

    
    def line_for_node(self = None, node = None):
        '''What is the right line number to use for this node?

        This dispatches to _line__Node functions where needed.

        '''
        node_name = node.__class__.__name__
        handler = cast(Optional[Callable[([
            ast.AST], TLineNo)]], getattr(self, f'''_line__{node_name}''', None))
    # WARNING: Decompyle incomplete

    
    def _line_decorated(self = None, node = None):
        '''Compute first line number for things that can be decorated (classes and functions).'''
        if node.decorator_list:
            lineno = node.decorator_list[0].lineno
        else:
            lineno = node.lineno
        return lineno

    
    def _line__Assign(self = None, node = None):
        return self.line_for_node(node.value)

    _line__ClassDef = _line_decorated
    
    def _line__Dict(self = None, node = None):
        pass
    # WARNING: Decompyle incomplete

    _line__FunctionDef = _line_decorated
    _line__AsyncFunctionDef = _line_decorated
    
    def _line__List(self = None, node = None):
        if node.elts:
            return self.line_for_node(node.elts[0])
        return None.lineno

    
    def _line__Module(self = None, node = None):
        return 1

    OK_TO_DEFAULT = {
        'Expr',
        'Pass',
        'Assert',
        'Assign',
        'Delete',
        'Global',
        'Import',
        'Nonlocal',
        'AnnAssign',
        'AugAssign',
        'ImportFrom'}
    
    def node_exits(self = None, node = None):
        '''Find the set of arc starts that exit this node.

        Return a set of ArcStarts, exits from this node to the next. Because a
        node represents an entire sub-tree (including its children), the exits
        from a node can be arbitrarily complex::

            if something(1):
                if other(2):
                    doit(3)
                else:
                    doit(5)

        There are three exits from line 1: they start at lines 1, 3 and 5.
        There are two exits from line 2: lines 3 and 5.

        '''
        node_name = node.__class__.__name__
        handler = cast(Optional[Callable[([
            ast.AST], set[ArcStart])]], getattr(self, f'''_handle__{node_name}''', None))
    # WARNING: Decompyle incomplete

    
    def process_body(self = None, body = None, from_start = None, prev_starts = (None, None)):
        '''Process the body of a compound statement.

        `body` is the body node to process.

        `from_start` is a single `ArcStart` that starts an arc into this body.
        `prev_starts` is a set of ArcStarts that can all be the start of arcs
        into this body.  Only one of `from_start` and `prev_starts` should be
        given.

        Records arcs within the body by calling `self.add_arc`.

        Returns a set of ArcStarts, the exits from this body.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def process_break_exits(self = None, exits = None):
        '''Add arcs due to jumps from `exits` being breaks.'''
        for block in self.nearest_blocks():
            if block.process_break_exits(exits, self.add_arc):
                return None
            return None

    
    def process_continue_exits(self = None, exits = None):
        '''Add arcs due to jumps from `exits` being continues.'''
        for block in self.nearest_blocks():
            if block.process_continue_exits(exits, self.add_arc):
                return None
            return None

    
    def process_raise_exits(self = None, exits = None):
        '''Add arcs due to jumps from `exits` being raises.'''
        for block in self.nearest_blocks():
            if block.process_raise_exits(exits, self.add_arc):
                return None
            return None

    
    def process_return_exits(self = None, exits = None):
        '''Add arcs due to jumps from `exits` being returns.'''
        for block in self.nearest_blocks():
            if block.process_return_exits(exits, self.add_arc):
                return None
            return None

    
    def _handle__Break(self = None, node = None):
        here = self.line_for_node(node)
        break_start = ArcStart(here, cause = "the break on line {lineno} wasn't executed")
        self.process_break_exits({
            break_start})
        return set()

    
    def _handle_decorated(self = None, node = None):
        '''Add arcs for things that can be decorated (classes and functions).'''
        main_line = node.lineno
        last = node.lineno
        decs = node.decorator_list
    # WARNING: Decompyle incomplete

    _handle__ClassDef = _handle_decorated
    
    def _handle__Continue(self = None, node = None):
        here = self.line_for_node(node)
        continue_start = ArcStart(here, cause = "the continue on line {lineno} wasn't executed")
        self.process_continue_exits({
            continue_start})
        return set()

    
    def _handle__For(self = None, node = None):
        start = self.line_for_node(node.iter)
        self.block_stack.append(LoopBlock(start = start))
        from_start = ArcStart(start, cause = 'the loop on line {lineno} never started')
        exits = self.process_body(node.body, from_start = from_start)
    # WARNING: Decompyle incomplete

    _handle__AsyncFor = _handle__For
    _handle__FunctionDef = _handle_decorated
    _handle__AsyncFunctionDef = _handle_decorated
    
    def _handle__If(self = None, node = None):
        start = self.line_for_node(node.test)
        (constant_test, val) = is_constant_test_expr(node.test)
        exits = set()
        if constant_test or val:
            from_start = ArcStart(start, cause = 'the condition on line {lineno} was never true')
            exits |= self.process_body(node.body, from_start = from_start)
        if not constant_test or val:
            from_start = ArcStart(start, cause = 'the condition on line {lineno} was always true')
            exits |= self.process_body(node.orelse, from_start = from_start)
        return exits

    
    def _handle__Match(self = None, node = None):
        start = self.line_for_node(node)
        last_start = start
        exits = set()
    # WARNING: Decompyle incomplete

    
    def _handle__Raise(self = None, node = None):
        here = self.line_for_node(node)
        raise_start = ArcStart(here, cause = "the raise on line {lineno} wasn't executed")
        self.process_raise_exits({
            raise_start})
        return set()

    
    def _handle__Return(self = None, node = None):
        here = self.line_for_node(node)
        return_start = ArcStart(here, cause = "the return on line {lineno} wasn't executed")
        self.process_return_exits({
            return_start})
        return set()

    
    def _handle__Try(self = None, node = None):
        if node.handlers:
            handler_start = self.line_for_node(node.handlers[0])
        else:
            handler_start = None
        if node.finalbody:
            final_start = self.line_for_node(node.finalbody[0])
        else:
            final_start = None
    # WARNING: Decompyle incomplete

    _handle__TryStar = _handle__Try
    
    def _handle__While(self = None, node = None):
        start = self.line_for_node(node.test)
        to_top = self.line_for_node(node.test)
        (constant_test, _) = is_constant_test_expr(node.test)
        self.block_stack.append(LoopBlock(start = to_top))
        from_start = ArcStart(start, cause = 'the condition on line {lineno} was never true')
        exits = self.process_body(node.body, from_start = from_start)
    # WARNING: Decompyle incomplete

    
    def _handle__With(self = None, node = None):
        pass
    # WARNING: Decompyle incomplete

    _handle__AsyncWith = _handle__With
