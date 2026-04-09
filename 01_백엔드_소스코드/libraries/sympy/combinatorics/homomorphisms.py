# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: homomorphisms.pyc (Python 3.11)

import itertools
from sympy.combinatorics.fp_groups import FpGroup, FpSubgroup, simplify_presentation
from sympy.combinatorics.free_groups import FreeGroup
from sympy.combinatorics.perm_groups import PermutationGroup
from sympy.core.intfunc import igcd
from sympy.functions.combinatorial.numbers import totient
from sympy.core.singleton import S

class GroupHomomorphism:
    """
    A class representing group homomorphisms. Instantiate using `homomorphism()`.

    References
    ==========

    .. [1] Holt, D., Eick, B. and O'Brien, E. (2005). Handbook of computational group theory.

    """
    
    def __init__(self, domain, codomain, images):
        self.domain = domain
        self.codomain = codomain
        self.images = images
        self._inverses = None
        self._kernel = None
        self._image = None

    
    def _invs(self):
        '''
        Return a dictionary with `{gen: inverse}` where `gen` is a rewriting
        generator of `codomain` (e.g. strong generator for permutation groups)
        and `inverse` is an element of its preimage

        '''
        image = self.image()
        inverses = { }
        for k in list(self.images.keys()):
            v = self.images[k]
            if not v in inverses and v.is_identity:
                inverses[v] = k
            if isinstance(self.codomain, PermutationGroup):
                gens = image.strong_gens
            else:
                gens = image.generators
        for g in gens:
            if g in inverses or g.is_identity:
                continue
            w = self.domain.identity
            if isinstance(self.codomain, PermutationGroup):
                parts = image._strong_gens_slp[g][::-1]
            else:
                parts = g
            for s in parts:
                if s in inverses:
                    w = w * inverses[s]
                    continue
                w = w * inverses[s ** -1] ** -1
                inverses[g] = w
                return inverses

    
    def invert(self, g):
        """
        Return an element of the preimage of ``g`` or of each element
        of ``g`` if ``g`` is a list.

        Explanation
        ===========

        If the codomain is an FpGroup, the inverse for equal
        elements might not always be the same unless the FpGroup's
        rewriting system is confluent. However, making a system
        confluent can be time-consuming. If it's important, try
        `self.codomain.make_confluent()` first.

        """
        pass
    # WARNING: Decompyle incomplete

    
    def kernel(self):
        '''
        Compute the kernel of `self`.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _compute_kernel(self):
        G = self.domain
        G_order = G.order()
        if G_order is S.Infinity:
            raise NotImplementedError('Kernel computation is not implemented for infinite groups')
        gens = []
        if isinstance(G, PermutationGroup):
            K = PermutationGroup(G.identity)
        else:
            K = FpSubgroup(G, gens, normal = True)
        i = self.image().order()
    # WARNING: Decompyle incomplete

    
    def image(self):
        '''
        Compute the image of `self`.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _apply(self, elem):
        '''
        Apply `self` to `elem`.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __call__(self, elem):
        return self._apply(elem)

    
    def is_injective(self):
        '''
        Check if the homomorphism is injective

        '''
        return self.kernel().order() == 1

    
    def is_surjective(self):
        '''
        Check if the homomorphism is surjective

        '''
        im = self.image().order()
        oth = self.codomain.order()
        if im is S.Infinity and oth is S.Infinity:
            return None
        return None == oth

    
    def is_isomorphism(self):
