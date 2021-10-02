# selenium_chrome

![PyPI - package version](https://img.shields.io/pypi/v/selenium_chrome?logo=pypi&style=flat-square)
![PyPI - license](https://img.shields.io/pypi/l/selenium_chrome?label=package%20license&style=flat-square)
![PyPI - python version](https://img.shields.io/pypi/pyversions/selenium_chrome?logo=pypi&style=flat-square)
![PyPI - downloads](https://img.shields.io/pypi/dm/selenium_chrome?logo=pypi&style=flat-square)

![GitHub - last commit](https://img.shields.io/github/last-commit/kkristof200/selenium_chrome?style=flat-square)
![GitHub - commit activity](https://img.shields.io/github/commit-activity/m/kkristof200/selenium_chrome?style=flat-square)

![GitHub - code size in bytes](https://img.shields.io/github/languages/code-size/kkristof200/selenium_chrome?style=flat-square)
![GitHub - repo size](https://img.shields.io/github/repo-size/kkristof200/selenium_chrome?style=flat-square)
![GitHub - lines of code](https://img.shields.io/tokei/lines/github/kkristof200/selenium_chrome?style=flat-square)

![GitHub - license](https://img.shields.io/github/license/kkristof200/selenium_chrome?label=repo%20license&style=flat-square)

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

[kproxy](https://pypi.org/project/kproxy), [selenium](https://pypi.org/project/selenium), [selenium-browser](https://pypi.org/project/selenium-browser), [undetected-chromedriver](https://pypi.org/project/undetected-chromedriver), [xpath-utils](https://pypi.org/project/xpath-utils)