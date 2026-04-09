# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: strategy_options.pyc (Python 3.11)

''' '''
from __future__ import annotations
import typing
from typing import Any
from typing import Callable
from typing import cast
from typing import Dict
from typing import Iterable
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union
from  import util as orm_util
from _typing import insp_is_aliased_class
from _typing import insp_is_attribute
from _typing import insp_is_mapper
from _typing import insp_is_mapper_property
from attributes import QueryableAttribute
from base import InspectionAttr
from interfaces import LoaderOption
from path_registry import _DEFAULT_TOKEN
from path_registry import _StrPathToken
from path_registry import _WILDCARD_TOKEN
from path_registry import AbstractEntityRegistry
from path_registry import path_is_property
from path_registry import PathRegistry
from path_registry import TokenRegistry
from util import _orm_full_deannotate
from util import AliasedInsp
from  import exc as sa_exc
from  import inspect
from  import util
from sql import and_
from sql import cache_key
from sql import coercions
from sql import roles
from sql import traversals
from sql import visitors
from sql.base import _generative
from util.typing import Final
from util.typing import Literal
from util.typing import Self
_RELATIONSHIP_TOKEN: "Final[Literal['relationship']]" = 'relationship'
_COLUMN_TOKEN: "Final[Literal['column']]" = 'column'
_FN = TypeVar('_FN', bound = 'Callable[..., Any]')
if typing.TYPE_CHECKING:
    from _typing import _EntityType
    from _typing import _InternalEntityType
    from context import _MapperEntity
    from context import ORMCompileState
    from context import QueryContext
    from interfaces import _StrategyKey
    from interfaces import MapperProperty
    from interfaces import ORMOption
    from mapper import Mapper
    from path_registry import _PathRepresentation
    from sql._typing import _ColumnExpressionArgument
    from sql._typing import _FromClauseArgument
    from sql.cache_key import _CacheKeyTraversalType
    from sql.cache_key import CacheKey
_AttrType = Union[(Literal['*'], 'QueryableAttribute[Any]')]
_WildcardKeyType = Literal[('relationship', 'column')]
_StrategySpec = Dict[(str, Any)]
_OptsType = Dict[(str, Any)]
_AttrGroupType = Tuple[(_AttrType, ...)]

class _AbstractLoad(LoaderOption, traversals.GenerativeOnTraversal):
    __slots__ = ('propagate_to_loaders',)
    propagate_to_loaders: 'bool' = True
    
    def contains_eager(self = None, attr = None, alias = None, _is_chain = (None, False, False), _propagate_to_loaders = ('attr', '_AttrType', 'alias', 'Optional[_FromClauseArgument]', '_is_chain', 'bool', '_propagate_to_loaders', 'bool', 'return', 'Self')):
        '''Indicate that the given attribute should be eagerly loaded from
        columns stated manually in the query.

        This function is part of the :class:`_orm.Load` interface and supports
        both method-chained and standalone operation.

        The option is used in conjunction with an explicit join that loads
        the desired rows, i.e.::

            sess.query(Order).join(Order.user).options(contains_eager(Order.user))

        The above query would join from the ``Order`` entity to its related
        ``User`` entity, and the returned ``Order`` objects would have the
        ``Order.user`` attribute pre-populated.

        It may also be used for customizing the entries in an eagerly loaded
        collection; queries will normally want to use the
        :ref:`orm_queryguide_populate_existing` execution option assuming the
        primary collection of parent objects may already have been loaded::

            sess.query(User).join(User.addresses).filter(
                Address.email_address.like("%@aol.com")
            ).options(contains_eager(User.addresses)).populate_existing()

        See the section :ref:`contains_eager` for complete usage details.

        .. seealso::

            :ref:`loading_toplevel`

            :ref:`contains_eager`

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def load_only(self = None, *, raiseload, *attrs):
        '''Indicate that for a particular entity, only the given list
        of column-based attribute names should be loaded; all others will be
        deferred.

        This function is part of the :class:`_orm.Load` interface and supports
        both method-chained and standalone operation.

        Example - given a class ``User``, load only the ``name`` and
        ``fullname`` attributes::

            session.query(User).options(load_only(User.name, User.fullname))

        Example - given a relationship ``User.addresses -> Address``, specify
        subquery loading for the ``User.addresses`` collection, but on each
        ``Address`` object load only the ``email_address`` attribute::

            session.query(User).options(
                subqueryload(User.addresses).load_only(Address.email_address)
            )

        For a statement that has multiple entities,
        the lead entity can be
        specifically referred to using the :class:`_orm.Load` constructor::

            stmt = (
                select(User, Address)
                .join(User.addresses)
                .options(
                    Load(User).load_only(User.name, User.fullname),
                    Load(Address).load_only(Address.email_address),
                )
            )

        When used together with the
        :ref:`populate_existing <orm_queryguide_populate_existing>`
        execution option only the attributes listed will be refreshed.

        :param \\*attrs: Attributes to be loaded, all others will be deferred.

        :param raiseload: raise :class:`.InvalidRequestError` rather than
         lazy loading a value when a deferred attribute is accessed. Used
         to prevent unwanted SQL from being emitted.

         .. versionadded:: 2.0

        .. seealso::

            :ref:`orm_queryguide_column_deferral` - in the
            :ref:`queryguide_toplevel`

        :param \\*attrs: Attributes to be loaded, all others will be deferred.

        :param raiseload: raise :class:`.InvalidRequestError` rather than
         lazy loading a value when a deferred attribute is accessed. Used
         to prevent unwanted SQL from being emitted.

         .. versionadded:: 2.0

        '''
        cloned = self._set_column_strategy(_expand_column_strategy_attrs(attrs), {
            'deferred': False,
            'instrument': True })
        wildcard_strategy = {
            'deferred': True,
            'instrument': True }
        if raiseload:
            wildcard_strategy['raiseload'] = True
        cloned = cloned._set_column_strategy(('*',), wildcard_strategy)
        return cloned

    
    def joinedload(self = None, attr = None, innerjoin = None):
        '''Indicate that the given attribute should be loaded using joined
        eager loading.

        This function is part of the :class:`_orm.Load` interface and supports
        both method-chained and standalone operation.

        examples::

            # joined-load the "orders" collection on "User"
            select(User).options(joinedload(User.orders))

            # joined-load Order.items and then Item.keywords
            select(Order).options(joinedload(Order.items).joinedload(Item.keywords))

            # lazily load Order.items, but when Items are loaded,
            # joined-load the keywords collection
            select(Order).options(lazyload(Order.items).joinedload(Item.keywords))

        :param innerjoin: if ``True``, indicates that the joined eager load
         should use an inner join instead of the default of left outer join::

            select(Order).options(joinedload(Order.user, innerjoin=True))

        In order to chain multiple eager joins together where some may be
        OUTER and others INNER, right-nested joins are used to link them::

            select(A).options(
                joinedload(A.bs, innerjoin=False).joinedload(B.cs, innerjoin=True)
            )

        The above query, linking A.bs via "outer" join and B.cs via "inner"
        join would render the joins as "a LEFT OUTER JOIN (b JOIN c)". When
        using older versions of SQLite (< 3.7.16), this form of JOIN is
        translated to use full subqueries as this syntax is otherwise not
        directly supported.

        The ``innerjoin`` flag can also be stated with the term ``"unnested"``.
        This indicates that an INNER JOIN should be used, *unless* the join
        is linked to a LEFT OUTER JOIN to the left, in which case it
        will render as LEFT OUTER JOIN.  For example, supposing ``A.bs``
        is an outerjoin::

            select(A).options(joinedload(A.bs).joinedload(B.cs, innerjoin="unnested"))

        The above join will render as "a LEFT OUTER JOIN b LEFT OUTER JOIN c",
        rather than as "a LEFT OUTER JOIN (b JOIN c)".

        .. note:: The "unnested" flag does **not** affect the JOIN rendered
            from a many-to-many association table, e.g. a table configured as
            :paramref:`_orm.relationship.secondary`, to the target table; for
            correctness of results, these joins are always INNER and are
            therefore right-nested if linked to an OUTER join.

        .. note::

            The joins produced by :func:`_orm.joinedload` are **anonymously
            aliased**. The criteria by which the join proceeds cannot be
            modified, nor can the ORM-enabled :class:`_sql.Select` or legacy
            :class:`_query.Query` refer to these joins in any way, including
            ordering. See :ref:`zen_of_eager_loading` for further detail.

            To produce a specific SQL JOIN which is explicitly available, use
            :meth:`_sql.Select.join` and :meth:`_query.Query.join`. To combine
            explicit JOINs with eager loading of collections, use
            :func:`_orm.contains_eager`; see :ref:`contains_eager`.

        .. seealso::

            :ref:`loading_toplevel`

            :ref:`joined_eager_loading`

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def subqueryload(self = None, attr = None):
        '''Indicate that the given attribute should be loaded using
        subquery eager loading.

        This function is part of the :class:`_orm.Load` interface and supports
        both method-chained and standalone operation.

        examples::

            # subquery-load the "orders" collection on "User"
            select(User).options(subqueryload(User.orders))

            # subquery-load Order.items and then Item.keywords
            select(Order).options(
                subqueryload(Order.items).subqueryload(Item.keywords)
            )

            # lazily load Order.items, but when Items are loaded,
            # subquery-load the keywords collection
            select(Order).options(lazyload(Order.items).subqueryload(Item.keywords))

        .. seealso::

            :ref:`loading_toplevel`

            :ref:`subquery_eager_loading`

        '''
        return self._set_relationship_strategy(attr, {
            'lazy': 'subquery' })

    
    def selectinload(self = None, attr = None, recursion_depth = None):
        '''Indicate that the given attribute should be loaded using
        SELECT IN eager loading.

        This function is part of the :class:`_orm.Load` interface and supports
        both method-chained and standalone operation.

        examples::

            # selectin-load the "orders" collection on "User"
            select(User).options(selectinload(User.orders))

            # selectin-load Order.items and then Item.keywords
            select(Order).options(
                selectinload(Order.items).selectinload(Item.keywords)
            )

            # lazily load Order.items, but when Items are loaded,
            # selectin-load the keywords collection
            select(Order).options(lazyload(Order.items).selectinload(Item.keywords))

        :param recursion_depth: optional int; when set to a positive integer
         in conjunction with a self-referential relationship,
         indicates "selectin" loading will continue that many levels deep
         automatically until no items are found.

         .. note:: The :paramref:`_orm.selectinload.recursion_depth` option
            currently supports only self-referential relationships.  There
            is not yet an option to automatically traverse recursive structures
            with more than one relationship involved.

            Additionally, the :paramref:`_orm.selectinload.recursion_depth`
            parameter is new and experimental and should be treated as "alpha"
            status for the 2.0 series.

         .. versionadded:: 2.0 added
            :paramref:`_orm.selectinload.recursion_depth`


        .. seealso::

            :ref:`loading_toplevel`

            :ref:`selectin_eager_loading`

        '''
        return self._set_relationship_strategy(attr, {
            'lazy': 'selectin' }, opts = {
            'recursion_depth': recursion_depth })

    
    def lazyload(self = None, attr = None):
        '''Indicate that the given attribute should be loaded using "lazy"
        loading.

        This function is part of the :class:`_orm.Load` interface and supports
        both method-chained and standalone operation.

        .. seealso::

            :ref:`loading_toplevel`

            :ref:`lazy_loading`

        '''
        return self._set_relationship_strategy(attr, {
            'lazy': 'select' })

    
    def immediateload(self = None, attr = None, recursion_depth = None):
        '''Indicate that the given attribute should be loaded using
        an immediate load with a per-attribute SELECT statement.

        The load is achieved using the "lazyloader" strategy and does not
        fire off any additional eager loaders.

        The :func:`.immediateload` option is superseded in general
        by the :func:`.selectinload` option, which performs the same task
        more efficiently by emitting a SELECT for all loaded objects.

        This function is part of the :class:`_orm.Load` interface and supports
        both method-chained and standalone operation.

        :param recursion_depth: optional int; when set to a positive integer
         in conjunction with a self-referential relationship,
         indicates "selectin" loading will continue that many levels deep
         automatically until no items are found.

         .. note:: The :paramref:`_orm.immediateload.recursion_depth` option
            currently supports only self-referential relationships.  There
            is not yet an option to automatically traverse recursive structures
            with more than one relationship involved.

         .. warning:: This parameter is new and experimental and should be
            treated as "alpha" status

         .. versionadded:: 2.0 added
            :paramref:`_orm.immediateload.recursion_depth`


        .. seealso::

            :ref:`loading_toplevel`

            :ref:`selectin_eager_loading`

        '''
        loader = self._set_relationship_strategy(attr, {
            'lazy': 'immediate' }, opts = {
            'recursion_depth': recursion_depth })
        return loader

    
    def noload(self = None, attr = None):
        '''Indicate that the given relationship attribute should remain
        unloaded.

        The relationship attribute will return ``None`` when accessed without
        producing any loading effect.

        This function is part of the :class:`_orm.Load` interface and supports
        both method-chained and standalone operation.

        :func:`_orm.noload` applies to :func:`_orm.relationship` attributes
        only.

        .. legacy:: The :func:`_orm.noload` option is **legacy**.  As it
           forces collections to be empty, which invariably leads to
           non-intuitive and difficult to predict results.  There are no
           legitimate uses for this option in modern SQLAlchemy.

        .. seealso::

            :ref:`loading_toplevel`

        '''
        return self._set_relationship_strategy(attr, {
            'lazy': 'noload' })

    
    def raiseload(self = None, attr = None, sql_only = None):
        """Indicate that the given attribute should raise an error if accessed.

        A relationship attribute configured with :func:`_orm.raiseload` will
        raise an :exc:`~sqlalchemy.exc.InvalidRequestError` upon access. The
        typical way this is useful is when an application is attempting to
        ensure that all relationship attributes that are accessed in a
        particular context would have been already loaded via eager loading.
        Instead of having to read through SQL logs to ensure lazy loads aren't
        occurring, this strategy will cause them to raise immediately.

        :func:`_orm.raiseload` applies to :func:`_orm.relationship` attributes
        only. In order to apply raise-on-SQL behavior to a column-based
        attribute, use the :paramref:`.orm.defer.raiseload` parameter on the
        :func:`.defer` loader option.

        :param sql_only: if True, raise only if the lazy load would emit SQL,
         but not if it is only checking the identity map, or determining that
         the related value should just be None due to missing keys. When False,
         the strategy will raise for all varieties of relationship loading.

        This function is part of the :class:`_orm.Load` interface and supports
        both method-chained and standalone operation.

        .. seealso::

            :ref:`loading_toplevel`

            :ref:`prevent_lazy_with_raiseload`

            :ref:`orm_queryguide_deferred_raiseload`

        """
        return self._set_relationship_strategy(attr, {
            'lazy': 'raise_on_sql' if sql_only else 'raise' })

    
    def defaultload(self = None, attr = None):
        '''Indicate an attribute should load using its predefined loader style.

        The behavior of this loading option is to not change the current
        loading style of the attribute, meaning that the previously configured
        one is used or, if no previous style was selected, the default
        loading will be used.

        This method is used to link to other loader options further into
        a chain of attributes without altering the loader style of the links
        along the chain.  For example, to set joined eager loading for an
        element of an element::

            session.query(MyClass).options(
                defaultload(MyClass.someattribute).joinedload(
                    MyOtherClass.someotherattribute
                )
            )

        :func:`.defaultload` is also useful for setting column-level options on
        a related class, namely that of :func:`.defer` and :func:`.undefer`::

            session.scalars(
                select(MyClass).options(
                    defaultload(MyClass.someattribute)
                    .defer("some_column")
                    .undefer("some_other_column")
                )
            )

        .. seealso::

            :ref:`orm_queryguide_relationship_sub_options`

            :meth:`_orm.Load.options`

        '''
        return self._set_relationship_strategy(attr, None)

    
    def defer(self = None, key = None, raiseload = None):
        '''Indicate that the given column-oriented attribute should be
        deferred, e.g. not loaded until accessed.

        This function is part of the :class:`_orm.Load` interface and supports
        both method-chained and standalone operation.

        e.g.::

            from sqlalchemy.orm import defer

            session.query(MyClass).options(
                defer(MyClass.attribute_one), defer(MyClass.attribute_two)
            )

        To specify a deferred load of an attribute on a related class,
        the path can be specified one token at a time, specifying the loading
        style for each link along the chain.  To leave the loading style
        for a link unchanged, use :func:`_orm.defaultload`::

            session.query(MyClass).options(
                defaultload(MyClass.someattr).defer(RelatedClass.some_column)
            )

        Multiple deferral options related to a relationship can be bundled
        at once using :meth:`_orm.Load.options`::


            select(MyClass).options(
                defaultload(MyClass.someattr).options(
                    defer(RelatedClass.some_column),
                    defer(RelatedClass.some_other_column),
                    defer(RelatedClass.another_column),
                )
            )

        :param key: Attribute to be deferred.

        :param raiseload: raise :class:`.InvalidRequestError` rather than
         lazy loading a value when the deferred attribute is accessed. Used
         to prevent unwanted SQL from being emitted.

        .. versionadded:: 1.4

        .. seealso::

            :ref:`orm_queryguide_column_deferral` - in the
            :ref:`queryguide_toplevel`

            :func:`_orm.load_only`

            :func:`_orm.undefer`

        '''
        strategy = {
            'deferred': True,
            'instrument': True }
        if raiseload:
            strategy['raiseload'] = True
        return self._set_column_strategy(_expand_column_strategy_attrs((key,)), strategy)

    
    def undefer(self = None, key = None):
        '''Indicate that the given column-oriented attribute should be
        undeferred, e.g. specified within the SELECT statement of the entity
        as a whole.

        The column being undeferred is typically set up on the mapping as a
        :func:`.deferred` attribute.

        This function is part of the :class:`_orm.Load` interface and supports
        both method-chained and standalone operation.

        Examples::

            # undefer two columns
            session.query(MyClass).options(
                undefer(MyClass.col1), undefer(MyClass.col2)
            )

            # undefer all columns specific to a single class using Load + *
            session.query(MyClass, MyOtherClass).options(Load(MyClass).undefer("*"))

            # undefer a column on a related object
            select(MyClass).options(defaultload(MyClass.items).undefer(MyClass.text))

        :param key: Attribute to be undeferred.

        .. seealso::

            :ref:`orm_queryguide_column_deferral` - in the
            :ref:`queryguide_toplevel`

            :func:`_orm.defer`

            :func:`_orm.undefer_group`

        '''
        return self._set_column_strategy(_expand_column_strategy_attrs((key,)), {
            'deferred': False,
            'instrument': True })

    
    def undefer_group(self = None, name = None):
        '''Indicate that columns within the given deferred group name should be
        undeferred.

        The columns being undeferred are set up on the mapping as
        :func:`.deferred` attributes and include a "group" name.

        E.g::

            session.query(MyClass).options(undefer_group("large_attrs"))

        To undefer a group of attributes on a related entity, the path can be
        spelled out using relationship loader options, such as
        :func:`_orm.defaultload`::

            select(MyClass).options(
                defaultload("someattr").undefer_group("large_attrs")
            )

        .. seealso::

            :ref:`orm_queryguide_column_deferral` - in the
            :ref:`queryguide_toplevel`

            :func:`_orm.defer`

            :func:`_orm.undefer`

        '''
        return self._set_column_strategy((_WILDCARD_TOKEN,), None, {
            f'''undefer_group_{name}''': True })

    
    def with_expression(self = None, key = None, expression = None):
        '''Apply an ad-hoc SQL expression to a "deferred expression"
        attribute.

        This option is used in conjunction with the
        :func:`_orm.query_expression` mapper-level construct that indicates an
        attribute which should be the target of an ad-hoc SQL expression.

        E.g.::

            stmt = select(SomeClass).options(
                with_expression(SomeClass.x_y_expr, SomeClass.x + SomeClass.y)
            )

        .. versionadded:: 1.2

        :param key: Attribute to be populated

        :param expr: SQL expression to be applied to the attribute.

        .. seealso::

            :ref:`orm_queryguide_with_expression` - background and usage
            examples

        '''
        expression = _orm_full_deannotate(coercions.expect(roles.LabeledColumnExprRole, expression))
        return self._set_column_strategy((key,), {
            'query_expression': True }, extra_criteria = (expression,))

    
    def selectin_polymorphic(self = None, classes = None):
        '''Indicate an eager load should take place for all attributes
        specific to a subclass.

        This uses an additional SELECT with IN against all matched primary
        key values, and is the per-query analogue to the ``"selectin"``
        setting on the :paramref:`.mapper.polymorphic_load` parameter.

        .. versionadded:: 1.2

        .. seealso::

            :ref:`polymorphic_selectin`

        '''
        self = 'entities'(None, opts = {
            tuple: sorted((lambda .0: pass# WARNING: Decompyle incomplete
)(classes(), key = id)) })
        return self

    _coerce_strat = (lambda self = None, strategy = None: pass)()
    _coerce_strat = (lambda self = None, strategy = None: pass)()
    
    def _coerce_strat(self = None, strategy = None):
        pass
    # WARNING: Decompyle incomplete

    _set_relationship_strategy = (lambda self, attr = None, strategy = None, propagate_to_loaders = _generative, opts = (True, None, None), _reconcile_to_other = ('attr', '_AttrType', 'strategy', 'Optional[_StrategySpec]', 'propagate_to_loaders', 'bool', 'opts', 'Optional[_OptsType]', '_reconcile_to_other', 'Optional[bool]', 'return', 'Self'): strategy_key = self._coerce_strat(strategy)self._clone_for_bind_strategy((attr,), strategy_key, _RELATIONSHIP_TOKEN, opts = opts, propagate_to_loaders = propagate_to_loaders, reconcile_to_other = _reconcile_to_other)self)()
    _set_column_strategy = (lambda self = None, attrs = None, strategy = _generative, opts = (None, None), extra_criteria = ('attrs', 'Tuple[_AttrType, ...]', 'strategy', 'Optional[_StrategySpec]', 'opts', 'Optional[_OptsType]', 'extra_criteria', 'Optional[Tuple[Any, ...]]', 'return', 'Self'): strategy_key = self._coerce_strat(strategy)self._clone_for_bind_strategy(attrs, strategy_key, _COLUMN_TOKEN, opts = opts, attr_group = attrs, extra_criteria = extra_criteria)self)()
    _set_generic_strategy = (lambda self = None, attrs = None, strategy = _generative, _reconcile_to_other = (None,): strategy_key = self._coerce_strat(strategy)self._clone_for_bind_strategy(attrs, strategy_key, None, propagate_to_loaders = True, reconcile_to_other = _reconcile_to_other)self)()
    _set_class_strategy = (lambda self = None, strategy = None, opts = _generative: strategy_key = self._coerce_strat(strategy)self._clone_for_bind_strategy(None, strategy_key, None, opts = opts)self)()
    
    def _apply_to_parent(self = None, parent = None):
        '''apply this :class:`_orm._AbstractLoad` object as a sub-option o
        a :class:`_orm.Load` object.

        Implementation is provided by subclasses.

        '''
        raise NotImplementedError()

    
    def options(self = None, *opts):
        '''Apply a series of options as sub-options to this
        :class:`_orm._AbstractLoad` object.

        Implementation is provided by subclasses.

        '''
        raise NotImplementedError()

    
    def _clone_for_bind_strategy(self, attrs, strategy, wildcard_key, opts = None, attr_group = None, propagate_to_loaders = None, reconcile_to_other = (None, None, True, None, None), extra_criteria = ('attrs', 'Optional[Tuple[_AttrType, ...]]', 'strategy', 'Optional[_StrategyKey]', 'wildcard_key', 'Optional[_WildcardKeyType]', 'opts', 'Optional[_OptsType]', 'attr_group', 'Optional[_AttrGroupType]', 'propagate_to_loaders', 'bool', 'reconcile_to_other', 'Optional[bool]', 'extra_criteria', 'Optional[Tuple[Any, ...]]', 'return', 'Self')):
        raise NotImplementedError()

    
    def process_compile_state_replaced_entities(self = None, compile_state = None, mapper_entities = None):
        if not compile_state.compile_options._enable_eagerloads:
            return None
        None._process(compile_state, mapper_entities, not bool(compile_state.current_path))

    
    def process_compile_state(self = None, compile_state = None):
