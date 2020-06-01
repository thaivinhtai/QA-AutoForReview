#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

from sqa_mobile_app.lib.ui_locator.versions import LoginScreen, SettingScreen,\
    PatientNavigationFooter


"""
Login Screen.
"""
LOGIN_SCREEN_USERNAME_FIELD = LoginScreen.username_field
LOGIN_SCREEN_PASSWORD_FIELD = LoginScreen.password_field
LOGIN_SCREEN_UN_HIDE_PASSWORD_BUTTON = LoginScreen.un_hide_password_button
LOGIN_SCREEN_LOGIN_BUTTON = LoginScreen.login_button
LOGIN_SCREEN_FORGOT_PASSWORD = LoginScreen.forgot_password
LOGIN_SCREEN_FB_LOGIN_BUTTON = LoginScreen.fb_login_button
LOGIN_SCREEN_GG_LOGIN_BUTTON = LoginScreen.gg_login_button
LOGIN_SCREEN_REGISTER_NOW = LoginScreen.register_now


"""
Patient navigation footer
"""
PATIENT_NAVIGATION_FOOTER_DASHBOARD = PatientNavigationFooter.dashboard_button
PATIENT_NAVIGATION_FOOTER_CONTACT = PatientNavigationFooter.contact_button
PATIENT_NAVIGATION_FOOTER_NOTIFICATION = \
    PatientNavigationFooter.notification_button
PATIENT_NAVIGATION_FOOTER_SETTING = PatientNavigationFooter.setting_button


"""
Setting Screen
"""
SETTING_SCREEN_LOGOUT_IMG_BTN = SettingScreen.logout_img_btn
SETTING_SCREEN_LOGOUT_IMG_DIALOG_OK_BTN = \
    SettingScreen.logout_img_dialog_ok_btn
SETTING_SCREEN_LOGOUT_IMG_DIALOG_CANCEL_BTN = \
    SettingScreen.logout_img_dialog_cancel_btn
SETTING_SCREEN_LOGOUT_DIALOG_OK_BTN = SettingScreen.logout_dialog_ok_btn
SETTING_SCREEN_LOGOUT_DIALOG_CANCEL_BTN = \
    SettingScreen.logout_img_dialog_cancel_btn
