#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module contain custom keyword for web testing."""


from robot.api.deco import keyword
from selenium.common.exceptions import NoSuchElementException

# from pynput.keyboard import Controller

from sqa_web_portal.lib.utilities.browsers_factory import get_browser
from sqa_engine.utilities.test_cases_management.common_robot_keywords import \
    CommonKeywords, open_reporter, log_current_executor


class DriverKeywords(CommonKeywords):

    def __init__(self):
        super().__init__()

    @keyword('Establish Browser')
    def establish_browser(self, browser: str, headless=False):
        self.driver = get_browser(browser, headless)
        self.logger.info('', timestamp=False)
        self.logger.info(f'Open {browser.upper()} browser')

    @keyword('Close Browser')
    def close_browser(self):
        self.driver.close()
        self.logger.info('Close browser')

    @keyword('Go To URL')
    def go_to_url(self, url: str):
        self.driver.get(url)
        self.logger.info(f'Access {url}')

    @keyword('Click To Element')
    def click_to_location(self, value: str):
        try:
            return super().click_to_location(value=value)
        except NoSuchElementException as E:
            self.logger.error(E.msg)
            return False

    @keyword('Send string to element')
    def send_string_to_element(self, locator: str,
                               str_to_be_sent: str) -> bool:
        try:
            return \
                super().send_string_to_element(locator=locator,
                                               str_to_be_sent=str_to_be_sent)
        except NoSuchElementException as E:
            self.logger.error(E.msg)
            return False

    # @keyword("Remove Value From Element")
    # def remove_value_from_element(self, locator: str) -> bool:
    #     locators = CommonKeywords.identify_locator(value=locator)
    #     location_type = locators[0]
    #     location = locators[1]

    @keyword("Check Text Present")
    def check_text_present(self, text: str) -> bool:
        return super().check_text_present(text=text)

    @keyword('Wait For')
    def wait_for(self, time: str):
        super().wait_for(time=time)
        self.driver.implicitly_wait(time)

    @keyword('Take Screenshot')
    def take_screenshot(self, full_path: str) -> None:
        self.driver. \
            get_screenshot_as_file(f'{full_path}' +
                                   f'{self.current_test_name}.png')
        return super().take_screenshot(full_path=full_path)

    @keyword('Open Reporter')
    def open_reporter(self) -> bool:
        return open_reporter(logger=self.logger)

    @keyword('Log Executor Info')
    def log_executor_info(self) -> None:
        return log_current_executor(logger=self.logger)

    @keyword('Info Log')
    def log_info_to_console(self, message: str) -> None:
        return self.logger.info(message)

    # def __press_and_release(self, key):
    #     self.__keyboard.press(key)
    #     self.__keyboard.release(key)
    #     sleep(0.1)
