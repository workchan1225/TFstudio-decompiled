# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: webelement.pyc (Python 3.11)

from __future__ import annotations
import os
import pkgutil
import warnings
import zipfile
from abc import ABCMeta
from base64 import b64decode, encodebytes
from hashlib import md5 as md5_hash
from io import BytesIO
from selenium.common.exceptions import JavascriptException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.utils import keys_to_typing
from selenium.webdriver.remote.command import Command
from selenium.webdriver.remote.shadowroot import ShadowRoot
getAttribute_js = None
isDisplayed_js = None

def _load_js():
    global getAttribute_js, isDisplayed_js
    _pkg = '.'.join(__name__.split('.')[:-1])
    getAttribute_js = pkgutil.get_data(_pkg, 'getAttribute.js').decode('utf8')
    isDisplayed_js = pkgutil.get_data(_pkg, 'isDisplayed.js').decode('utf8')


def BaseWebElement():
    '''BaseWebElement'''
    __doc__ = "Abstract Base Class for WebElement.\n\n    ABC's will allow custom types to be registered as a WebElement to\n    pass type checks.\n    "

BaseWebElement = <NODE:27>(BaseWebElement, 'BaseWebElement', metaclass = ABCMeta)

class WebElement(BaseWebElement):
    '''Represents a DOM element.

    Generally, all interesting operations that interact with a document will be
    performed through this interface.

    All method calls will do a freshness check to ensure that the element
    reference is still valid.  This essentially determines whether the
    element is still attached to the DOM.  If this test fails, then an
    `StaleElementReferenceException` is thrown, and all future calls to this
    instance will fail.
    '''
    
    def __init__(self = None, parent = None, id_ = None):
        self._parent = parent
        self._id = id_

    
    def __repr__(self):
        return f'''<{type(self).__module__}.{type(self).__name__} (session="{self.session_id}", element="{self._id}")>'''

    session_id = (lambda self = None: self._parent.session_id)()
    tag_name = (lambda self = None: self._execute(Command.GET_ELEMENT_TAG_NAME)['value'])()
    text = (lambda self = None: self._execute(Command.GET_ELEMENT_TEXT)['value'])()
    
    def click(self = None):
        '''Clicks the element.

        Example:
            element = driver.find_element(By.ID, "foo")
            element.click()
        '''
        self._execute(Command.CLICK_ELEMENT)

    
    def submit(self = None):
        '''Submits a form.

        Example:
            form = driver.find_element(By.NAME, "login")
            form.submit()
        '''
        script = '/* submitForm */var form = arguments[0];\nwhile (form.nodeName != "FORM" && form.parentNode) {\n  form = form.parentNode;\n}\nif (!form) { throw Error(\'Unable to find containing form element\'); }\nif (!form.ownerDocument) { throw Error(\'Unable to find owning document\'); }\nvar e = form.ownerDocument.createEvent(\'Event\');\ne.initEvent(\'submit\', true, true);\nif (form.dispatchEvent(e)) { HTMLFormElement.prototype.submit.call(form) }\n'
        
        try:
            self._parent.execute_script(script, self)
            return None
        except JavascriptException:
            exc = None
            raise WebDriverException('To submit an element, it must be nested inside a form element'), exc
            exc = None
            del exc


    
    def clear(self = None):
        '''Clears the text if it\'s a text entry element.

        Example:
            text_field = driver.find_element(By.NAME, "username")
            text_field.clear()
        '''
        self._execute(Command.CLEAR_ELEMENT)

    
    def get_property(self = None, name = None):
        '''Gets the given property of the element.

        Args:
            name: Name of the property to retrieve.

        Returns:
            The value of the property.

        Example:
            text_length = target_element.get_property("text_length")
        '''
        
        try:
            return self._execute(Command.GET_ELEMENT_PROPERTY, {
                'name': name })['value']
        except WebDriverException:
            return 


    
    def get_dom_attribute(self = None, name = None):
        '''Get the HTML attribute value (not reflected properties) of the element.

        Returns only attributes declared in the element\'s HTML markup, unlike
        `selenium.webdriver.remote.BaseWebElement.get_attribute`.

        Args:
            name: Name of the attribute to retrieve.

        Returns:
            The value of the attribute.

        Example:
            text_length = target_element.get_dom_attribute("class")
        '''
        return self._execute(Command.GET_ELEMENT_ATTRIBUTE, {
            'name': name })['value']

    
    def get_attribute(self = None, name = None):
        '''Gets the given attribute or property of the element.

        This method will first try to return the value of a property with the
        given name. If a property with that name doesn\'t exist, it returns the
        value of the attribute with the same name. If there\'s no attribute with
        that name, ``None`` is returned.

        Values which are considered truthy, that is equals "true" or "false",
        are returned as booleans.  All other non-``None`` values are returned
        as strings.  For attributes or properties which do not exist, ``None``
        is returned.

        To obtain the exact value of the attribute or property,
        use :func:`~selenium.webdriver.remote.BaseWebElement.get_dom_attribute` or
        :func:`~selenium.webdriver.remote.BaseWebElement.get_property` methods respectively.

        Args:
            name: Name of the attribute/property to retrieve.

        Returns:
            The value of the attribute/property.

        Example:
            # Check if the "active" CSS class is applied to an element.
            is_active = "active" in target_element.get_attribute("class")
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def is_selected(self = None):
        '''Returns whether the element is selected.

        This method is generally used on checkboxes, options in a select
        and radio buttons.

        Example:
            is_selected = element.is_selected()
        '''
        return self._execute(Command.IS_ELEMENT_SELECTED)['value']

    
    def is_enabled(self = None):
        '''Returns whether the element is enabled.

        Example:
            is_enabled = element.is_enabled()
        '''
        return self._execute(Command.IS_ELEMENT_ENABLED)['value']

    
    def send_keys(self = None, *value):
        '''Simulates typing into the element.

        Use this to send simple key events or to fill out form fields.
        This can also be used to set file inputs.

        Args:
            value: A string for typing, or setting form fields. For setting
                file inputs, this could be a local file path.

        Examples:
            To send a simple key event::

            form_textfield = driver.find_element(By.NAME, "username")
            form_textfield.send_keys("admin")

            or to set a file input field::

            file_input = driver.find_element(By.NAME, "profilePic")
            file_input.send_keys("path/to/profilepic.gif")
            # Generally it\'s better to wrap the file path in one of the methods
            # in os.path to return the actual path to support cross OS testing.
            # file_input.send_keys(os.path.abspath("path/to/profilepic.gif"))
        '''
        pass
    # WARNING: Decompyle incomplete

    shadow_root = (lambda self = None: self._execute(Command.GET_SHADOW_ROOT)['value'])()
    
    def is_displayed(self = None):
        '''Whether the element is visible to a user.

        Example:
            is_displayed = element.is_displayed()
        '''
        pass
    # WARNING: Decompyle incomplete

    location_once_scrolled_into_view = (lambda self = None: old_loc = self._execute(Command.W3C_EXECUTE_SCRIPT, {
'script': 'arguments[0].scrollIntoView(true); return arguments[0].getBoundingClientRect()',
'args': [
self] })['value']{
'x': round(old_loc['x']),
'y': round(old_loc['y']) })()
    size = (lambda self = None: size = self._execute(Command.GET_ELEMENT_RECT)['value']new_size = {
'height': size['height'],
'width': size['width'] }new_size)()
    
    def value_of_css_property(self = None, property_name = None):
        '''Get the value of a CSS property.

        Args:
            property_name: The name of the CSS property to get the value of.

        Returns:
            The value of the CSS property.

        Example:
            value = element.value_of_css_property("color")
        '''
        return self._execute(Command.GET_ELEMENT_VALUE_OF_CSS_PROPERTY, {
            'propertyName': property_name })['value']

    location = (lambda self = None: old_loc = self._execute(Command.GET_ELEMENT_RECT)['value']new_loc = {
'x': round(old_loc['x']),
'y': round(old_loc['y']) }new_loc)()
    rect = (lambda self = None: self._execute(Command.GET_ELEMENT_RECT)['value'])()
    aria_role = (lambda self = None: self._execute(Command.GET_ELEMENT_ARIA_ROLE)['value'])()
    accessible_name = (lambda self = None: self._execute(Command.GET_ELEMENT_ARIA_LABEL)['value'])()
    screenshot_as_base64 = (lambda self = None: self._execute(Command.ELEMENT_SCREENSHOT)['value'])()
    screenshot_as_png = (lambda self = None: b64decode(self.screenshot_as_base64.encode('ascii')))()
    
    def screenshot(self = None, filename = None):
        '''Save a PNG screenshot of the current element to a file.

        Use full paths in your filename.

        Args:
            filename: The full path you wish to save your screenshot to. This
                should end with a `.png` extension.

        Returns:
            True if the screenshot was saved successfully, False otherwise.

        Example:
            element.screenshot("/Screenshots/foo.png")
        '''
        if not filename.lower().endswith('.png'):
            warnings.warn('name used for saved screenshot does not match file type. It should end with a `.png` extension', UserWarning)
        png = self.screenshot_as_png
        
        try:
            f = open(filename, 'wb')
            f.write(png)
            
            try:
                None(None, None)
            with None:
                if not None:
                    
                    try:
                        
                        try:
                            
                            try:
                                pass
                            except OSError:
                                
                                try:
                                    del png
                                    return False
                                    
                                    try:
                                        del png
                                    except:
                                        del png

                                    return True







    parent = (lambda self: self._parent)()
    id = (lambda self = None: self._id)()
    
    def __eq__(self, element):
