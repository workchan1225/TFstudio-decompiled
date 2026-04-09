# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _metadata_requests.pyc (Python 3.11)

'''
Metadata Routing Utility

In order to better understand the components implemented in this file, one
needs to understand their relationship to one another.

The only relevant public API for end users are the ``set_{method}_request`` methods,
e.g. ``estimator.set_fit_request(sample_weight=True)``. However, third-party
developers and users who implement custom meta-estimators, need to deal with
the objects implemented in this file.

The routing is coordinated by building ``MetadataRequest`` objects
for objects that consume metadata, and ``MetadataRouter`` objects for objects that
can route metadata, which are then aligned during a call to `process_routing()`. This
function returns a Bunch object (dictionary-like) with all the information on the
consumers and which metadata they had requested and the actual metadata values. A
routing method (such as `fit` in a meta-estimator) can now provide the metadata to the
relevant consuming method (such as `fit` in a sub-estimator).

The ``MetadataRequest`` and ``MetadataRouter`` objects are constructed via a
``get_metadata_routing`` method, which all scikit-learn estimators provide.
This method is automatically implemented via ``BaseEstimator`` for all simple
estimators, but needs a custom implementation for meta-estimators.

MetadataRequest
~~~~~~~~~~~~~~~

In non-routing consumers, the simplest case, e.g. ``SVM``, ``get_metadata_routing``
returns a ``MetadataRequest`` object  which is assigned to the consumer\'s
`_metadata_request` attribute. It stores which metadata is required by each method of
the consumer by including one ``MethodMetadataRequest`` per method in ``METHODS``
(e. g. ``fit``, ``score``, etc).

Users and developers almost never need to directly add a new ``MethodMetadataRequest``,
to the consumer\'s `_metadata_request` attribute, since these are generated
automatically. This attribute is modified while running `set_{method}_request` methods
(such as `set_fit_request()`), which adds the request via
`method_metadata_request.add_request(param=prop, alias=alias)`.

The ``alias`` in the ``add_request`` method has to be either a string (an alias),
or one of ``[True (requested), False (unrequested), None (error if passed)]``. There
are some other special values such as ``UNUSED`` and ``WARN`` which are used
for purposes such as warning of removing a metadata in a child class, but not
used by the end users.

MetadataRouter
~~~~~~~~~~~~~~

In routers (such as meta-estimators or multi metric scorers), ``get_metadata_routing``
returns a ``MetadataRouter`` object. It provides information about which method, from
the router object, calls which method in a consumer\'s object, and also, which metadata
had been requested by the consumer\'s methods, thus specifying how metadata is to be
passed. If a sub-estimator is a router as well, their routing information is also stored
in the meta-estimators router.

Conceptually, this information looks like:

```
{
    "sub_estimator1": (
        mapping=[(caller="fit", callee="transform"), ...],
        router=MetadataRequest(...),  # or another MetadataRouter
    ),
    ...
}
```

The `MetadataRouter` objects are never stored and are always recreated anew whenever
the object\'s `get_metadata_routing` method is called.

An object that is both a router and a consumer, e.g. a meta-estimator which
consumes ``sample_weight`` and routes ``sample_weight`` to its sub-estimators
also returns a ``MetadataRouter`` object. Its routing information includes both
information about what metadata is required by the object itself (added via
``MetadataRouter.add_self_request``), as well as the routing information for its
sub-estimators (added via ``MetadataRouter.add``).

Implementation Details
~~~~~~~~~~~~~~~~~~~~~~

To give the above representation some structure, we use the following objects:

- ``(caller=..., callee=...)`` is a namedtuple called ``MethodPair``.

- The list of ``MethodPair`` stored in the ``mapping`` field of a `RouterMappingPair` is
  a ``MethodMapping`` object.

- ``(mapping=..., router=...)`` is a namedtuple called ``RouterMappingPair``.

The ``set_{method}_request`` methods are dynamically generated for estimators
which inherit from ``BaseEstimator``. This is done by attaching instances
of the ``RequestMethod`` descriptor to classes, which is done in the
``_MetadataRequester`` class, and ``BaseEstimator`` inherits from this mixin.
This mixin also implements the ``get_metadata_routing``, which meta-estimators
need to override, but it works for simple consumers as is.
'''
import inspect
from collections import defaultdict, namedtuple
from copy import deepcopy
from typing import TYPE_CHECKING, Optional, Union
from warnings import warn
from sklearn import get_config
from sklearn.exceptions import UnsetMetadataPassedError
from sklearn.utils._bunch import Bunch
SIMPLE_METHODS = [
    'fit',
    'partial_fit',
    'predict',
    'predict_proba',
    'predict_log_proba',
    'decision_function',
    'score',
    'split',
    'transform',
    'inverse_transform']
COMPOSITE_METHODS = {
    'fit_transform': [
        'fit',
        'transform'],
    'fit_predict': [
        'fit',
        'predict'] }
METHODS = SIMPLE_METHODS + list(COMPOSITE_METHODS.keys())

def _routing_repr(obj):
    """Get a representation suitable for messages printed in the routing machinery.

    This is different than `repr(obj)`, since repr(estimator) can be verbose when
    there are many constructor arguments set by the user.

    This is most suitable for Scorers as it gives a nice representation of what they
    are. This is done by implementing a `_routing_repr` method on the object.

    Since the `owner` object could be the type name (str), we return that string if the
    given `obj` is a string, otherwise we return the object's type name.

    .. versionadded:: 1.8
    """
    
    try:
        return obj._routing_repr()
    except AttributeError:
        return 



def _routing_enabled():
    '''Return whether metadata routing is enabled.

    .. versionadded:: 1.3

    Returns
    -------
    enabled : bool
        Whether metadata routing is enabled. If the config is not set, it
        defaults to False.
    '''
    return get_config().get('enable_metadata_routing', False)


def _raise_for_params(params, owner, method, allow = (None,)):
    '''Raise an error if metadata routing is not enabled and params are passed.

    .. versionadded:: 1.4

    Parameters
    ----------
    params : dict
        The metadata passed to a method.

    owner : object
        The object to which the method belongs.

    method : str
        The name of the method, e.g. "fit".

    allow : list of str, default=None
        A list of parameters which are allowed to be passed even if metadata
        routing is not enabled.

    Raises
    ------
    ValueError
        If metadata routing is not enabled and params are passed.
    '''
    caller = f'''{_routing_repr(owner)}.{method}''' if method else _routing_repr(owner)
# WARNING: Decompyle incomplete


def _raise_for_unsupported_routing(obj, method, **kwargs):
    """Raise when metadata routing is enabled and metadata is passed.

    This is used in meta-estimators which have not implemented metadata routing
    to prevent silent bugs. There is no need to use this function if the
    meta-estimator is not accepting any metadata, especially in `fit`, since
    if a meta-estimator accepts any metadata, they would do that in `fit` as
    well.

    Parameters
    ----------
    obj : estimator
        The estimator for which we're raising the error.

    method : str
        The method where the error is raised.

    **kwargs : dict
        The metadata passed to the method.
    """
    kwargs = kwargs.items()()
    if _routing_enabled() or kwargs:
        cls_name = _routing_repr(obj)
        raise NotImplementedError(f'''{cls_name}.{method} cannot accept given metadata ({set(kwargs.keys())}) since metadata routing is not yet implemented for {cls_name}.''')
    return None


class _RoutingNotSupportedMixin:
    '''A mixin to be used to remove the default `get_metadata_routing`.

    This is used in meta-estimators where metadata routing is not yet
    implemented.

    This also makes it clear in our rendered documentation that this method
    cannot be used.
    '''
    
    def get_metadata_routing(self):
        '''Raise `NotImplementedError`.

        This estimator does not support metadata routing yet.'''
        raise NotImplementedError(f'''{_routing_repr(self)} has not implemented metadata routing yet.''')


UNUSED = '$UNUSED$'
WARN = '$WARN$'
UNCHANGED = '$UNCHANGED$'
VALID_REQUEST_VALUES = [
    False,
    True,
    None,
    UNUSED,
    WARN]

def request_is_alias(item):
