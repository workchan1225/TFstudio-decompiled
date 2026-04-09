# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: baseclasses.pyc (Python 3.11)

from sympy.core import S, Basic, Dict, Symbol, Tuple, sympify
from sympy.core.symbol import Str
from sympy.sets import Set, FiniteSet, EmptySet
from sympy.utilities.iterables import iterable

class Class(Set):
    '''
    The base class for any kind of class in the set-theoretic sense.

    Explanation
    ===========

    In axiomatic set theories, everything is a class.  A class which
    can be a member of another class is a set.  A class which is not a
    member of another class is a proper class.  The class `\\{1, 2\\}`
    is a set; the class of all sets is a proper class.

    This class is essentially a synonym for :class:`sympy.core.Set`.
    The goal of this class is to assure easier migration to the
    eventual proper implementation of set theory.
    '''
    is_proper = False


class Object(Symbol):
    '''
    The base class for any kind of object in an abstract category.

    Explanation
    ===========

    While technically any instance of :class:`~.Basic` will do, this
    class is the recommended way to create abstract objects in
    abstract categories.
    '''
    pass


class Morphism(Basic):
    '''
    The base class for any morphism in an abstract category.

    Explanation
    ===========

    In abstract categories, a morphism is an arrow between two
    category objects.  The object where the arrow starts is called the
    domain, while the object where the arrow ends is called the
    codomain.

    Two morphisms between the same pair of objects are considered to
    be the same morphisms.  To distinguish between morphisms between
    the same objects use :class:`NamedMorphism`.

    It is prohibited to instantiate this class.  Use one of the
    derived classes instead.

    See Also
    ========

    IdentityMorphism, NamedMorphism, CompositeMorphism
    '''
    
    def __new__(cls, domain, codomain):
        raise NotImplementedError('Cannot instantiate Morphism.  Use derived classes instead.')

    domain = (lambda self: self.args[0])()
    codomain = (lambda self: self.args[1])()
    
    def compose(self, other):
        '''
        Composes self with the supplied morphism.

        The order of elements in the composition is the usual order,
        i.e., to construct `g\\circ f` use ``g.compose(f)``.

        Examples
        ========

        >>> from sympy.categories import Object, NamedMorphism
        >>> A = Object("A")
        >>> B = Object("B")
        >>> C = Object("C")
        >>> f = NamedMorphism(A, B, "f")
        >>> g = NamedMorphism(B, C, "g")
        >>> g * f
        CompositeMorphism((NamedMorphism(Object("A"), Object("B"), "f"),
        NamedMorphism(Object("B"), Object("C"), "g")))
        >>> (g * f).domain
        Object("A")
        >>> (g * f).codomain
        Object("C")

        '''
        return CompositeMorphism(other, self)

    
    def __mul__(self, other):
        '''
        Composes self with the supplied morphism.

        The semantics of this operation is given by the following
        equation: ``g * f == g.compose(f)`` for composable morphisms
        ``g`` and ``f``.

        See Also
        ========

        compose
        '''
        return self.compose(other)



class IdentityMorphism(Morphism):
    '''
    Represents an identity morphism.

    Explanation
    ===========

    An identity morphism is a morphism with equal domain and codomain,
    which acts as an identity with respect to composition.

    Examples
    ========

    >>> from sympy.categories import Object, NamedMorphism, IdentityMorphism
    >>> A = Object("A")
    >>> B = Object("B")
    >>> f = NamedMorphism(A, B, "f")
    >>> id_A = IdentityMorphism(A)
    >>> id_B = IdentityMorphism(B)
    >>> f * id_A == f
    True
    >>> id_B * f == f
    True

    See Also
    ========

    Morphism
    '''
    
    def __new__(cls, domain):
        return Basic.__new__(cls, domain)

    codomain = (lambda self: self.domain)()


class NamedMorphism(Morphism):
    '''
    Represents a morphism which has a name.

    Explanation
    ===========

    Names are used to distinguish between morphisms which have the
    same domain and codomain: two named morphisms are equal if they
    have the same domains, codomains, and names.

    Examples
    ========

    >>> from sympy.categories import Object, NamedMorphism
    >>> A = Object("A")
    >>> B = Object("B")
    >>> f = NamedMorphism(A, B, "f")
    >>> f
    NamedMorphism(Object("A"), Object("B"), "f")
    >>> f.name
    \'f\'

    See Also
    ========

    Morphism
    '''
    
    def __new__(cls, domain, codomain, name):
        if not name:
            raise ValueError('Empty morphism names not allowed.')
        if not isinstance(name, Str):
            name = Str(name)
        return Basic.__new__(cls, domain, codomain, name)

    name = (lambda self: self.args[2].name)()


class CompositeMorphism(Morphism):
    '''
    Represents a morphism which is a composition of other morphisms.

    Explanation
    ===========

    Two composite morphisms are equal if the morphisms they were
    obtained from (components) are the same and were listed in the
    same order.

    The arguments to the constructor for this class should be listed
    in diagram order: to obtain the composition `g\\circ f` from the
    instances of :class:`Morphism` ``g`` and ``f`` use
    ``CompositeMorphism(f, g)``.

    Examples
    ========

    >>> from sympy.categories import Object, NamedMorphism, CompositeMorphism
    >>> A = Object("A")
    >>> B = Object("B")
    >>> C = Object("C")
    >>> f = NamedMorphism(A, B, "f")
    >>> g = NamedMorphism(B, C, "g")
    >>> g * f
    CompositeMorphism((NamedMorphism(Object("A"), Object("B"), "f"),
    NamedMorphism(Object("B"), Object("C"), "g")))
    >>> CompositeMorphism(f, g) == g * f
    True

    '''
    _add_morphism = (lambda t, morphism: if isinstance(morphism, CompositeMorphism):
t + morphism.componentsif None(morphism, IdentityMorphism):
tNone + Tuple(morphism))()
    
    def __new__(cls, *components):
        pass
    # WARNING: Decompyle incomplete

    components = (lambda self: self.args[0])()
    domain = (lambda self: self.components[0].domain)()
    codomain = (lambda self: self.components[-1].codomain)()
    
    def flatten(self, new_name):
        '''
        Forgets the composite structure of this morphism.

        Explanation
        ===========

        If ``new_name`` is not empty, returns a :class:`NamedMorphism`
        with the supplied name, otherwise returns a :class:`Morphism`.
        In both cases the domain of the new morphism is the domain of
        this composite morphism and the codomain of the new morphism
        is the codomain of this composite morphism.

        Examples
        ========

        >>> from sympy.categories import Object, NamedMorphism
        >>> A = Object("A")
        >>> B = Object("B")
        >>> C = Object("C")
        >>> f = NamedMorphism(A, B, "f")
        >>> g = NamedMorphism(B, C, "g")
        >>> (g * f).flatten("h")
        NamedMorphism(Object("A"), Object("C"), "h")

        '''
        return NamedMorphism(self.domain, self.codomain, new_name)



class Category(Basic):
    '''
    An (abstract) category.

    Explanation
    ===========

    A category [JoyOfCats] is a quadruple `\\mbox{K} = (O, \\hom, id,
    \\circ)` consisting of

    * a (set-theoretical) class `O`, whose members are called
      `K`-objects,

    * for each pair `(A, B)` of `K`-objects, a set `\\hom(A, B)` whose
      members are called `K`-morphisms from `A` to `B`,

    * for a each `K`-object `A`, a morphism `id:A\\rightarrow A`,
      called the `K`-identity of `A`,

    * a composition law `\\circ` associating with every `K`-morphisms
      `f:A\\rightarrow B` and `g:B\\rightarrow C` a `K`-morphism `g\\circ
      f:A\\rightarrow C`, called the composite of `f` and `g`.

    Composition is associative, `K`-identities are identities with
    respect to composition, and the sets `\\hom(A, B)` are pairwise
    disjoint.

    This class knows nothing about its objects and morphisms.
    Concrete cases of (abstract) categories should be implemented as
    classes derived from this one.

    Certain instances of :class:`Diagram` can be asserted to be
    commutative in a :class:`Category` by supplying the argument
    ``commutative_diagrams`` in the constructor.

    Examples
    ========

    >>> from sympy.categories import Object, NamedMorphism, Diagram, Category
    >>> from sympy import FiniteSet
    >>> A = Object("A")
    >>> B = Object("B")
    >>> C = Object("C")
    >>> f = NamedMorphism(A, B, "f")
    >>> g = NamedMorphism(B, C, "g")
    >>> d = Diagram([f, g])
    >>> K = Category("K", commutative_diagrams=[d])
    >>> K.commutative_diagrams == FiniteSet(d)
    True

    See Also
    ========

    Diagram
    '''
    
    def __new__(cls, name, objects, commutative_diagrams = (EmptySet, EmptySet)):
        if not name:
            raise ValueError('A Category cannot have an empty name.')
        if not isinstance(name, Str):
            name = Str(name)
        if not isinstance(objects, Class):
            objects = Class(objects)
    # WARNING: Decompyle incomplete

    name = (lambda self: self.args[0].name)()
    objects = (lambda self: self.args[1])()
    commutative_diagrams = (lambda self: self.args[2])()
    
    def hom(self, A, B):
        raise NotImplementedError('hom-sets are not implemented in Category.')

    
    def all_morphisms(self):
        raise NotImplementedError('Obtaining the class of morphisms is not implemented in Category.')



class Diagram(Basic):
    '''
    Represents a diagram in a certain category.

    Explanation
    ===========

    Informally, a diagram is a collection of objects of a category and
    certain morphisms between them.  A diagram is still a monoid with
    respect to morphism composition; i.e., identity morphisms, as well
    as all composites of morphisms included in the diagram belong to
    the diagram.  For a more formal approach to this notion see
    [Pare1970].

    The components of composite morphisms are also added to the
    diagram.  No properties are assigned to such morphisms by default.

    A commutative diagram is often accompanied by a statement of the
    following kind: "if such morphisms with such properties exist,
    then such morphisms which such properties exist and the diagram is
    commutative".  To represent this, an instance of :class:`Diagram`
    includes a collection of morphisms which are the premises and
    another collection of conclusions.  ``premises`` and
    ``conclusions`` associate morphisms belonging to the corresponding
    categories with the :class:`~.FiniteSet`\'s of their properties.

    The set of properties of a composite morphism is the intersection
    of the sets of properties of its components.  The domain and
    codomain of a conclusion morphism should be among the domains and
    codomains of the morphisms listed as the premises of a diagram.

    No checks are carried out of whether the supplied object and
    morphisms do belong to one and the same category.

    Examples
    ========

    >>> from sympy.categories import Object, NamedMorphism, Diagram
    >>> from sympy import pprint, default_sort_key
    >>> A = Object("A")
    >>> B = Object("B")
    >>> C = Object("C")
    >>> f = NamedMorphism(A, B, "f")
    >>> g = NamedMorphism(B, C, "g")
    >>> d = Diagram([f, g])
    >>> premises_keys = sorted(d.premises.keys(), key=default_sort_key)
    >>> pprint(premises_keys, use_unicode=False)
    [g*f:A-->C, id:A-->A, id:B-->B, id:C-->C, f:A-->B, g:B-->C]
    >>> pprint(d.premises, use_unicode=False)
    {g*f:A-->C: EmptySet, id:A-->A: EmptySet, id:B-->B: EmptySet,
     id:C-->C: EmptySet, f:A-->B: EmptySet, g:B-->C: EmptySet}
    >>> d = Diagram([f, g], {g * f: "unique"})
    >>> pprint(d.conclusions,use_unicode=False)
    {g*f:A-->C: {unique}}

    References
    ==========

    [Pare1970] B. Pareigis: Categories and functors.  Academic Press, 1970.

    '''
    _set_dict_union = (lambda dictionary, key, value: if key in dictionary:
dictionary[key] = dictionary[key] | valueTruedictionary[key] = NoneFalse)()
    _add_morphism_closure = (lambda morphisms, morphism, props, add_identities, recurse_composites = (True, True): if not Diagram._set_dict_union(morphisms, morphism, props):
if isinstance(morphism, IdentityMorphism):
if props:
raise ValueError('Instances of IdentityMorphism cannot have properties.')Noneif None:
empty = EmptySetid_dom = IdentityMorphism(morphism.domain)id_cod = IdentityMorphism(morphism.codomain)Diagram._set_dict_union(morphisms, id_dom, empty)Diagram._set_dict_union(morphisms, id_cod, empty)for existing_morphism, existing_props in list(morphisms.items()):
new_props = existing_props & propsif morphism.domain == existing_morphism.codomain:
left = morphism * existing_morphismDiagram._set_dict_union(morphisms, left, new_props)if morphism.codomain == existing_morphism.domain:
right = existing_morphism * morphismDiagram._set_dict_union(morphisms, right, new_props)if isinstance(morphism, CompositeMorphism) or recurse_composites:
empty = EmptySetfor component in morphism.components:
Diagram._add_morphism_closure(morphisms, component, empty, add_identities)NoneNoneNoneNone)()
    
    def __new__(cls, *args):
        '''
        Construct a new instance of Diagram.

        Explanation
        ===========

        If no arguments are supplied, an empty diagram is created.

        If at least an argument is supplied, ``args[0]`` is
        interpreted as the premises of the diagram.  If ``args[0]`` is
        a list, it is interpreted as a list of :class:`Morphism`\'s, in
        which each :class:`Morphism` has an empty set of properties.
        If ``args[0]`` is a Python dictionary or a :class:`Dict`, it
        is interpreted as a dictionary associating to some
        :class:`Morphism`\'s some properties.

        If at least two arguments are supplied ``args[1]`` is
        interpreted as the conclusions of the diagram.  The type of
        ``args[1]`` is interpreted in exactly the same way as the type
        of ``args[0]``.  If only one argument is supplied, the diagram
        has no conclusions.

        Examples
        ========

        >>> from sympy.categories import Object, NamedMorphism
        >>> from sympy.categories import IdentityMorphism, Diagram
        >>> A = Object("A")
        >>> B = Object("B")
        >>> C = Object("C")
        >>> f = NamedMorphism(A, B, "f")
        >>> g = NamedMorphism(B, C, "g")
        >>> d = Diagram([f, g])
        >>> IdentityMorphism(A) in d.premises.keys()
        True
        >>> g * f in d.premises.keys()
        True
        >>> d = Diagram([f, g], {g * f: "unique"})
        >>> d.conclusions[g * f]
        {unique}

        '''
        premises = { }
        conclusions = { }
        objects = EmptySet
    # WARNING: Decompyle incomplete

    premises = (lambda self: self.args[0])()
    conclusions = (lambda self: self.args[1])()
    objects = (lambda self: self.args[2])()
    
    def hom(self, A, B):
        '''
        Returns a 2-tuple of sets of morphisms between objects ``A`` and
        ``B``: one set of morphisms listed as premises, and the other set
        of morphisms listed as conclusions.

        Examples
        ========

        >>> from sympy.categories import Object, NamedMorphism, Diagram
        >>> from sympy import pretty
        >>> A = Object("A")
        >>> B = Object("B")
        >>> C = Object("C")
        >>> f = NamedMorphism(A, B, "f")
        >>> g = NamedMorphism(B, C, "g")
        >>> d = Diagram([f, g], {g * f: "unique"})
        >>> print(pretty(d.hom(A, C), use_unicode=False))
        ({g*f:A-->C}, {g*f:A-->C})

        See Also
        ========
        Object, Morphism
        '''
        premises = EmptySet
        conclusions = EmptySet
        for morphism in self.premises.keys():
            if morphism.domain == A and morphism.codomain == B:
                premises |= FiniteSet(morphism)
            for morphism in self.conclusions.keys():
                if morphism.domain == A and morphism.codomain == B:
                    conclusions |= FiniteSet(morphism)
                return (premises, conclusions)

    
    def is_subdiagram(self, diagram):
        '''
        Checks whether ``diagram`` is a subdiagram of ``self``.
        Diagram `D\'` is a subdiagram of `D` if all premises
        (conclusions) of `D\'` are contained in the premises
        (conclusions) of `D`.  The morphisms contained
        both in `D\'` and `D` should have the same properties for `D\'`
        to be a subdiagram of `D`.

        Examples
        ========

        >>> from sympy.categories import Object, NamedMorphism, Diagram
        >>> A = Object("A")
        >>> B = Object("B")
        >>> C = Object("C")
        >>> f = NamedMorphism(A, B, "f")
        >>> g = NamedMorphism(B, C, "g")
        >>> d = Diagram([f, g], {g * f: "unique"})
        >>> d1 = Diagram([f])
        >>> d.is_subdiagram(d1)
        True
        >>> d1.is_subdiagram(d)
        False
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def subdiagram_from_objects(self, objects):
        '''
        If ``objects`` is a subset of the objects of ``self``, returns
        a diagram which has as premises all those premises of ``self``
        which have a domains and codomains in ``objects``, likewise
        for conclusions.  Properties are preserved.

        Examples
        ========

        >>> from sympy.categories import Object, NamedMorphism, Diagram
        >>> from sympy import FiniteSet
        >>> A = Object("A")
        >>> B = Object("B")
        >>> C = Object("C")
        >>> f = NamedMorphism(A, B, "f")
        >>> g = NamedMorphism(B, C, "g")
        >>> d = Diagram([f, g], {f: "unique", g*f: "veryunique"})
        >>> d1 = d.subdiagram_from_objects(FiniteSet(A, B))
        >>> d1 == Diagram([f], {f: "unique"})
        True
        '''
        if not objects.is_subset(self.objects):
            raise ValueError('Supplied objects should all belong to the diagram.')
        new_premises = { }
        for morphism, props in self.premises.items():
            if sympify(objects.contains(morphism.domain)) is S.true and sympify(objects.contains(morphism.codomain)) is S.true:
                new_premises[morphism] = props
            new_conclusions = { }
            for morphism, props in self.conclusions.items():
                if sympify(objects.contains(morphism.domain)) is S.true and sympify(objects.contains(morphism.codomain)) is S.true:
                    new_conclusions[morphism] = props
                return Diagram(new_premises, new_conclusions)
