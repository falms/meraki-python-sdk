# -*- coding: utf-8 -*-

from meraki.decorators import lazy_property
from meraki.configuration import Configuration
from meraki.meraki_client import MerakiClient
from meraki.controllers_login.login_controller import LoginController


class MerakiClientLogin(MerakiClient):

    config = Configuration

    @lazy_property
    def login(self):
        return LoginController()

    def __init__(self, email=None, password=None):
        Configuration.login_email = email
        Configuration.login_password = password
