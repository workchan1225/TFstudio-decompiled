# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: params.pyc (Python 3.11)

import html
import inspect
import re
import reprlib
from collections import UserDict
from functools import lru_cache
from urllib.parse import quote
from sklearn.externals._numpydoc import docscrape
from sklearn.utils._repr_html.base import ReprHTMLMixin

def _generate_link_to_param_doc(estimator_class, param_name, doc_link):
    '''URL to the relevant section of the docstring using a Text Fragment

    https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Fragment/Text_fragments
    '''
    docstring = estimator_class.__doc__
# WARNING: Decompyle incomplete


def _read_params(name, value, non_default_params):
    """Categorizes parameters as 'default' or 'user-set' and formats their values.
    Escapes or truncates parameter values for display safety and readability.
    """
    name = html.escape(name)
    r = reprlib.Repr()
    r.maxlist = 2
    r.maxtuple = 1
    r.maxstring = 50
    cleaned_value = html.escape(r.repr(value))
    param_type = 'user-set' if name in non_default_params else 'default'
    return {
        'param_type': param_type,
        'param_name': name,
        'param_value': cleaned_value }

_scrape_estimator_docstring = (lambda docstring: docscrape.NumpyDocString(docstring))()

def _params_html_repr(params):
    '''Generate HTML representation of estimator parameters.

    Creates an HTML table with parameter names and values, wrapped in a
    collapsible details element. Parameters are styled differently based
    on whether they are default or user-set values.
    '''
    PARAMS_TABLE_TEMPLATE = '\n        <div class="estimator-table">\n            <details>\n                <summary>Parameters</summary>\n                <table class="parameters-table">\n                  <tbody>\n                    {rows}\n                  </tbody>\n                </table>\n            </details>\n        </div>\n    '
    PARAM_ROW_TEMPLATE = '\n        <tr class="{param_type}">\n            <td><i class="copy-paste-icon"\n                 onclick="copyToClipboard(\'{param_name}\',\n                          this.parentElement.nextElementSibling)"\n            ></i></td>\n            <td class="param">{param_display}</td>\n            <td class="value">{param_value}</td>\n        </tr>\n    '
    PARAM_AVAILABLE_DOC_LINK_TEMPLATE = '\n        <a class="param-doc-link"\n            rel="noreferrer" target="_blank" href="{link}">\n            {param_name}\n            <span class="param-doc-description">{param_description}</span>\n        </a>\n    '
    estimator_class_docs = inspect.getdoc(params.estimator_class)
    if estimator_class_docs:
        structured_docstring = _scrape_estimator_docstring(estimator_class_docs)
    rows = []
# WARNING: Decompyle incomplete


class ParamsDict(UserDict, ReprHTMLMixin):
    pass
# WARNING: Decompyle incomplete
