#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module contains functions and abstract class for the keywords lib in every
testing module.
"""


from abc import ABC
from getpass import getuser

from time import sleep

from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choice, randint

from robot.libraries.BuiltIn import BuiltIn
from allure_commons._allure import attach
from allure_commons.types import AttachmentType

from sqa_engine.utilities.logging.custom_logger import CustomLogger
from sqa_engine.utilities.executor import run_manual_reporter
from sqa_engine.utilities.workspace_vars import inter_path


class CommonKeywords(ABC):
    """
    This abstract class is a blueprint for common keyword for each testing
    module.
    """

    def __init__(self):
        """Constructor."""
        self.current_test_name = BuiltIn().get_variable_value("${TEST_NAME}")
        self.driver = None
        self.logger = CustomLogger(self.current_test_name)

    def get_element(self, value: str):
        """Get element.

        This function resolves the webview element identifier.

        Parameters
        ----------
        value : str

        Returns
        -------
        The Webview Element.
        """
        value = value.split(":")
        location_type = value[0]
        location = value[1]
        if location_type == 'xpath':
            return self.driver.find_element_by_xpath(location)
        if location_type == 'id':
            return self.driver.find_element_by_id(location)
        if location_type == 'name':
            return self.driver.find_element_by_name(location)
        if location_type == 'partial_text':
            return self.driver.find_element_by_partial_link_text(location)

    def click_to_location(self, value: str) -> bool:
        self.get_element(value).click()
        self.logger.info(f'click to {value}')
        return True

    def send_string_to_element(self, locator: str,
                               str_to_be_sent: str) -> bool:
        try:
            self.get_element(locator).clear()
        except IndexError:
            self.logger.warn("Can not clear before send new string on mobile")
            pass
        self.get_element(locator).send_keys(str_to_be_sent)
        self.logger.info(f'Send "{str_to_be_sent} to {locator}')
        return True

    def check_text_present(self, text: str) -> bool:
        self.logger.info(f'Check "{text}" exists on page.')
        if text in self.driver.page_source:
            return True
        return False

    def wait_for(self, time: str, log=True):
        if log:
            self.logger.info(f'Wait for {time} seconds')
        sleep(int(time))

    def take_screenshot(self, full_path: str) -> None:
        self.logger.info(f'Take screenshot {full_path}' +
                         f'{self.current_test_name}.png')
        image_file = open(f'{full_path}{self.current_test_name}.png', 'rb')
        attach_image = image_file.read()
        attach(attach_image, name='image', attachment_type=AttachmentType.PNG)
        image_file.close()
        return


def open_reporter(logger) -> bool:
    """Open reporter.

    This function call the manual reporter and attach image, message to
    manual testing report.

    Parameters
    ----------
    logger : CustomLogger

    Returns
    -------
    bool
        True - Passed
        False - Failed
    """
    logger.info('', timestamp=False)
    logger.info('Open Manual Reporter.')
    message, screenshot, result = run_manual_reporter()
    logger.info(message)
    logger.info(f'Screenshot: {screenshot}')
    try:
        image_file = open(screenshot, 'rb')
        attach_image = image_file.read()
        attach(attach_image, name='image',
               attachment_type=AttachmentType.PNG)
        image_file.close()
    except FileNotFoundError:
        pass
    return result


def log_current_executor(logger: CustomLogger) -> None:
    """Log current executor's info.

    This function helps to log current tester, who executes the test case.

    Parameters
    ----------
    logger : CustomLogger

    Returns
    -------
    None
    """
    current_user = getuser()
    current_dir = inter_path().workspace_path
    logger.info(f'Test case ' +
                f'is conducted by: {current_user}')
    logger.info(f'Workspace locates at {current_dir}')
    logger.info(f'========== Test Case Begins ==========')


def random_str(length: int) -> str:
    """Generate random string.

    This function generates random string with given length.

    Parameters
    ----------
    length : int
        Length of string to be generated.

    Returns
    -------
    string
        A random string.
    """
    letters = ascii_lowercase + ascii_uppercase + digits + punctuation
    return ''.join(choice(letters) for i in range(length))


def random_number(max_num: int) -> int:
    """Generate random number.

    This function generates a random number from 0 to given max_num.

    Parameters
    ----------
    max_num : int
        The largest number can be generated.

    Returns
    -------
    int
        A random number.
    """
    return randint(0, max_num)
