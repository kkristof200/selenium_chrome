# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
import time

# Pip
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from xpath_utils import XPathConditionEquals

# Local
from .builtin_addon_install_settings import BuiltinAddonInstallSettings

# -------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------- class: FoxyProxyAddonSettings ------------------------------------------------ #

class FoxyProxyAddonSettings(BuiltinAddonInstallSettings):

    # --------------------------------------------------- Public properties -------------------------------------------------- #

    _name = 'foxy_proxy'
    _id   = 'gcknhkkoolaabfmlnjonogaaifnjlfnp'


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def post_install_action(
        self,
        chrome,
    ) -> None:
        proxy = chrome.proxy

        if not proxy:
            return

        time.sleep(1)

        chrome.get('{}/options.html'.format(self.addon_url), force=True)

        if chrome.find_by('td', conditions=[XPathConditionEquals('text()', '{}:{}'.format(proxy.host, proxy.port))], timeout=2) is None:
            chrome.find_by('button', id='addNewProxy').click()

            chrome.find_by('input', id='proxyHost').send_keys(proxy.host)
            port_field = chrome.find_by('input', id='proxyPort')
            port_field.send_keys(Keys.BACKSPACE)
            port_field.send_keys(str(proxy.port))

            if proxy.needs_auth:
                chrome.find_by('input', name='username').send_keys(proxy.username)
                chrome.find_by('input', name='password').send_keys(proxy.password)
                chrome.find_by('input', name='passwordConfirm').send_keys(proxy.password)

            chrome.find_by('button', in_element=chrome.find_by('div', class_='ui-dialog-buttonset')).click()

            chrome.get('{}/options.html'.format(self.addon_url), force=True)
            time.sleep(1)

        select = Select(chrome.find_by('select', id='proxyModeGlobal'))
        select.select_by_index(1)


# -------------------------------------------------------------------------------------------------------------------------------- #