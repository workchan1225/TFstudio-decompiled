# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: print_page_options.pyc (Python 3.11)

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Literal, TypedDict
    Orientation = Literal[('portrait', 'landscape')]
    
    def _MarginOpts():
        '''_MarginOpts'''
        bottom: float = '_MarginOpts'

    _MarginOpts = <NODE:27>(_MarginOpts, '_MarginOpts', TypedDict, total = False)
    
    def _PageOpts():
        '''_PageOpts'''
        height: float = '_PageOpts'

    _PageOpts = <NODE:27>(_PageOpts, '_PageOpts', TypedDict, total = False)
    
    def _PrintOpts():
        '''_PrintOpts'''
        pageRanges: list[str] = '_PrintOpts'

    _PrintOpts = <NODE:27>(_PrintOpts, '_PrintOpts', TypedDict, total = False)
else:
    from typing import Any
    Orientation = str
    _MarginOpts = dict[(str, Any)]
    _PageOpts = dict[(str, Any)]
    _PrintOpts = dict[(str, Any)]

class _PageSettingsDescriptor:
    """Descriptor which validates `height` and 'width' of page."""
    
    def __init__(self, name):
        self.name = name

    
    def __get__(self = None, obj = None, cls = None):
        return obj._page.get(self.name, None)

    
    def __set__(self = None, obj = None, value = None):
        getattr(obj, '_validate_num_property')(self.name, value)
        obj._page[self.name] = value
        obj._print_options['page'] = obj._page



class _MarginSettingsDescriptor:
    '''Descriptor which validates below attributes.

    - top
    - bottom
    - left
    - right
    '''
    
    def __init__(self, name):
        self.name = name

    
    def __get__(self = None, obj = None, cls = None):
        return obj._margin.get(self.name, None)

    
    def __set__(self = None, obj = None, value = None):
        getattr(obj, '_validate_num_property')(f'''Margin {self.name}''', value)
        obj._margin[self.name] = value
        obj._print_options['margin'] = obj._margin



class _ScaleDescriptor:
    '''Scale descriptor which validates scale.'''
    
    def __init__(self, name):
        self.name = name

    
    def __get__(self = None, obj = None, cls = None):
        return obj._print_options.get(self.name)

    
    def __set__(self = None, obj = None, value = None):
        getattr(obj, '_validate_num_property')(self.name, value)
        if value < 0.1 or value > 2:
            raise ValueError('Value of scale should be between 0.1 and 2')
        obj._print_options[self.name] = value



class _PageOrientationDescriptor:
    '''PageOrientation descriptor which validates orientation of page.'''
    ORIENTATION_VALUES = [
        'portrait',
        'landscape']
    
    def __init__(self, name):
        self.name = name

    
    def __get__(self = None, obj = None, cls = None):
        return obj._print_options.get(self.name, None)

    
    def __set__(self = None, obj = None, value = None):
        if value not in self.ORIENTATION_VALUES:
            raise ValueError(f'''Orientation value must be one of {self.ORIENTATION_VALUES}''')
        obj._print_options[self.name] = value



class _ValidateTypeDescriptor:
    '''Base Class Descriptor which validates type of any subclass attribute.'''
    
    def __init__(self = None, name = None, expected_type = None):
        self.name = name
        self.expected_type = expected_type

    
    def __get__(self, obj, cls):
        return obj._print_options.get(self.name, None)

    
    def __set__(self = None, obj = None, value = None):
        if not isinstance(value, self.expected_type):
            raise ValueError(f'''{self.name} should be of type {self.expected_type.__name__}''')
        obj._print_options[self.name] = value



class _ValidateBackGround(_ValidateTypeDescriptor):
    pass
# WARNING: Decompyle incomplete


class _ValidateShrinkToFit(_ValidateTypeDescriptor):
    pass
# WARNING: Decompyle incomplete


class _ValidatePageRanges(_ValidateTypeDescriptor):
    pass
# WARNING: Decompyle incomplete


class PrintOptions:
    page_height = _PageSettingsDescriptor('height')
    page_width = _PageSettingsDescriptor('width')
    margin_top = _MarginSettingsDescriptor('top')
    margin_bottom = _MarginSettingsDescriptor('bottom')
    margin_left = _MarginSettingsDescriptor('left')
    margin_right = _MarginSettingsDescriptor('right')
    scale = _ScaleDescriptor('scale')
    orientation = _PageOrientationDescriptor('orientation')
    background = _ValidateBackGround('background')
    shrink_to_fit = _ValidateShrinkToFit('shrinkToFit')
    page_ranges = _ValidatePageRanges('pageRanges')
    A4 = {
        'height': 29.7,
        'width': 21 }
    LEGAL = {
        'height': 35.56,
        'width': 21.59 }
    LETTER = {
        'height': 27.94,
        'width': 21.59 }
    TABLOID = {
        'height': 43.18,
        'width': 27.94 }
    
    def __init__(self = None):
        self._print_options = { }
        self._page = {
            'height': PrintOptions.A4['height'],
            'width': PrintOptions.A4['width'] }
        self._margin = { }

    
    def to_dict(self = None):
        '''Returns a hash of print options configured.'''
        return self._print_options

    
    def set_page_size(self = None, page_size = None):
        '''Sets the page size to predefined or custom dimensions.

        Args:
            page_size: A dictionary containing \'height\' and \'width\' keys with
                respective values in cm.

        Example:
            self.set_page_size(PageSize.A4)  # A4 predefined size
            self.set_page_size({"height": 15.0, "width": 20.0})  # Custom size
        '''
        self._validate_num_property('height', page_size['height'])
        self._validate_num_property('width', page_size['width'])
        self._page['height'] = page_size['height']
        self._page['width'] = page_size['width']
        self._print_options['page'] = self._page

    
    def _validate_num_property(self = None, property_name = None, value = None):
        '''Helper function to validate some of the properties.'''
        if not isinstance(value, (int, float)):
            raise ValueError(f'''{property_name} should be an integer or a float''')
        if value < 0:
            raise ValueError(f'''{property_name} cannot be less than 0''')
