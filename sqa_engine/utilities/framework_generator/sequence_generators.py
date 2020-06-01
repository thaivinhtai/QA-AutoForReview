#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module module handles python script generating.
"""

from sqa_engine.utilities.test_cases_management.test_suite_retriever import\
    get_module_children


def generate_sequence(test_module: str, test_design: str) -> None:
    """Generate sequence.

    This module rewrites the sequence of test suite base on the moderation of
    robot file. It will update the sequence_{test_design_name}.py

    Parameters
    ----------
    test_module : str
        Name of test module {mobile_app, web_portal, rest_api}
    test_design : str
        Test domain specification

    Returns
    -------
    None
    """
    packages = get_module_children(module_name=test_module)
    test_suite = f'{packages["test_design"]}/{test_design}'
    sequence_file = f'{test_suite}/sequence_{test_design}.py'
    robot_file = f'{test_suite}/{test_design}.robot'

    # Generate empty list to store names of test cases.
    list_test_cases = list()

    # Read content on Robot file.
    with open(robot_file, 'r') as robot_file_content:
        contents = robot_file_content.readlines()
        # Generate a temp list that store line index of test cases name.
        test_cases_index = list()

        # Add test case's index to temp list.
        for index, line in enumerate(contents):
            if line.startswith('*** Test Cases ***'):
                test_cases_index.append(index + 1)

        # Add statement that contents test case's name
        # to the fist generated list.
        for index in test_cases_index:
            list_test_cases.\
                append(f'        self.__list_test_cases.\
append("{contents[index][:-1]}")' + '\n')

    list_test_cases.sort()

    # Generate list that stores content of header and footer of sequence file.
    start_of_sequence_file = list()
    end_of_sequence_file = ['\n']

    # Open sequence file to get header and footer content.
    with open(sequence_file, 'r') as sequence_file_content:
        contents = sequence_file_content.readlines()
        temp_index = int()

        # Get header content.
        for index, line in enumerate(contents):
            start_of_sequence_file.append(line)
            if line.find('self.__list_test_cases = list()') != -1:
                temp_index = index
                break

        for index, line in enumerate(contents[temp_index:]):
            if line.find('@property') != -1:
                temp_index += index
                break

        # Get footer content.
        for line in contents[temp_index:]:
            end_of_sequence_file.append(line)

    # Full content to rewrite sequence file.
    contents_to_be_written =\
        start_of_sequence_file + list_test_cases + end_of_sequence_file

    # Rewrite sequence file.
    with open(sequence_file, 'w') as sequence:
        sequence.writelines(contents_to_be_written)

    print(*contents_to_be_written)

    return
