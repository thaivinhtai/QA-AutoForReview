#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

from os import environ


__version__ = environ['VERSION'].replace('.', '_', 2)

__import_module__ = 'sqa_web_portal.lib.ui_locator.versions.' + __version__

__page__ = __import__(__import_module__, globals(),
                      locals(), ['LoginPage', 'OverviewPage'], 0)

LoginPage = __page__.LoginPage
OverviewPage = __page__.OverviewPage
