# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: shadowroot.pyc (Python 3.11)

from __future__ import annotations
from hashlib import md5 as md5_hash
from typing import TYPE_CHECKING
from selenium.common.exceptions import InvalidSelectorException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.command import Command
if TYPE_CHECKING:
    from selenium.webdriver.remote.webelement import WebElement

class ShadowRoot:
    
    def __init__(self = None, session = None, id_ = None):
        self.session = session
        self._id = id_

    
    def __eq__(self = None, other_shadowroot = None):
        return self._id == other_shadowroot._id

    
    def __hash__(self = None):
        return int(md5_hash(self._id.encode('utf-8')).hexdigest(), 16)

    
    def __repr__(self = None):
        return '<{0.__module__}.{0.__name__} (session="{1}", element="{2}")>'.format(type(self), self.session.session_id, self._id)

    id = (lambda self = None: self._id)()
    
    def find_element(self = None, by = None, value = None):
        '''Find an element inside a shadow root given a By strategy and locator.

        Args:
            by: The locating strategy to use. Default is `By.ID`. Supported values include:
                - By.ID: Locate by element ID.
                - By.NAME: Locate by the `name` attribute.
                - By.XPATH: Locate by an XPath expression.
                - By.CSS_SELECTOR: Locate by a CSS selector.
                - By.CLASS_NAME: Locate by the `class` attribute.
                - By.TAG_NAME: Locate by the tag name (e.g., "input", "button").
                - By.LINK_TEXT: Locate a link element by its exact text.
                - By.PARTIAL_LINK_TEXT: Locate a link element by partial text match.
            value: The locator value to use with the specified `by` strategy.

        Returns:
            The first matching `WebElement` found on the page.

        Example:
            >>> element = driver.find_element(By.ID, "foo")
        '''
        if by == By.ID:
            by = By.CSS_SELECTOR
            value = f'''[id="{value}"]'''
        elif by == By.CLASS_NAME:
            if value and (lambda .0: pass# WARNING: Decompyle incomplete
)(value.strip()()):
                raise InvalidSelectorException('Compound class names are not allowed.')
            by = By.CSS_SELECTOR
            value = f'''.{value}'''
        elif by == By.NAME:
            by = By.CSS_SELECTOR
            value = f'''[name="{value}"]'''
        return self._execute(Command.FIND_ELEMENT_FROM_SHADOW_ROOT, {
            'using': by,
            'value': value })['value']

    
    def find_elements(self = None, by = None, value = None):
        '''Find elements inside a shadow root given a By strategy and locator.

        Args:
            by: The locating strategy to use. Default is `By.ID`. Supported values include:
                - By.ID: Locate by element ID.
                - By.NAME: Locate by the `name` attribute.
                - By.XPATH: Locate by an XPath expression.
                - By.CSS_SELECTOR: Locate by a CSS selector.
                - By.CLASS_NAME: Locate by the `class` attribute.
                - By.TAG_NAME: Locate by the tag name (e.g., "input", "button").
                - By.LINK_TEXT: Locate a link element by its exact text.
                - By.PARTIAL_LINK_TEXT: Locate a link element by partial text match.
            value: The locator value to use with the specified `by` strategy.

        Returns:
            List of `WebElements` matching locator strategy found on the page.

        Example:
            >>> element = driver.find_elements(By.ID, "foo")
        '''
        if by == By.ID:
            by = By.CSS_SELECTOR
            value = f'''[id="{value}"]'''
        elif by == By.CLASS_NAME:
            if value and (lambda .0: pass# WARNING: Decompyle incomplete
)(value.strip()()):
                raise InvalidSelectorException('Compound class names are not allowed.')
            by = By.CSS_SELECTOR
            value = f'''.{value}'''
        elif by == By.NAME:
            by = By.CSS_SELECTOR
            value = f'''[name="{value}"]'''
        return self._execute(Command.FIND_ELEMENTS_FROM_SHADOW_ROOT, {
            'using': by,
            'value': value })['value']

    
    def _execute(self, command, params = (None,)):
        """Executes a command against the underlying HTML element.

        Args:
          command: The name of the command to _execute as a string.
          params: A dictionary of named parameters to send with the command.

        Returns:
          The command's JSON response loaded into a dictionary object.
        """
        if not params:
            params = { }
        params['shadowId'] = self._id
        return self.session.execute(command, params)
