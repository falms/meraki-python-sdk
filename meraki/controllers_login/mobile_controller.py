# -*- coding: utf-8 -*-

from meraki.api_helper import APIHelper
from meraki.configuration import Configuration
from meraki.controllers.base_controller import BaseController


class MobileController(BaseController):

    def get_token(self):
        _url_path = '/mobile/token'
        _query_builder = Configuration.dash_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        _headers = {
            'accept': 'application/json',
            'x-meraki-user-agent': 'DashboardMobile'
        }

        _request = self.http_client.post(_query_url, headers=_headers)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        _response = APIHelper.json_deserialize(_context.response.raw_body)

        # Set CSRF Token for later API calls
        Configuration.csrf_token = _response['csrf_token']

        return APIHelper.json_deserialize(_context.response.raw_body)
