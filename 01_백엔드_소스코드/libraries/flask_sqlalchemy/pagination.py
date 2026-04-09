# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pagination.pyc (Python 3.11)

from __future__ import annotations
import typing as t
from math import ceil
import sqlalchemy as sa
from sqlalchemy.orm import orm as sa_orm
from flask import abort
from flask import request

class Pagination:
    """Apply an offset and limit to the query based on the current page and number of
    items per page.

    Don't create pagination objects manually. They are created by
    :meth:`.SQLAlchemy.paginate` and :meth:`.Query.paginate`.

    This is a base class, a subclass must implement :meth:`_query_items` and
    :meth:`_query_count`. Those methods will use arguments passed as ``kwargs`` to
    perform the queries.

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
    :param kwargs: Information about the query to paginate. Different subclasses will
        require different arguments.

    .. versionchanged:: 3.0
        Iterating over a pagination object iterates over its items.

    .. versionchanged:: 3.0
        Creating instances manually is not a public API.
    """
    
    def __init__(self, page = None, per_page = None, max_per_page = None, error_out = (None, None, 100, True, True), count = ('page', 'int | None', 'per_page', 'int | None', 'max_per_page', 'int | None', 'error_out', 'bool', 'count', 'bool', 'kwargs', 't.Any', 'return', 'None'), **kwargs):
        self._query_args = kwargs
        (page, per_page) = self._prepare_page_args(page = page, per_page = per_page, max_per_page = max_per_page, error_out = error_out)
        self.page = page
        self.per_page = per_page
        self.max_per_page = max_per_page
        items = self._query_items()
        if items and page != 1 and error_out:
            abort(404)
        self.items = items
        if count:
            total = self._query_count()
        else:
            total = None
        self.total = total

    _prepare_page_args = (lambda *: pass# WARNING: Decompyle incomplete
)()
    _query_offset = (lambda self = None: (self.page - 1) * self.per_page)()
    
    def _query_items(self = None):
        '''Execute the query to get the items on the current page.

        Uses init arguments stored in :attr:`_query_args`.

        :meta private:

        .. versionadded:: 3.0
        '''
        raise NotImplementedError

    
    def _query_count(self = None):
        '''Execute the query to get the total number of items.

        Uses init arguments stored in :attr:`_query_args`.

        :meta private:

        .. versionadded:: 3.0
        '''
        raise NotImplementedError

    first = (lambda self = None: if len(self.items) == 0:
0(None.page - 1) * self.per_page + 1)()
    last = (lambda self = None: first = self.firstmax(first, first + len(self.items) - 1))()
    pages = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    has_prev = (lambda self = None: self.page > 1)()
    prev_num = (lambda self = None: if not self.has_prev:
NoneNone.page - 1)()
    
    def prev(self = None, *, error_out):
        '''Query the :class:`Pagination` object for the previous page.

        :param error_out: Abort with a ``404 Not Found`` error if no items are returned
            and ``page`` is not 1, or if ``page`` or ``per_page`` is less than 1, or if
            either are not ints.
        '''
        pass
    # WARNING: Decompyle incomplete

    has_next = (lambda self = None: self.page < self.pages)()
    next_num = (lambda self = None: if not self.has_next:
NoneNone.page + 1)()
    
    def next(self = None, *, error_out):
        '''Query the :class:`Pagination` object for the next page.

        :param error_out: Abort with a ``404 Not Found`` error if no items are returned
            and ``page`` is not 1, or if ``page`` or ``per_page`` is less than 1, or if
            either are not ints.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def iter_pages(self = None, *, left_edge, left_current, right_current, right_edge):
        '''Yield page numbers for a pagination widget. Skipped pages between the edges
        and middle are represented by a ``None``.

        For example, if there are 20 pages and the current page is 7, the following
        values are yielded.

        .. code-block:: python

            1, 2, None, 5, 6, 7, 8, 9, 10, 11, None, 19, 20

        :param left_edge: How many pages to show from the first page.
        :param left_current: How many pages to show left of the current page.
        :param right_current: How many pages to show right of the current page.
        :param right_edge: How many pages to show from the last page.

        .. versionchanged:: 3.0
            Improved efficiency of calculating what to yield.

        .. versionchanged:: 3.0
            ``right_current`` boundary is inclusive.

        .. versionchanged:: 3.0
            All parameters are keyword-only.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete



class SelectPagination(Pagination):
    '''Returned by :meth:`.SQLAlchemy.paginate`. Takes ``select`` and ``session``
    arguments in addition to the :class:`Pagination` arguments.

    .. versionadded:: 3.0
    '''
    
    def _query_items(self = None):
        select = self._query_args['select']
        select = select.limit(self.per_page).offset(self._query_offset)
        session = self._query_args['session']
        return list(session.execute(select).unique().scalars())

    
    def _query_count(self = None):
        select = self._query_args['select']
        sub = select.options(sa_orm.lazyload('*')).order_by(None).subquery()
        session = self._query_args['session']
        out = session.execute(sa.select(sa.func.count()).select_from(sub)).scalar()
        return out



class QueryPagination(Pagination):
    '''Returned by :meth:`.Query.paginate`. Takes a ``query`` argument in addition to
    the :class:`Pagination` arguments.

    .. versionadded:: 3.0
    '''
    
    def _query_items(self = None):
        query = self._query_args['query']
        out = query.limit(self.per_page).offset(self._query_offset).all()
        return out

    
    def _query_count(self = None):
        out = self._query_args['query'].order_by(None).count()
        return out
