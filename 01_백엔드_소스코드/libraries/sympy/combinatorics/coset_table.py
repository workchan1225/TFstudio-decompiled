# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: coset_table.pyc (Python 3.11)

from sympy.combinatorics.free_groups import free_group
from sympy.printing.defaults import DefaultPrinting
from itertools import chain, product
from bisect import bisect_left

class CosetTable(DefaultPrinting):
    '''

    Properties
    ==========

    [1] `0 \\in \\Omega` and `\\tau(1) = \\epsilon`
    [2] `\\alpha^x = \\beta \\Leftrightarrow \\beta^{x^{-1}} = \\alpha`
    [3] If `\\alpha^x = \\beta`, then `H \\tau(\\alpha)x = H \\tau(\\beta)`
    [4] `\\forall \\alpha \\in \\Omega, 1^{\\tau(\\alpha)} = \\alpha`

    References
    ==========

    .. [1] Holt, D., Eick, B., O\'Brien, E.
           "Handbook of Computational Group Theory"

    .. [2] John J. Cannon; Lucien A. Dimino; George Havas; Jane M. Watson
           Mathematics of Computation, Vol. 27, No. 123. (Jul., 1973), pp. 463-490.
           "Implementation and Analysis of the Todd-Coxeter Algorithm"

    '''
    coset_table_max_limit = 4096000
    coset_table_limit = None
    max_stack_size = 100
    
    def __init__(self, fp_grp, subgroup, max_cosets = (None,)):
        pass
    # WARNING: Decompyle incomplete

    omega = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def copy(self):
        '''
        Return a shallow copy of Coset Table instance ``self``.

        '''
        self_copy = self.__class__(self.fp_group, self.subgroup)
        self_copy.table = self.table()
        self_copy.p = list(self.p)
        self_copy.deduction_stack = list(self.deduction_stack)
        return self_copy

    
    def __str__(self):
        return f'''Coset Table on {self.fp_group!s} with {self.subgroup!s} as subgroup generators'''

    __repr__ = __str__
    n = (lambda self: if not self.table:
0None(self.omega) + 1)()
    
    def is_complete(self):
        '''
        The coset table is called complete if it has no undefined entries
        on the live cosets; that is, `\\alpha^x` is defined for all
        `\\alpha \\in \\Omega` and `x \\in A`.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def define(self, alpha, x, modified = (False,)):
        '''
        This routine is used in the relator-based strategy of Todd-Coxeter
        algorithm if some `\\alpha^x` is undefined. We check whether there is
        space available for defining a new coset. If there is enough space
        then we remedy this by adjoining a new coset `\\beta` to `\\Omega`
        (i.e to set of live cosets) and put that equal to `\\alpha^x`, then
        make an assignment satisfying Property[1]. If there is not enough space
        then we halt the Coset Table creation. The maximum amount of space that
        can be used by Coset Table can be manipulated using the class variable
        ``CosetTable.coset_table_max_limit``.

        See Also
        ========

        define_c

        '''
        A = self.A
        table = self.table
        len_table = len(table)
        if len_table >= self.coset_table_limit:
            raise ValueError('the coset enumeration has defined more than %s cosets. Try with a greater value max number of cosets ' % self.coset_table_limit)
        table.append([
            None] * len(A))
        self.P.append([
            None] * len(self.A))
        beta = len_table
        self.p.append(beta)
        table[alpha][self.A_dict[x]] = beta
        table[beta][self.A_dict_inv[x]] = alpha
        if modified:
            self.P[alpha][self.A_dict[x]] = self._grp.identity
            self.P[beta][self.A_dict_inv[x]] = self._grp.identity
            self.p_p[beta] = self._grp.identity
            return None

    
    def define_c(self, alpha, x):
        '''
        A variation of ``define`` routine, described on Pg. 165 [1], used in
        the coset table-based strategy of Todd-Coxeter algorithm. It differs
        from ``define`` routine in that for each definition it also adds the
        tuple `(\\alpha, x)` to the deduction stack.

        See Also
        ========

        define

        '''
        A = self.A
        table = self.table
        len_table = len(table)
        if len_table >= self.coset_table_limit:
            raise ValueError('the coset enumeration has defined more than %s cosets. Try with a greater value max number of cosets ' % self.coset_table_limit)
        table.append([
            None] * len(A))
        beta = len_table
        self.p.append(beta)
        table[alpha][self.A_dict[x]] = beta
        table[beta][self.A_dict_inv[x]] = alpha
        self.deduction_stack.append((alpha, x))

    
    def scan_c(self, alpha, word):
        '''
        A variation of ``scan`` routine, described on pg. 165 of [1], which
        puts at tuple, whenever a deduction occurs, to deduction stack.

        See Also
        ========

        scan, scan_check, scan_and_fill, scan_and_fill_c

        '''
        A_dict = self.A_dict
        A_dict_inv = self.A_dict_inv
        table = self.table
        f = alpha
        i = 0
        r = len(word)
        b = alpha
        j = r - 1
    # WARNING: Decompyle incomplete

    
    def coincidence_c(self, alpha, beta):
        '''
        A variation of ``coincidence`` routine used in the coset-table based
        method of coset enumeration. The only difference being on addition of
        a new coset in coset table(i.e new coset introduction), then it is
        appended to ``deduction_stack``.

        See Also
        ========

        coincidence

        '''
        A_dict = self.A_dict
        A_dict_inv = self.A_dict_inv
        table = self.table
        q = []
        self.merge(alpha, beta, q)
    # WARNING: Decompyle incomplete

    
    def scan(self, alpha, word, y, fill, modified = (None, False, False)):
        '''
        ``scan`` performs a scanning process on the input ``word``.
        It first locates the largest prefix ``s`` of ``word`` for which
        `\\alpha^s` is defined (i.e is not ``None``), ``s`` may be empty. Let
        ``word=sv``, let ``t`` be the longest suffix of ``v`` for which
        `\\alpha^{t^{-1}}` is defined, and let ``v=ut``. Then three
        possibilities are there:

        1. If ``t=v``, then we say that the scan completes, and if, in addition
        `\\alpha^s = \\alpha^{t^{-1}}`, then we say that the scan completes
        correctly.

        2. It can also happen that scan does not complete, but `|u|=1`; that
        is, the word ``u`` consists of a single generator `x \\in A`. In that
        case, if `\\alpha^s = \\beta` and `\\alpha^{t^{-1}} = \\gamma`, then we can
        set `\\beta^x = \\gamma` and `\\gamma^{x^{-1}} = \\beta`. These assignments
        are known as deductions and enable the scan to complete correctly.

        3. See ``coicidence`` routine for explanation of third condition.

        Notes
        =====

        The code for the procedure of scanning `\\alpha \\in \\Omega`
        under `w \\in A*` is defined on pg. 155 [1]

        See Also
        ========

        scan_c, scan_check, scan_and_fill, scan_and_fill_c

        Scan and Fill
        =============

        Performed when the default argument fill=True.

        Modified Scan
        =============

        Performed when the default argument modified=True

        '''
        A_dict = self.A_dict
        A_dict_inv = self.A_dict_inv
        table = self.table
        f = alpha
        i = 0
        r = len(word)
        b = alpha
        j = r - 1
        b_p = y
        if modified:
            f_p = self._grp.identity
        flag = 0
    # WARNING: Decompyle incomplete

    
    def scan_check(self, alpha, word):
        '''
        Another version of ``scan`` routine, described on, it checks whether
        `\\alpha` scans correctly under `word`, it is a straightforward
        modification of ``scan``. ``scan_check`` returns ``False`` (rather than
        calling ``coincidence``) if the scan completes incorrectly; otherwise
        it returns ``True``.

        See Also
        ========

        scan, scan_c, scan_and_fill, scan_and_fill_c

        '''
        A_dict = self.A_dict
        A_dict_inv = self.A_dict_inv
        table = self.table
        f = alpha
        i = 0
        r = len(word)
        b = alpha
        j = r - 1
    # WARNING: Decompyle incomplete

    
    def merge(self, k, lamda, q, w, modified = (None, False)):
        """
        Merge two classes with representatives ``k`` and ``lamda``, described
        on Pg. 157 [1] (for pseudocode), start by putting ``p[k] = lamda``.
        It is more efficient to choose the new representative from the larger
        of the two classes being merged, i.e larger among ``k`` and ``lamda``.
        procedure ``merge`` performs the merging operation, adds the deleted
        class representative to the queue ``q``.

        Parameters
        ==========

        'k', 'lamda' being the two class representatives to be merged.

        Notes
        =====

        Pg. 86-87 [1] contains a description of this method.

        See Also
        ========

        coincidence, rep

        """
        p = self.p
        rep = self.rep
        phi = rep(k, modified = modified)
        psi = rep(lamda, modified = modified)
        if phi != psi:
            mu = min(phi, psi)
            v = max(phi, psi)
            p[v] = mu
            if modified:
                if v == phi:
                    self.p_p[phi] = self.p_p[k] ** -1 * w * self.p_p[lamda]
                else:
                    self.p_p[psi] = self.p_p[lamda] ** -1 * w ** -1 * self.p_p[k]
            q.append(v)
            return None

    
    def rep(self, k, modified = (False,)):
        """
        Parameters
        ==========

        `k \\in [0 \\ldots n-1]`, as for ``self`` only array ``p`` is used

        Returns
        =======

        Representative of the class containing ``k``.

        Returns the representative of `\\sim` class containing ``k``, it also
        makes some modification to array ``p`` of ``self`` to ease further
        computations, described on Pg. 157 [1].

        The information on classes under `\\sim` is stored in array `p` of
        ``self`` argument, which will always satisfy the property:

        `p[\\alpha] \\sim \\alpha` and `p[\\alpha]=\\alpha \\iff \\alpha=rep(\\alpha)`
        `\\forall \\in [0 \\ldots n-1]`.

        So, for `\\alpha \\in [0 \\ldots n-1]`, we find `rep(self, \\alpha)` by
        continually replacing `\\alpha` by `p[\\alpha]` until it becomes
        constant (i.e satisfies `p[\\alpha] = \\alpha`):w

        To increase the efficiency of later ``rep`` calculations, whenever we
        find `rep(self, \\alpha)=\\beta`, we set
        `p[\\gamma] = \\beta \\forall \\gamma \\in p-chain` from `\\alpha` to `\\beta`

        Notes
        =====

        ``rep`` routine is also described on Pg. 85-87 [1] in Atkinson's
        algorithm, this results from the fact that ``coincidence`` routine
        introduces functionality similar to that introduced by the
        ``minimal_block`` routine on Pg. 85-87 [1].

        See Also
        ========

        coincidence, merge

        """
        p = self.p
        lamda = k
        rho = p[lamda]
        if modified:
            s = p[:]
    # WARNING: Decompyle incomplete

    
    def coincidence(self, alpha, beta, w, modified = (None, False)):
        '''
        The third situation described in ``scan`` routine is handled by this
        routine, described on Pg. 156-161 [1].

        The unfortunate situation when the scan completes but not correctly,
        then ``coincidence`` routine is run. i.e when for some `i` with
        `1 \\le i \\le r+1`, we have `w=st` with `s = x_1 x_2 \\dots x_{i-1}`,
        `t = x_i x_{i+1} \\dots x_r`, and `\\beta = \\alpha^s` and
        `\\gamma = \\alpha^{t-1}` are defined but unequal. This means that
        `\\beta` and `\\gamma` represent the same coset of `H` in `G`. Described
        on Pg. 156 [1]. ``rep``

        See Also
        ========

        scan

        '''
        A_dict = self.A_dict
        A_dict_inv = self.A_dict_inv
        table = self.table
        q = []
        if modified:
            self.modified_merge(alpha, beta, w, q)
        else:
            self.merge(alpha, beta, q)
    # WARNING: Decompyle incomplete

    
    def scan_and_fill(self, alpha, word):
        '''
        A modified version of ``scan`` routine used in the relator-based
        method of coset enumeration, described on pg. 162-163 [1], which
        follows the idea that whenever the procedure is called and the scan
        is incomplete then it makes new definitions to enable the scan to
        complete; i.e it fills in the gaps in the scan of the relator or
        subgroup generator.

        '''
        self.scan(alpha, word, fill = True)

    
    def scan_and_fill_c(self, alpha, word):
        '''
        A modified version of ``scan`` routine, described on Pg. 165 second
        para. [1], with modification similar to that of ``scan_anf_fill`` the
        only difference being it calls the coincidence procedure used in the
        coset-table based method i.e. the routine ``coincidence_c`` is used.

        See Also
        ========

        scan, scan_and_fill

        '''
        A_dict = self.A_dict
        A_dict_inv = self.A_dict_inv
        table = self.table
        r = len(word)
        f = alpha
        i = 0
        b = alpha
        j = r - 1
    # WARNING: Decompyle incomplete

    
    def look_ahead(self):
        '''
        When combined with the HLT method this is known as HLT+Lookahead
        method of coset enumeration, described on pg. 164 [1]. Whenever
        ``define`` aborts due to lack of space available this procedure is
        executed. This routine helps in recovering space resulting from
        "coincidence" of cosets.

        '''
        R = self.fp_group.relators
        p = self.p
        for beta in self.omega:
            for w in R:
                self.scan(beta, w)
                if p[beta] < beta:
                    pass
                
                return None

    
    def process_deductions(self, R_c_x, R_c_x_inv):
        '''
        Processes the deductions that have been pushed onto ``deduction_stack``,
        described on Pg. 166 [1] and is used in coset-table based enumeration.

        See Also
        ========

        deduction_stack

        '''
        p = self.p
        table = self.table
    # WARNING: Decompyle incomplete

    
    def process_deductions_check(self, R_c_x, R_c_x_inv):
        '''
        A variation of ``process_deductions``, this calls ``scan_check``
        wherever ``process_deductions`` calls ``scan``, described on Pg. [1].

        See Also
        ========

        process_deductions

        '''
        table = self.table
    # WARNING: Decompyle incomplete

    
    def switch(self, beta, gamma):
        '''Switch the elements `\\beta, \\gamma \\in \\Omega` of ``self``, used
        by the ``standardize`` procedure, described on Pg. 167 [1].

        See Also
        ========

        standardize

        '''
        A = self.A
        A_dict = self.A_dict
        table = self.table
        for x in A:
            z = table[gamma][A_dict[x]]
            table[gamma][A_dict[x]] = table[beta][A_dict[x]]
            table[beta][A_dict[x]] = z
            for alpha in range(len(self.p)):
                if self.p[alpha] == alpha:
                    if table[alpha][A_dict[x]] == beta:
                        table[alpha][A_dict[x]] = gamma
                        continue
                    if table[alpha][A_dict[x]] == gamma:
                        table[alpha][A_dict[x]] = beta
                return None

    
    def standardize(self):
