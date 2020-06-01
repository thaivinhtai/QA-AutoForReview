#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module handles test cases execution.
"""

import argparse

from sqa_engine.utilities.logging.log_dirs_generator import\
    generate_logs_folder
from sqa_engine.utilities.workspace_vars import\
    set_robot_syslog_file_env_var
from sqa_engine.utilities.test_cases_management import switch_to_tds
from sqa_engine.utilities.executor.process_executor import\
    execute_robot_test_cases, run_allure_report_server, run_appium_server,\
    run_android_emulator
from tkinter import Tk, Button, Text, Label, filedialog


def execute_test_cases(parameters: argparse.Namespace) -> None:
    """Execute test cases.

    This function gets arguments and calls module process_executor to run test
    cases.

    Parameters
    ----------
    parameters : argparse.Namespace
        All arguments that user specified.

    Returns
    -------
    None
    """

    test_module = parameters.module
    test_design = parameters.test_design
    tags = parameters.tags
    version = parameters.version
    run_allure_server = parameters.run_allure
    level = parameters.level
    mode = parameters.mode
    browser = parameters.browser
    phone_simulator = parameters.mobile_device
    app_package = parameters.app_package
    app = parameters.app
    mobile_platform = parameters.mobile_platform
    mobile_platform_ver = parameters.mobile_platform_ver
    run_appium = parameters.run_appium_server
    keep_appium = parameters.keep_appium_alive
    run_job = parameters.run_job

    generate_logs_folder(module_name=test_module, test_design=test_design)
    set_robot_syslog_file_env_var()

    all_params = switch_to_tds(module=test_module, test_design=test_design,
                               tags=tags, level=level, browser=browser,
                               phone_simulator=phone_simulator, app=app,
                               app_package=app_package, version=version,
                               mobile_platform=mobile_platform, mode=mode,
                               mobile_platform_ver=mobile_platform_ver,
                               run_job=run_job)

    android_emulator_session = None
    appium_session = None

    if run_job and test_module.lower() == 'mobile_app':
        android_emulator_session = run_android_emulator(phone_simulator)

    if run_appium and test_module.lower() == 'mobile_app':
        appium_session = run_appium_server()

    execute_robot_test_cases(*all_params)

    if not keep_appium and test_module == 'mobile_app' and run_appium:
        appium_session.terminate()
        appium_session.wait()

    if run_allure_server:
        run_allure_report_server()

    if run_job and test_module.lower() == 'mobile_app':
        android_emulator_session.terminate()
        android_emulator_session.wait()
    return


def run_manual_reporter() -> tuple:
    """Run manual reporter.

    This function is used for reporting manual test cases and push the result
    to dashboard.

    Returns
    -------
    tuple
        report_message : massage to attach to the report.
        screenshot : path to the screenshot.
        result : True if passed, False if failed.
    """
    # Generate returned variables
    report_message = str()
    screenshot = str()
    result = bool()

    # Generate reporter window.
    window = Tk()
    window.title('SQA Manual Reporter')
    window.geometry('640x480')

    message_label = Label(window, text='Message:')
    message_label.place(relx=0.5, rely=0.04, anchor='center')

    message = Text(window, width=74, height=18)
    message.place(relx=0.5, rely=0.4, anchor='center')

    screenshot_label = Label(window, text='Path to screenshot:')
    screenshot_label.place(relx=0.5, rely=0.76, anchor='center')

    screenshot_path = Text(window, width=64, height=2)
    screenshot_path.place(relx=0.435, rely=0.84, anchor='center')

    def __assign_value():
        nonlocal report_message, screenshot
        report_message = message.get("1.0", "end")[:-1]
        screenshot = screenshot_path.get("1.0", "end")[:-1]

    def click_passed_btn():
        nonlocal result
        __assign_value()
        result = True
        window.destroy()

    def click_failed_btn():
        nonlocal result
        __assign_value()
        result = False
        window.destroy()

    def file_dialog():
        nonlocal screenshot_path
        file_name =\
            filedialog.askopenfilename(initialdir="/", title = "Select A File",
                                       filetypes=(("JPEG files", "*.jpg"),
                                                  ("PNG files", "*.png"),
                                                  ("all files", "*.*")))
        screenshot_path.replace("1.0", "end", file_name)

    file_browse_btn = Button(window, text='Browse', command=file_dialog)
    file_browse_btn.place(relx=0.91, rely=0.84, anchor='center')

    true_button = Button(window, text='Passed', command=click_passed_btn)
    true_button.place(relx=0.3, rely=0.94, anchor='center')
    fail_button = Button(window, text='Failed', command=click_failed_btn)
    fail_button.place(relx=0.7, rely=0.94, anchor='center')

    window.mainloop()
    return report_message, screenshot, result
