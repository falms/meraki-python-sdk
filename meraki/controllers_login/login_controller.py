# -*- coding: utf-8 -*-

from meraki.api_helper import APIHelper
from meraki.configuration import Configuration
from meraki.controllers.base_controller import BaseController
from meraki.exceptions.api_exception import APIException
from meraki.http.auth.custom_header_auth import CustomHeaderAuth


class LoginController(BaseController):

    def login(self, email=None, password=None, options=dict()):
        _url_path = '/login/login'
        _query_builder = Configuration.dash_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        _edition = options.get('edition', 'Enterprise')

        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8',
            'x-meraki-user-agent': 'DashboardMobile.' + _edition
        }

        _login = {
            'email': email,
            'password': password
        }

        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(_login))
        _context = self.execute_request(_request)
        self.validate_response(_context)

        _response = APIHelper.json_deserialize(_context.response.raw_body)

        if _response.get('mode') == 'org_choose':
            if 'eid' not in options.keys():
                _eids = list(map(lambda org: org['eid'], _response.get('orgs')))
                raise APIException('Please choose organization(eid) from {}.'.format(_eids), _context)
            _response = self.org_choose(options.get('eid'))

        if not _response.get('success', False):
            raise APIException('Could not login. Current mode: {}'.format(_response.get('mode')), _context)

        # Set shard uri for later API calls
        if 'eid' in options.keys():
            _org = list(filter(lambda org: org['eid'] == options.get('eid'), _response['orgs']))[0]
        else:
            _org = _response['orgs'][0]

        _shard_origin = 'https://n{}.meraki.com'.format(_org['shard_id'])
        Configuration.base_uri = _shard_origin + '/api/v0'
        Configuration.dash_uri = _shard_origin

        return _response

    def org_choose(self, eid=None):
        _url_path = '/login/org_choose'
        _query_builder = Configuration.dash_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        _params = {
            'eid': eid
        }

        _request = self.http_client.post(_query_url, headers=_headers,
                                         parameters=APIHelper.json_serialize(_params))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        return APIHelper.json_deserialize(_context.response.raw_body)

    def logout(self):
        _url_path = '/login/logout'
        _query_builder = Configuration.dash_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        _headers = {
            'accept': 'application/json',
        }

        _request = self.http_client.get(_query_url, headers=_headers)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        return APIHelper.json_deserialize(_context.response.raw_body)
