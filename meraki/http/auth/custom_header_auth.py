# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

from meraki.configuration import Configuration
from meraki.http.http_method_enum import HttpMethodEnum


class CustomHeaderAuth:

    @staticmethod
    def apply(http_request):
        """ Add custom authentication to the request.

        Args:
            http_request (HttpRequest): The HttpRequest object to which 
                authentication will be added.

        """                
        http_request.add_header("X-Cisco-Meraki-API-Key", Configuration.x_cisco_meraki_api_key)

        if http_request.http_method not in [HttpMethodEnum.GET, HttpMethodEnum.HEAD]:
            http_request.add_header("X-CSRF-Token", Configuration.csrf_token)
