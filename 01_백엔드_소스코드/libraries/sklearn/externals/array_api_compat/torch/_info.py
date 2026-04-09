# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _info.pyc (Python 3.11)

'''
Array API Inspection namespace

This is the namespace for inspection functions as defined by the array API
standard. See
https://data-apis.org/array-api/latest/API_specification/inspection.html for
more details.

'''
import torch
from functools import cache

class __array_namespace_info__:
    """
    Get the array API inspection namespace for PyTorch.

    The array API inspection namespace defines the following functions:

    - capabilities()
    - default_device()
    - default_dtypes()
    - dtypes()
    - devices()

    See
    https://data-apis.org/array-api/latest/API_specification/inspection.html
    for more details.

    Returns
    -------
    info : ModuleType
        The array API inspection namespace for PyTorch.

    Examples
    --------
    >>> info = xp.__array_namespace_info__()
    >>> info.default_dtypes()
    {'real floating': numpy.float64,
     'complex floating': numpy.complex128,
     'integral': numpy.int64,
     'indexing': numpy.int64}

    """
    __module__ = 'torch'
    
    def capabilities(self):
        '''
        Return a dictionary of array API library capabilities.

        The resulting dictionary has the following keys:

        - **"boolean indexing"**: boolean indicating whether an array library
          supports boolean indexing. Always ``True`` for PyTorch.

        - **"data-dependent shapes"**: boolean indicating whether an array
          library supports data-dependent output shapes. Always ``True`` for
          PyTorch.

        See
        https://data-apis.org/array-api/latest/API_specification/generated/array_api.info.capabilities.html
        for more details.

        See Also
        --------
        __array_namespace_info__.default_device,
        __array_namespace_info__.default_dtypes,
        __array_namespace_info__.dtypes,
        __array_namespace_info__.devices

        Returns
        -------
        capabilities : dict
            A dictionary of array API library capabilities.

        Examples
        --------
        >>> info = xp.__array_namespace_info__()
        >>> info.capabilities()
        {\'boolean indexing\': True,
         \'data-dependent shapes\': True,
         \'max dimensions\': 64}

        '''
        return {
            'boolean indexing': True,
            'data-dependent shapes': True,
            'max dimensions': 64 }

    
    def default_device(self):
        """
        The default device used for new PyTorch arrays.

        See Also
        --------
        __array_namespace_info__.capabilities,
        __array_namespace_info__.default_dtypes,
        __array_namespace_info__.dtypes,
        __array_namespace_info__.devices

        Returns
        -------
        device : Device
            The default device used for new PyTorch arrays.

        Examples
        --------
        >>> info = xp.__array_namespace_info__()
        >>> info.default_device()
        device(type='cpu')

        Notes
        -----
        This method returns the static default device when PyTorch is initialized.
        However, the *current* device used by creation functions (``empty`` etc.)
        can be changed at runtime.

        See Also
        --------
        https://github.com/data-apis/array-api/issues/835
        """
        return torch.device('cpu')

    
    def default_dtypes(self = None, *, device):
        """
        The default data types used for new PyTorch arrays.

        Parameters
        ----------
        device : Device, optional
            The device to get the default data types for.
            Unused for PyTorch, as all devices use the same default dtypes.

        Returns
        -------
        dtypes : dict
            A dictionary describing the default data types used for new PyTorch
            arrays.

        See Also
        --------
        __array_namespace_info__.capabilities,
        __array_namespace_info__.default_device,
        __array_namespace_info__.dtypes,
        __array_namespace_info__.devices

        Examples
        --------
        >>> info = xp.__array_namespace_info__()
        >>> info.default_dtypes()
        {'real floating': torch.float32,
         'complex floating': torch.complex64,
         'integral': torch.int64,
         'indexing': torch.int64}

        """
        default_floating = torch.get_default_dtype()
        default_complex = torch.complex64 if default_floating == torch.float32 else torch.complex128
        default_integral = torch.int64
        return {
            'real floating': default_floating,
            'complex floating': default_complex,
            'integral': default_integral,
            'indexing': default_integral }

    
    def _dtypes(self, kind):
        bool = torch.bool
        int8 = torch.int8
        int16 = torch.int16
        int32 = torch.int32
        int64 = torch.int64
        uint8 = torch.uint8
        float32 = torch.float32
        float64 = torch.float64
        complex64 = torch.complex64
        complex128 = torch.complex128
    # WARNING: Decompyle incomplete

    dtypes = (lambda self = cache, *, device: res = self._dtypes(kind)for k, v in res.copy().items():
torch.empty((0,), dtype = v, device = device)del res[k]res)()
    devices = (lambda self: try:
torch.device('notadevice')raise AssertionError('unreachable')except RuntimeError:
e = Nonedevices_names = e.args[0].split('Expected one of ')[1].split(' device type')[0].split(', ')e = Nonedel eexcept:
e = Nonedel edevices = []for device_name in devices_names:
i = 0a = torch.empty((0,), device = torch.device(device_name, index = i))if a.device in devices:
passelse:
devices.append(a.device)i += 1continuecontinuedevices)()
