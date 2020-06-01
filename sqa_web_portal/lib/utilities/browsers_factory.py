#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from selenium import webdriver
from os import environ
from pathlib import Path


def __get_current_path():
    return str(Path(__file__).parent.absolute())


def __get_firefox(headless: str) -> webdriver:
    """This function establishes firefox browser."""
    firefox_options = None
    if headless:
        firefox_options = webdriver.firefox.options.Options()
        firefox_options.add_argument('--headless')
        firefox_options.add_argument('--disable-gpu')
        firefox_options.add_argument('--debug')
    geckodriver = __get_current_path() +\
        "/drivers/geckodriver_linux64/geckodriver"
    environ["webdriver.gecko.driver"] = geckodriver
    return webdriver.Firefox(executable_path=geckodriver,
                             firefox_options=firefox_options)


def __get_chrome(headless: str) -> webdriver:
    """This function establishes chrome browser."""
    chrome_options = None
    if headless:
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')
        # open Browser in maximized mode
        chrome_options.add_argument('start-maximized')
        # disable info bars
        # chrome_options.add_argument('disable-infobars')
        # disable extensions
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-gpu')  # For windows os only
        chrome_options.add_argument('--no-sandbox')  # bypass OS security model
        # overcome limited resource problems
        chrome_options.add_argument('--disable-dev-shm-usage')
    chromedriver = __get_current_path() +\
        "/drivers/chromedriver_linux64/chromedriver"
    environ["webdriver.chrome.driver"] = chromedriver
    return webdriver.Chrome(executable_path=chromedriver,
                            chrome_options=chrome_options)


def get_browser(name: str, headless: bool):
    """This function is used for quick selection of browser."""
    switcher = {
        "firefox": __get_firefox,
        "chrome": __get_chrome
    }
    func = switcher.get(name)
    return func(headless)
