#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Custom logging module.
"""

from robot.api import logger
from datetime import datetime


class CustomLogger:
    """Custom logger.

    This class is a custom logger for the framework. Via implement module
    logger of robot.api library, this class provides logging for multiple
    levels (info, debug, warn, error).

    Parameters
    ----------
    current_test_name : str
        Current executing test case's name.

    Attributes
    ----------
    __current_test_name : str
        Current executing test case's name.
    __robot_logging : robot.api.logger
        Robot logger instance.

    Methods
    -------
    __log_to_console(self, level: str, message: str) -> None
        Private method, print log to console.

    debug(self, message: str) -> None:
        Call Logger at Debug level.

    info(self, message: str, timestamp=True) -> None:
        Call Logger at Info level.

    warn(self, message: str) -> None:
        Call Logger at Warn level.

    error(self, message: str) -> None:
        Call Logger at Error level.
    """

    def __init__(self, current_test_name):
        """Constructor."""
        self.__current_test_name = current_test_name
        self.__robot_logging = logger

    def __log_to_console(self, level: str, message: str) -> None:
        """Log to console.

        This method print log to console.

        Parameters
        ----------
        level : str
            Level of log.
        message : str
            Content to be logged.

        Returns
        -------
        None
        """
        current = datetime.now().strftime("%Y-%m-%d %H-%M-%S.%f")
        self.__robot_logging.console(current + ' - ' + level + ' - ' + message)

    def debug(self, message: str) -> None:
        """Debug.

        This method logs at Debug level.

        Parameters
        ----------
        message : str
            Content to be logged.

        Returns
        -------
        None
        """
        self.__robot_logging.debug(message)
        self.__log_to_console(level='DEBUG', message=message)

    def info(self, message: str, timestamp=True) -> None:
        """Info.

        This method logs at Info level.

        Parameters
        ----------
        message : str
            Content to be logged.
        timestamp : bool
            True -> add timestamp to message.

        Returns
        -------
        None
        """
        if timestamp:
            self.__robot_logging.info(message)
            self.__log_to_console(level='INFO', message=message)
        else:
            self.__robot_logging.console(message)

    def warn(self, message: str) -> None:
        """Warn.

        This method logs at Warn level.

        Parameters
        ----------
        message : str
            Content to be logged.

        Returns
        -------
        None
        """
        self.__robot_logging.warn(message)
        self.__log_to_console(level='WARN', message=message)

    def error(self, message: str) -> None:
        """Error.

        This method logs at Error level.

        Parameters
        ----------
        message : str
            Content tobe logged.

        Returns
        -------
        None
        """
        self.__robot_logging.error(message)
        self.__log_to_console(level='ERROR', message=message)

    @property
    def current_test_name(self) -> str:
        """Get current test name.

        Returns
        -------
        str
        """
        return self.__current_test_name
