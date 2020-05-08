# coding: utf-8

#
# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file
# except in compliance with the License. A copy of the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for
# the specific language governing permissions and limitations under the License.
#

import pprint
import re  # noqa: F401
import six
import typing
from enum import Enum
from ask_smapi_model.v1.nlu.evaluations.paged_results_response import PagedResultsResponse


if typing.TYPE_CHECKING:
    from typing import Dict, List, Optional, Union
    from datetime import datetime
    from ask_smapi_model.v1.nlu.evaluations.links import LinksV1
    from ask_smapi_model.v1.nlu.evaluations.test_case import TestCaseV1
    from ask_smapi_model.v1.nlu.evaluations.paged_results_response_pagination_context import PagedResultsResponsePaginationContextV1


class GetNLUEvaluationResultsResponse(PagedResultsResponse):
    """

    :param pagination_context: 
    :type pagination_context: (optional) ask_smapi_model.v1.nlu.evaluations.paged_results_response_pagination_context.PagedResultsResponsePaginationContext
    :param links: 
    :type links: (optional) ask_smapi_model.v1.nlu.evaluations.links.Links
    :param total_failed: count of tests failed. A test fails when the expected intent and expected slots are not identical. 
    :type total_failed: (optional) float
    :param test_cases: 
    :type test_cases: (optional) list[ask_smapi_model.v1.nlu.evaluations.test_case.TestCase]

    """
    deserialized_types = {
        'pagination_context': 'ask_smapi_model.v1.nlu.evaluations.paged_results_response_pagination_context.PagedResultsResponsePaginationContext',
        'links': 'ask_smapi_model.v1.nlu.evaluations.links.Links',
        'total_failed': 'float',
        'test_cases': 'list[ask_smapi_model.v1.nlu.evaluations.test_case.TestCase]'
    }  # type: Dict

    attribute_map = {
        'pagination_context': 'paginationContext',
        'links': '_links',
        'total_failed': 'totalFailed',
        'test_cases': 'testCases'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, pagination_context=None, links=None, total_failed=None, test_cases=None):
        # type: (Optional[PagedResultsResponsePaginationContextV1], Optional[LinksV1], Optional[float], Optional[List[TestCaseV1]]) -> None
        """

        :param pagination_context: 
        :type pagination_context: (optional) ask_smapi_model.v1.nlu.evaluations.paged_results_response_pagination_context.PagedResultsResponsePaginationContext
        :param links: 
        :type links: (optional) ask_smapi_model.v1.nlu.evaluations.links.Links
        :param total_failed: count of tests failed. A test fails when the expected intent and expected slots are not identical. 
        :type total_failed: (optional) float
        :param test_cases: 
        :type test_cases: (optional) list[ask_smapi_model.v1.nlu.evaluations.test_case.TestCase]
        """
        self.__discriminator_value = None  # type: str

        super(GetNLUEvaluationResultsResponse, self).__init__(pagination_context=pagination_context, links=links)
        self.total_failed = total_failed
        self.test_cases = test_cases

    def to_dict(self):
        # type: () -> Dict[str, object]
        """Returns the model properties as a dict"""
        result = {}  # type: Dict

        for attr, _ in six.iteritems(self.deserialized_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else
                    x.value if isinstance(x, Enum) else x,
                    value
                ))
            elif isinstance(value, Enum):
                result[attr] = value.value
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else
                    (item[0], item[1].value)
                    if isinstance(item[1], Enum) else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        # type: () -> str
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        # type: () -> str
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are equal"""
        if not isinstance(other, GetNLUEvaluationResultsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
