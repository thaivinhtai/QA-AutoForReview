#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module contains .
"""

from sqa_web_portal.lib.common_vars import ROOT_URL


NOTIFICATION_BUTTON = 'id:notification-bell-btn'


class LoginPage:
    """
    This class contains ui locator of login page's elements.
    """
    url = ROOT_URL + '/login'
    username_field = "id:username"
    password_field = "id:password"
    login_button = "id:btn-login"


class OverviewPage:
    """
    This class contains ui locator of Overview page's elements.
    """
    url = ROOT_URL + '/overview'
