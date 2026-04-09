# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dpll2.pyc (Python 3.11)

'''Implementation of DPLL algorithm

Features:
  - Clause learning
  - Watch literal scheme
  - VSIDS heuristic

References:
  - https://en.wikipedia.org/wiki/DPLL_algorithm
'''
from collections import defaultdict
from heapq import heappush, heappop
from sympy.core.sorting import ordered
from sympy.assumptions.cnf import EncodedCNF
from sympy.logic.algorithms.lra_theory import LRASolver

def dpll_satisfiable(expr, all_models, use_lra_theory = (False, False)):
    '''
    Check satisfiability of a propositional sentence.
    It returns a model rather than True when it succeeds.
    Returns a generator of all models if all_models is True.

    Examples
    ========

    >>> from sympy.abc import A, B
    >>> from sympy.logic.algorithms.dpll2 import dpll_satisfiable
    >>> dpll_satisfiable(A & ~B)
    {A: True, B: False}
    >>> dpll_satisfiable(A & ~A)
    False

    '''
    if not isinstance(expr, EncodedCNF):
        exprs = EncodedCNF()
        exprs.add_prop(expr)
        expr = exprs
    if {
        0} in expr.data:
        if all_models:
            return (False,)()
        return None
    if None:
        (lra, immediate_conflicts) = LRASolver.from_encoded_cnf(expr)
    else:
        lra = None
        immediate_conflicts = []
    solver = SATSolver(expr.data + immediate_conflicts, expr.variables, set(), expr.symbols, lra_theory = lra)
    models = solver._find_model()
    if all_models:
        return _all_models(models)
    
    try:
        return next(models)
    except StopIteration:
        return False



def _all_models(models):
    pass
# WARNING: Decompyle incomplete


class SATSolver:
    '''
    Class for representing a SAT solver capable of
     finding a model to a boolean theory in conjunctive
     normal form.
    '''
    
    def __init__(self, clauses, variables, var_settings, symbols, heuristic, clause_learning, INTERVAL, lra_theory = (None, 'vsids', 'none', 500, None)):
        self.var_settings = var_settings
        self.heuristic = heuristic
        self.is_unsatisfied = False
        self._unit_prop_queue = []
        self.update_functions = []
        self.INTERVAL = INTERVAL
    # WARNING: Decompyle incomplete

    
    def _initialize_variables(self, variables):
        '''Set up the variable data structures needed.'''
        self.sentinels = defaultdict(set)
        self.occurrence_count = defaultdict(int)
        self.variable_set = [
            False] * (len(variables) + 1)

    
    def _initialize_clauses(self, clauses):
        '''Set up the clause data structures needed.

        For each clause, the following changes are made:
        - Unit clauses are queued for propagation right away.
        - Non-unit clauses have their first and last literals set as sentinels.
        - The number of clauses a literal appears in is computed.
        '''
        self.clauses = clauses()
        for i, clause in enumerate(self.clauses):
            if 1 == len(clause):
                self._unit_prop_queue.append(clause[0])
                continue
            self.sentinels[clause[0]].add(i)
            self.sentinels[clause[-1]].add(i)
            for lit in clause:
                return None

    
    def _find_model(self):
        '''
        Main DPLL loop. Returns a generator of models.

        Variables are chosen successively, and assigned to be either
        True or False. If a solution is not found with this setting,
        the opposite is chosen and the search continues. The solver
        halts when every variable has a setting.

        Examples
        ========

        >>> from sympy.logic.algorithms.dpll2 import SATSolver
        >>> l = SATSolver([{2, -3}, {1}, {3, -3}, {2, -2},
        ... {3, -2}], {1, 2, 3}, set())
        >>> list(l._find_model())
        [{1: True, 2: False, 3: False}, {1: True, 2: True, 3: True}]

        >>> from sympy.abc import A, B, C
        >>> l = SATSolver([{2, -3}, {1}, {3, -3}, {2, -2},
        ... {3, -2}], {1, 2, 3}, set(), [A, B, C])
        >>> list(l._find_model())
        [{A: True, B: False, C: False}, {A: True, B: True, C: True}]

        '''
        pass
    # WARNING: Decompyle incomplete

    _current_level = (lambda self: self.levels[-1])()
    
    def _clause_sat(self, cls):
        '''Check if a clause is satisfied by the current variable setting.

        Examples
        ========

        >>> from sympy.logic.algorithms.dpll2 import SATSolver
        >>> l = SATSolver([{1}, {-1}], {1}, set())
        >>> try:
        ...     next(l._find_model())
        ... except StopIteration:
        ...     pass
        >>> l._clause_sat(0)
        False
        >>> l._clause_sat(1)
        True

        '''
        for lit in self.clauses[cls]:
            if lit in self.var_settings:
                return True
            return False

    
    def _is_sentinel(self, lit, cls):
        '''Check if a literal is a sentinel of a given clause.

        Examples
        ========

        >>> from sympy.logic.algorithms.dpll2 import SATSolver
        >>> l = SATSolver([{2, -3}, {1}, {3, -3}, {2, -2},
        ... {3, -2}], {1, 2, 3}, set())
        >>> next(l._find_model())
        {1: True, 2: False, 3: False}
        >>> l._is_sentinel(2, 3)
        True
        >>> l._is_sentinel(-3, 1)
        False

        '''
        return cls in self.sentinels[lit]

    
    def _assign_literal(self, lit):
        '''Make a literal assignment.

        The literal assignment must be recorded as part of the current
        decision level. Additionally, if the literal is marked as a
        sentinel of any clause, then a new sentinel must be chosen. If
        this is not possible, then unit propagation is triggered and
        another literal is added to the queue to be set in the future.

        Examples
        ========

        >>> from sympy.logic.algorithms.dpll2 import SATSolver
        >>> l = SATSolver([{2, -3}, {1}, {3, -3}, {2, -2},
        ... {3, -2}], {1, 2, 3}, set())
        >>> next(l._find_model())
        {1: True, 2: False, 3: False}
        >>> l.var_settings
        {-3, -2, 1}

        >>> l = SATSolver([{2, -3}, {1}, {3, -3}, {2, -2},
        ... {3, -2}], {1, 2, 3}, set())
        >>> l._assign_literal(-1)
        >>> try:
        ...     next(l._find_model())
        ... except StopIteration:
        ...     pass
        >>> l.var_settings
        {-1}

        '''
        self.var_settings.add(lit)
        self._current_level.var_settings.add(lit)
        self.variable_set[abs(lit)] = True
        self.heur_lit_assigned(lit)
        sentinel_list = list(self.sentinels[-lit])
        for cls in sentinel_list:
            if not self._clause_sat(cls):
                other_sentinel = None
                for newlit in self.clauses[cls]:
                    if newlit != -lit:
                        if self._is_sentinel(newlit, cls):
                            other_sentinel = newlit
                            continue
                        if not self.variable_set[abs(newlit)]:
                            self.sentinels[-lit].remove(cls)
                            self.sentinels[newlit].add(cls)
                            other_sentinel = None
                        
                        if other_sentinel:
                            self._unit_prop_queue.append(other_sentinel)
            return None

    
    def _undo(self):
        '''
        _undo the changes of the most recent decision level.

        Examples
        ========

        >>> from sympy.logic.algorithms.dpll2 import SATSolver
        >>> l = SATSolver([{2, -3}, {1}, {3, -3}, {2, -2},
        ... {3, -2}], {1, 2, 3}, set())
        >>> next(l._find_model())
        {1: True, 2: False, 3: False}
        >>> level = l._current_level
        >>> level.decision, level.var_settings, level.flipped
        (-3, {-3, -2}, False)
        >>> l._undo()
        >>> level = l._current_level
        >>> level.decision, level.var_settings, level.flipped
        (0, {1}, False)

        '''
        for lit in self._current_level.var_settings:
            self.var_settings.remove(lit)
            self.heur_lit_unset(lit)
            self.variable_set[abs(lit)] = False
            self.levels.pop()
            return None

    
    def _simplify(self):
        '''Iterate over the various forms of propagation to simplify the theory.

        Examples
        ========

        >>> from sympy.logic.algorithms.dpll2 import SATSolver
        >>> l = SATSolver([{2, -3}, {1}, {3, -3}, {2, -2},
        ... {3, -2}], {1, 2, 3}, set())
        >>> l.variable_set
        [False, False, False, False]
        >>> l.sentinels
        {-3: {0, 2}, -2: {3, 4}, 2: {0, 3}, 3: {2, 4}}

        >>> l._simplify()

        >>> l.variable_set
        [False, True, False, False]
        >>> l.sentinels
        {-3: {0, 2}, -2: {3, 4}, -1: set(), 2: {0, 3},
        ...3: {2, 4}}

        '''
        changed = True
    # WARNING: Decompyle incomplete

    
    def _unit_prop(self):
        '''Perform unit propagation on the current theory.'''
        result = len(self._unit_prop_queue) > 0
    # WARNING: Decompyle incomplete

    
    def _pure_literal(self):
        '''Look for pure literals and assign them when found.'''
        return False

    
    def _vsids_init(self):
        '''Initialize the data structures needed for the VSIDS heuristic.'''
        self.lit_heap = []
        self.lit_scores = { }
        for var in range(1, len(self.variable_set)):
            self.lit_scores[var] = float(-self.occurrence_count[var])
            self.lit_scores[-var] = float(-self.occurrence_count[-var])
            heappush(self.lit_heap, (self.lit_scores[var], var))
            heappush(self.lit_heap, (self.lit_scores[-var], -var))
            return None

    
    def _vsids_decay(self):
        '''Decay the VSIDS scores for every literal.

        Examples
        ========

        >>> from sympy.logic.algorithms.dpll2 import SATSolver
        >>> l = SATSolver([{2, -3}, {1}, {3, -3}, {2, -2},
        ... {3, -2}], {1, 2, 3}, set())

        >>> l.lit_scores
        {-3: -2.0, -2: -2.0, -1: 0.0, 1: 0.0, 2: -2.0, 3: -2.0}

        >>> l._vsids_decay()

        >>> l.lit_scores
        {-3: -1.0, -2: -1.0, -1: 0.0, 1: 0.0, 2: -1.0, 3: -1.0}

        '''
        for lit in self.lit_scores.keys():
            return None

    
    def _vsids_calculate(self):
        '''
            VSIDS Heuristic Calculation

        Examples
        ========

        >>> from sympy.logic.algorithms.dpll2 import SATSolver
        >>> l = SATSolver([{2, -3}, {1}, {3, -3}, {2, -2},
        ... {3, -2}], {1, 2, 3}, set())

        >>> l.lit_heap
        [(-2.0, -3), (-2.0, 2), (-2.0, -2), (0.0, 1), (-2.0, 3), (0.0, -1)]

        >>> l._vsids_calculate()
        -3

        >>> l.lit_heap
        [(-2.0, -2), (-2.0, 2), (0.0, -1), (0.0, 1), (-2.0, 3)]

        '''
        if len(self.lit_heap) == 0:
            return 0
    # WARNING: Decompyle incomplete

    
    def _vsids_lit_assigned(self, lit):
        '''Handle the assignment of a literal for the VSIDS heuristic.'''
        pass

    
    def _vsids_lit_unset(self, lit):
        '''Handle the unsetting of a literal for the VSIDS heuristic.

        Examples
        ========

        >>> from sympy.logic.algorithms.dpll2 import SATSolver
        >>> l = SATSolver([{2, -3}, {1}, {3, -3}, {2, -2},
        ... {3, -2}], {1, 2, 3}, set())
        >>> l.lit_heap
        [(-2.0, -3), (-2.0, 2), (-2.0, -2), (0.0, 1), (-2.0, 3), (0.0, -1)]

        >>> l._vsids_lit_unset(2)

        >>> l.lit_heap
        [(-2.0, -3), (-2.0, -2), (-2.0, -2), (-2.0, 2), (-2.0, 3), (0.0, -1),
        ...(-2.0, 2), (0.0, 1)]

        '''
        var = abs(lit)
        heappush(self.lit_heap, (self.lit_scores[var], var))
        heappush(self.lit_heap, (self.lit_scores[-var], -var))

    
    def _vsids_clause_added(self, cls):
        '''Handle the addition of a new clause for the VSIDS heuristic.

        Examples
        ========

        >>> from sympy.logic.algorithms.dpll2 import SATSolver
        >>> l = SATSolver([{2, -3}, {1}, {3, -3}, {2, -2},
        ... {3, -2}], {1, 2, 3}, set())

        >>> l.num_learned_clauses
        0
        >>> l.lit_scores
        {-3: -2.0, -2: -2.0, -1: 0.0, 1: 0.0, 2: -2.0, 3: -2.0}

        >>> l._vsids_clause_added({2, -3})

        >>> l.num_learned_clauses
        1
        >>> l.lit_scores
        {-3: -1.0, -2: -2.0, -1: 0.0, 1: 0.0, 2: -1.0, 3: -2.0}

        '''
        for None in cls:
            return None

    
    def _simple_add_learned_clause(self, cls):
        '''Add a new clause to the theory.

        Examples
        ========

        >>> from sympy.logic.algorithms.dpll2 import SATSolver
        >>> l = SATSolver([{2, -3}, {1}, {3, -3}, {2, -2},
        ... {3, -2}], {1, 2, 3}, set())

        >>> l.num_learned_clauses
        0
        >>> l.clauses
        [[2, -3], [1], [3, -3], [2, -2], [3, -2]]
        >>> l.sentinels
        {-3: {0, 2}, -2: {3, 4}, 2: {0, 3}, 3: {2, 4}}

        >>> l._simple_add_learned_clause([3])

        >>> l.clauses
        [[2, -3], [1], [3, -3], [2, -2], [3, -2], [3]]
        >>> l.sentinels
        {-3: {0, 2}, -2: {3, 4}, 2: {0, 3}, 3: {2, 4, 5}}

        '''
        cls_num = len(self.clauses)
        self.clauses.append(cls)
        for lit in cls:
            self.sentinels[cls[0]].add(cls_num)
            self.sentinels[cls[-1]].add(cls_num)
            self.heur_clause_added(cls)
            return None

    
    def _simple_compute_conflict(self):
        ''' Build a clause representing the fact that at least one decision made
        so far is wrong.

        Examples
        ========

        >>> from sympy.logic.algorithms.dpll2 import SATSolver
        >>> l = SATSolver([{2, -3}, {1}, {3, -3}, {2, -2},
        ... {3, -2}], {1, 2, 3}, set())
        >>> next(l._find_model())
        {1: True, 2: False, 3: False}
        >>> l._simple_compute_conflict()
        [3]

        '''
        return self.levels[1:]()

    
    def _simple_clean_clauses(self):
        '''Clean up learned clauses.'''
        pass



class Level:
    '''
    Represents a single level in the DPLL algorithm, and contains
    enough information for a sound backtracking procedure.
    '''
    
    def __init__(self, decision, flipped = (False,)):
        self.decision = decision
        self.var_settings = set()
        self.flipped = flipped
