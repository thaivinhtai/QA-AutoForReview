#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module is for storing path of project.
"""

from pathlib import Path
from os import listdir, path, environ


class InternalPath:
    """Internal path container.

    This class stores all the path of every packages, files that will be used
    in execution progressing.

    Attributes
    ----------
    __workspace_path : str
        Absolute path of workspace folder.
    __logs_folder : str
        Absolute path of root log folder.
    __document_folder : str
        Absolute path of root document folder.
    __sqa_package : dict
        A dictionary of absolute path of packages in workspace (project).
    __mobile_app : dict
        A dictionary of test domain and their absolute path of mobile app.
    __rest_api : dict
        A dictionary of test domain and their absolute path of rest api.
    __web_portal : dict
        A dictionary of test domain and their absolute path of web portal.
    __allure_bin : str
        Absolute path of Allure executable bin file.
    __android_sdk_dir : str
        Absolute path of Android SDK directory.
    __current_allure_report_folder : str
        Absolute path of folder that stores Allure report files.
    __current_robot_report_folder : str
        Absolute path of folder that stores Robot report files.
    __current_log_folder : str
        Absolute path of root folder that stores log files.
    __current_doc_folder : str
        Absolute path of root folder that stores documentation.
    __allure_job_result_folder : str
        Absolute path of folder that stores result allure for report sever
    __report_server_info : str
        Absolute path of report_server_info.json

    Methods
    -------
    __get_path(self, module: str) -> dict
        A private method to return all the files (files and folders are
        included) in a module.
    """

    def __init__(self):
        """Constructor."""
        self.__workspace_path =\
            str(Path(__file__).parent.absolute().parent.parent.parent)

        self.__logs_folder = f'{self.__workspace_path}/logs'
        self.__document_folder = f'{self.__workspace_path}/documentations'

        self.__sqa_package = dict()
        for directory in listdir(self.__workspace_path):
            self.__sqa_package[directory.replace('sqa_', '')] =\
                f'{self.__workspace_path}/{directory}'
        if 'SQA_TOOLS' in environ.keys():
            self.__sqa_package['tools'] = environ['SQA_TOOLS']

        self.__report_server_info =\
            f'{self.__sqa_package["engine"]}/utilities/report_server_info.json'

        self.__mobile_app = self.__get_path('mobile_app')
        self.__rest_api = self.__get_path('rest_api')
        self.__web_portal = self.__get_path('web_portal')
        self.__integration = self.__get_path('integration')

        self.__allure_bin = f'{self.__sqa_package["tools"]}/allure/bin/allure'
        self.__android_sdk_dir =\
            f'{self.__sqa_package["tools"]}/android_sdk'
        self.__android_emulator_bin =\
            f'{self.__sqa_package["tools"]}/android_sdk/emulator/emulator'

        self.__current_allure_result_folder = str()
        self.__current_allure_report_folder = str()
        self.__current_robot_report_folder = str()
        self.__current_screenshot_folder = str()
        self.__current_log_folder = str()
        self.__current_syslog_robot_path = str()

        self.__current_doc_folder = str()

        self.__allure_job_result_folder =\
            f'{self.__workspace_path}/allure-results'

    def __get_path(self, module: str) -> dict:
        """Get path.

        This private function gets name of module and collects all files of a
        module bases on its name.

        Parameters
        ----------
        module : str
            Name of testing module {mobile_app, web_portal, rest_api}

        Returns
        -------
        dict
            A dictionary of module and its file.
        """
        temp_dict = dict()
        for directory in listdir(self.__sqa_package[module]):
            # Ignore files and __pycache__ directory.
            if path.isfile(directory) or directory.find('__') == 0:
                continue
            temp_dict[directory] = \
                f'{self.__sqa_package[module]}/{directory}'
        return temp_dict

    @property
    def workspace_path(self) -> str:
        """workspace path.

        Getter of __workspace_path

        Returns
        -------
        str
            Value of attribute __workspace_path
        """
        return self.__workspace_path

    @property
    def logs_folder(self) -> str:
        """logs folder.

        Getter of __logs_folder

        Returns
        -------
        str
            Value of attribute __logs_folder
        """
        return self.__logs_folder

    @property
    def document_folder(self) -> str:
        """Document folder.

        Getter of __document_folder

        Returns
        -------
        str
            Value of __document_folder
        """
        return self.__document_folder

    @property
    def sqa_package(self) -> dict:
        """SQA package.

        Getter of __sqa_package

        Returns
        -------
        dict
            Value of __sqa_package
        """
        return self.__sqa_package

    @property
    def mobile_app(self) -> dict:
        """Mobile app.

        Getter of __mobile_app

        Returns
        -------
        dict
            Value of __mobile_app
        """
        return self.__mobile_app

    @property
    def rest_api(self) -> dict:
        """REST API.

        Getter of __rest_api

        Returns
        -------
        dict
            Value of __rest_api
        """
        return self.__rest_api

    @property
    def web_portal(self) -> dict:
        """Web portal.

        Getter of __web_portal

        Returns
        -------
        dict
            Value of __web_portal
        """
        return self.__web_portal

    @property
    def integration(self) -> dict:
        """Web portal.

        Getter of __integration

        Returns
        -------
        dict
            Value of __integration
        """
        return self.__integration

    @property
    def allure_bin(self) -> str:
        """Allure Bin.

        Getter of __allure_bin

        Returns
        -------
        str
            Value of __allure_bin
        """
        return self.__allure_bin

    @property
    def android_sdk_dir(self) -> str:
        """Android SDK directory.

        Getter of __android_sdk_dir

        Returns
        -------
        str
            Value of __android_sdk_dir
        """
        return self.__android_sdk_dir

    @property
    def android_emulator_bin(self) -> str:
        """Android emulator bin.

        Getter of __android_emulator_bin

        Returns
        -------
        str
            Path to Android emulator bin
        """
        return self.__android_emulator_bin

    @property
    def allure_job_result_folder(self) -> str:
        """Allure job result folder.

        Getter of __allure_job_result_folder

        Returns
        -------
        str
            Path to Allure job results folder
        """
        return self.__allure_job_result_folder

    # @property
    # def java_jdk_dir(self) -> str:
    #     """Java JDK directory.
    #
    #     Getter of __java_jdk_dir
    #
    #     Returns
    #     -------
    #     str
    #         Value of __java_jdk_dir
    #     """
    #     return self.__java_jdk_dir

    @property
    def current_allure_result_folder(self) -> str:
        """Current Allure result folder.

        Getter of __current_allure_result_folder

        Returns
        -------
        str
            Value of __current_allure_result_folder
        """
        return self.__current_allure_result_folder

    @current_allure_result_folder.setter
    def current_allure_result_folder(self, value: str) -> None:
        """Set current Allure result folder.

        Setter of __current_allure_result_folder

        Parameters
        ----------
        value : str
            Path to Allure result folder

        Returns
        -------
        None
        """
        self.__current_allure_result_folder = value
        return

    @property
    def current_allure_report_folder(self) -> str:
        """Current Allure report folder.

        Getter of __current_allure_report_folder

        Returns
        -------
        str
            Value of __current_allure_report_folder
        """
        return self.__current_allure_report_folder

    @current_allure_report_folder.setter
    def current_allure_report_folder(self, value: str) -> None:
        """Set current Allure report folder.

        Setter of __current_allure_report_folder

        Parameters
        ----------
        value : str
            Path to Allure report folder.

        Returns
        -------
        None
        """
        self.__current_allure_report_folder = value
        return

    @property
    def current_robot_report_folder(self) -> str:
        """Current Robot report folder.

        Getter of __current_robot_report_folder

        Returns
        -------
        str
            Value of __current_robot_report_folder
        """
        return self.__current_robot_report_folder

    @current_robot_report_folder.setter
    def current_robot_report_folder(self, value: str) -> None:
        """Set current Robot report folder.

        Setter of __current_robot_report_folder

        Parameters
        ----------
        value : str
            Path to Robot report folder.

        Returns
        -------
        None
        """
        self.__current_robot_report_folder = value
        return

    @property
    def current_log_folder(self) -> str:
        """Current log folder.

        Getter of __current_log_folder

        Returns
        -------
        str
            Value of __current_log_folder
        """
        return self.__current_log_folder

    @current_log_folder.setter
    def current_log_folder(self, value: str) -> None:
        """Set current log folder.

        Setter of __current_log_folder

        Parameters
        ----------
        value : str
            Path to current log folder.

        Returns
        -------
        None
        """
        self.__current_log_folder = value
        return

    @property
    def current_doc_folder(self) -> str:
        """Current document folder.

        Getter of __current_doc_folder

        Returns
        -------
        str
            Value of __current_doc_folder
        """
        return self.__current_doc_folder

    @current_doc_folder.setter
    def current_doc_folder(self, value: str) -> None:
        """Set current doc folder.

        Setter of __current_doc_folder

        Parameters
        ----------
        value : str
            Path to current doc folder.

        Returns
        -------
        None
        """
        self.__current_doc_folder = value
        return

    @property
    def current_screenshot_folder(self) -> str:
        """Current screenshot folder.

        Getter of __current_screenshot_folder

        Returns
        -------
        str
            Value of __current_screenshot_folder
        """
        return self.__current_screenshot_folder

    @current_screenshot_folder.setter
    def current_screenshot_folder(self, value: str) -> None:
        """Set current screenshot folder.

        Setter of __current_screenshot_folder

        Parameters
        ----------
        value : str
            Path to current screenshot folder.

        Returns
        -------
        None
        """
        self.__current_screenshot_folder = value
        return

    @property
    def current_sys_log_robot_path(self) -> str:
        """Current system log Robot Path.

        Getter of __current_syslog_robot_path

        Returns
        -------
        str
            Value of __current_syslog_robot_path
        """
        return self.__current_syslog_robot_path

    @current_sys_log_robot_path.setter
    def current_sys_log_robot_path(self, value: str) -> None:
        """Set current system log Robot path.

        Setter of __current_sys_log_robot_path

        Parameters
        ----------
        value : str
            Path to current syslog robot

        Returns
        -------
        None
        """
        self.__current_syslog_robot_path = value
        return

    @property
    def report_server_info(self) -> str:
        """Absolute path to report_server_info.json

        Getter of __report_server_info

        Returns
        -------
        dict
            Absolute path to report_server_info.json
        """
        return self.__report_server_info


"""
This global variable is a instance of InternalPath, it will store state of
InternalPath during execution progressing and improve performance.
"""
__WORKSPACE_PATH = InternalPath()


def inter_path() -> InternalPath:
    """Internal Path.

    This function actually dose not do anything but return __WORKSPACE_PATH.

    The purpose of this function is avoiding error when import an instance.

    Returns
    -------
    InternalPath
        Value of __WORKSPACE_PATH
    """
    return __WORKSPACE_PATH
