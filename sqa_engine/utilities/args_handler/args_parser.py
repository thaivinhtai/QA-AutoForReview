#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module gets arguments via specified flags.
"""


import argparse


def __get_args() -> argparse.Namespace:
    """Get test arguments.

    Returns
    -------
    argparse.Namespace
        module : module to be tested
        test_design : test design specification of module to be tested
        version : Specify version
        level : {REG1, REG2, .. }
        mode : {auto, manual}
        tags : tag of test cases
        browser : browser to execute test on
        mobile_device : device to test on
        mobile_platform : {iOS, Android}
        mobile_platform_ver : mobile platform version
        app_package : package to be tested
        app : The path to a .ipa, .apk or .zip file containing the app to test
        run_allure : start allure reporting server after test
        run_appium_server : start appium server before test
        keep_appium_alive : keep appium server running after test
        gen_scripts : generate sequence and test documentation
        run_job : run test cases in non-desktop environment
        push_result : push execution results to reporting server
    """
    parser = argparse.ArgumentParser(description='Test Execution handling')
    parser.add_argument('--module', required=True,
                        help='{REST, mobile_app, web}')
    parser.add_argument('--test-design', required=True,
                        help='The TDS name to use for execution of tests')
    parser.add_argument('--version', required=True,
                        help='Specify version UI/API')
    parser.add_argument('--level', required=True, help='{Reg1, Reg2, All}')
    parser.add_argument('--mode', required=True, help='Auto, Manual')
    parser.add_argument('--tags', required=False, nargs='*',
                        help='Identifier of test cases to be run')
    parser.add_argument('--browser', required=False, help='Browser to be run')
    parser.add_argument('--mobile-device', required=False,
                        help='Device to run test cases for mobile apps')
    parser.add_argument('--mobile-platform', required=False,
                        help='{iOS, Android}')
    parser.add_argument('--mobile-platform-ver', required=False,
                        help='Version of platform OS')
    parser.add_argument('--app-package', required=False,
                        help='App to be tested')
    parser.add_argument('--app', required=False,
                        help='The path to a .ipa, .apk or .zip \
file containing the app to test.')
    parser.add_argument('--run-allure', required=False, action='store_true',
                        help='Run Allure report server')
    parser.add_argument('--run-appium-server', required=False,
                        action='store_true', help='Run Appium server')
    parser.add_argument('--keep-appium-alive', required=False,
                        action='store_true',
                        help='Keep Appium server running after test suite')
    parser.add_argument('--gen-scripts', required=False, action='store_true',
                        help='Generate sequence and create test documentation')
    parser.add_argument('--run-job', required=False, action='store_true',
                        help='Only use this flag for running CI/CD')
    parser.add_argument('--push-result', required=False, action='store_true',
                        help='Push execution results to reporting server')

    return parser.parse_args()


'''
This global variable stores value of __get_args(), this makes ArgumentParser be
initialed just one time and store the argparse.Namespace that we can use later.
'''
__ARGUMENTS = __get_args()


def get_args() -> argparse.Namespace:
    """Get arguments.

    This function actually is a retriever of __ARGUMENTS, this helps us to
    import in other modules.

    Returns
    -------
    argparse.Namespace
    """
    return __ARGUMENTS
