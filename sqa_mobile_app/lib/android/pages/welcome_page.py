#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""


class Navigator:
    """

    """

    def __init__(self):
        self.__get_started_btn = "xpath:/hierarchy/android.widget.FrameLayout\
/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View\
/android.view.View/android.view.View/android.view.View/android.view.View\
/android.view.View[2]"

    @property
    def start_btn(self):
        """

        Returns
        -------

        """
        return self.__get_started_btn


startBtn = Navigator().start_btn
