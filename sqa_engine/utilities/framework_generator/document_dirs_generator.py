#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module generate folders that stores documentation of test cases and test
Library.
"""

from datetime import datetime
from os import mkdir, path
from sqa_engine.utilities.workspace_vars import inter_path


def generate_docs_folder(module_name: str, test_design: str,
                         version: str) -> None:
    """Generate folder for documentation.

    This function generates folder that stores documentations before generate
    document files.

    The folder structure are classified by:
        workspace/{date}/{module}/{version}/{current_time}-{test_design}

    Parameters
    ----------
    module_name : str
        Module name {mobile_app, web_portal, rest_api}
    test_design : str
        Test suite specification domain
    version : str
        Version of documentations

    Returns
    -------
    None
    """
    today = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H-%M-%S")
    doc_path = inter_path().document_folder

    today_doc_folder = f'{doc_path}/{today}'
    module_doc_folder = f'{today_doc_folder}/{module_name}'
    version_doc_folder = f'{module_doc_folder}/{version}'
    executing_doc_folder = f'{version_doc_folder}/{current_time}-{test_design}'

    if not path.exists(doc_path):
        mkdir(doc_path)
    if not path.exists(today_doc_folder):
        mkdir(today_doc_folder)
    if not path.exists(module_doc_folder):
        mkdir(module_doc_folder)
    if not path.exists(version_doc_folder):
        mkdir(version_doc_folder)
    if not path.exists(executing_doc_folder):
        mkdir(executing_doc_folder)

    # update path to InternalPath instance attribute.
    inter_path().current_doc_folder = executing_doc_folder

    return
