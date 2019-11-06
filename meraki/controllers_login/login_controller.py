# -*- coding: utf-8 -*-

from meraki.api_helper import APIHelper
from meraki.configuration import Configuration
from meraki.controllers.base_controller import BaseController


class LoginController(BaseController):

    def login(self):
        _query_url = APIHelper.clean_url('https://dashboard.meraki.com/login/login')

        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8',
            'x-meraki-user-agent': 'DashboardMobile.Go'
        }

        login = {
            'email': Configuration.login_email,
            'password': Configuration.login_password
        }

        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(login))
        _context = self.execute_request(_request)
        self.validate_response(_context)

        _response = APIHelper.json_deserialize(_context.response.raw_body)

        # Set shard uri for later API calls
        Configuration.base_uri = _response['user']['path'] + 'api/v0'

        return APIHelper.json_deserialize(_context.response.raw_body)

    def logout(self):
        _query_url = APIHelper.clean_url('https://dashboard.meraki.com/login/logout')

        _headers = {
            'accept': 'application/json',
        }

        _request = self.http_client.get(_query_url, headers=_headers)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        _response = APIHelper.json_deserialize(_context.response.raw_body)

        return APIHelper.json_deserialize(_context.response.raw_body)
