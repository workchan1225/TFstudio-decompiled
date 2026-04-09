# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fedcm.pyc (Python 3.11)

from selenium.webdriver.remote.command import Command

class FedCM:
    
    def __init__(self = None, driver = None):
        self._driver = driver

    title = (lambda self = None: self._driver.execute(Command.GET_FEDCM_TITLE)['value'].get('title'))()
    subtitle = (lambda self = None: self._driver.execute(Command.GET_FEDCM_TITLE)['value'].get('subtitle'))()
    dialog_type = (lambda self = None: self._driver.execute(Command.GET_FEDCM_DIALOG_TYPE).get('value'))()
    account_list = (lambda self = None: self._driver.execute(Command.GET_FEDCM_ACCOUNT_LIST).get('value'))()
    
    def select_account(self = None, index = None):
        '''Selects an account from the dialog by index.'''
        self._driver.execute(Command.SELECT_FEDCM_ACCOUNT, {
            'accountIndex': index })

    
    def accept(self = None):
        '''Clicks the continue button in the dialog.'''
        self._driver.execute(Command.CLICK_FEDCM_DIALOG_BUTTON, {
            'dialogButton': 'ConfirmIdpLoginContinue' })

    
    def dismiss(self = None):
        '''Cancels/dismisses the FedCM dialog.'''
        self._driver.execute(Command.CANCEL_FEDCM_DIALOG)

    
    def enable_delay(self = None):
        '''Re-enables the promise rejection delay for FedCM.'''
        self._driver.execute(Command.SET_FEDCM_DELAY, {
            'enabled': True })

    
    def disable_delay(self = None):
        '''Disables the promise rejection delay for FedCM.'''
        self._driver.execute(Command.SET_FEDCM_DELAY, {
            'enabled': False })

    
    def reset_cooldown(self = None):
        '''Resets the FedCM dialog cooldown, allowing immediate retriggers.'''
        self._driver.execute(Command.RESET_FEDCM_COOLDOWN)
