# -*- coding: utf-8 -*-
#
# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the
# License.
#
import unittest
import json

from ask_sdk_model_runtime import (
    ApiClientRequest, DefaultApiClient, ApiClientException)

from .data.mock_response_object import MockResponse

try:
    import mock
except ImportError:
    from unittest import mock


class TestDefaultApiClient(unittest.TestCase):
    def setUp(self):
        self.valid_request = ApiClientRequest(
            method="GET", url="https://test.com", body=None, headers=None)
        self.valid_mock_response = MockResponse(
            json_data="some test data", status_code=200)
        self.test_api_client = DefaultApiClient()

    def test_convert_null_header_tuples_to_dict(self):
        test_headers_list = None
        expected_headers_dict = {}

        self.assertEqual(self.test_api_client._convert_list_tuples_to_dict(
            test_headers_list), expected_headers_dict, (
            "DefaultApiClient failed to convert null headers list to empty "
            "dict object"))

    def test_convert_header_tuples_to_dict(self):
        test_headers_list = [
            ("header_1", "test_1"), ("header_2", "test_2"),
            ("header_1", "test_3")]
        expected_headers_dict = {
            "header_1": "test_1, test_3", "header_2": "test_2"}

        self.assertEqual(self.test_api_client._convert_list_tuples_to_dict(
            test_headers_list), expected_headers_dict, (
            "DefaultApiClient failed to convert header list of tuples to "
            "dictionary format needed for http "
            "request call"))

    def test_convert_null_header_dict_to_tuples(self):
        test_headers_dict = None
        expected_headers_list = []

        self.assertEqual(self.test_api_client._convert_dict_to_list_tuples(
            test_headers_dict), expected_headers_list, (
            "DefaultApiClient failed to convert null headers dict to empty "
            "list object"))

    def test_convert_header_dict_to_tuples(self):
        test_headers_dict = {
            "header_1": "test_1, test_3", "header_2": "test_2",
            "header_3": "test_4,"}
        expected_headers_list = [
            ("header_1", "test_1"), ("header_1", "test_3"),
            ("header_2", "test_2"), ("header_3", "test_4")]

        self.assertEqual(set(self.test_api_client._convert_dict_to_list_tuples(
            test_headers_dict)), set(
            expected_headers_list), (
            "DefaultApiClient failed to convert headers dict to list of "
            "tuples format for ApiClientResponse"))

    def test_resolve_valid_http_method(self):
        with mock.patch("requests.get",
                        side_effect=lambda *args, **kwargs:
                        self.valid_mock_response):
            try:
                actual_response = self.test_api_client.invoke(
                    self.valid_request)
            except:
                # Should never reach here
                raise Exception("DefaultApiClient couldn't resolve valid "
                                "HTTP Method for calling")

    def test_resolve_invalid_http_method_throw_exception(self):
        test_invalid_method_request = ApiClientRequest(
            method="GET_TEST", url="http://test.com", body=None, headers=None)

        with mock.patch("requests.get",
                        side_effect=lambda *args, **kwargs:
                        self.valid_mock_response):
            with self.assertRaises(ApiClientException) as exc:
                self.test_api_client.invoke(test_invalid_method_request)

            self.assertIn("Invalid request method: GET_TEST", str(exc.exception))

    def test_invoke_http_method_throw_exception(self):
        with mock.patch("requests.get",
                        side_effect=Exception("test exception")):
            with self.assertRaises(ApiClientException) as exc:
                self.test_api_client.invoke(self.valid_request)

            self.assertIn("Error executing the request: test exception", str(exc.exception))

    def test_api_client_invoke_with_method_headers_processed(self):
        self.valid_request.headers = [
            ("request_header_1", "test_1"), ("request_header_2", "test_2"),
            ("request_header_1", "test_3")]
        self.valid_request.method = "PUT"

        test_response = MockResponse(
            headers={
                "response_header_1": "test_1, test_3",
                "response_header_2": "test_2", "response_header_3": "test_4,"},
            status_code=400,
            json_data="test response body")

        with mock.patch("requests.put",
                        side_effect=lambda *args, **kwargs: test_response):
            actual_response = self.test_api_client.invoke(self.valid_request)

            self.assertEqual(set(actual_response.headers), set([
                ("response_header_1", "test_1"),
                ("response_header_1", "test_3"),
                ("response_header_2", "test_2"),
                ("response_header_3", "test_4")]), (
                "Response headers from client doesn't match with the "
                "expected headers"))

            self.assertEqual(actual_response.status_code, 400, (
                "Status code from client response doesn't match with the "
                "expected response status code"))

            self.assertEqual(actual_response.body, "test response body", (
                "Body from client response doesn't match with the expected "
                "response body"))

    def test_api_client_invoke_with_http_url_throw_error(self):
        test_invalid_url_scheme_request = ApiClientRequest(
            method="GET", url="http://test.com", body=None, headers=None)

        with mock.patch("requests.get",
                        side_effect=lambda *args, **kwargs:
                        self.valid_mock_response):
            with self.assertRaises(ApiClientException) as exc:
                self.test_api_client.invoke(test_invalid_url_scheme_request)

            self.assertIn("Requests against non-HTTPS endpoints are not allowed.", str(exc.exception))

    def test_api_client_invoke_with_http_case_sensitive_url_throw_error(self):
        test_invalid_url_scheme_request = ApiClientRequest(
            method="GET", url="HTTP://test.com", body=None, headers=None)

        with mock.patch("requests.get",
                        side_effect=lambda *args, **kwargs:
                        self.valid_mock_response):
            with self.assertRaises(ApiClientException) as exc:
                self.test_api_client.invoke(test_invalid_url_scheme_request)

            self.assertIn("Requests against non-HTTPS endpoints are not allowed.", str(exc.exception))

    def test_api_client_invoke_with_no_url_schema_throw_error(self):
        test_invalid_url_scheme_request = ApiClientRequest(
            method="GET", url="test.com", body=None, headers=None)

        with mock.patch("requests.get",
                        side_effect=lambda *args, **kwargs:
                        self.valid_mock_response):
            with self.assertRaises(ApiClientException) as exc:
                self.test_api_client.invoke(test_invalid_url_scheme_request)

            self.assertIn("Requests against non-HTTPS endpoints are not allowed.", str(exc.exception))

    def test_api_client_send_request_with_raw_data_serialized_for_json_content(
            self):
        test_data = "test\nstring"
        self.valid_request.body = "test\nstring"
        self.valid_request.method = "POST"
        headers = [("Content-type", "application/json")]
        self.valid_request.headers = headers

        with mock.patch(
                "requests.post",
                side_effect=lambda *args, **kwargs: self.valid_mock_response
        ) as mock_put:
            actual_response = self.test_api_client.invoke(self.valid_request)
            mock_put.assert_called_once_with(
                data=json.dumps(test_data),
                headers={'Content-type': 'application/json'},
                url=self.valid_request.url)

    def test_api_client_send_request_with_raw_data_unchanged_for_non_json_content(
            self):
        test_data = "test\nstring"
        self.valid_request.body = "test\nstring"
        self.valid_request.method = "POST"

        with mock.patch(
                "requests.post",
                side_effect=lambda *args, **kwargs: self.valid_mock_response
        ) as mock_put:
            actual_response = self.test_api_client.invoke(self.valid_request)
            mock_put.assert_called_once_with(
                data=test_data, headers={},
                url=self.valid_request.url)