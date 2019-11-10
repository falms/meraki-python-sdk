# -*- coding: utf-8 -*-

from meraki.decorators import lazy_property
from meraki.configuration import Configuration
from meraki.meraki_client import MerakiClient
from meraki.controllers_login.login_controller import LoginController
from meraki.controllers_login.mobile_controller import MobileController
from meraki.controllers_login.guests_controller import GuestsController


class MerakiClientLogin(MerakiClient):

    config = Configuration

    @lazy_property
    def login(self):
        return LoginController()

    @lazy_property
    def mobile(self):
        return MobileController()

    @lazy_property
    def guests(self):
        return GuestsController()

    def __init__(self, email=None, password=None):
        Configuration.login_email = email
        Configuration.login_password = password
