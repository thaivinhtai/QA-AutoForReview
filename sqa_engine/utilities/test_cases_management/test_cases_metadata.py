#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module handles test cases metadata.

    Functions in this module:

        +   get_test_metadata(name: str, tags: list) -> str
                Get test case metadata via tags.

        +   get_tags(robot_suite: str) -> tuple
                Get tags of test suite and tags of each test cases
"""


from robot.parsing import TestData


def foo():
    pass


def get_test_metadata(name: str, tags: list) -> str:
    """Get test case metadata.

    This function get test case metadata via tags of that test case.

    Parameters
    ----------
    name : str
        Name of metadata.
    tags : list
        List contains all tags of test case.

    Returns
    -------
    str
        Value of metadata.
    """
    prefix = name.lower() + '='
    for tag in tags:
        if tag.lower().startswith(prefix):
            return tag[len(prefix):]
    raise ValueError(f"Metadata {name} not found!")


def get_tags(robot_suite: str) -> tuple:
    """Get tags.

    This function get robot file as argument and return a tuple of:
        + a list of all tags in test suite
        + a dictionary of pairs "test case name": list of tags.

    Parameters
    ----------
    robot_suite : str
        Path to robot file.

    Returns
    -------
    tuple
        list : all tags in test suite.
        dict : {"test case name": [tag1, tag2, ...].
    """
    suite = TestData(parent=None, source=robot_suite)

    tags = list()
    tags_by_test_case = dict()

    if suite.setting_table.force_tags:
        tags.extend(suite.setting_table.force_tags.value)

    if suite.setting_table.default_tags:
        tags.extend(suite.setting_table.default_tags.value)

    for test_case in suite.testcase_table.tests:
        if test_case.tags:
            tags.extend(test_case.tags.value)
            tags_by_test_case[test_case.name] = test_case.tags

    for child_suite in suite.children:
        tags.extend(get_tags(child_suite))

    return tags, tags_by_test_case
