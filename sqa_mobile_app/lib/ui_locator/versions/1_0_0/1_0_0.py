#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

__CURRENT_DIR__ = Path(__file__).parent.absolute()
ROOT = f'{__CURRENT_DIR__}/image_static/'

print(ROOT)

"""
This module contains .
"""


class LoginScreen:
    """
    This class contains ui locator of login page's elements.
    """
    username_field = "xpath:/hierarchy/android.widget.FrameLayout/\
android.widget.LinearLayout/android.widget.FrameLayout/\
android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/\
android.view.View/android.view.View/android.widget.EditText[1]"
    password_field = "xpath:/hierarchy/android.widget.FrameLayout/\
android.widget.LinearLayout/android.widget.FrameLayout/\
android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/\
android.view.View/android.view.View/android.widget.EditText[2]"
    un_hide_password_button = "xpath:hierarchy/android.widget.FrameLayout/\
android.widget.LinearLayout/android.widget.FrameLayout/\
android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/\
android.view.View/android.view.View/android.widget.EditText[2]/\
android.widget.Button"
    forgot_password = "xpath:/hierarchy/android.widget.FrameLayout/\
android.widget.LinearLayout/android.widget.FrameLayout/\
android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/\
android.view.View/android.view.View/android.view.View[2]"
    login_button = "xpath:/hierarchy/android.widget.FrameLayout/\
android.widget.LinearLayout/android.widget.FrameLayout/\
android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/\
android.view.View/android.view.View/android.widget.Button[1]"
    fb_login_button = "xpath:/hierarchy/android.widget.FrameLayout/\
android.widget.LinearLayout/android.widget.FrameLayout/\
android.widget.FrameLayout/android.widget.FrameLayout/\
android.view.View/android.view.View/android.view.View/android.widget.Button[2]"
    gg_login_button = "xpath:/hierarchy/android.widget.FrameLayout/\
android.widget.LinearLayout/android.widget.FrameLayout/\
android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/\
android.view.View/android.view.View/android.widget.Button[3]"
    register_now = "xpath:/hierarchy/android.widget.FrameLayout/\
android.widget.LinearLayout/android.widget.FrameLayout/\
android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/\
android.view.View/android.view.View/android.view.View[5]"


class PatientNavigationFooter:
    """

    """
    dashboard_button = "xpath:/hierarchy/android.widget.FrameLayout/\
android.widget.LinearLayout/android.widget.FrameLayout/\
android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/\
android.view.View/android.view.View/android.view.View[2]/android.view.View"
    contact_button = "xpath:hierarchy/android.widget.FrameLayout/\
android.widget.LinearLayout/android.widget.FrameLayout/\
android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/\
android.view.View/android.view.View/android.view.View[3]/android.view.View"
    notification_button = "xpath:/hierarchy/android.widget.FrameLayout/\
android.widget.LinearLayout/android.widget.FrameLayout/\
android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/\
android.view.View/android.view.View/android.view.View[4]/android.view.View"
    setting_button = "xpath:/hierarchy/android.widget.FrameLayout/\
android.widget.LinearLayout/android.widget.FrameLayout/\
android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/\
android.view.View/android.view.View/android.view.View[5]/android.view.View"


class PatientDashboard:
    """

    """
    steps_view = "xpath:/hierarchy/android.widget.FrameLayout/\
android.widget.LinearLayout/android.widget.FrameLayout/\
android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/\
android.view.View/android.view.View/android.view.View[1]/android.view.View/\
android.view.View/android.view.View[2]/\
android.widget.ScrollView/android.view.View"
    heart_rate_view = "xpath:/hierarchy/android.widget.FrameLayout/\
android.widget.LinearLayout/android.widget.FrameLayout/\
android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/\
android.view.View/android.view.View/android.view.View[1]/android.view.View/\
android.view.View/android.view.View[2]/\
android.widget.ScrollView/android.view.View"


class SettingScreen:
    """

    """
    logout_img_btn = f'{ROOT}setting_screen/logout.png'
    logout_img_dialog_ok_btn = f'{ROOT}setting_screen/logout_dialog_ok_btn.png'
    logout_img_dialog_cancel_btn = \
        f'{ROOT}setting_screen/logout_dialog_cancel_btn.png'
    logout_dialog_ok_btn = "xpath:/hierarchy/android.widget.FrameLayout/\
android.widget.LinearLayout/android.widget.FrameLayout/\
android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/\
android.view.View/android.view.View/android.view.View/android.view.View[3]"
    logout_dialog_cancel_btn = "xpath:/hierarchy/android.widget.FrameLayout/\
android.widget.LinearLayout/android.widget.FrameLayout/\
android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/\
android.view.View/android.view.View/android.view.View/android.view.View[2]"
