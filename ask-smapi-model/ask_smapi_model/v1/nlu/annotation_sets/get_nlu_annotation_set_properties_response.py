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
from ask_smapi_model.v1.nlu.annotation_sets.annotation_set_entity import AnnotationSetEntity


if typing.TYPE_CHECKING:
    from typing import Dict, List, Optional, Union
    from datetime import datetime


class GetNLUAnnotationSetPropertiesResponse(AnnotationSetEntity):
    """

    :param locale: 
    :type locale: (optional) str
    :param name: Name of the NLU annotation set
    :type name: (optional) str
    :param number_of_entries: Number of entries which represents number of utterances in each NLU annotation set content
    :type number_of_entries: (optional) int
    :param updated_timestamp: The lastest updated timestamp for the NLU annotation set
    :type updated_timestamp: (optional) datetime

    """
    deserialized_types = {
        'locale': 'str',
        'name': 'str',
        'number_of_entries': 'int',
        'updated_timestamp': 'datetime'
    }  # type: Dict

    attribute_map = {
        'locale': 'locale',
        'name': 'name',
        'number_of_entries': 'numberOfEntries',
        'updated_timestamp': 'updatedTimestamp'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, locale=None, name=None, number_of_entries=None, updated_timestamp=None):
        # type: (Optional[str], Optional[str], Optional[int], Optional[datetime]) -> None
        """

        :param locale: 
        :type locale: (optional) str
        :param name: Name of the NLU annotation set
        :type name: (optional) str
        :param number_of_entries: Number of entries which represents number of utterances in each NLU annotation set content
        :type number_of_entries: (optional) int
        :param updated_timestamp: The lastest updated timestamp for the NLU annotation set
        :type updated_timestamp: (optional) datetime
        """
        self.__discriminator_value = None  # type: str

        super(GetNLUAnnotationSetPropertiesResponse, self).__init__(locale=locale, name=name, number_of_entries=number_of_entries, updated_timestamp=updated_timestamp)

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
        if not isinstance(other, GetNLUAnnotationSetPropertiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
