# -*- coding: utf-8 -*-

from meraki.api_helper import APIHelper
from meraki.configuration import Configuration
from meraki.controllers.base_controller import BaseController
from meraki.http.auth.custom_header_auth import CustomHeaderAuth


class GuestsController(BaseController):

    def get_guests(self):
        _url_path = '/manage/configure/guests'
        _query_builder = Configuration.dash_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        _headers = {
            'accept': 'application/json',
        }

        _request = self.http_client.get(_query_url, headers=_headers)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        _response = APIHelper.json_deserialize(_context.response.raw_body)

        return APIHelper.json_deserialize(_context.response.raw_body)

    def update_guest(self, options=dict()):
        self.validate_parameters(encrypted_network_id=options.get("encrypted_network_id"))

        _url_path = '/n/{encryptedNetworkId}/manage/configure/update_guests'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'encryptedNetworkId': options.get('encrypted_network_id', None)
        })
        _query_builder = Configuration.dash_uri
        _query_builder += _url_path
        _query_parameters = {
            'send_emails': options.get('send_emails', False)
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
                                                                    _query_parameters,
                                                                    Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        _headers = {
            'accept': 'application/json',
            'content-type': 'application/x-www-form-urlencoded',
        }

        _request = self.http_client.post(_query_url, headers=_headers,
                                         parameters=APIHelper.form_encode_parameters(options.get('update_guest')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        _response = APIHelper.json_deserialize(_context.response.raw_body)

        return APIHelper.json_deserialize(_context.response.raw_body)
