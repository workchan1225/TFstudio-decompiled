# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: extension.pyc (Python 3.11)

from __future__ import annotations
import os
import types
import typing as t
import warnings
from weakref import WeakKeyDictionary
import sqlalchemy as sa
from sqlalchemy.event import event as sa_event
from sqlalchemy.exc import exc as sa_exc
from sqlalchemy.orm import orm as sa_orm
from flask import abort
from flask import current_app
from flask import Flask
from flask import has_app_context
from model import _QueryProperty
from model import BindMixin
from model import DefaultMeta
from model import DefaultMetaNoName
from model import Model
from model import NameMixin
from pagination import Pagination
from pagination import SelectPagination
from query import Query
from session import _app_ctx_id
from session import Session
from table import _Table
_O = t.TypeVar('_O', bound = object)
_FSA_MCT = t.TypeVar('_FSA_MCT', bound = t.Union[(t.Type[Model], sa_orm.DeclarativeMeta, t.Type[sa_orm.DeclarativeBase], t.Type[sa_orm.DeclarativeBaseNoMeta])])

class _FSAModel(Model):
    metadata: 'sa.MetaData' = '_FSAModel'


def _get_2x_declarative_bases(model_class = None):
    return model_class.__bases__()


class SQLAlchemy:
    '''Integrates SQLAlchemy with Flask. This handles setting up one or more engines,
    associating tables and models with specific engines, and cleaning up connections and
    sessions after each request.

    Only the engine configuration is specific to each application, other things like
    the model, table, metadata, and session are shared for all applications using that
    extension instance. Call :meth:`init_app` to configure the extension on an
    application.

    After creating the extension, create model classes by subclassing :attr:`Model`, and
    table classes with :attr:`Table`. These can be accessed before :meth:`init_app` is
    called, making it possible to define the models separately from the application.

    Accessing :attr:`session` and :attr:`engine` requires an active Flask application
    context. This includes methods like :meth:`create_all` which use the engine.

    This class also provides access to names in SQLAlchemy\'s ``sqlalchemy`` and
    ``sqlalchemy.orm`` modules. For example, you can use ``db.Column`` and
    ``db.relationship`` instead of importing ``sqlalchemy.Column`` and
    ``sqlalchemy.orm.relationship``. This can be convenient when defining models.

    :param app: Call :meth:`init_app` on this Flask application now.
    :param metadata: Use this as the default :class:`sqlalchemy.schema.MetaData`. Useful
        for setting a naming convention.
    :param session_options: Arguments used by :attr:`session` to create each session
        instance. A ``scopefunc`` key will be passed to the scoped session, not the
        session instance. See :class:`sqlalchemy.orm.sessionmaker` for a list of
        arguments.
    :param query_class: Use this as the default query class for models and dynamic
        relationships. The query interface is considered legacy in SQLAlchemy.
    :param model_class: Use this as the model base class when creating the declarative
        model class :attr:`Model`. Can also be a fully created declarative model class
        for further customization.
    :param engine_options: Default arguments used when creating every engine. These are
        lower precedence than application config. See :func:`sqlalchemy.create_engine`
        for a list of arguments.
    :param add_models_to_shell: Add the ``db`` instance and all model classes to
        ``flask shell``.

    .. versionchanged:: 3.1.0
        The ``metadata`` parameter can still be used with SQLAlchemy 1.x classes,
        but is ignored when using SQLAlchemy 2.x style of declarative classes.
        Instead, specify metadata on your Base class.

    .. versionchanged:: 3.1.0
        Added the ``disable_autonaming`` parameter.

    .. versionchanged:: 3.1.0
        Changed ``model_class`` parameter to accepta SQLAlchemy 2.x
        declarative base subclass.

    .. versionchanged:: 3.0
        An active Flask application context is always required to access ``session`` and
        ``engine``.

    .. versionchanged:: 3.0
        Separate ``metadata`` are used for each bind key.

    .. versionchanged:: 3.0
        The ``engine_options`` parameter is applied as defaults before per-engine
        configuration.

    .. versionchanged:: 3.0
        The session class can be customized in ``session_options``.

    .. versionchanged:: 3.0
        Added the ``add_models_to_shell`` parameter.

    .. versionchanged:: 3.0
        Engines are created when calling ``init_app`` rather than the first time they
        are accessed.

    .. versionchanged:: 3.0
        All parameters except ``app`` are keyword-only.

    .. versionchanged:: 3.0
        The extension instance is stored directly as ``app.extensions["sqlalchemy"]``.

    .. versionchanged:: 3.0
        Setup methods are renamed with a leading underscore. They are considered
        internal interfaces which may change at any time.

    .. versionchanged:: 3.0
        Removed the ``use_native_unicode`` parameter and config.

    .. versionchanged:: 2.4
        Added the ``engine_options`` parameter.

    .. versionchanged:: 2.1
        Added the ``metadata``, ``query_class``, and ``model_class`` parameters.

    .. versionchanged:: 2.1
        Use the same query class across ``session``, ``Model.query`` and
        ``Query``.

    .. versionchanged:: 0.16
        ``scopefunc`` is accepted in ``session_options``.

    .. versionchanged:: 0.10
        Added the ``session_options`` parameter.
    '''
    
    def __init__(self = None, app = None, *, metadata, session_options, query_class, model_class, engine_options, add_models_to_shell, disable_autonaming):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        if not has_app_context():
            return f'''<{type(self).__name__}>'''
        message = f'''{None(self).__name__} {self.engine.url}'''
        if len(self.engines) > 1:
            message = f'''{message} +{len(self.engines) - 1}'''
        return f'''<{message}>'''

    
    def init_app(self = None, app = None):
        '''Initialize a Flask application for use with this extension instance. This
        must be called before accessing the database engine or session with the app.

        This sets default configuration values, then configures the extension on the
        application and creates the engines for each bind key. Therefore, this must be
        called after the application has been configured. Changes to application config
        after this call will not be reflected.

        The following keys from ``app.config`` are used:

        - :data:`.SQLALCHEMY_DATABASE_URI`
        - :data:`.SQLALCHEMY_ENGINE_OPTIONS`
        - :data:`.SQLALCHEMY_ECHO`
        - :data:`.SQLALCHEMY_BINDS`
        - :data:`.SQLALCHEMY_RECORD_QUERIES`
        - :data:`.SQLALCHEMY_TRACK_MODIFICATIONS`

        :param app: The Flask application to initialize.
        '''
        if 'sqlalchemy' in app.extensions:
            raise RuntimeError("A 'SQLAlchemy' instance has already been registered on this Flask app. Import and use that instance instead.")
        app.extensions['sqlalchemy'] = self
        app.teardown_appcontext(self._teardown_session)
        if self._add_models_to_shell:
            add_models_to_shell = add_models_to_shell
            import cli
            app.shell_context_processor(add_models_to_shell)
        basic_uri = app.config.setdefault('SQLALCHEMY_DATABASE_URI', None)
        basic_engine_options = self._engine_options.copy()
        basic_engine_options.update(app.config.setdefault('SQLALCHEMY_ENGINE_OPTIONS', { }))
        echo = app.config.setdefault('SQLALCHEMY_ECHO', False)
        config_binds = app.config.setdefault('SQLALCHEMY_BINDS', { })
        engine_options = { }
    # WARNING: Decompyle incomplete

    
    def _make_scoped_session(self = None, options = None):
        '''Create a :class:`sqlalchemy.orm.scoping.scoped_session` around the factory
        from :meth:`_make_session_factory`. The result is available as :attr:`session`.

        The scope function can be customized using the ``scopefunc`` key in the
        ``session_options`` parameter to the extension. By default it uses the current
        thread or greenlet id.

        This method is used for internal setup. Its signature may change at any time.

        :meta private:

        :param options: The ``session_options`` parameter from ``__init__``. Keyword
            arguments passed to the session factory. A ``scopefunc`` key is popped.

        .. versionchanged:: 3.0
            The session is scoped to the current app context.

        .. versionchanged:: 3.0
            Renamed from ``create_scoped_session``, this method is internal.
        '''
        scope = options.pop('scopefunc', _app_ctx_id)
        factory = self._make_session_factory(options)
        return sa_orm.scoped_session(factory, scope)

    
    def _make_session_factory(self = None, options = None):
        '''Create the SQLAlchemy :class:`sqlalchemy.orm.sessionmaker` used by
        :meth:`_make_scoped_session`.

        To customize, pass the ``session_options`` parameter to :class:`SQLAlchemy`. To
        customize the session class, subclass :class:`.Session` and pass it as the
        ``class_`` key.

        This method is used for internal setup. Its signature may change at any time.

        :meta private:

        :param options: The ``session_options`` parameter from ``__init__``. Keyword
            arguments passed to the session factory.

        .. versionchanged:: 3.0
            The session class can be customized.

        .. versionchanged:: 3.0
            Renamed from ``create_session``, this method is internal.
        '''
        options.setdefault('class_', Session)
        options.setdefault('query_cls', self.Query)
    # WARNING: Decompyle incomplete

    
    def _teardown_session(self = None, exc = None):
        '''Remove the current session at the end of the request.

        :meta private:

        .. versionadded:: 3.0
        '''
        self.session.remove()

    
    def _make_metadata(self = None, bind_key = None):
        '''Get or create a :class:`sqlalchemy.schema.MetaData` for the given bind key.

        This method is used for internal setup. Its signature may change at any time.

        :meta private:

        :param bind_key: The name of the metadata being created.

        .. versionadded:: 3.0
        '''
        if bind_key in self.metadatas:
            return self.metadatas[bind_key]
    # WARNING: Decompyle incomplete

    
    def _make_table_class(self = None):
        '''Create a SQLAlchemy :class:`sqlalchemy.schema.Table` class that chooses a
        metadata automatically based on the ``bind_key``. The result is available as
        :attr:`Table`.

        This method is used for internal setup. Its signature may change at any time.

        :meta private:

        .. versionadded:: 3.0
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _make_declarative_base(self = None, model_class = None, disable_autonaming = None):
        '''Create a SQLAlchemy declarative model class. The result is available as
        :attr:`Model`.

        To customize, subclass :class:`.Model` and pass it as ``model_class`` to
        :class:`SQLAlchemy`. To customize at the metaclass level, pass an already
        created declarative model class as ``model_class``.

        This method is used for internal setup. Its signature may change at any time.

        :meta private:

        :param model_class: A model base class, or an already created declarative model
        class.

        :param disable_autonaming: Turns off automatic tablename generation in models.

        .. versionchanged:: 3.1.0
            Added support for passing SQLAlchemy 2.x base class as model class.
            Added optional ``disable_autonaming`` parameter.

        .. versionchanged:: 3.0
            Renamed with a leading underscore, this method is internal.

        .. versionchanged:: 2.3
            ``model`` can be an already created declarative model class.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _apply_driver_defaults(self = None, options = None, app = None):
        '''Apply driver-specific configuration to an engine.

        SQLite in-memory databases use ``StaticPool`` and disable ``check_same_thread``.
        File paths are relative to the app\'s :attr:`~flask.Flask.instance_path`,
        which is created if it doesn\'t exist.

        MySQL sets ``charset="utf8mb4"``, and ``pool_timeout`` defaults to 2 hours.

        This method is used for internal setup. Its signature may change at any time.

        :meta private:

        :param options: Arguments passed to the engine.
        :param app: The application that the engine configuration belongs to.

        .. versionchanged:: 3.0
            SQLite paths are relative to ``app.instance_path``. It does not use
            ``NullPool`` if ``pool_size`` is 0. Driver-level URIs are supported.

        .. versionchanged:: 3.0
            MySQL sets ``charset="utf8mb4". It does not set ``pool_size`` to 10. It
            does not set ``pool_recycle`` if not using a queue pool.

        .. versionchanged:: 3.0
            Renamed from ``apply_driver_hacks``, this method is internal. It does not
            return anything.

        .. versionchanged:: 2.5
            Returns ``(sa_url, options)``.
        '''
        url = sa.engine.make_url(options['url'])
    # WARNING: Decompyle incomplete

    
    def _make_engine(self = None, bind_key = None, options = None, app = ('bind_key', 'str | None', 'options', 'dict[str, t.Any]', 'app', 'Flask', 'return', 'sa.engine.Engine')):
        '''Create the :class:`sqlalchemy.engine.Engine` for the given bind key and app.

        To customize, use :data:`.SQLALCHEMY_ENGINE_OPTIONS` or
        :data:`.SQLALCHEMY_BINDS` config. Pass ``engine_options`` to :class:`SQLAlchemy`
        to set defaults for all engines.

        This method is used for internal setup. Its signature may change at any time.

        :meta private:

        :param bind_key: The name of the engine being created.
        :param options: Arguments passed to the engine.
        :param app: The application that the engine configuration belongs to.

        .. versionchanged:: 3.0
            Renamed from ``create_engine``, this method is internal.
        '''
        return sa.engine_from_config(options, prefix = '')

    metadata = (lambda self = None: self.metadatas[None])()
    engines = (lambda self = None: app = current_app._get_current_object()if app not in self._app_engines:
raise RuntimeError("The current Flask app is not registered with this 'SQLAlchemy' instance. Did you forget to call 'init_app', or did you create multiple 'SQLAlchemy' instances?")self._app_engines[app])()
    engine = (lambda self = None: self.engines[None])()
    
    def get_engine(self = None, bind_key = None, **kwargs):
        '''Get the engine for the given bind key for the current application.
        This requires that a Flask application context is active.

        :param bind_key: The name of the engine.

        .. deprecated:: 3.0
            Will be removed in Flask-SQLAlchemy 3.2. Use ``engines[key]`` instead.

        .. versionchanged:: 3.0
            Renamed the ``bind`` parameter to ``bind_key``. Removed the ``app``
            parameter.
        '''
        warnings.warn("'get_engine' is deprecated and will be removed in Flask-SQLAlchemy 3.2. Use 'engine' or 'engines[key]' instead. If you're using Flask-Migrate or Alembic, you'll need to update your 'env.py' file.", DeprecationWarning, stacklevel = 2)
        if 'bind' in kwargs:
            bind_key = kwargs.pop('bind')
        return self.engines[bind_key]

    
    def get_or_404(self = None, entity = None, ident = None, *, description, **kwargs):
        '''Like :meth:`session.get() <sqlalchemy.orm.Session.get>` but aborts with a
        ``404 Not Found`` error instead of returning ``None``.

        :param entity: The model class to query.
        :param ident: The primary key to query.
        :param description: A custom message to show on the error page.
        :param kwargs: Extra arguments passed to ``session.get()``.

        .. versionchanged:: 3.1
            Pass extra keyword arguments to ``session.get()``.

        .. versionadded:: 3.0
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def first_or_404(self = None, statement = None, *, description):
        '''Like :meth:`Result.scalar() <sqlalchemy.engine.Result.scalar>`, but aborts
        with a ``404 Not Found`` error instead of returning ``None``.

        :param statement: The ``select`` statement to execute.
        :param description: A custom message to show on the error page.

        .. versionadded:: 3.0
        '''
        value = self.session.execute(statement).scalar()
    # WARNING: Decompyle incomplete

    
    def one_or_404(self = None, statement = None, *, description):
        '''Like :meth:`Result.scalar_one() <sqlalchemy.engine.Result.scalar_one>`,
        but aborts with a ``404 Not Found`` error instead of raising ``NoResultFound``
        or ``MultipleResultsFound``.

        :param statement: The ``select`` statement to execute.
        :param description: A custom message to show on the error page.

        .. versionadded:: 3.0
        '''
        
        try:
            return self.session.execute(statement).scalar_one()
        except (sa_exc.NoResultFound, sa_exc.MultipleResultsFound):
            abort(404, description = description)
            return None


    
    def paginate(self = None, select = None, *, page, per_page, max_per_page, error_out, count):
        '''Apply an offset and limit to a select statment based on the current page and
        number of items per page, returning a :class:`.Pagination` object.

        The statement should select a model class, like ``select(User)``. This applies
        ``unique()`` and ``scalars()`` modifiers to the result, so compound selects will
        not return the expected results.

        :param select: The ``select`` statement to paginate.
        :param page: The current page, used to calculate the offset. Defaults to the
            ``page`` query arg during a request, or 1 otherwise.
        :param per_page: The maximum number of items on a page, used to calculate the
            offset and limit. Defaults to the ``per_page`` query arg during a request,
            or 20 otherwise.
        :param max_per_page: The maximum allowed value for ``per_page``, to limit a
            user-provided value. Use ``None`` for no limit. Defaults to 100.
        :param error_out: Abort with a ``404 Not Found`` error if no items are returned
            and ``page`` is not 1, or if ``page`` or ``per_page`` is less than 1, or if
            either are not ints.
        :param count: Calculate the total number of values by issuing an extra count
            query. For very complex queries this may be inaccurate or slow, so it can be
            disabled and set manually if necessary.

        .. versionchanged:: 3.0
            The ``count`` query is more efficient.

        .. versionadded:: 3.0
        '''
        return SelectPagination(select = select, session = self.session(), page = page, per_page = per_page, max_per_page = max_per_page, error_out = error_out, count = count)

    
    def _call_for_binds(self = None, bind_key = None, op_name = None):
        '''Call a method on each metadata.

        :meta private:

        :param bind_key: A bind key or list of keys. Defaults to all binds.
        :param op_name: The name of the method to call.

        .. versionchanged:: 3.0
            Renamed from ``_execute_for_all_tables``.
        '''
        if bind_key == '__all__':
            keys = list(self.metadatas)
    # WARNING: Decompyle incomplete

    
    def create_all(self = None, bind_key = None):
        '''Create tables that do not exist in the database by calling
        ``metadata.create_all()`` for all or some bind keys. This does not
        update existing tables, use a migration library for that.

        This requires that a Flask application context is active.

        :param bind_key: A bind key or list of keys to create the tables for. Defaults
            to all binds.

        .. versionchanged:: 3.0
            Renamed the ``bind`` parameter to ``bind_key``. Removed the ``app``
            parameter.

        .. versionchanged:: 0.12
            Added the ``bind`` and ``app`` parameters.
        '''
        self._call_for_binds(bind_key, 'create_all')

    
    def drop_all(self = None, bind_key = None):
        '''Drop tables by calling ``metadata.drop_all()`` for all or some bind keys.

        This requires that a Flask application context is active.

        :param bind_key: A bind key or list of keys to drop the tables from. Defaults to
            all binds.

        .. versionchanged:: 3.0
            Renamed the ``bind`` parameter to ``bind_key``. Removed the ``app``
            parameter.

        .. versionchanged:: 0.12
            Added the ``bind`` and ``app`` parameters.
        '''
        self._call_for_binds(bind_key, 'drop_all')

    
    def reflect(self = None, bind_key = None):
        '''Load table definitions from the database by calling ``metadata.reflect()``
        for all or some bind keys.

        This requires that a Flask application context is active.

        :param bind_key: A bind key or list of keys to reflect the tables from. Defaults
            to all binds.

        .. versionchanged:: 3.0
            Renamed the ``bind`` parameter to ``bind_key``. Removed the ``app``
            parameter.

        .. versionchanged:: 0.12
            Added the ``bind`` and ``app`` parameters.
        '''
        self._call_for_binds(bind_key, 'reflect')

    
    def _set_rel_query(self = None, kwargs = None):
        """Apply the extension's :attr:`Query` class as the default for relationships
        and backrefs.

        :meta private:
        """
        kwargs.setdefault('query_class', self.Query)
        if 'backref' in kwargs:
            backref = kwargs['backref']
            if isinstance(backref, str):
                backref = (backref, { })
            backref[1].setdefault('query_class', self.Query)
            return None

    
    def relationship(self = None, *args, **kwargs):
        """A :func:`sqlalchemy.orm.relationship` that applies this extension's
        :attr:`Query` class for dynamic relationships and backrefs.

        .. versionchanged:: 3.0
            The :attr:`Query` class is set on ``backref``.
        """
        self._set_rel_query(kwargs)
    # WARNING: Decompyle incomplete

    
    def dynamic_loader(self = None, argument = None, **kwargs):
        """A :func:`sqlalchemy.orm.dynamic_loader` that applies this extension's
        :attr:`Query` class for relationships and backrefs.

        .. versionchanged:: 3.0
            The :attr:`Query` class is set on ``backref``.
        """
        self._set_rel_query(kwargs)
    # WARNING: Decompyle incomplete

    
    def _relation(self = None, *args, **kwargs):
        """A :func:`sqlalchemy.orm.relationship` that applies this extension's
        :attr:`Query` class for dynamic relationships and backrefs.

        SQLAlchemy 2.0 removes this name, use ``relationship`` instead.

        :meta private:

        .. versionchanged:: 3.0
            The :attr:`Query` class is set on ``backref``.
        """
        self._set_rel_query(kwargs)
        f = sa_orm.relationship
    # WARNING: Decompyle incomplete

    
    def __getattr__(self = None, name = None):
        if name == 'relation':
            return self._relation
        if None == 'event':
            return sa_event
        if None.startswith('_'):
            raise AttributeError(name)
        for mod in (sa, sa_orm):
            if hasattr(mod, name):
                
                return None, getattr(mod, name)
            raise AttributeError(name)
