# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from  typing import Optional, Tuple, Union
import os, subprocess

# Pip
from kproxy import Proxy

from selenium.webdriver.chrome.options import Options as ChromeOptions

from undetected_chromedriver.v2 import Chrome as ChromeDriver

# -------------------------------------------------------------------------------------------------------------------------------- #



# --------------------------------------------------------- class: Utils --------------------------------------------------------- #

class Utils:

    # ---------------------------------------------------- Public methods ---------------------------------------------------- #
    
    @staticmethod
    def get_chromedriver_main_version(
        chromedriver_class,
        chromedriver_path: Optional[str],
        update_chromedriver: bool
    ) -> Optional[int]:
        if update_chromedriver and (chromedriver_class != ChromeDriver or not chromedriver_path or not os.path.exists(chromedriver_path)):
            return None

        try:
            version_response = subprocess.getoutput(f'"{chromedriver_path}" --version')

            return int(version_response.split(' ', 1)[1].split('.')[0])
        except:
            return None
        
        
    @staticmethod
    def proxy(
        proxy: Optional[Union[Proxy, str]] = None,

        # proxy - legacy (kept for convenience)
        host: Optional[str] = None,
        port: Optional[int] = None,
    ) -> Optional[Proxy]:
        if not proxy:
            if not host and not port:
                return None

            proxy = Proxy(host=host, port=port)

        return proxy if isinstance(proxy, Proxy) else Proxy.from_str(proxy)

    @staticmethod
    def options(
        user_agent: Optional[str] = None,
        language: str = 'en-us',
        private: bool = False,
        disable_images: bool = False,
        mute_audio: bool = False,
        proxy: Optional[Proxy] = None,
        profile_path: Optional[str] = None,

        screen_size: Optional[Tuple[int, int]] = None, # (width, height)
        full_screen: bool = True,
        headless: bool = False,
        home_page_url: Optional[str] = None
    ) -> ChromeOptions:
        options = ChromeOptions()
        options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
        prefs = {}

        if user_agent:
            options.add_argument('--user-agent={}'.format(user_agent))

        if language:
            options.add_argument('--lang={}'.format(language))
            prefs['intl.accept_languages'] = language.replace('-', '_')

        if private:
            options.add_argument('incognito')

        if disable_images:
            prefs['profile.managed_default_content_settings.images'] = 2

        if mute_audio:
            options.add_argument('--mute-audio')

        if proxy:
            options.add_argument('--proxy-server=http://{}'.format(proxy.string))

        if profile_path:
            options.user_data_dir = profile_path

        if screen_size:
            options.add_argument('--window-size={},{}'.format(screen_size[0], screen_size[1]))

        if headless:
            options.headless = True

        options.add_argument('--homepage \"{}\"'.format(home_page_url or 'data:,'))

        if full_screen:
            options.add_argument('--start-maximized' if os.name == 'nt' else '--kiosk')

        # if prefs:
        #     options.add_experimental_option('prefs', prefs)

        return options


# -------------------------------------------------------------------------------------------------------------------------------- #