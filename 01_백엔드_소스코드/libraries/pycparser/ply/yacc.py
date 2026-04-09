# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: yacc.pyc (Python 3.11)

import re
import types
import sys
import os.path as os
import inspect
import base64
import warnings
__version__ = '3.10'
__tabversion__ = '3.10'
yaccdebug = True
debug_file = 'parser.out'
tab_module = 'parsetab'
default_lr = 'LALR'
error_count = 3
yaccdevel = False
resultlimit = 40
pickle_protocol = 0
if sys.version_info[0] < 3:
    string_types = basestring
else:
    string_types = str
MAXINT = sys.maxsize

class PlyLogger(object):
    
    def __init__(self, f):
        self.f = f

    
    def debug(self, msg, *args, **kwargs):
        self.f.write(msg % args + '\n')

    info = debug
    
    def warning(self, msg, *args, **kwargs):
        self.f.write('WARNING: ' + msg % args + '\n')

    
    def error(self, msg, *args, **kwargs):
        self.f.write('ERROR: ' + msg % args + '\n')

    critical = debug


class NullLogger(object):
    
    def __getattribute__(self, name):
        return self

    
    def __call__(self, *args, **kwargs):
        return self



class YaccError(Exception):
    pass


def format_result(r):
    repr_str = repr(r)
    if '\n' in repr_str:
        repr_str = repr(repr_str)
    if len(repr_str) > resultlimit:
        repr_str = repr_str[:resultlimit] + ' ...'
    result = '<%s @ 0x%x> (%s)' % (type(r).__name__, id(r), repr_str)
    return result


def format_stack_entry(r):
    repr_str = repr(r)
    if '\n' in repr_str:
        repr_str = repr(repr_str)
    if len(repr_str) < 16:
        return repr_str
    return None % (type(r).__name__, id(r))

_errok = None
_token = None
_restart = None
_warnmsg = "PLY: Don't use global functions errok(), token(), and restart() in p_error().\nInstead, invoke the methods on the associated parser instance:\n\n    def p_error(p):\n        ...\n        # Use parser.errok(), parser.token(), parser.restart()\n        ...\n\n    parser = yacc.yacc()\n"

def errok():
    warnings.warn(_warnmsg)
    return _errok()


def restart():
    warnings.warn(_warnmsg)
    return _restart()


def token():
    warnings.warn(_warnmsg)
    return _token()


def call_errorfunc(errorfunc, token, parser):
    global _errok, _token, _restart, _errok, _token, _restart
    _errok = parser.errok
    _token = parser.token
    _restart = parser.restart
    r = errorfunc(token)
    
    try:
        del _errok
        del _token
        del _restart
    except NameError:
        pass

    return r


class YaccSymbol:
    
    def __str__(self):
        return self.type

    
    def __repr__(self):
        return str(self)



class YaccProduction:
    
    def __init__(self, s, stack = (None,)):
        self.slice = s
        self.stack = stack
        self.lexer = None
        self.parser = None

    
    def __getitem__(self, n):
        if isinstance(n, slice):
            return self.slice[n]()
        if None >= 0:
            return self.slice[n].value
        return None.stack[n].value

    
    def __setitem__(self, n, v):
        self.slice[n].value = v

    
    def __getslice__(self, i, j):
        return self.slice[i:j]()

    
    def __len__(self):
        return len(self.slice)

    
    def lineno(self, n):
        return getattr(self.slice[n], 'lineno', 0)

    
    def set_lineno(self, n, lineno):
        self.slice[n].lineno = lineno

    
    def linespan(self, n):
        startline = getattr(self.slice[n], 'lineno', 0)
        endline = getattr(self.slice[n], 'endlineno', startline)
        return (startline, endline)

    
    def lexpos(self, n):
        return getattr(self.slice[n], 'lexpos', 0)

    
    def lexspan(self, n):
        startpos = getattr(self.slice[n], 'lexpos', 0)
        endpos = getattr(self.slice[n], 'endlexpos', startpos)
        return (startpos, endpos)

    
    def error(self):
        raise SyntaxError



class LRParser:
    
    def __init__(self, lrtab, errorf):
        self.productions = lrtab.lr_productions
        self.action = lrtab.lr_action
        self.goto = lrtab.lr_goto
        self.errorfunc = errorf
        self.set_defaulted_states()
        self.errorok = True

    
    def errok(self):
        self.errorok = True

    
    def restart(self):
        del self.statestack[:]
        del self.symstack[:]
        sym = YaccSymbol()
        sym.type = '$end'
        self.symstack.append(sym)
        self.statestack.append(0)

    
    def set_defaulted_states(self):
        self.defaulted_states = { }
        for state, actions in self.action.items():
            rules = list(actions.values())
            if len(rules) == 1 and rules[0] < 0:
                self.defaulted_states[state] = rules[0]
            return None

    
    def disable_defaulted_states(self):
        self.defaulted_states = { }

    
    def parse(self, input, lexer, debug, tracking, tokenfunc = (None, None, False, False, None)):
        if debug or yaccdevel:
            if isinstance(debug, int):
                debug = PlyLogger(sys.stderr)
            return self.parsedebug(input, lexer, debug, tracking, tokenfunc)
        if None:
            return self.parseopt(input, lexer, debug, tracking, tokenfunc)
        return None.parseopt_notrack(input, lexer, debug, tracking, tokenfunc)

    
    def parsedebug(self, input, lexer, debug, tracking, tokenfunc = (None, None, False, False, None)):
        lookahead = None
        lookaheadstack = []
        actions = self.action
        goto = self.goto
        prod = self.productions
        defaulted_states = self.defaulted_states
        pslice = YaccProduction(None)
        errorcount = 0
        debug.info('PLY: PARSE DEBUG START')
        if not lexer:
            lex = lex
            import 
            lexer = lex.lexer
        pslice.lexer = lexer
        pslice.parser = self
    # WARNING: Decompyle incomplete

    
    def parseopt(self, input, lexer, debug, tracking, tokenfunc = (None, None, False, False, None)):
        lookahead = None
        lookaheadstack = []
        actions = self.action
        goto = self.goto
        prod = self.productions
        defaulted_states = self.defaulted_states
        pslice = YaccProduction(None)
        errorcount = 0
        if not lexer:
            lex = lex
            import 
            lexer = lex.lexer
        pslice.lexer = lexer
        pslice.parser = self
    # WARNING: Decompyle incomplete

    
    def parseopt_notrack(self, input, lexer, debug, tracking, tokenfunc = (None, None, False, False, None)):
        lookahead = None
        lookaheadstack = []
        actions = self.action
        goto = self.goto
        prod = self.productions
        defaulted_states = self.defaulted_states
        pslice = YaccProduction(None)
        errorcount = 0
        if not lexer:
            lex = lex
            import 
            lexer = lex.lexer
        pslice.lexer = lexer
        pslice.parser = self
    # WARNING: Decompyle incomplete


_is_identifier = re.compile('^[a-zA-Z0-9_-]+$')

class Production(object):
    reduced = 0
    
    def __init__(self, number, name, prod, precedence, func, file, line = (('right', 0), None, '', 0)):
        self.name = name
        self.prod = tuple(prod)
        self.number = number
        self.func = func
        self.callable = None
        self.file = file
        self.line = line
        self.prec = precedence
        self.len = len(self.prod)
        self.usyms = []
        for s in self.prod:
            if s not in self.usyms:
                self.usyms.append(s)
            self.lr_items = []
            self.lr_next = None
            if self.prod:
                self.str = f'''{self.name!s} -> {' '.join(self.prod)!s}'''
                return None
            self.str = None % self.name
            return None

    
    def __str__(self):
        return self.str

    
    def __repr__(self):
        return 'Production(' + str(self) + ')'

    
    def __len__(self):
        return len(self.prod)

    
    def __nonzero__(self):
        return 1

    
    def __getitem__(self, index):
        return self.prod[index]

    
    def lr_item(self, n):
        if n > len(self.prod):
            return None
        p = None(self, n)
        
        try:
            p.lr_after = Prodnames[p.prod[n + 1]]
        except (IndexError, KeyError):
            p.lr_after = []

        
        try:
            p.lr_before = p.prod[n - 1]
        except IndexError:
            p.lr_before = None

        return p

    
    def bind(self, pdict):
        if self.func:
            self.callable = pdict[self.func]
            return None



class MiniProduction(object):
    
    def __init__(self, str, name, len, func, file, line):
        self.name = name
        self.len = len
        self.func = func
        self.callable = None
        self.file = file
        self.line = line
        self.str = str

    
    def __str__(self):
        return self.str

    
    def __repr__(self):
        return 'MiniProduction(%s)' % self.str

    
    def bind(self, pdict):
        if self.func:
            self.callable = pdict[self.func]
            return None



class LRItem(object):
    
    def __init__(self, p, n):
        self.name = p.name
        self.prod = list(p.prod)
        self.number = p.number
        self.lr_index = n
        self.lookaheads = { }
        self.prod.insert(n, '.')
        self.prod = tuple(self.prod)
        self.len = len(self.prod)
        self.usyms = p.usyms

    
    def __str__(self):
        if self.prod:
            s = f'''{self.name!s} -> {' '.join(self.prod)!s}'''
        else:
            s = '%s -> <empty>' % self.name
        return s

    
    def __repr__(self):
        return 'LRItem(' + str(self) + ')'



def rightmost_terminal(symbols, terminals):
    i = len(symbols) - 1
# WARNING: Decompyle incomplete


class GrammarError(YaccError):
    pass


class Grammar(object):
    
    def __init__(self, terminals):
        self.Productions = [
            None]
        self.Prodnames = { }
        self.Prodmap = { }
        self.Terminals = { }
        for term in terminals:
            self.Terminals[term] = []
            self.Terminals['error'] = []
            self.Nonterminals = { }
            self.First = { }
            self.Follow = { }
            self.Precedence = { }
            self.UsedPrecedence = set()
            self.Start = None
            return None

    
    def __len__(self):
        return len(self.Productions)

    
    def __getitem__(self, index):
        return self.Productions[index]

    
    def set_precedence(self, term, assoc, level):
        pass
    # WARNING: Decompyle incomplete

    
    def add_production(self, prodname, syms, func, file, line = (None, '', 0)):
        if prodname in self.Terminals:
            raise GrammarError('%s:%d: Illegal rule name %r. Already defined as a token' % (file, line, prodname))
        if prodname == 'error':
            raise GrammarError('%s:%d: Illegal rule name %r. error is a reserved word' % (file, line, prodname))
        if not _is_identifier.match(prodname):
            raise GrammarError('%s:%d: Illegal rule name %r' % (file, line, prodname))
        for n, s in enumerate(syms):
            if s[0] in '\'"':
                c = eval(s)
                if len(c) > 1:
                    raise GrammarError('%s:%d: Literal token %s in rule %r may only be a single character' % (file, line, s, prodname))
                if c not in self.Terminals:
                    self.Terminals[c] = []
                syms[n] = c
                continue
                except SyntaxError:
                    pass
                if _is_identifier.match(s) and s != '%prec':
                    raise GrammarError('%s:%d: Illegal name %r in rule %r' % (file, line, s, prodname))
                continue
                if '%prec' in syms:
                    if syms[-1] == '%prec':
                        raise GrammarError('%s:%d: Syntax error. Nothing follows %%prec' % (file, line))
                    if syms[-2] != '%prec':
                        raise GrammarError('%s:%d: Syntax error. %%prec can only appear at the end of a grammar rule' % (file, line))
                    precname = syms[-1]
                    prodprec = self.Precedence.get(precname)
                    if not prodprec:
                        raise GrammarError('%s:%d: Nothing known about the precedence of %r' % (file, line, precname))
                    self.UsedPrecedence.add(precname)
                    del syms[-2:]
                else:
                    precname = rightmost_terminal(syms, self.Terminals)
                    prodprec = self.Precedence.get(precname, ('right', 0))
        map = f'''{prodname!s} -> {syms!s}'''
        if map in self.Prodmap:
            m = self.Prodmap[map]
            raise GrammarError('%s:%d: Duplicate rule %s. ' % (file, line, m) + 'Previous definition at %s:%d' % (m.file, m.line))
        pnumber = len(self.Productions)
        if prodname not in self.Nonterminals:
            self.Nonterminals[prodname] = []
        for t in syms:
            if t in self.Terminals:
                self.Terminals[t].append(pnumber)
                continue
            if t not in self.Nonterminals:
                self.Nonterminals[t] = []
            self.Nonterminals[t].append(pnumber)
            p = Production(pnumber, prodname, syms, prodprec, func, file, line)
            self.Productions.append(p)
            self.Prodmap[map] = p
            
            try:
                self.Prodnames[prodname].append(p)
                return None
            except KeyError:
                self.Prodnames[prodname] = [
                    p]
                return None


    
    def set_start(self, start = (None,)):
        if not start:
            start = self.Productions[1].name
        if start not in self.Nonterminals:
            raise GrammarError('start symbol %s undefined' % start)
        self.Productions[0] = Production(0, "S'", [
            start])
        self.Nonterminals[start].append(0)
        self.Start = start

    
    def find_unreachable(self):
        pass
    # WARNING: Decompyle incomplete

    
    def infinite_cycles(self):
        terminates = { }
        for t in self.Terminals:
            terminates[t] = True
            terminates['$end'] = True
            for n in self.Nonterminals:
                terminates[n] = False
                some_change = False
                for n, pl in self.Prodnames.items():
                    for p in pl:
                        for s in p.prod:
                            if not terminates[s]:
                                p_terminates = False
                            
                            p_terminates = True
                            if p_terminates:
                                if not terminates[n]:
                                    terminates[n] = True
                                    some_change = True
                            
                            if not some_change:
                                pass
                            
                            infinite = []
                            for s, term in terminates.items():
                                if not term:
                                    if s not in self.Prodnames and s not in self.Terminals and s != 'error':
                                        continue
                                    infinite.append(s)
                                return infinite

    
    def undefined_symbols(self):
        result = []
        for p in self.Productions:
            if not p:
                continue
            for s in p.prod:
                if s not in self.Prodnames and s not in self.Terminals and s != 'error':
                    result.append((s, p))
                return result

    
    def unused_terminals(self):
        unused_tok = []
        for s, v in self.Terminals.items():
            if not s != 'error' and v:
                unused_tok.append(s)
            return unused_tok

    
    def unused_rules(self):
        unused_prod = []
        for s, v in self.Nonterminals.items():
            if not v:
                p = self.Prodnames[s][0]
                unused_prod.append(p)
            return unused_prod

    
    def unused_precedence(self):
        unused = []
        for termname in self.Precedence:
            if not termname in self.Terminals and termname in self.UsedPrecedence:
                unused.append((termname, self.Precedence[termname][0]))
            return unused

    
    def _first(self, beta):
        result = []
        for x in beta:
            x_produces_empty = False
            for f in self.First[x]:
                if f == '<empty>':
                    x_produces_empty = True
                    continue
                if f not in result:
                    result.append(f)
                if x_produces_empty:
                    continue
        result.append('<empty>')
        return result

    
    def compute_first(self):
        if self.First:
            return self.First
        for t in None.Terminals:
            self.First[t] = [
                t]
            self.First['$end'] = [
                '$end']
            for n in self.Nonterminals:
                self.First[n] = []
                some_change = False
                for n in self.Nonterminals:
                    for p in self.Prodnames[n]:
                        for f in self._first(p.prod):
                            if f not in self.First[n]:
                                self.First[n].append(f)
                                some_change = True
                            if not some_change:
                                pass
                            
                            return self.First

    
    def compute_follow(self, start = (None,)):
        if self.Follow:
            return self.Follow
        if not None.First:
            self.compute_first()
        for k in self.Nonterminals:
            self.Follow[k] = []
            if not start:
                start = self.Productions[1].name
        self.Follow[start] = [
            '$end']
        didadd = False
        for p in self.Productions[1:]:
            for i, B in enumerate(p.prod):
                if B in self.Nonterminals:
                    fst = self._first(p.prod[i + 1:])
                    hasempty = False
                    for f in fst:
                        if f != '<empty>' and f not in self.Follow[B]:
                            self.Follow[B].append(f)
                            didadd = True
                        if f == '<empty>':
                            hasempty = True
                        if hasempty or i == len(p.prod) - 1:
                            for f in self.Follow[p.name]:
                                if f not in self.Follow[B]:
                                    self.Follow[B].append(f)
                                    didadd = True
                                if not didadd:
                                    pass
                                
                                return self.Follow

    
    def build_lritems(self):
        for p in self.Productions:
            lastlri = p
            i = 0
            lr_items = []
            if i > len(p):
                lri = None
            else:
                lri = LRItem(p, i)
                lri.lr_after = self.Prodnames[lri.prod[i + 1]]
        except (IndexError, KeyError):
            lri.lr_after = []
        lri.lr_before = lri.prod[i - 1]



class VersionError(YaccError):
    pass


class LRTable(object):
    
    def __init__(self):
        self.lr_action = None
        self.lr_goto = None
        self.lr_productions = None
        self.lr_method = None

    
    def read_table(self, module):
        if isinstance(module, types.ModuleType):
            parsetab = module
        else:
            exec('import %s' % module)
            parsetab = sys.modules[module]
        if parsetab._tabversion != __tabversion__:
            raise VersionError('yacc table file version is out of date')
        self.lr_action = parsetab._lr_action
        self.lr_goto = parsetab._lr_goto
        self.lr_productions = []
    # WARNING: Decompyle incomplete

    
    def read_pickle(self, filename):
        
        try:
            import cPickle as pickle
        except ImportError:
            import pickle

        if not os.path.exists(filename):
            raise ImportError
        in_f = open(filename, 'rb')
        tabversion = pickle.load(in_f)
        if tabversion != __tabversion__:
            raise VersionError('yacc table file version is out of date')
        self.lr_method = pickle.load(in_f)
        signature = pickle.load(in_f)
        self.lr_action = pickle.load(in_f)
        self.lr_goto = pickle.load(in_f)
        productions = pickle.load(in_f)
        self.lr_productions = []
    # WARNING: Decompyle incomplete

    
    def bind_callables(self, pdict):
        for p in self.lr_productions:
            p.bind(pdict)
            return None



def digraph(X, R, FP):
    N = { }
    for x in X:
        N[x] = 0
        stack = []
        F = { }
        for x in X:
            if N[x] == 0:
                traverse(x, N, stack, F, X, R, FP)
            return F


def traverse(x, N, stack, F, X, R, FP):
    stack.append(x)
    d = len(stack)
    N[x] = d
    F[x] = FP(x)
    rel = R(x)
# WARNING: Decompyle incomplete


class LALRError(YaccError):
    pass


class LRGeneratedTable(LRTable):
    
    def __init__(self, grammar, method, log = ('LALR', None)):
        if method not in ('SLR', 'LALR'):
            raise LALRError('Unsupported method %s' % method)
        self.grammar = grammar
        self.lr_method = method
        if not log:
            log = NullLogger()
        self.log = log
        self.lr_action = { }
        self.lr_goto = { }
        self.lr_productions = grammar.Productions
        self.lr_goto_cache = { }
        self.lr0_cidhash = { }
        self._add_count = 0
        self.sr_conflict = 0
        self.rr_conflict = 0
        self.conflicts = []
        self.sr_conflicts = []
        self.rr_conflicts = []
        self.grammar.build_lritems()
        self.grammar.compute_first()
        self.grammar.compute_follow()
        self.lr_parse_table()

    
    def lr0_closure(self, I):
        I[:] = self, self._add_count += 1, ._add_count
        didadd = True
    # WARNING: Decompyle incomplete

    
    def lr0_goto(self, I, x):
        g = self.lr_goto_cache.get((id(I), x))
        if g:
            return g
        s = None.lr_goto_cache.get(x)
        if not s:
            s = { }
            self.lr_goto_cache[x] = s
        gs = []
        for p in I:
            n = p.lr_next
            if n and n.lr_before == x:
                s1 = s.get(id(n))
                if not s1:
                    s1 = { }
                    s[id(n)] = s1
                gs.append(n)
                s = s1
            g = s.get('$end')
            if not g:
                if gs:
                    g = self.lr0_closure(gs)
                    s['$end'] = g
                else:
                    s['$end'] = gs
        self.lr_goto_cache[(id(I), x)] = g
        return g

    
    def lr0_items(self):
        C = [
            self.lr0_closure([
                self.grammar.Productions[0].lr_next])]
        i = 0
    # WARNING: Decompyle incomplete

    
    def compute_nullable_nonterminals(self):
        nullable = set()
        num_nullable = 0
        for p in self.grammar.Productions[1:]:
            if p.len == 0:
                nullable.add(p.name)
                continue
            for t in p.prod:
                if t not in nullable:
                    pass
                
                nullable.add(p.name)
                if len(nullable) == num_nullable:
                    pass
                else:
                    num_nullable = len(nullable)
                return nullable

    
    def find_nonterminal_transitions(self, C):
        trans = []
        for stateno, state in enumerate(C):
            for p in state:
                if p.lr_index < p.len - 1:
                    t = (stateno, p.prod[p.lr_index + 1])
                    if t[1] in self.grammar.Nonterminals and t not in trans:
                        trans.append(t)
                return trans

    
    def dr_relation(self, C, trans, nullable):
        dr_set = { }
        (state, N) = trans
        terms = []
        g = self.lr0_goto(C[state], N)
        for p in g:
            if p.lr_index < p.len - 1:
                a = p.prod[p.lr_index + 1]
                if a in self.grammar.Terminals and a not in terms:
                    terms.append(a)
            if state == 0 and N == self.grammar.Productions[0].prod[0]:
                terms.append('$end')
        return terms

    
    def reads_relation(self, C, trans, empty):
        rel = []
        (state, N) = trans
        g = self.lr0_goto(C[state], N)
        j = self.lr0_cidhash.get(id(g), -1)
        for p in g:
            if p.lr_index < p.len - 1:
                a = p.prod[p.lr_index + 1]
                if a in empty:
                    rel.append((j, a))
            return rel

    
    def compute_lookback_includes(self, C, trans, nullable):
        lookdict = { }
        includedict = { }
        dtrans = { }
    # WARNING: Decompyle incomplete

    
    def compute_read_sets(self, C, ntrans, nullable):
        pass
    # WARNING: Decompyle incomplete

    
    def compute_follow_sets(self, ntrans, readsets, inclsets):
        pass
    # WARNING: Decompyle incomplete

    
    def add_lookaheads(self, lookbacks, followset):
        for trans, lb in lookbacks.items():
            for state, p in lb:
                if state not in p.lookaheads:
                    p.lookaheads[state] = []
                f = followset.get(trans, [])
                for a in f:
                    if a not in p.lookaheads[state]:
                        p.lookaheads[state].append(a)
                    return None

    
    def add_lalr_lookaheads(self, C):
        nullable = self.compute_nullable_nonterminals()
        trans = self.find_nonterminal_transitions(C)
        readsets = self.compute_read_sets(C, trans, nullable)
        (lookd, included) = self.compute_lookback_includes(C, trans, nullable)
        followsets = self.compute_follow_sets(trans, readsets, included)
        self.add_lookaheads(lookd, followsets)

    
    def lr_parse_table(self):
        Productions = self.grammar.Productions
        Precedence = self.grammar.Precedence
        goto = self.lr_goto
        action = self.lr_action
        log = self.log
        actionp = { }
        log.info('Parsing method: %s', self.lr_method)
        C = self.lr0_items()
        if self.lr_method == 'LALR':
            self.add_lalr_lookaheads(C)
        st = 0
    # WARNING: Decompyle incomplete

    
    def write_table(self, tabmodule, outputdir, signature = ('', '')):
        if isinstance(tabmodule, types.ModuleType):
            raise IOError("Won't overwrite existing tabmodule")
        basemodulename = tabmodule.split('.')[-1]
        filename = os.path.join(outputdir, basemodulename) + '.py'
        
        try:
            f = open(filename, 'w')
            f.write(f'''\n# {os.path.basename(filename)!s}\n# This file is automatically generated. Do not edit.\n_tabversion = {__tabversion__!r}\n\n_lr_method = {self.lr_method!r}\n\n_lr_signature = {signature!r}\n    ''')
            smaller = 1
            if smaller:
                items = { }
                for s, nd in self.lr_action.items():
                    for name, v in nd.items():
                        i = items.get(name)
                        if not i:
                            i = ([], [])
                            items[name] = i
                        i[0].append(s)
                        i[1].append(v)
                        f.write('\n_lr_action_items = {')
                        for k, v in items.items():
                            f.write('%r:([' % k)
                            for i in v[0]:
                                f.write('%r,' % i)
                                f.write('],[')
                                for i in v[1]:
                                    f.write('%r,' % i)
                                    f.write(']),')
                                    f.write('}\n')
                                    f.write('\n_lr_action = {}\nfor _k, _v in _lr_action_items.items():\n   for _x,_y in zip(_v[0],_v[1]):\n      if not _x in _lr_action:  _lr_action[_x] = {}\n      _lr_action[_x][_k] = _y\ndel _lr_action_items\n')
                                f.write('\n_lr_action = { ')
                                for k, v in self.lr_action.items():
                                    f.write(f'''({k[0]!r},{k[1]!r}):{v!r},''')
                                    f.write('}\n')
                                    if smaller:
                                        items = { }
                                        for s, nd in self.lr_goto.items():
                                            for name, v in nd.items():
                                                i = items.get(name)
                                                if not i:
                                                    i = ([], [])
                                                    items[name] = i
                                                i[0].append(s)
                                                i[1].append(v)
                                                f.write('\n_lr_goto_items = {')
                                                for k, v in items.items():
                                                    f.write('%r:([' % k)
                                                    for i in v[0]:
                                                        f.write('%r,' % i)
                                                        f.write('],[')
                                                        for i in v[1]:
                                                            f.write('%r,' % i)
                                                            f.write(']),')
                                                            f.write('}\n')
                                                            f.write('\n_lr_goto = {}\nfor _k, _v in _lr_goto_items.items():\n   for _x, _y in zip(_v[0], _v[1]):\n       if not _x in _lr_goto: _lr_goto[_x] = {}\n       _lr_goto[_x][_k] = _y\ndel _lr_goto_items\n')
                                                        f.write('\n_lr_goto = { ')
                                                        for k, v in self.lr_goto.items():
                                                            f.write(f'''({k[0]!r},{k[1]!r}):{v!r},''')
                                                            f.write('}\n')
                                                            f.write('_lr_productions = [\n')
                                                            for p in self.lr_productions:
                                                                if p.func:
                                                                    f.write('  (%r,%r,%d,%r,%r,%d),\n' % (p.str, p.name, p.len, p.func, os.path.basename(p.file), p.line))
                                                                    continue
                                                                f.write('  (%r,%r,%d,None,None,None),\n' % (str(p), p.name, p.len))
                                                                f.write(']\n')
                                                                f.close()
                                                                return None
                                                                except IOError:
                                                                    e = None
                                                                    raise 
                                                                    e = None
                                                                    del e


    
    def pickle_table(self, filename, signature = ('',)):
        
        try:
            import cPickle as pickle
        except ImportError:
            import pickle

        outf = open(filename, 'wb')
        pickle.dump(__tabversion__, outf, pickle_protocol)
        pickle.dump(self.lr_method, outf, pickle_protocol)
        pickle.dump(signature, outf, pickle_protocol)
        pickle.dump(self.lr_action, outf, pickle_protocol)
        pickle.dump(self.lr_goto, outf, pickle_protocol)
        outp = []
        for p in self.lr_productions:
            if p.func:
                outp.append((p.str, p.name, p.len, p.func, os.path.basename(p.file), p.line))
                continue
            outp.append((str(p), p.name, p.len, None, None, None))
            pickle.dump(outp, outf, pickle_protocol)
            None(None, None)
            return None
            with None:
                if not None:
                    pass



def get_caller_module_dict(levels):
    f = sys._getframe(levels)
    ldict = f.f_globals.copy()
    if f.f_globals != f.f_locals:
        ldict.update(f.f_locals)
    return ldict


def parse_grammar(doc, file, line):
    grammar = []
    pstrings = doc.splitlines()
    lastp = None
    dline = line
    for ps in pstrings:
        dline += 1
        p = ps.split()
        if not p:
            continue
        if p[0] == '|':
            if not lastp:
                raise SyntaxError("%s:%d: Misplaced '|'" % (file, dline))
            prodname = lastp
            syms = p[1:]
        else:
            prodname = p[0]
            lastp = prodname
            syms = p[2:]
            assign = p[1]
            if assign != ':' and assign != '::=':
                raise SyntaxError("%s:%d: Syntax error. Expected ':'" % (file, dline))
        grammar.append((file, dline, prodname, syms))
        except SyntaxError:
            raise 
        except Exception:
            raise SyntaxError('%s:%d: Syntax error in rule %r' % (file, dline, ps.strip()))
        return grammar


class ParserReflect(object):
    
    def __init__(self, pdict, log = (None,)):
        self.pdict = pdict
        self.start = None
        self.error_func = None
        self.tokens = None
        self.modules = set()
        self.grammar = []
        self.error = False
    # WARNING: Decompyle incomplete

    
    def get_all(self):
        self.get_start()
        self.get_error_func()
        self.get_tokens()
        self.get_precedence()
        self.get_pfunctions()

    
    def validate_all(self):
        self.validate_start()
        self.validate_error_func()
        self.validate_tokens()
        self.validate_precedence()
        self.validate_pfunctions()
        self.validate_modules()
        return self.error

    
    def signature(self):
        parts = []
        
        try:
            if self.start:
                parts.append(self.start)
            if self.prec:
                ''.join((lambda .0: [ ''.join(p) for p in .0 ])(self.prec()))
            if self.tokens:
                parts.append(' '.join(self.tokens))
            for f in self.pfuncs:
                if f[3]:
                    parts.append(f[3])
        except (TypeError, ValueError):
            pass

        return ''.join(parts)

    
    def validate_modules(self):
        fre = re.compile('\\s*def\\s+(p_[a-zA-Z_0-9]*)\\(')
        for module in self.modules:
            (lines, linen) = inspect.getsourcelines(module)
        except IOError:
            continue
        counthash = { }
        for linen, line in enumerate(lines):
            linen += 1
            m = fre.match(line)
            if m:
                name = m.group(1)
                prev = counthash.get(name)
                if not prev:
                    counthash[name] = linen
                    continue
                filename = inspect.getsourcefile(module)
                self.log.warning('%s:%d: Function %s redefined. Previously defined on line %d', filename, linen, name, prev)
            return None

    
    def get_start(self):
        self.start = self.pdict.get('start')

    
    def validate_start(self):
        pass
    # WARNING: Decompyle incomplete

    
    def get_error_func(self):
        self.error_func = self.pdict.get('p_error')

    
    def validate_error_func(self):
        if self.error_func:
            if isinstance(self.error_func, types.FunctionType):
                ismethod = 0
            elif isinstance(self.error_func, types.MethodType):
                ismethod = 1
            else:
                self.log.error("'p_error' defined, but is not a function or method")
                self.error = True
                return None
            eline = None.error_func.__code__.co_firstlineno
            efile = self.error_func.__code__.co_filename
            module = inspect.getmodule(self.error_func)
            self.modules.add(module)
            argcount = self.error_func.__code__.co_argcount - ismethod
            if argcount != 1:
                self.log.error('%s:%d: p_error() requires 1 argument', efile, eline)
                self.error = True
                return None
            return None

    
    def get_tokens(self):
        tokens = self.pdict.get('tokens')
        if not tokens:
            self.log.error('No token list is defined')
            self.error = True
            return None
        if not None(tokens, (list, tuple)):
            self.log.error('tokens must be a list or tuple')
            self.error = True
            return None
        if not None:
            self.log.error('tokens is empty')
            self.error = True
            return None
        self.tokens = None

    
    def validate_tokens(self):
        if 'error' in self.tokens:
            self.log.error("Illegal token name 'error'. Is a reserved word")
            self.error = True
            return None
        terminals = None()
        for n in self.tokens:
            if n in terminals:
                self.log.warning('Token %r multiply defined', n)
            terminals.add(n)
            return None

    
    def get_precedence(self):
        self.prec = self.pdict.get('precedence')

    
    def validate_precedence(self):
        preclist = []
        if self.prec:
            if not isinstance(self.prec, (list, tuple)):
                self.log.error('precedence must be a list or tuple')
                self.error = True
                return None
            for level, p in None(self.prec):
                if not isinstance(p, (list, tuple)):
                    self.log.error('Bad precedence table')
                    self.error = True
                    return None
                if None(p) < 2:
                    self.log.error('Malformed precedence entry %s. Must be (assoc, term, ..., term)', p)
                    self.error = True
                    return None
                assoc = None[0]
                if not isinstance(assoc, string_types):
                    self.log.error('precedence associativity must be a string')
                    self.error = True
                    return None
                for term in None[1:]:
                    if not isinstance(term, string_types):
                        self.log.error('precedence items must be strings')
                        self.error = True
                        return None
                    None.append((term, assoc, level + 1))
                    self.preclist = preclist
                    return None

    
    def get_pfunctions(self):
        p_functions = []
        for name, item in self.pdict.items():
            if name.startswith('p_') or name == 'p_error':
                continue
            if isinstance(item, (types.FunctionType, types.MethodType)):
                line = getattr(item, 'co_firstlineno', item.__code__.co_firstlineno)
                module = inspect.getmodule(item)
                p_functions.append((line, module, name, item.__doc__))
            p_functions.sort(key = (lambda p_function: (p_function[0], str(p_function[1]), p_function[2], p_function[3])))
            self.pfuncs = p_functions
            return None

    
    def validate_pfunctions(self):
        grammar = []
        if len(self.pfuncs) == 0:
            self.log.error('no rules of the form p_rulename are defined')
            self.error = True
            return None
        for line, module, name, doc in None.pfuncs:
            file = inspect.getsourcefile(module)
            func = self.pdict[name]
            if isinstance(func, types.MethodType):
                reqargs = 2
            else:
                reqargs = 1
            if func.__code__.co_argcount > reqargs:
                self.log.error('%s:%d: Rule %r has too many arguments', file, line, func.__name__)
                self.error = True
                continue
            if func.__code__.co_argcount < reqargs:
                self.log.error('%s:%d: Rule %r requires an argument', file, line, func.__name__)
                self.error = True
                continue
            if not func.__doc__:
                self.log.warning('%s:%d: No documentation string specified in function %r (ignored)', file, line, func.__name__)
                continue
            parsed_g = parse_grammar(doc, file, line)
            for g in parsed_g:
                grammar.append((name, g))
            except SyntaxError:
                e = None
                self.log.error(str(e))
                self.error = True
                e = None
                del e
            except:
                e = None
                del e
            self.modules.add(module)
            for n, v in self.pdict.items():
                if n.startswith('p_') and isinstance(v, (types.FunctionType, types.MethodType)):
                    continue
                if n.startswith('t_'):
                    continue
                if n.startswith('p_') and n != 'p_error':
                    self.log.warning('%r not defined as a function', n)
                if (isinstance(v, types.FunctionType) or v.__code__.co_argcount == 1 or isinstance(v, types.MethodType)) and v.__func__.__code__.co_argcount == 2 and v.__doc__:
                    doc = v.__doc__.split(' ')
                    if doc[1] == ':':
                        self.log.warning('%s:%d: Possible grammar rule %r defined without p_ prefix', v.__code__.co_filename, v.__code__.co_firstlineno, n)
                    continue
                    except IndexError:
                        continue
                self.grammar = grammar
                return None



def yacc(method, debug, module, tabmodule, start, check_recursion, optimize, write_tables, debugfile, outputdir, debuglog, errorlog, picklefile = ('LALR', yaccdebug, None, tab_module, None, True, False, True, debug_file, None, None, None, None)):
    pass
# WARNING: Decompyle incomplete
