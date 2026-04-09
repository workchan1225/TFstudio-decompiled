# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: estimator.pyc (Python 3.11)

import html
from contextlib import closing
from inspect import isclass
from io import StringIO
from pathlib import Path
from string import Template
from sklearn import config_context

class _IDCounter:
    '''Generate sequential ids with a prefix.'''
    
    def __init__(self, prefix):
        self.prefix = prefix
        self.count = 0

    
    def get_id(self):
        return f'''{self.prefix}-{self.count}'''



def _get_css_style():
    estimator_css_file = Path(__file__).parent / 'estimator.css'
    params_css_file = Path(__file__).parent / 'params.css'
    estimator_css = estimator_css_file.read_text(encoding = 'utf-8')
    params_css = params_css_file.read_text(encoding = 'utf-8')
    return f'''{estimator_css}\n{params_css}'''

_CONTAINER_ID_COUNTER = _IDCounter('sk-container-id')
_ESTIMATOR_ID_COUNTER = _IDCounter('sk-estimator-id')
_CSS_STYLE = _get_css_style()

class _VisualBlock:
    '''HTML Representation of Estimator

    Parameters
    ----------
    kind : {\'serial\', \'parallel\', \'single\'}
        kind of HTML block

    estimators : list of estimators or `_VisualBlock`s or a single estimator
        If kind != \'single\', then `estimators` is a list of
        estimators.
        If kind == \'single\', then `estimators` is a single estimator.

    names : list of str, default=None
        If kind != \'single\', then `names` corresponds to estimators.
        If kind == \'single\', then `names` is a single string corresponding to
        the single estimator.

    name_details : list of str, str, or None, default=None
        If kind != \'single\', then `name_details` corresponds to `names`.
        If kind == \'single\', then `name_details` is a single string
        corresponding to the single estimator.

    name_caption : str, default=None
        The caption below the name. `None` stands for no caption.
        Only active when kind == \'single\'.

    doc_link_label : str, default=None
        The label for the documentation link. If provided, the label would be
        "Documentation for {doc_link_label}". Otherwise it will look for `names`.
        Only active when kind == \'single\'.

    dash_wrapped : bool, default=True
        If true, wrapped HTML element will be wrapped with a dashed border.
        Only active when kind != \'single\'.
    '''
    
    def __init__(self, kind = None, estimators = {
        'names': None,
        'name_details': None,
        'name_caption': None,
        'doc_link_label': None,
        'dash_wrapped': True }, *, names, name_details, name_caption, doc_link_label, dash_wrapped):
        self.kind = kind
        self.estimators = estimators
        self.dash_wrapped = dash_wrapped
        self.name_caption = name_caption
        self.doc_link_label = doc_link_label
    # WARNING: Decompyle incomplete

    
    def _sk_visual_block_(self):
        return self



def _write_label_html(out, params, name, name_details, name_caption, doc_link_label, outer_class, inner_class, checked, doc_link, is_fitted_css_class, is_fitted_icon, param_prefix = (None, None, 'sk-label-container', 'sk-label', False, '', '', '', '')):
    '''Write labeled html with or without a dropdown with named details.

    Parameters
    ----------
    out : file-like object
        The file to write the HTML representation to.
    params: str
        If estimator has `get_params` method, this is the HTML representation
        of the estimator\'s parameters and their values. When the estimator
        does not have `get_params`, it is an empty string.
    name : str
        The label for the estimator. It corresponds either to the estimator class name
        for a simple estimator or in the case of a `Pipeline` and `ColumnTransformer`,
        it corresponds to the name of the step.
    name_details : str
        The details to show as content in the dropdown part of the toggleable label. It
        can contain information such as non-default parameters or column information for
        `ColumnTransformer`.
    name_caption : str, default=None
        The caption below the name. If `None`, no caption will be created.
    doc_link_label : str, default=None
        The label for the documentation link. If provided, the label would be
        "Documentation for {doc_link_label}". Otherwise it will look for `name`.
    outer_class : {"sk-label-container", "sk-item"}, default="sk-label-container"
        The CSS class for the outer container.
    inner_class : {"sk-label", "sk-estimator"}, default="sk-label"
        The CSS class for the inner container.
    checked : bool, default=False
        Whether the dropdown is folded or not. With a single estimator, we intend to
        unfold the content.
    doc_link : str, default=""
        The link to the documentation for the estimator. If an empty string, no link is
        added to the diagram. This can be generated for an estimator if it uses the
        `_HTMLDocumentationLinkMixin`.
    is_fitted_css_class : {"", "fitted"}
        The CSS class to indicate whether or not the estimator is fitted. The
        empty string means that the estimator is not fitted and "fitted" means that the
        estimator is fitted.
    is_fitted_icon : str, default=""
        The HTML representation to show the fitted information in the diagram. An empty
        string means that no information is shown.
    param_prefix : str, default=""
        The prefix to prepend to parameter names for nested estimators.
    '''
    out.write(f'''<div class="{outer_class}"><div class="{inner_class} {is_fitted_css_class} sk-toggleable">''')
    name = html.escape(name)
# WARNING: Decompyle incomplete


def _get_visual_block(estimator):
    '''Generate information about how to display an estimator.'''
    pass
# WARNING: Decompyle incomplete


def _write_estimator_html(out, estimator, estimator_label, estimator_label_details, is_fitted_css_class, is_fitted_icon, first_call, param_prefix = ('', False, '')):
    '''Write estimator to html in serial, parallel, or by itself (single).

    For multiple estimators, this function is called recursively.

    Parameters
    ----------
    out : file-like object
        The file to write the HTML representation to.
    estimator : estimator object
        The estimator to visualize.
    estimator_label : str
        The label for the estimator. It corresponds either to the estimator class name
        for simple estimator or in the case of `Pipeline` and `ColumnTransformer`, it
        corresponds to the name of the step.
    estimator_label_details : str
        The details to show as content in the dropdown part of the toggleable label.
        It can contain information as non-default parameters or column information for
        `ColumnTransformer`.
    is_fitted_css_class : {"", "fitted"}
        The CSS class to indicate whether or not the estimator is fitted or not. The
        empty string means that the estimator is not fitted and "fitted" means that the
        estimator is fitted.
    is_fitted_icon : str, default=""
        The HTML representation to show the fitted information in the diagram. An empty
        string means that no information is shown. If the estimator to be shown is not
        the first estimator (i.e. `first_call=False`), `is_fitted_icon` is always an
        empty string.
    first_call : bool, default=False
        Whether this is the first time this function is called.
    param_prefix : str, default=""
        The prefix to prepend to parameter names for nested estimators.
        For example, in a pipeline this might be "pipeline__stepname__".
    '''
    if first_call:
        est_block = _get_visual_block(estimator)
    else:
        is_fitted_icon = ''
        config_context(print_changed_only = True)
        est_block = _get_visual_block(estimator)
        None(None, None)
    with None:
        if not None:
            pass
    if hasattr(estimator, '_get_doc_link'):
        doc_link = estimator._get_doc_link()
    else:
        doc_link = ''
    if est_block.kind in ('serial', 'parallel'):
        if not first_call:
            dashed_wrapped = est_block.dash_wrapped
        dash_cls = ' sk-dashed-wrapped' if dashed_wrapped else ''
        out.write(f'''<div class="sk-item{dash_cls}">''')
        if estimator_label:
            if hasattr(estimator, 'get_params') and hasattr(estimator, '_get_params_html'):
                params = estimator._get_params_html(False, doc_link)._repr_html_inner()
            else:
                params = ''
            _write_label_html(out, params, estimator_label, estimator_label_details, doc_link = doc_link, is_fitted_css_class = is_fitted_css_class, is_fitted_icon = is_fitted_icon, param_prefix = param_prefix)
        kind = est_block.kind
        out.write(f'''<div class="sk-{kind}">''')
        est_infos = zip(est_block.estimators, est_block.names, est_block.name_details)
        for est, name, name_details in est_infos:
            if param_prefix and hasattr(name, 'split'):
                new_prefix = f'''{param_prefix}{name.split(':')[0]}__'''
            elif hasattr(name, 'split'):
                new_prefix = f'''{name.split(':')[0]}__''' if name else ''
            else:
                new_prefix = param_prefix
            if kind == 'serial':
                _write_estimator_html(out, est, name, name_details, is_fitted_css_class = is_fitted_css_class, param_prefix = new_prefix)
                continue
            out.write('<div class="sk-parallel-item">')
            serial_block = _VisualBlock('serial', [
                est], dash_wrapped = False)
            _write_estimator_html(out, serial_block, name, name_details, is_fitted_css_class = is_fitted_css_class, param_prefix = new_prefix)
            out.write('</div>')
            out.write('</div></div>')
            return None
            if est_block.kind == 'single':
                if hasattr(estimator, '_get_params_html'):
                    params = estimator._get_params_html(doc_link = doc_link)._repr_html_inner()
                else:
                    params = ''
                _write_label_html(out, params, est_block.names, est_block.name_details, est_block.name_caption, est_block.doc_link_label, outer_class = 'sk-item', inner_class = 'sk-estimator', checked = first_call, doc_link = doc_link, is_fitted_css_class = is_fitted_css_class, is_fitted_icon = is_fitted_icon, param_prefix = param_prefix)
                return None
            return None


def estimator_html_repr(estimator):
    """Build a HTML representation of an estimator.

    Read more in the :ref:`User Guide <visualizing_composite_estimators>`.

    Parameters
    ----------
    estimator : estimator object
        The estimator to visualize.

    Returns
    -------
    html: str
        HTML representation of estimator.

    Examples
    --------
    >>> from sklearn.utils._repr_html.estimator import estimator_html_repr
    >>> from sklearn.linear_model import LogisticRegression
    >>> estimator_html_repr(LogisticRegression())
    '<style>#sk-container-id...'
    """
    NotFittedError = NotFittedError
    import sklearn.exceptions
    check_is_fitted = check_is_fitted
    import sklearn.utils.validation
    if not hasattr(estimator, 'fit'):
        status_label = '<span>Not fitted</span>'
        is_fitted_css_class = ''
    else:
        
        try:
            check_is_fitted(estimator)
            status_label = '<span>Fitted</span>'
            is_fitted_css_class = 'fitted'
        except NotFittedError:
            status_label = '<span>Not fitted</span>'
            is_fitted_css_class = ''

        is_fitted_icon = f'''<span class="sk-estimator-doc-link {is_fitted_css_class}">i{status_label}</span>'''
        out = closing(StringIO())
        container_id = _CONTAINER_ID_COUNTER.get_id()
        style_template = Template(_CSS_STYLE)
        style_with_id = style_template.substitute(id = container_id)
        estimator_str = str(estimator)
        fallback_msg = 'In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.'
        html_template = f'''<style>{style_with_id}</style><body><div id="{container_id}" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>{html.escape(estimator_str)}</pre><b>{fallback_msg}</b></div><div class="sk-container" hidden>'''
        out.write(html_template)
        _write_estimator_html(out, estimator, estimator.__class__.__name__, estimator_str, first_call = True, is_fitted_css_class = is_fitted_css_class, is_fitted_icon = is_fitted_icon)
        f = open(str(Path(__file__).parent / 'estimator.js'), 'r')
        script = f.read()
        None(None, None)
    with None:
        if not None:
            pass
    html_end = f'''</div></div><script>{script}\nforceTheme(\'{container_id}\');</script></body>'''
    out.write(html_end)
    html_output = out.getvalue()
    None(None, None)
    return 
    with None:
        if not None, html_output:
            pass
