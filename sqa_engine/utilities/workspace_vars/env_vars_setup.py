#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module contains functions to setup environ variables for the project.

        Function in this module:

            +   set_python_path_env_var() -> None
                    Setup value for PYTHONPATH

            +   set_android_home_env_var() -> None
                    Set value for ANDROID_HOME

            +   set_robot_syslog_file_env_var() -> None
                    Set value for ROBOT_SYSLOG_FILE

            +   set_android_avd_home_env_var() -> None
                    Set value for ANDROID_AVD_HOME
"""

from os import environ
from sqa_engine.utilities.workspace_vars import inter_path


def set_proxy() -> None:
    """Set proxy.

    Returns
    -------
    None
    """
    environ['HTTP_PROXY'] = ''
    environ['HTTPS_PROXY'] = ''
    environ['NO_PROXY'] = '192.168.82.95, 192.168.82.96, localhost, 127.0.0.1'


def set_python_path_env_var() -> None:
    """Setup Python path environment variable.

    This function setup PYTHONPATH environment variable that's used for
    robot file to understand the import libraries in entire project.

    Returns
    -------
    None
    """
    environ['PYTHONPATH'] = inter_path().workspace_path
    return


def set_android_home_env_var() -> None:
    """Set Android home environ variable.

    This function set value for ANDROID_HOME to specify Android SDK directory.

    Returns
    -------
    None
    """
    environ['ANDROID_HOME'] = inter_path().android_sdk_dir
    environ['JAVA_HOME'] = '/usr/lib/jvm/java-8-openjdk-amd64'
    return


def set_robot_syslog_file_env_var() -> None:
    """Set Robot syslog file environ variable.

    This function set value for ROBOT_SYSLOG_FILE environ variable to specify
    path of robot syslog file, that will store log of system when running
    robot.

    Returns
    -------
    None
    """
    environ['ROBOT_SYSLOG_FILE'] = inter_path().current_syslog_robot_path
    return


def set_version_env_var(version: str) -> None:
    """

    Parameters
    ----------
    version

    Returns
    -------

    """
    environ['VERSION'] = version
