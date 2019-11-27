# -*- coding: utf-8 -*-
#
# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may
# not use this file except in compliance with the License. A copy of the
# License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.
#
import typing

from .api_client_message import ApiClientMessage

if typing.TYPE_CHECKING:
    from typing import List, Tuple


class ApiClientRequest(ApiClientMessage):
    """Represents a request sent from Service Clients to an
    :py:class:`ask_sdk_model_runtime.api_client.ApiClient` implementation.

    :param headers: List of header tuples
    :type headers: list[tuple[str, str]]
    :param body: Body of the message
    :type body: str
    :param url: Url of the request
    :type url: str
    :param method: Method called with the request
    :type method: str
    """

    def __init__(self, headers=None, body=None, url=None, method=None):
        # type: (List[Tuple[str, str]], str, str, str) -> None
        """Represents a request sent from Service Clients to an
        :py:class:`ask_sdk_model_runtime.api_client.ApiClient`
        implementation.

        :param headers: List of header tuples
        :type headers: list[tuple[str, str]]
        :param body: Body of the message
        :type body: str
        :param url: Url of the request
        :type url: str
        :param method: Method called with the request
        :type method: str
        """
        super(ApiClientRequest, self).__init__(headers=headers, body=body)
        self.url = url
        self.method = method
