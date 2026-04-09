# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: desired_capabilities.pyc (Python 3.11)

'''The Desired Capabilities implementation.'''

class DesiredCapabilities:
    '''Set of default supported desired capabilities.

    Use this as a starting point for creating a desired capabilities object for
    requesting remote webdrivers for connecting to selenium server or selenium grid.

    Usage Example::

        from selenium import webdriver
        from selenium.webdriver.firefox.options import Options

        selenium_grid_url = "http://198.0.0.1:4444/wd/hub"

        # Create a new Options object for the desired browser.
        options = Options()
        options.set_capability("platformName", "windows")
        options.browser_version = "142"

        # Instantiate an instance of Remote WebDriver with the new options.
        driver = webdriver.Remote(command_executor=selenium_grid_url, options=options)
    '''
    FIREFOX = {
        'browserName': 'firefox',
        'acceptInsecureCerts': True,
        'moz:debuggerAddress': True }
    INTERNETEXPLORER = {
        'browserName': 'internet explorer',
        'platformName': 'windows' }
    EDGE = {
        'browserName': 'MicrosoftEdge' }
    CHROME = {
        'browserName': 'chrome' }
    SAFARI = {
        'browserName': 'safari',
        'platformName': 'mac' }
    HTMLUNIT = {
        'browserName': 'htmlunit',
        'version': '',
        'platform': 'ANY' }
    HTMLUNITWITHJS = {
        'browserName': 'htmlunit',
        'version': 'firefox',
        'platform': 'ANY',
        'javascriptEnabled': True }
    IPHONE = {
        'browserName': 'iPhone',
        'version': '',
        'platform': 'mac' }
    IPAD = {
        'browserName': 'iPad',
        'version': '',
        'platform': 'mac' }
    WEBKITGTK = {
        'browserName': 'MiniBrowser' }
    WPEWEBKIT = {
        'browserName': 'MiniBrowser' }
