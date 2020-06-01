#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

from os import environ

# __version_package__ = environ['E_HEALTH_VERSION']
__version__ = environ['E_HEALTH_VERSION'].replace('.', '_', 2)

# print(__version_package__)

__import_module__ = ('sqa_mobile_app.lib.ui_locator.versions.' +
                     __version__ + '.' + __version__)

print(__import_module__)

__page__ = __import__(__import_module__, globals(),
                      locals(), ['LoginScreen', 'SettingScreen',
                                 'PatientNavigationFooter'], 0)

LoginScreen = __page__.LoginScreen
SettingScreen = __page__.SettingScreen
PatientNavigationFooter = __page__.PatientNavigationFooter
