#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Software versioning is the process of assigning unique version numbers to
unique states of computer software. These numbers are generally assigned
increasing order and correspond to new developments in the software. Modern
computer software is often tracked using two different software versioning
schemes—internal version number that may be incremented many times in a single
day, such as a revision control number, and a released version that typically
changes far less often, such as semantic versioning or a project codename.

Semantic versioning is a simple set of rules and requirements that dictate
how version numbers are assigned and incremented. These rules are based on
but not necessarily limited to pre-existing widespread common practices in
use in both closed and open-source software.
Version numbers are denoted using a standard tuple of integers:

                                major.minor.patch

        A 'major' version identifies the product stage of the project. The
        basic intent is that 'major' versions are incompatible, large-scale
        upgrades of the software component. This enables a check of a client
        application against the latest version of the software component to
        ensure compatibility. If there is a discrepancy between the two,
        the client application MUST be updated accordingly.

        A 'minor' version is incremented when substantial new functionality or
        improvement are introduced; the 'major' version number doesn't change.
        A 'minor' version retains backward compatibility with older 'minor'
        versions. It is NOT forward compatible as a previous minor version
        doesn't include new functionality or improvement that has been
        introduced in this newer 'minor' version.

        A 'patch' version is incremented when bugs were fixed or implementation
        details were refactored. The major and 'minor' version don't change.
        A 'patch' version is backward and forward compatible with older and
        newer patches of the same 'major' and 'minor' version.
"""


class Version:
    """Versioning handler.

    This class defines a "version data structure" that contains method to do
    comparison between Version instances.

    Parameters
    ----------
    version_in_string : str
         Version in string format that collected from user's input.
         The structure must be x.x.x which "x" are number.

    Attributes
    ----------
    major : int
        Major version identifier.
    minor : int
        Minor version identifier.
    patch : int
        Patch version identifier.
    """

    def __init__(self, version_in_string: str):
        __version = list()
        if version_in_string:
            __version = version_in_string.split('.')
        while len(__version) < 3:
            __version.append('0')
        self.major = int(__version[0])
        self.minor = int(__version[1])
        self.patch = int(__version[2])

    def __repr__(self) -> str:
        """Compute "Official" String Representations."""
        return f"Version({self.major}, {self.minor}, {self.patch})"

    def __str__(self) -> str:
        """Compute "Informal" String Representation."""
        return f"{self.major}.{self.minor}.{self.patch}"

    def __lt__(self, other) -> bool:
        """self < other"""
        try:
            if self.major < other.major:
                return True
            if self.major > other.major:
                return False
            if self.minor < other.minor:
                return True
            if self.minor > other.minor:
                return False
            if self.patch < other.patch:
                return True
            if self.patch > other.patch:
                return False
            return False
        except TypeError:
            raise TypeError("Can not compare.")

    def __le__(self, other) -> bool:
        """self <= other"""
        less = self.__lt__(other)
        equal = self.__eq__(other)
        if less or equal:
            return True
        return False

    def __eq__(self, other) -> bool:
        """self == other"""
        try:
            if self.major == other.major and self.minor == other.minor and\
                    self.patch == other.patch:
                return True
            return False
        except TypeError:
            raise TypeError("Can not compare.")

    def __ne__(self, other) -> bool:
        """self != other"""
        try:
            if self.major != other.major:
                return True
            if self.minor != other.minor:
                return True
            if self.patch != other.patch:
                return True
            return False
        except TypeError:
            raise TypeError("Can not compare.")

    def __gt__(self, other) -> bool:
        """self > other"""
        try:
            if self.major > other.major:
                return True
            if self.major < other.major:
                return False
            if self.minor > other.minor:
                return True
            if self.minor < other.minor:
                return False
            if self.patch > other.patch:
                return True
            if self.patch < other.patch:
                return False
            return False
        except TypeError:
            raise TypeError("Can not compare.")

    def __ge__(self, other) -> bool:
        """self >= other"""
        greater = self.__gt__(other)
        equal = self.__eq__(other)
        if greater or equal:
            return True
        return False
