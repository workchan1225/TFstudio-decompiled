# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: plotgrid.pyc (Python 3.11)

from sympy.external import import_module


base_backend
{
    ('PlotGrid',): [
        'matplotlib'] } = import sympy.plotting.backends.base_backend, plotting, backends

class PlotGrid:
    """This class helps to plot subplots from already created SymPy plots
    in a single figure.

    Examples
    ========

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

        >>> from sympy import symbols
        >>> from sympy.plotting import plot, plot3d, PlotGrid
        >>> x, y = symbols('x, y')
        >>> p1 = plot(x, x**2, x**3, (x, -5, 5))
        >>> p2 = plot((x**2, (x, -6, 6)), (x, (x, -5, 5)))
        >>> p3 = plot(x**3, (x, -5, 5))
        >>> p4 = plot3d(x*y, (x, -5, 5), (y, -5, 5))

    Plotting vertically in a single line:

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

        >>> PlotGrid(2, 1, p1, p2)
        PlotGrid object containing:
        Plot[0]:Plot object containing:
        [0]: cartesian line: x for x over (-5.0, 5.0)
        [1]: cartesian line: x**2 for x over (-5.0, 5.0)
        [2]: cartesian line: x**3 for x over (-5.0, 5.0)
        Plot[1]:Plot object containing:
        [0]: cartesian line: x**2 for x over (-6.0, 6.0)
        [1]: cartesian line: x for x over (-5.0, 5.0)

    Plotting horizontally in a single line:

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

        >>> PlotGrid(1, 3, p2, p3, p4)
        PlotGrid object containing:
        Plot[0]:Plot object containing:
        [0]: cartesian line: x**2 for x over (-6.0, 6.0)
        [1]: cartesian line: x for x over (-5.0, 5.0)
        Plot[1]:Plot object containing:
        [0]: cartesian line: x**3 for x over (-5.0, 5.0)
        Plot[2]:Plot object containing:
        [0]: cartesian surface: x*y for x over (-5.0, 5.0) and y over (-5.0, 5.0)

    Plotting in a grid form:

    .. plot::
       :context: close-figs
       :format: doctest
       :include-source: True

        >>> PlotGrid(2, 2, p1, p2, p3, p4)
        PlotGrid object containing:
        Plot[0]:Plot object containing:
        [0]: cartesian line: x for x over (-5.0, 5.0)
        [1]: cartesian line: x**2 for x over (-5.0, 5.0)
        [2]: cartesian line: x**3 for x over (-5.0, 5.0)
        Plot[1]:Plot object containing:
        [0]: cartesian line: x**2 for x over (-6.0, 6.0)
        [1]: cartesian line: x for x over (-5.0, 5.0)
        Plot[2]:Plot object containing:
        [0]: cartesian line: x**3 for x over (-5.0, 5.0)
        Plot[3]:Plot object containing:
        [0]: cartesian surface: x*y for x over (-5.0, 5.0) and y over (-5.0, 5.0)

    """
    
    def __init__(self, nrows = None, ncolumns = {
        'show': True,
        'size': None }, *, show, size, *args, **kwargs):
        '''
        Parameters
        ==========

        nrows :
            The number of rows that should be in the grid of the
            required subplot.
        ncolumns :
            The number of columns that should be in the grid
            of the required subplot.

        nrows and ncolumns together define the required grid.

        Arguments
        =========

        A list of predefined plot objects entered in a row-wise sequence
        i.e. plot objects which are to be in the top row of the required
        grid are written first, then the second row objects and so on

        Keyword arguments
        =================

        show : Boolean
            The default value is set to ``True``. Set show to ``False`` and
            the function will not display the subplot. The returned instance
            of the ``PlotGrid`` class can then be used to save or display the
            plot by calling the ``save()`` and ``show()`` methods
            respectively.
        size : (float, float), optional
            A tuple in the form (width, height) in inches to specify the size of
            the overall figure. The default value is set to ``None``, meaning
            the size will be set by the default backend.
        '''
        self.matplotlib = import_module('matplotlib', import_kwargs = {
            'fromlist': [
                'pyplot',
                'cm',
                'collections'] }, min_module_version = '1.1.0', catch = (RuntimeError,))
        self.nrows = nrows
        self.ncolumns = ncolumns
        self._series = []
        self._fig = None
        self.args = args
        for arg in args:
            self._series.append(arg._series)
            self.size = size
            if show or self.matplotlib:
                self.show()
                return None
            return None
            return None

    
    def _create_figure(self):
        gs = self.matplotlib.gridspec.GridSpec(self.nrows, self.ncolumns)
        mapping = { }
        c = 0
        for i in range(self.nrows):
            for j in range(self.ncolumns):
                if c < len(self.args):
                    mapping[gs[(i, j)]] = self.args[c]
                c += 1
        kw = { } if not self.size else {
            'figsize': self.size }
    # WARNING: Decompyle incomplete

    fig = (lambda self: if not self._fig:
self._create_figure()self._fig)()
    _backend = (lambda self: self)()
    
    def close(self):
        self.matplotlib.pyplot.close(self.fig)

    
    def show(self):
        if base_backend._show:
            self.fig.tight_layout()
            self.matplotlib.pyplot.show()
            return None
        None.close()

    
    def save(self, path):
        self.fig.savefig(path)

    
    def __str__(self):
        plot_strs = enumerate(self.args)()
        return 'PlotGrid object containing:\n' + '\n'.join(plot_strs)
