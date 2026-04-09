# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: diagram_drawing.pyc (Python 3.11)

'''
This module contains the functionality to arrange the nodes of a
diagram on an abstract grid, and then to produce a graphical
representation of the grid.

The currently supported back-ends are Xy-pic [Xypic].

Layout Algorithm
================

This section provides an overview of the algorithms implemented in
:class:`DiagramGrid` to lay out diagrams.

The first step of the algorithm is the removal composite and identity
morphisms which do not have properties in the supplied diagram.  The
premises and conclusions of the diagram are then merged.

The generic layout algorithm begins with the construction of the
"skeleton" of the diagram.  The skeleton is an undirected graph which
has the objects of the diagram as vertices and has an (undirected)
edge between each pair of objects between which there exist morphisms.
The direction of the morphisms does not matter at this stage.  The
skeleton also includes an edge between each pair of vertices `A` and
`C` such that there exists an object `B` which is connected via
a morphism to `A`, and via a morphism to `C`.

The skeleton constructed in this way has the property that every
object is a vertex of a triangle formed by three edges of the
skeleton.  This property lies at the base of the generic layout
algorithm.

After the skeleton has been constructed, the algorithm lists all
triangles which can be formed.  Note that some triangles will not have
all edges corresponding to morphisms which will actually be drawn.
Triangles which have only one edge or less which will actually be
drawn are immediately discarded.

The list of triangles is sorted according to the number of edges which
correspond to morphisms, then the triangle with the least number of such
edges is selected.  One of such edges is picked and the corresponding
objects are placed horizontally, on a grid.  This edge is recorded to
be in the fringe.  The algorithm then finds a "welding" of a triangle
to the fringe.  A welding is an edge in the fringe where a triangle
could be attached.  If the algorithm succeeds in finding such a
welding, it adds to the grid that vertex of the triangle which was not
yet included in any edge in the fringe and records the two new edges in
the fringe.  This process continues iteratively until all objects of
the diagram has been placed or until no more weldings can be found.

An edge is only removed from the fringe when a welding to this edge
has been found, and there is no room around this edge to place
another vertex.

When no more weldings can be found, but there are still triangles
left, the algorithm searches for a possibility of attaching one of the
remaining triangles to the existing structure by a vertex.  If such a
possibility is found, the corresponding edge of the found triangle is
placed in the found space and the iterative process of welding
triangles restarts.

When logical groups are supplied, each of these groups is laid out
independently.  Then a diagram is constructed in which groups are
objects and any two logical groups between which there exist morphisms
are connected via a morphism.  This diagram is laid out.  Finally,
the grid which includes all objects of the initial diagram is
constructed by replacing the cells which contain logical groups with
the corresponding laid out grids, and by correspondingly expanding the
rows and columns.

The sequential layout algorithm begins by constructing the
underlying undirected graph defined by the morphisms obtained after
simplifying premises and conclusions and merging them (see above).
The vertex with the minimal degree is then picked up and depth-first
search is started from it.  All objects which are located at distance
`n` from the root in the depth-first search tree, are positioned in
the `n`-th column of the resulting grid.  The sequential layout will
therefore attempt to lay the objects out along a line.

References
==========

.. [Xypic] https://xy-pic.sourceforge.net/

'''
from sympy.categories import CompositeMorphism, IdentityMorphism, NamedMorphism, Diagram
from sympy.core import Dict, Symbol, default_sort_key
from sympy.printing.latex import latex
from sympy.sets import FiniteSet
from sympy.utilities.iterables import iterable
from sympy.utilities.decorator import doctest_depends_on
from itertools import chain
__doctest_requires__ = {
    ('preview_diagram',): 'pyglet' }

class _GrowableGrid:
    '''
    Holds a growable grid of objects.

    Explanation
    ===========

    It is possible to append or prepend a row or a column to the grid
    using the corresponding methods.  Prepending rows or columns has
    the effect of changing the coordinates of the already existing
    elements.

    This class currently represents a naive implementation of the
    functionality with little attempt at optimisation.
    '''
    
    def __init__(self, width, height):
        pass
    # WARNING: Decompyle incomplete

    width = (lambda self: self._width)()
    height = (lambda self: self._height)()
    
    def __getitem__(self, i_j):
        '''
        Returns the element located at in the i-th line and j-th
        column.
        '''
        (i, j) = i_j
        return self._array[i][j]

    
    def __setitem__(self, i_j, newvalue):
        '''
        Sets the element located at in the i-th line and j-th
        column.
        '''
        (i, j) = i_j
        self._array[i][j] = newvalue

    
    def append_row(self):
        '''
        Appends an empty row to the grid.
        '''
        (lambda .0: [ None for j in .0 ])(range(self._width)())

    
    def append_column(self):
        '''
        Appends an empty column to the grid.
        '''
        for None in range(self._height):
            self._array[i].append(None)
            return None

    
    def prepend_row(self):
        '''
        Prepends the grid with an empty row.
        '''
        
        def <listcomp>(.0):
            return [ None for j in .0 ]

        0(<listcomp>, range(self._width)())

    
    def prepend_column(self):
        '''
        Prepends the grid with an empty column.
        '''
        for None in range(self._height):
            self._array[i].insert(0, None)
            return None



class DiagramGrid:
    '''
    Constructs and holds the fitting of the diagram into a grid.

    Explanation
    ===========

    The mission of this class is to analyse the structure of the
    supplied diagram and to place its objects on a grid such that,
    when the objects and the morphisms are actually drawn, the diagram
    would be "readable", in the sense that there will not be many
    intersections of moprhisms.  This class does not perform any
    actual drawing.  It does strive nevertheless to offer sufficient
    metadata to draw a diagram.

    Consider the following simple diagram.

    >>> from sympy.categories import Object, NamedMorphism
    >>> from sympy.categories import Diagram, DiagramGrid
    >>> from sympy import pprint
    >>> A = Object("A")
    >>> B = Object("B")
    >>> C = Object("C")
    >>> f = NamedMorphism(A, B, "f")
    >>> g = NamedMorphism(B, C, "g")
    >>> diagram = Diagram([f, g])

    The simplest way to have a diagram laid out is the following:

    >>> grid = DiagramGrid(diagram)
    >>> (grid.width, grid.height)
    (2, 2)
    >>> pprint(grid)
    A  B
    <BLANKLINE>
       C

    Sometimes one sees the diagram as consisting of logical groups.
    One can advise ``DiagramGrid`` as to such groups by employing the
    ``groups`` keyword argument.

    Consider the following diagram:

    >>> D = Object("D")
    >>> f = NamedMorphism(A, B, "f")
    >>> g = NamedMorphism(B, C, "g")
    >>> h = NamedMorphism(D, A, "h")
    >>> k = NamedMorphism(D, B, "k")
    >>> diagram = Diagram([f, g, h, k])

    Lay it out with generic layout:

    >>> grid = DiagramGrid(diagram)
    >>> pprint(grid)
    A  B  D
    <BLANKLINE>
       C

    Now, we can group the objects `A` and `D` to have them near one
    another:

    >>> grid = DiagramGrid(diagram, groups=[[A, D], B, C])
    >>> pprint(grid)
    B     C
    <BLANKLINE>
    A  D

    Note how the positioning of the other objects changes.

    Further indications can be supplied to the constructor of
    :class:`DiagramGrid` using keyword arguments.  The currently
    supported hints are explained in the following paragraphs.

    :class:`DiagramGrid` does not automatically guess which layout
    would suit the supplied diagram better.  Consider, for example,
    the following linear diagram:

    >>> E = Object("E")
    >>> f = NamedMorphism(A, B, "f")
    >>> g = NamedMorphism(B, C, "g")
    >>> h = NamedMorphism(C, D, "h")
    >>> i = NamedMorphism(D, E, "i")
    >>> diagram = Diagram([f, g, h, i])

    When laid out with the generic layout, it does not get to look
    linear:

    >>> grid = DiagramGrid(diagram)
    >>> pprint(grid)
    A  B
    <BLANKLINE>
       C  D
    <BLANKLINE>
          E

    To get it laid out in a line, use ``layout="sequential"``:

    >>> grid = DiagramGrid(diagram, layout="sequential")
    >>> pprint(grid)
    A  B  C  D  E

    One may sometimes need to transpose the resulting layout.  While
    this can always be done by hand, :class:`DiagramGrid` provides a
    hint for that purpose:

    >>> grid = DiagramGrid(diagram, layout="sequential", transpose=True)
    >>> pprint(grid)
    A
    <BLANKLINE>
    B
    <BLANKLINE>
    C
    <BLANKLINE>
    D
    <BLANKLINE>
    E

    Separate hints can also be provided for each group.  For an
    example, refer to ``tests/test_drawing.py``, and see the different
    ways in which the five lemma [FiveLemma] can be laid out.

    See Also
    ========

    Diagram

    References
    ==========

    .. [FiveLemma] https://en.wikipedia.org/wiki/Five_lemma
    '''
    _simplify_morphisms = (lambda morphisms: newmorphisms = { }for morphism, props in morphisms.items():
if not isinstance(morphism, CompositeMorphism) and props:
continueif isinstance(morphism, IdentityMorphism):
continuenewmorphisms[morphism] = propsnewmorphisms)()
    _merge_premises_conclusions = (lambda premises, conclusions: dict(chain(premises.items(), conclusions.items())))()
    _juxtapose_edges = (lambda edge1, edge2: intersection = edge1 & edge2if len(intersection) != 1:
NoneNone - intersection | edge2 - intersection)()
    _add_edge_append = (lambda dictionary, edge, elem: if edge in dictionary:
dictionary[edge].append(elem)Nonedictionary[edge] = [
None])()
    _build_skeleton = (lambda morphisms: edges = { }for morphism in morphisms:
DiagramGrid._add_edge_append(edges, frozenset([
morphism.domain,
morphism.codomain]), morphism)edges1 = dict(edges)for w in edges1:
for v in edges1:
wv = DiagramGrid._juxtapose_edges(w, v)if wv and wv not in edges:
edges[wv] = []edges)()
    _list_triangles = (lambda edges: triangles = set()for w in edges:
for v in edges:
wv = DiagramGrid._juxtapose_edges(w, v)if wv and wv in edges:
triangles.add(frozenset([
w,
v,
wv]))triangles)()
    _drop_redundant_triangles = (lambda triangles, skeleton: pass# WARNING: Decompyle incomplete
)()
    _morphism_length = (lambda morphism: if isinstance(morphism, CompositeMorphism):
len(morphism.components))()
    _compute_triangle_min_sizes = (lambda triangles, edges: triangle_sizes = { }for triangle in triangles:
size = 0for e in triangle:
morphisms = edges[e]if morphisms:
max += (lambda .0: pass# WARNING: Decompyle incomplete
)(morphisms())
                triangle_sizes[triangle] = size
                return triangle_sizes
)()
    _triangle_objects = (lambda triangle: pass# WARNING: Decompyle incomplete
)()
    _other_vertex = (lambda triangle, edge: list(DiagramGrid._triangle_objects(triangle) - set(edge))[0])()
    _empty_point = (lambda pt, grid: if pt[0] < 0 and pt[1] < 0 and pt[0] >= grid.height or pt[1] >= grid.width:
TrueNone[pt] is None)()
    _put_object = (lambda coords, obj, grid, fringe: (i, j) = coordsoffset = (0, 0)if i == -1:
grid.prepend_row()i = 0offset = (1, 0)for k in range(len(fringe)):
(i1, j1) = ()(i2, j2) = fringe[k]fringe[k] = ((i1 + 1, j1), (i2 + 1, j2))if i == grid.height:
grid.append_row()if j == -1:
j = 0offset = (offset[0], 1)grid.prepend_column()for k in range(len(fringe)):
(i1, j1) = ()(i2, j2) = fringe[k]fringe[k] = ((i1, j1 + 1), (i2, j2 + 1))if j == grid.width:
grid.append_column()grid[(i, j)] = objoffset)()
    _choose_target_cell = (lambda pt1, pt2, edge, obj, skeleton, grid: pt1_empty = DiagramGrid._empty_point(pt1, grid)pt2_empty = DiagramGrid._empty_point(pt2, grid)if pt1_empty and pt2_empty:
A = grid[edge[0]]if skeleton.get(frozenset([
A,
obj])):
pt1Noneif None:
pt1if None:
pt2)()
    _find_triangle_to_weld = (lambda triangles, fringe, grid: for triangle in triangles:
for a, b in fringe:
if frozenset([
grid[a],
grid[b]]) in triangle:
None, None, (triangle, (a, b))None)()
    _weld_triangle = (lambda tri, welding_edge, fringe, grid, skeleton:
