#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module contains list of all test case in demo_func Test Design
Specification.
"""


class SequenceDemoFunc:
    """
    This class have one property that is all names of test case in TDS
    demo_func.
    """

    def __init__(self):
        """Constructor."""
        self.__list_test_cases = list()
        self.__list_test_cases.append("Demo_Logout_Func_1")

    @property
    def list_test_cases(self):
        return self.__list_test_cases


def get_list_test_cases() -> list:
    """Get list test cases.

    Returns
    -------
    list
        list of all names of test cases in TDS auth_Service
    """
    return SequenceDemoFunc().list_test_cases
