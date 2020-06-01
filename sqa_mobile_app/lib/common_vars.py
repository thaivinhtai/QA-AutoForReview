#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module contains common variables for testing purpose.
"""


from base64 import b64encode


ADMIN_ACCOUNT = {
    'username': 'randomuser',
    'password': '1234'
}
ADMIN_USERNAME = ADMIN_ACCOUNT.get("username")  # Default ADMIN username.
ADMIN_PASSWORD = ADMIN_ACCOUNT.get("password")  # Default ADMIN password.

DOCTOR_ACCOUNT = {
    'username': 'bbthinh',
    'password': '123456789'
}
DOCTOR_USERNAME = DOCTOR_ACCOUNT.get("username")  # Default DOCTOR username.
DOCTOR_PASSWORD = DOCTOR_ACCOUNT.get("password")  # Default DOCTOR password.

NORMAL_ACCOUNT = {
    'username': 'normaluser',
    'password': '123456789'
}
NORMAL_USERNAME = NORMAL_ACCOUNT.get("username")  # Default normal username.
NORMAL_PASSWORD = NORMAL_ACCOUNT.get("password")  # Default normal password.

DEFAULT_CLIENT_ID = 'browser'
DEFAULT_CLIENT_SECRET = 'K3k9SaGkHr3GSyrS'

CLIENT_AUTHORIZATION = \
    b64encode(f'{DEFAULT_CLIENT_ID}:{DEFAULT_CLIENT_SECRET}'.encode()) \
    .decode('utf-8')

ROOT_URL = 'https://ehealth-dev.pt-infra.net/'
