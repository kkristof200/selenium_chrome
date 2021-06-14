# selenium_chrome



## Description

User-friendly implementation of a chrome based selenium client

## Features
- Easily create a firefox selenium webdriver with proxy(host/port), extensions and other settings, such as, full-screen-window,
private session.
- Override user-agent
- Easily save and load cookies for websites
- protects against bot-detection, because it uses undetected-chromedriver

## Install

~~~~bash
pip install selenium_chrome
# or
pip3 install selenium_chrome
~~~~

## Usage

~~~~python
from selenium_chrome import Chrome

chrome = Chrome()
chrome.get('https://www.google.com')

import time
time.sleep(999)
~~~~

## Dependencies

[geckodriver-autoinstaller](https://pypi.org/project/geckodriver-autoinstaller), [kproxy](https://pypi.org/project/kproxy), [noraise](https://pypi.org/project/noraise), [selenium](https://pypi.org/project/selenium), [selenium-browser](https://pypi.org/project/selenium-browser), [undetected-chromedriver](https://pypi.org/project/undetected-chromedriver), [xpath-utils](https://pypi.org/project/xpath-utils)