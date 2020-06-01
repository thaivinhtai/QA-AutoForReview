#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module handles custom testing library generating.
"""

from robot.libdoc import libdoc
from robot.testdoc import testdoc

from sqa_engine.utilities.workspace_vars import inter_path
from sqa_engine.utilities.test_cases_management.test_suite_retriever import\
    get_module_children


def generate_docs(test_module: str, test_design: str) -> None:
    """Generate documentation.

    This function uses robot libdoc and robot testdoc to generates
    documentation of custom keyword library and test cases documentations,
    base on module and test domain.

    Parameters
    ----------
    test_module : str
        Test module {mobile_app, web_portal, rest_api}
    test_design : str
        Test domain specification

    Returns
    -------
    None
    """
    packages = get_module_children(module_name=test_module)
    test_suite = f'{packages["test_design"]}/{test_design}'
    robot_file = f'{test_suite}/{test_design}.robot'
    keywords_file = f'{packages["lib"]}/common_keywords.py'

    doc_out_file = f'{inter_path().current_doc_folder}/\
{test_design}_document.html'
    lib_out_file = f'{inter_path().current_doc_folder}/keywords_document.html'

    libdoc(library_or_resource=keywords_file, outfile=lib_out_file,
           name='', version='', format=None, docformat='HTML')
    testdoc(robot_file, doc_out_file, title='',
            name='', version='', format=None, docformat='HTML')
    return
