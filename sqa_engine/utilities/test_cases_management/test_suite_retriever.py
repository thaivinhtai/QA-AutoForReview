#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module contains functions that relate to retrieving test suite.

    Private functions:

        +   __to_camel_case(snake_str: str) -> str
                Converts snake case to camel case.

        +   __convert_path_to_module(path: str, module: str) -> str
                Converts a path and module name to Python's import form.

    Public function:

        +   get_module_children(module_name: str) -> dict
                Get a dictionary that stores path of sequence file, robot file
                and other metadata of module.

        +   get_list_test_cases_and_robot_file(module_name: str,
                                               test_design: str) -> tuple:
                Get list test cases and path of robot file.
"""

from os import listdir

from sqa_engine.utilities.workspace_vars.internal_path import inter_path


def __to_camel_case(snake_str: str) -> str:
    """To camel case.

    This private function converts snake case to camel case and inserts
    statement 'Sequence' at the beginning.

    Parameters
    ----------
    snake_str : str
        A string in snake case form.

    Returns
    -------
    str
        'Sequence' + '{camel_case}'
    """
    components = snake_str.split('_')
    return 'Sequence' + ''.join(component.title() for component in components)


def __convert_path_to_module(path: str, module: str) -> str:
    """Convert path to module.

    This private function converts a path and module name to Python's import
    form.

    Parameters
    ----------
    path : str
        A path.
    module : str
        A name.

    Returns
    -------
    str
        a string with construct: '{parent}.{child}'
    """
    path = path[path.find(f'sqa_{module}'):len(path) - 3]
    components = path.split('/')
    return f'{components[0]}.'\
        + '.'.join(component for component in components[1:])


def get_module_children(module_name: str) -> dict:
    """Get module's children.

    This module bases on module_name to get a dictionary that stores path of
    sequence file, robot file and other metadata of module.

    Parameters
    ----------
    module_name : str
        Name of module to be tested {mobile_app, web_portal, rest_api}

    Returns
    -------
    dict
        A dictionary that stores path of sequence file, robot file, metadata.
    """
    module_switcher = {
        'web_portal': inter_path().web_portal,
        'mobile_app': inter_path().mobile_app,
        'rest_api': inter_path().rest_api,
        'integration': inter_path().integration
    }
    module = module_switcher.get(module_name.lower())
    return module


def get_list_test_cases_and_robot_file(module_name: str,
                                       test_design: str) -> tuple:
    """Get list test cases and path of robot file.

    This function get list of test cases via calling method of sequence class
    of test domain. Also, return path to robot file that contains test suite
    as well.

    Parameters
    ----------
    module_name : str
        Name of test module {mobile_app, web_portal, rest_api}.
    test_design : str
        Test domain specification.

    Returns
    -------
    tuple
        list : list of test cases.
        str : path to robot file that contains test suite.
    """
    packages = get_module_children(module_name=module_name)

    test_suite_collection = dict()
    for suite in listdir(packages['test_design']):
        test_suite_collection[suite] = f'{packages["test_design"]}/{suite}'

    test_suite_to_be_executed = {
        'sequence_file': f'{test_suite_collection[test_design]}/\
sequence_{test_design}.py',
        'robot_file': f'{test_suite_collection[test_design]}/\
{test_design}.robot'
    }

    sequence_file = test_suite_to_be_executed['sequence_file']
    robot_file = test_suite_to_be_executed['robot_file']

    sequence_module = __convert_path_to_module(path=sequence_file,
                                               module=module_name)
    sequence_class = __to_camel_case(test_design)

    __import_module = __import__(sequence_module,
                                 globals(), locals(), [sequence_class], 0)

    list_test_cases = __import_module.get_list_test_cases()

    return list_test_cases, robot_file
