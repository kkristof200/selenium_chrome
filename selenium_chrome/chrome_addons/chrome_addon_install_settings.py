# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# Pip
from selenium_browser import AddonInstallSettings

# -------------------------------------------------------------------------------------------------------------------------------- #



# ----------------------------------------------- class: ChromeAddonInstallSettings ---------------------------------------------- #

class ChromeAddonInstallSettings(AddonInstallSettings):

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        path: str, # path to extracted extension folder, NOT .crx (this is a limitation by undetected-chromedriver)
        addon_id: str
    ):
        super().__init__(path)

        self.addon_id = addon_id
        self.addon_url = 'chrome-extension://{}'.format(addon_id)


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def post_install_action(
        self,
        browser,#: Chrome
    ) -> None:
        return None


# -------------------------------------------------------------------------------------------------------------------------------- #