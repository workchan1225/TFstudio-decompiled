# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: facts.pyc (Python 3.11)

"""This is rule-based deduction system for SymPy

The whole thing is split into two parts

 - rules compilation and preparation of tables
 - runtime inference

For rule-based inference engines, the classical work is RETE algorithm [1],
[2] Although we are not implementing it in full (or even significantly)
it's still worth a read to understand the underlying ideas.

In short, every rule in a system of rules is one of two forms:

 - atom                     -> ...      (alpha rule)
 - And(atom1, atom2, ...)   -> ...      (beta rule)


The major complexity is in efficient beta-rules processing and usually for an
expert system a lot of effort goes into code that operates on beta-rules.


Here we take minimalistic approach to get something usable first.

 - (preparation)    of alpha- and beta- networks, everything except
 - (runtime)        FactRules.deduce_all_facts

             _____________________________________
            ( Kirr: I've never thought that doing )
            ( logic stuff is that difficult...    )
             -------------------------------------
                    o   ^__^
                     o  (oo)\\_______
                        (__)\\       )\\/\\
                            ||----w |
                            ||     ||


Some references on the topic
----------------------------

[1] https://en.wikipedia.org/wiki/Rete_algorithm
[2] http://reports-archive.adm.cs.cmu.edu/anon/1995/CMU-CS-95-113.pdf

https://en.wikipedia.org/wiki/Propositional_formula
https://en.wikipedia.org/wiki/Inference_rule
https://en.wikipedia.org/wiki/List_of_rules_of_inference
"""
from collections import defaultdict
from typing import Iterator
from logic import Logic, And, Or, Not

def _base_fact(atom):
    '''Return the literal fact of an atom.

    Effectively, this merely strips the Not around a fact.
    '''
    if isinstance(atom, Not):
        return atom.arg


def _as_pair(atom):
    if isinstance(atom, Not):
        return (atom.arg, False)
    return (None, True)


def transitive_closure(implications):
    """
    Computes the transitive closure of a list of implications

    Uses Warshall's algorithm, as described at
    http://www.cs.hope.edu/~cusack/Notes/Notes/DiscreteMath/Warshall.pdf.
    """
    full_implications = set(implications)
# WARNING: Decompyle incomplete


def deduce_alpha_implications(implications):
    '''deduce all implications

       Description by example
       ----------------------

       given set of logic rules:

         a -> b
         b -> c

       we deduce all possible rules:

         a -> b, c
         b -> c


       implications: [] of (a,b)
       return:       {} of a -> set([b, c, ...])
    '''
    implications = (lambda .0: [ (Not(j), Not(i)) for i, j in .0 ]) + implications()
    res = defaultdict(set)
    full_implications = transitive_closure(implications)
    for a, b in full_implications:
        if a == b:
            continue
        res[a].add(b)
        for a, impl in res.items():
            impl.discard(a)
            na = Not(a)
            if na in impl:
                raise ValueError(f'''implications are inconsistent: {a!s} -> {na!s} {impl!s}''')
            return res


def apply_beta_to_alpha_route(alpha_implications, beta_rules):
    """apply additional beta-rules (And conditions) to already-built
    alpha implication tables

       TODO: write about

       - static extension of alpha-chains
       - attaching refs to beta-nodes to alpha chains


       e.g.

       alpha_implications:

       a  ->  [b, !c, d]
       b  ->  [d]
       ...


       beta_rules:

       &(b,d) -> e


       then we'll extend a's rule to the following

       a  ->  [b, !c, d, e]
    """
    pass
# WARNING: Decompyle incomplete


def rules_2prereq(rules):
    """build prerequisites table from rules

       Description by example
       ----------------------

       given set of logic rules:

         a -> b, c
         b -> c

       we build prerequisites (from what points something can be deduced):

         b <- a
         c <- a, b

       rules:   {} of a -> [b, c, ...]
       return:  {} of c <- [a, b, ...]

       Note however, that this prerequisites may be *not* enough to prove a
       fact. An example is 'a -> b' rule, where prereq(a) is b, and prereq(b)
       is a. That's because a=T -> b=T, and b=F -> a=F, but a=F -> b=?
    """
    prereq = defaultdict(set)
    for a, _ in rules.items():
        impl = None
        if isinstance(a, Not):
            a = a.args[0]
        for i, _ in impl:
            if isinstance(i, Not):
                i = i.args[0]
            prereq[i].add(a)
            return prereq


class TautologyDetected(Exception):
    '''(internal) Prover uses it for reporting detected tautology'''
    pass


class Prover:
    '''ai - prover of logic rules

       given a set of initial rules, Prover tries to prove all possible rules
       which follow from given premises.

       As a result proved_rules are always either in one of two forms: alpha or
       beta:

       Alpha rules
       -----------

       This are rules of the form::

         a -> b & c & d & ...


       Beta rules
       ----------

       This are rules of the form::

         &(a,b,...) -> c & d & ...


       i.e. beta rules are join conditions that say that something follows when
       *several* facts are true at the same time.
    '''
    
    def __init__(self):
        self.proved_rules = []
        self._rules_seen = set()

    
    def split_alpha_beta(self):
        '''split proved rules into alpha and beta chains'''
        rules_alpha = []
        rules_beta = []
        for a, b in self.proved_rules:
            if isinstance(a, And):
                rules_beta.append((a, b))
                continue
            rules_alpha.append((a, b))
            return (rules_alpha, rules_beta)

    rules_alpha = (lambda self: self.split_alpha_beta()[0])()
    rules_beta = (lambda self: self.split_alpha_beta()[1])()
    
    def process_rule(self, a, b):
        '''process a -> b rule'''
        if a or isinstance(b, bool):
            return None
        if None(a, bool):
            return None
        if (None, b) in self._rules_seen:
            return None
        None._rules_seen.add((a, b))
        
        try:
            self._process_rule(a, b)
            return None
        except TautologyDetected:
            return None


    
    def _process_rule(self, a, b):
        pass
    # WARNING: Decompyle incomplete



class FactRules:
    """Rules that describe how to deduce facts in logic space

       When defined, these rules allow implications to quickly be determined
       for a set of facts. For this precomputed deduction tables are used.
       see `deduce_all_facts`   (forward-chaining)

       Also it is possible to gather prerequisites for a fact, which is tried
       to be proven.    (backward-chaining)


       Definition Syntax
       -----------------

       a -> b       -- a=T -> b=T  (and automatically b=F -> a=F)
       a -> !b      -- a=T -> b=F
       a == b       -- a -> b & b -> a
       a -> b & c   -- a=T -> b=T & c=T
       # TODO b | c


       Internals
       ---------

       .full_implications[k, v]: all the implications of fact k=v
       .beta_triggers[k, v]: beta rules that might be triggered when k=v
       .prereq  -- {} k <- [] of k's prerequisites

       .defined_facts -- set of defined fact names
    """
    
    def __init__(self, rules):
        '''Compile rules into internal lookup tables'''
        if isinstance(rules, str):
            rules = rules.splitlines()
        P = Prover()
        for rule in rules:
            (a, op, b) = rule.split(None, 2)
            a = Logic.fromstring(a)
            b = Logic.fromstring(b)
            if op == '->':
                P.process_rule(a, b)
                continue
            if op == '==':
                P.process_rule(a, b)
                P.process_rule(b, a)
                continue
            raise ValueError('unknown op %r' % op)
            self.beta_rules = []
            for bcond, bimpl in P.rules_beta:
                (lambda .0: pass# WARNING: Decompyle incomplete
)((bcond.args(), _as_pair(bimpl)))
                impl_a = deduce_alpha_implications(P.rules_alpha)
                impl_ab = apply_beta_to_alpha_route(impl_a, P.rules_beta)
                self.defined_facts = impl_ab.keys()()
                full_implications = defaultdict(set)
                beta_triggers = defaultdict(set)
                for impl, betaidxs in impl_ab.items():
                    full_implications[_as_pair(k)] = impl()
                    beta_triggers[_as_pair(k)] = betaidxs
                    self.full_implications = full_implications
                    self.beta_triggers = beta_triggers
                    prereq = defaultdict(set)
                    rel_prereq = rules_2prereq(full_implications)
                    for k, pitems in rel_prereq.items():
                        
                        def prereq(.0):
                            pass
                        # WARNING: Decompyle incomplete

                        return None

    
    def _to_python(self = None):
        ''' Generate a string with plain python representation of the instance '''
        return '\n'.join(self.print_rules())

    _from_python = (lambda cls = None, data = None: self = cls('')for key in ('full_implications', 'beta_triggers', 'prereq'):
d = defaultdict(set)d.update(data[key])setattr(self, key, d)self.beta_rules = data['beta_rules']self.defined_facts = set(data['defined_facts'])self)()
    
    def _defined_facts_lines(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _full_implications_lines(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _prereq_lines(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _beta_rules_lines(self):
        pass
    # WARNING: Decompyle incomplete

    
    def print_rules(self = None):
        ''' Returns a generator with lines to represent the facts and rules '''
        pass
    # WARNING: Decompyle incomplete



class InconsistentAssumptions(ValueError):
    
    def __str__(self):
        (kb, fact, value) = self.args
        return f'''{kb!s}, {fact!s}={value!s}'''



class FactKB(dict):
    '''
    A simple propositional knowledge base relying on compiled inference rules.
    '''
    
    def __str__(self):
        return ',\n'.join % (lambda .0: [ '\t%s: %s' % i for i in .0 ])(sorted(self.items())())

    
    def __init__(self, rules):
        self.rules = rules

    
    def _tell(self, k, v):
        '''Add fact k=v to the knowledge base.

        Returns True if the KB has actually been updated, False otherwise.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def deduce_all_facts(self, facts):
        '''
        Update the KB with all the implications of a list of facts.

        Facts can be specified as a dictionary or as a list of (key, value)
        pairs.
        '''
        pass
    # WARNING: Decompyle incomplete
