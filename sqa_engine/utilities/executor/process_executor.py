#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module handles call to other processes.

    Functions in this module:

        +   create_empty_file(path_to_file: str) -> None
                Create empty file.

        +   copy_files(source_path: str, des_path: str) -> None
                Copy all items of a folder to other folder.

        +   execute_robot_test_cases(*args) -> None
                Execute robot test cases.

        +   generate_allure_report() -> None
                Generate allure report

        +   run_allure_report_server() -> None
                Open Allure report.

        +   run_appium_server() -> Popen
                Run Appium server.

        +   run_android_emulator(name: str) -> Popen
                Run Android emulator

        +   push_result() -> None
                Push execution results to report sever.
"""

from subprocess import run, Popen, PIPE
from os import listdir, path
from time import sleep
from json import load, loads, dumps
from requests import post
from getpass import getuser

import base64

from sqa_engine.utilities.workspace_vars import inter_path


def create_empty_file(path_to_file: str) -> None:
    """Create an empty file.

    This function creates an empty file with specified path.

    Parameters
    ----------
    path_to_file : str
        Should be a full path to file.

    Returns
    -------
    None
    """
    run(['touch', path_to_file])
    return


def copy_files(source_path: str, des_path: str) -> None:
    """Copy all file in source directory to an other directory.

    Parameters
    ----------
    source_path : str
        Path of source directory.
    des_path : str
        Path of des-directory.

    Returns
    -------
    None
    """
    run(['cp', '-av', f'{source_path}/', f'{des_path}/'])
    return


def execute_robot_test_cases(*args) -> None:
    """Execute robot test cases.

    This function call robot as sub-subprocess, execute robot test cases and
    export log.

    Parameters
    ----------
    args : list
        List of arguments to put into robot sub-process.

    Returns
    -------
    None
    """
    # Call robot sub-process with Allure report listener
    robot_executor = Popen([
        'robot', '--listener',
        f'allure_robotframework;{inter_path().current_allure_result_folder}',
        '--outputdir',
        f'{inter_path().current_robot_report_folder}',
        *args], stdout=PIPE)

    # Print and save log
    while True:
        with open(f'{inter_path().current_log_folder}/execution.log', 'a')\
                as log_file:
            line = robot_executor.stdout.readline()
            if not line:
                break
            print(line.rstrip().decode('utf-8'))
            log_file.write(line.decode('utf-8'))

    generate_allure_report()
    return


def generate_allure_report() -> None:
    """Generate Allure report.

    This function generates Allure report from Allure result.

    Returns
    -------
    None
    """
    run([inter_path().allure_bin, 'generate',
         inter_path().current_allure_result_folder,
         '--output', inter_path().current_allure_report_folder])
    return


def run_allure_report_server() -> None:
    """Run Allure report server.

    This function run Allure server with the latest log information.

    Returns
    -------
    None
    """
    run([inter_path().allure_bin, 'open',
         inter_path().current_allure_report_folder])
    return


def run_appium_server() -> Popen:
    """Run Appium server.

    Call Appium sever.

    Returns
    -------
    Popen
        Appium session
    """
    appium_session = Popen(['appium'])
    sleep(20)
    return appium_session


def run_android_emulator(name: str) -> Popen:
    """Run Android emulator.

    Run an Android emulator base on provided name.

    Returns
    -------
    Popen
        Android emulator session.
    """
    list_param = [inter_path().android_emulator_bin,
                  '-avd', name, '-noaudio', '-no-boot-anim',
                  '-no-window']
    if getuser() != 'root':
        list_param.insert(0, 'sudo')
        list_param.insert(1, '-E')
    emulator_session = Popen(list_param)
    sleep(10)
    return emulator_session


def push_result() -> None:
    """Push result.

    This function pushes execution result to report sever.

    Returns
    -------
    None
    """
    server_meta_data = dict()
    with open(inter_path().report_server_info) as data:
        server_meta_data = load(data)
    server_address = server_meta_data['server_address']
    send_results_endpoint = server_meta_data['send-results_api_endpoint']

    result_dir = inter_path().current_allure_result_folder
    result_files = listdir(result_dir)

    results = list()
    for file in result_files:
        result = dict()

        file_path = f'{result_dir}/{file}'
        if path.isfile(file_path):
            try:
                with open(file_path, 'rb') as file_obj:
                    content = file_obj.read()
                    if content.strip():
                        base64_content = base64.b64encode(content)
                        result['file_name'] = file
                        result['content_base64'] =\
                            base64_content.decode('UTF-8')
                        results.append(result)
                    else:
                        print('Empty file skipped: ' + file_path)
            finally:
                file_obj.close()
        else:
            print('Directory skipped: ' + file_path)

    headers = {'Content-type': 'application/json'}
    request_body = {
        'results': results
    }
    json_request_body = dumps(request_body)

    print(f'{server_address}{send_results_endpoint}')

    response =\
        post(f'{server_address}{send_results_endpoint}',
             headers=headers, data=json_request_body)

    # print('RESPONSE:')
    # json_response_body = loads(response.content)
    # json_prettier_response_body =\
    #     dumps(json_response_body, indent=4, sort_keys=True)
    # print(json_prettier_response_body)
    print('STATUS CODE:')
    print(response.status_code)
