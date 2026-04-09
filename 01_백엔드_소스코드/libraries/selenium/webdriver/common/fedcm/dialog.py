# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dialog.pyc (Python 3.11)

from selenium.webdriver.common.fedcm.account import Account

class Dialog:
    '''Represents a FedCM dialog that can be interacted with.'''
    DIALOG_TYPE_ACCOUNT_LIST = 'AccountChooser'
    DIALOG_TYPE_AUTO_REAUTH = 'AutoReauthn'
    
    def __init__(self = None, driver = None):
        self._driver = driver

    type = (lambda self = None: self._driver.fedcm.dialog_type)()
    title = (lambda self = None: self._driver.fedcm.title)()
    subtitle = (lambda self = None: result = self._driver.fedcm.subtitleresult.get('subtitle') if result else None)()
    
    def get_accounts(self = None):
        '''Gets the list of accounts shown in the dialog.'''
        accounts = self._driver.fedcm.account_list
        return accounts()

    
    def select_account(self = None, index = None):
        '''Selects an account from the dialog by index.'''
        self._driver.fedcm.select_account(index)

    
    def accept(self = None):
        '''Clicks the continue button in the dialog.'''
        self._driver.fedcm.accept()

    
    def dismiss(self = None):
        '''Cancels/dismisses the dialog.'''
        self._driver.fedcm.dismiss()
