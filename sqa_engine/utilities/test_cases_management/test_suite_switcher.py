#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module handles switching test suite and get data.

    Private function in this module:

        +   __get_robot_vars(**kwargs) -> list
                Collects input of user and return a list that contains flags
                of robot to assign value for variables in robot test cases.

    Public function:

        +   switch_to_tds(**kwargs) -> list
                Collects all arguments as a list based on user's input.
"""

from .test_suite_retriever import get_list_test_cases_and_robot_file
from .semantic_versioning import Version
from .test_cases_metadata import get_tags, get_test_metadata
from sqa_engine.utilities.workspace_vars.internal_path import inter_path


def __get_robot_vars(**kwargs) -> list:
    """Get robot framework variables.

    This private function collects input of user and return a list that
    contains flags of robot to assign value for variables in robot test cases.

    Parameters
    ----------
    kwargs : dict

    Returns
    -------
    list
        List of robot argument to assign value to robot test cases variables.
    """
    defaul_list = \
        ['--variable',
         f'screenshot_path:{inter_path().current_screenshot_folder}']
    if kwargs['run_job']:
        defaul_list += ['--variable', 'headless:True']

    if kwargs['browser'] and kwargs['test_module'].lower() == 'web_portal':
        return ['--variable', f'browser:{kwargs["browser"]}'] + defaul_list
    if kwargs['test_module'].lower() == 'web_portal':
        # return ['--variable', f'browser:{kwargs["browser"]}']
        return defaul_list

    if kwargs['phone_simulator'] and kwargs['mobile_platform'] \
            and kwargs['mobile_platform_ver'] and kwargs['app'] \
            and kwargs['test_module'].lower() == 'mobile_app':
        return ['--variable', f'deviceName:{kwargs["phone_simulator"]}',
                '--variable', f'platformName:{kwargs["mobile_platform"]}',
                '--variable',
                f'platformVersion:{kwargs["mobile_platform_ver"]}',
                '--variable', f'appPackage:{kwargs["app_package"]}',
                '--variable', f'app:{kwargs["app"]}'] + \
                defaul_list
    if kwargs['test_module'].lower() == 'mobile_app':
        return ['--variable', f'deviceName:{kwargs["phone_simulator"]}',
                '--variable', f'platformName:{kwargs["mobile_platform"]}',
                '--variable',
                f'platformVersion:{kwargs["mobile_platform_ver"]}',
                '--variable', f'appPackage:{kwargs["app_package"]}',
                '--variable', f'app:{kwargs["app"]}'] + \
                defaul_list
    return defaul_list


def switch_to_tds(**kwargs) -> list:
    """Switch to Test Domain Specification.

    This function collects all arguments as a list based on user's input.

    Parameters
    ----------
    kwargs : dict

    Returns
    -------
    list
        List of all arguments that will be input of robot subprocess.
    """
    test_module = kwargs['module']
    test_design = kwargs['test_design']
    temp_tags = kwargs['tags']
    level = kwargs["level"].lower()
    mode = kwargs["mode"].lower()
    browser = kwargs['browser']
    phone_simulator = kwargs['phone_simulator']
    app_package = kwargs['app_package']
    app = kwargs['app']
    mobile_platform = kwargs['mobile_platform']
    mobile_platform_ver = kwargs['mobile_platform_ver']
    version = Version(kwargs['version'])
    run_job = kwargs['run_job']

    list_test_cases, robot_file =\
        get_list_test_cases_and_robot_file(module_name=test_module,
                                           test_design=test_design)

    # Prepare tags list
    tags = []
    if temp_tags:
        for tag in temp_tags:
            tags.append('-i')
            tags.append(tag)

    # Get value for robot vars
    robot_vars = __get_robot_vars(test_module=test_module, browser=browser,
                                  phone_simulator=phone_simulator,
                                  mobile_platform=mobile_platform, app=app,
                                  mobile_platform_ver=mobile_platform_ver,
                                  app_package=app_package, run_job=run_job)

    executed_test_cases = list()
    tags_by_test_case = get_tags(robot_suite=robot_file)[1]
    # Handle version, if test case has version specification that does not
    # match, ignore it.
    for test_case in list_test_cases:
        if version >=\
                Version(get_test_metadata(name='min_version',
                                          tags=tags_by_test_case[test_case]))\
                and\
                get_test_metadata(name='max_version',
                                  tags=tags_by_test_case[test_case]) == "None":
            pass
        elif version >\
                Version(get_test_metadata(name='max_version',
                                          tags=tags_by_test_case[test_case]))\
                or version <\
                Version(get_test_metadata(name='min_version',
                                          tags=tags_by_test_case[test_case])):
            continue
        if get_test_metadata(name='level',
                             tags=tags_by_test_case[test_case]).lower()\
                != level.lower() and level.lower() != 'all':
            continue
        if get_test_metadata(name='mode',
                             tags=tags_by_test_case[test_case]).lower()\
                != mode.lower():
            continue
        executed_test_cases.append('-t')
        executed_test_cases.append(test_case)

    if executed_test_cases:
        return [*robot_vars, *tags, *executed_test_cases, robot_file]

    print("There is no test case to execute.")
    raise RuntimeError("There is no test case to execute.")
