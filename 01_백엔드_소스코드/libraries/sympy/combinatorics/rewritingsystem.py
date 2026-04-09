# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rewritingsystem.pyc (Python 3.11)

from collections import deque
from sympy.combinatorics.rewritingsystem_fsm import StateMachine

class RewritingSystem:
    """
    A class implementing rewriting systems for `FpGroup`s.

    References
    ==========
    .. [1] Epstein, D., Holt, D. and Rees, S. (1991).
           The use of Knuth-Bendix methods to solve the word problem in automatic groups.
           Journal of Symbolic Computation, 12(4-5), pp.397-414.

    .. [2] GAP's Manual on its KBMAG package
           https://www.gap-system.org/Manuals/pkg/kbmag-1.5.3/doc/manual.pdf

    """
    
    def __init__(self, group):
        self.group = group
        self.alphabet = group.generators
        self._is_confluent = None
        self.maxeqns = 32767
        self.tidyint = 100
        self._max_exceeded = False
        self.reduction_automaton = None
        self._new_rules = { }
        self.rules = { }
        self.rules_cache = deque([], 50)
        self._init_rules()
        generators = list(self.alphabet)
        (lambda .0: [ gen ** -1 for gen in .0 ]) += generators()
        self.reduction_automaton = StateMachine('Reduction automaton for ' + repr(self.group), generators)
        self.construct_automaton()

    
    def set_max(self, n):
        '''
        Set the maximum number of rules that can be defined

        '''
        if n > self.maxeqns:
            self._max_exceeded = False
        self.maxeqns = n

    is_confluent = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def _init_rules(self):
        identity = self.group.free_group.identity
        for r in self.group.relators:
            self.add_rule(r, identity)
            self._remove_redundancies()
            return None

    
    def _add_rule(self, r1, r2):
        '''
        Add the rule r1 -> r2 with no checking or further
        deductions

        '''
        if len(self.rules) + 1 > self.maxeqns:
            self._is_confluent = self._check_confluence()
            self._max_exceeded = True
            raise RuntimeError('Too many rules were defined.')
        self.rules[r1] = r2
        if self.reduction_automaton:
            self._new_rules[r1] = r2
            return None

    
    def add_rule(self, w1, w2, check = (False,)):
        new_keys = set()
        if w1 == w2:
            return new_keys
        if None < w2:
            w2 = w1
            w1 = w2
        if (w1, w2) in self.rules_cache:
            return new_keys
        None.rules_cache.append((w1, w2))
        s2 = w2
        s1 = w1
        if len(s1) - len(s2) < 3:
            if s1 not in self.rules:
                new_keys.add(s1)
                if not check:
                    self._add_rule(s1, s2)
            if s2 ** -1 > s1 ** -1 and s2 ** -1 not in self.rules:
                new_keys.add(s2 ** -1)
                if not check:
                    self._add_rule(s2 ** -1, s1 ** -1)
    # WARNING: Decompyle incomplete

    
    def _remove_redundancies(self, changes = (False,)):
        '''
        Reduce left- and right-hand sides of reduction rules
        and remove redundant equations (i.e. those for which
        lhs == rhs). If `changes` is `True`, return a set
        containing the removed keys and a set containing the
        added keys

        '''
        removed = set()
        added = set()
        rules = self.rules.copy()
        for r in rules:
            v = self.reduce(r, exclude = r)
            w = self.reduce(rules[r])
            if v != r:
                del self.rules[r]
                removed.add(r)
                if v > w:
                    added.add(v)
                    self.rules[v] = w
                    continue
                if v < w:
                    added.add(w)
                    self.rules[w] = v
                continue
            self.rules[v] = w
            if changes:
                return (removed, added)
            return None

    
    def make_confluent(self, check = (False,)):
        '''
        Try to make the system confluent using the Knuth-Bendix
        completion algorithm

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _check_confluence(self):
        return self.make_confluent(check = True)

    
    def reduce(self, word, exclude = (None,)):
        '''
        Apply reduction rules to `word` excluding the reduction rule
        for the lhs equal to `exclude`

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _compute_inverse_rules(self, rules):
        '''
        Compute the inverse rules for a given set of rules.
        The inverse rules are used in the automaton for word reduction.

        Arguments:
            rules (dictionary): Rules for which the inverse rules are to computed.

        Returns:
            Dictionary of inverse_rules.

        '''
        inverse_rules = { }
        for r in rules:
            rule_key_inverse = r ** -1
            rule_value_inverse = rules[r] ** -1
            if rule_value_inverse < rule_key_inverse:
                inverse_rules[rule_key_inverse] = rule_value_inverse
                continue
            inverse_rules[rule_value_inverse] = rule_key_inverse
            return inverse_rules

    
    def construct_automaton(self):
        '''
        Construct the automaton based on the set of reduction rules of the system.

        Automata Design:
        The accept states of the automaton are the proper prefixes of the left hand side of the rules.
        The complete left hand side of the rules are the dead states of the automaton.

        '''
        self._add_to_automaton(self.rules)

    
    def _add_to_automaton(self, rules):
        '''
        Add new states and transitions to the automaton.

        Summary:
        States corresponding to the new rules added to the system are computed and added to the automaton.
        Transitions in the previously added states are also modified if necessary.

        Arguments:
            rules (dictionary) -- Dictionary of the newly added rules.

        '''
        automaton_alphabet = []
        proper_prefixes = { }
        all_rules = rules
        inverse_rules = self._compute_inverse_rules(all_rules)
        all_rules.update(inverse_rules)
        accept_states = []
    # WARNING: Decompyle incomplete

    
    def reduce_using_automaton(self, word):
        '''
        Reduce a word using an automaton.

        Summary:
        All the symbols of the word are stored in an array and are given as the input to the automaton.
        If the automaton reaches a dead state that subword is replaced and the automaton is run from the beginning.
        The complete word has to be replaced when the word is read and the automaton reaches a dead state.
        So, this process is repeated until the word is read completely and the automaton reaches the accept state.

        Arguments:
            word (instance of FreeGroupElement) -- Word that needs to be reduced.

        '''
        if self._new_rules:
            self._add_to_automaton(self._new_rules)
            self._new_rules = { }
        flag = 1
    # WARNING: Decompyle incomplete
