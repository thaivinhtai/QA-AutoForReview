#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Package workspace_vars contains modules that relate to environ variables of
project.
"""

from .internal_path import inter_path
from .env_vars_setup import\
    set_python_path_env_var, set_robot_syslog_file_env_var,\
    set_android_home_env_var, set_version_env_var, set_proxy
