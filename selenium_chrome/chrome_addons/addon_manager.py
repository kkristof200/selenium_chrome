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
        for addon in self.addons:
            options.add_extension(addon.path)

        return options

    def run_post_install_calls(
        self,
        chrome # Chrome
    ) -> None:
        for addon in self.addons:
            addon.post_install_action(chrome)


# -------------------------------------------------------------------------------------------------------------------------------- #