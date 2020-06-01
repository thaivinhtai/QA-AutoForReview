#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module contain custom keyword for web testing."""


from robot.api.deco import keyword

# from pynput.keyboard import Controller

from pyautogui import locateCenterOnScreen, moveTo, click
from time import sleep

from appium import webdriver
from appium.common.exceptions import NoSuchContextException

from sqa_engine.utilities.test_cases_management.common_robot_keywords import \
    CommonKeywords, open_reporter, log_current_executor, random_number,\
    random_str
from sqa_mobile_app.lib.android.keycode import KEY_CODE


class DriverKeywords(CommonKeywords):
    """

    """

    def __init__(self):
        """

        Parameters
        ----------
        # platform_name
        # platform_version
        # device_name
        # app_package
        # app_activity
        """
        super().__init__()
        self.__default_timeout = '360'
        self.__appium_remote_server = 'http://0.0.0.0:4723/wd/hub'

    def __finish_action(self):
        # press back
        self.driver.press_keycode(KEY_CODE['BACK'])
        self.driver.implicitly_wait(5)

    @keyword('Set Driver')
    def set_driver(self, platform_name: str, platform_version: str,
                   device_name: str, app: str, app_package: str):
        desired_cap = {
            'platformName': platform_name,
            'platformVersion': platform_version,
            'deviceName': device_name,
            'newCommandTimeout': self.__default_timeout,
            # 'fullReset': "true",  # TODO: transfer to optional parameter
            'enablePerformanceLogging': "true",
            'ignoreUnimportantViews': 'true'
        }
        if app != "None":
            desired_cap['app'] = app
        if app_package != "None":
            desired_cap['appPackage'] = app_package
        self.driver = webdriver.Remote(self.__appium_remote_server,
                                       desired_cap)
        self.driver.implicitly_wait(2)
        self.logger.info('', timestamp=False)
        self.logger.info(f'Execute test on {device_name}, platform \
{platform_name} version {platform_version}')

    @keyword('Click To Element')
    def click_to_element(self, value: str):
        try:
            return super().click_to_location(value=value)
        except NoSuchContextException as E:
            self.logger.error(E.msg)
            return False

    @keyword("Remove Value From Element")
    def remove_value_from_element(self, locator: str) -> bool:
        element = super().get_element(value=locator)
        element.click()
        string_length = len(element.text)
        for index in range(string_length):
            # press backspace
            # self.driver.press_keycode(KEY_CODE['BACKSPACE'])
            self.driver.keyevent(keycode=KEY_CODE['BACKSPACE'])
        self.__finish_action()
        return True

    @keyword('Type String To Element')
    def type_string_to_element(self, locator: str,
                               str_to_be_typed: str) -> bool:
        self.logger.info(f'Type "{str_to_be_typed}" to {locator}')
        self.click_to_element(value=locator)
        for char in str_to_be_typed:
            # self.driver.press_keycode(KEY_CODE[char.upper()])
            self.driver.keyevent(keycode=KEY_CODE[char.upper()])
        self.__finish_action()
        return True

    @keyword('Scroll Down Until Element')
    def scroll_down_to_element(self, element: str) -> bool:
        screen_size = self.driver.get_window_size()
        height = screen_size.get('height')
        width = screen_size.get('width')
        scroll_height_start = int(height * 0.5)
        scroll_height_end = int(height * 0.2)

        condition = locateCenterOnScreen(element)

        while not condition:
            self.driver.swipe(start_x=width * 0.5, start_y=scroll_height_start,
                              end_x=width * 0.5, end_y=scroll_height_end)
            condition = locateCenterOnScreen(element)
        return True

    @keyword('Click To Image Object')
    def click_to_image_object(self, img_obj: str) -> bool:
        self.logger.info(f'Click to image {img_obj}')
        img_position_x, img_position_y = locateCenterOnScreen(img_obj)
        click(img_position_x, img_position_y)
        return True

    @keyword('Wait for')
    def wait_for(self, time: str) -> None:
        super().wait_for(time=time)
        self.driver.implicitly_wait(time)

    @keyword('Close app')
    def close_app(self):
        self.driver.close_app()
        self.logger.info('Close app')

    @keyword('Take screenshot')
    def take_screenshot(self, full_path: str) -> None:
        self.driver.save_screenshot(f'{full_path}' +
                                    f'{self.current_test_name}.png')
        return super().take_screenshot(full_path=full_path)

    @keyword('Open Manual reporter')
    def open_manual_reporter(self) -> bool:
        return open_reporter(logger=self.logger)

    @keyword("Check Text Present")
    def check_text_present(self, text: str) -> bool:
        return super().check_text_present(text=text)

    @keyword('Log Executor Info')
    def log_executor_info(self) -> None:
        return log_current_executor(logger=self.logger)

    @keyword('Info Log')
    def log_info_to_console(self, message: str) -> None:
        return self.logger.info(message)

    @keyword('Close session')
    def close_session(self):
        self.driver.quit()
        self.logger.info('End session')

    @keyword('Random Number')
    def random_number(self, max_num: int) -> int:
        return random_number(max_num=max_num)

    @keyword('Random String')
    def random_string(self, string_length: int) -> str:
        return random_str(length=string_length)

    # def __press_and_release(self, key):
    #     self.__keyboard.press(key)
    #     self.__keyboard.release(key)
    #     sleep(0.1)

    # @keyword('Type string')
    # def type_string(self, str_to_be_type: str):
    #     for char in str_to_be_type:
    #         self.__press_and_release(char)
    #     self.__logger.info(f'Input "{str_to_be_type}" by typing')
