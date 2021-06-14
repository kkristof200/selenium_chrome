# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional, List, Callable
import os

# Pip
from undetected_chromedriver.v2 import ChromeOptions

# Local
from .chrome_addon_install_settings import ChromeAddonInstallSettings

# -------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------ class: AddonManager ----------------------------------------------------- #

class AddonManager:

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        addons: Optional[List[ChromeAddonInstallSettings]] = None
    ):
        self.__addons = addons or []


    # --------------------------------------------------- Public properties -------------------------------------------------- #

    @property
    def addons(self) -> List[ChromeAddonInstallSettings]:
        return self.__addons


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def add_addon(
        self,
        addon: ChromeAddonInstallSettings
    ) -> None:
        self.__addons.append(addon)

    def add_addons_to_options(
        self,
        options: ChromeOptions
    ) -> ChromeOptions:
        options.add_argument(
            '--load-extension={}'.format(
                ','.join([
                    addon.path for addon in self.addons
                ])
            )
        )

        return options

    def run_post_install_calls(
        self,
        chrome # Chrome
    ) -> None:
        org_handle = chrome.driver.current_window_handle

        for addon in self.addons:
            addon.post_install_action(chrome)

        for handle in chrome.window_handles:
            if handle != org_handle:
                chrome.switch_to_window(handle)
                chrome.close()

        chrome.switch_to_window(org_handle)


# -------------------------------------------------------------------------------------------------------------------------------- #