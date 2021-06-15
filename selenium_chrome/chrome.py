# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional, Union, List, Tuple
import os, shutil, time

# Pip
from undetected_chromedriver.v2 import Chrome as ChromeDriver

from noraise import noraise
from kproxy import Proxy
from selenium_browser import Browser, Utils as BrowserUtils

# Local
from .chrome_addons import AddonManager, FoxyProxyAddonSettings, ChromeAddonInstallSettings

from .__constants import Constants
from .__utils import Utils

# -------------------------------------------------------------------------------------------------------------------------------- #



# --------------------------------------------------------- class: Chrome -------------------------------------------------------- #

class Chrome(Browser):

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        
        # profile
        profile_path: Optional[str] = None,
        profile_id: Optional[str] = None,

        # cookies
        pickle_cookies: bool = False,

        # proxy
        proxy: Optional[Union[Proxy, str]] = None,

        # addons
        addon_settings: Optional[List[ChromeAddonInstallSettings]] = None,

        # other paths
        chromedriver_path: Optional[str] = None,

        # chrome option settings
        private: bool = False,
        full_screen: bool = True,
        language: str = 'en-us',
        user_agent: Optional[str] = None,
        disable_images: bool = False,
        mute_audio: bool = False,

        screen_size: Optional[Tuple[int, int]] = None, # (width, height)
        headless: bool = False,
        home_page_url: Optional[str] = None,

        # selenium-wire support
        webdriver_class: Optional = None,

        # find function
        default_find_func_timeout: int = 2.5
    ):
        '''EITHER PROVIDE 'profile_id' OR  'profile_path'.
           webdriver_class: override class used to create webdriver (for example: seleniumwire.webdriver.Chrome), Defaults to: 'undetected_chromedriver.v2.Chrome'
        '''

        proxy = BrowserUtils.proxy(proxy)
        profile_path, cookies_folder_path, user_agent_file_path = BrowserUtils.get_cache_paths(profile_path, profile_id)
        os.makedirs(cookies_folder_path, exist_ok=True)

        self.source_profile_path = profile_path

        am = AddonManager(addon_settings)

        if proxy and proxy.needs_auth:
            am.add_addon(FoxyProxyAddonSettings())

        options = am.add_addons_to_options(
            Utils.options(
                user_agent=BrowserUtils.user_agent(
                    user_agent=user_agent,
                    file_path=user_agent_file_path
                ),
                language=language,
                private=private,
                disable_images=disable_images,
                mute_audio=mute_audio,
                proxy=proxy if proxy and not proxy.needs_auth else None,
                profile_path=profile_path,

                screen_size=screen_size or (1920,1080),
                full_screen=full_screen,
                headless=headless,
                home_page_url=home_page_url
            )
        )

        super().__init__(
            webdriver_class or ChromeDriver,
            cookies_folder_path=cookies_folder_path,
            pickle_cookies=pickle_cookies,
            proxy=proxy,
            default_find_func_timeout=default_find_func_timeout,
            webdriver_executable_path=chromedriver_path,
            options=options
        )

        am.run_post_install_calls(self)


# -------------------------------------------------------------------------------------------------------------------------------- #