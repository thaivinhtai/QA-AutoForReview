#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module contains function that generates log folders.
"""

from datetime import datetime
from os import mkdir, path
from sqa_engine.utilities.workspace_vars import inter_path
from sqa_engine.utilities.executor import create_empty_file


def generate_logs_folder(module_name: str, test_design: str) -> None:
    """Create and return path of folder that stores log files.

    This function takes the timestamp when test cases are run, then create
    directories to store log files. The directories are classified by Module,
    TDS.

    The structure of generated folders:
        workspace/{today}/{module}/{test_design}-{current_time}

    Parameters
    ----------
    module_name : str
        The name of module to be tested {REST, web, app}.
    test_design : str
        Test Domain Specification.

    Returns
    -------
    None
    """
    today = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H-%M-%S")
    logs_path = inter_path().logs_folder

    today_log_folder = f'{logs_path}/{today}'
    module_log_folder = f'{today_log_folder}/{module_name}'
    executing_log_folder = f'{module_log_folder}/{current_time}-{test_design}'
    robot_report_folder = f'{executing_log_folder}/robot'
    allure_report_folder = f'{executing_log_folder}/allure-report'
    allure_result_folder = f'{executing_log_folder}/allure-results'
    screenshot_folder = f'{executing_log_folder}/screenshots'

    if not path.exists(logs_path):
        mkdir(logs_path)
    if not path.exists(today_log_folder):
        mkdir(today_log_folder)
    if not path.exists(module_log_folder):
        mkdir(module_log_folder)
    if not path.exists(executing_log_folder):
        mkdir(executing_log_folder)
        mkdir(robot_report_folder)
        mkdir(allure_report_folder)
        mkdir(allure_result_folder)
        mkdir(screenshot_folder)
        create_empty_file(f'{robot_report_folder}/syslog.txt')

    # update path to InternalPath instance attribute.
    inter_path().current_allure_result_folder = allure_result_folder
    inter_path().current_allure_report_folder = allure_report_folder
    inter_path().current_robot_report_folder = robot_report_folder
    inter_path().current_log_folder = executing_log_folder
    inter_path().current_screenshot_folder = screenshot_folder
    inter_path().current_syslog_robot_path =\
        f'{robot_report_folder}/syslog.txt'

    return
