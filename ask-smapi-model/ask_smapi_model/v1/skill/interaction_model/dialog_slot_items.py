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


if typing.TYPE_CHECKING:
    from typing import Dict, List, Optional, Union
    from datetime import datetime
    from ask_smapi_model.v1.skill.interaction_model.slot_validation import SlotValidationV1
    from ask_smapi_model.v1.skill.interaction_model.dialog_prompts import DialogPromptsV1


class DialogSlotItems(object):
    """

    :param name: The name of the slot that has dialog rules associated with it.
    :type name: (optional) str
    :param object_type: Type of the slot in the dialog intent.
    :type object_type: (optional) str
    :param elicitation_required: Describes whether elicitation of the slot is required.
    :type elicitation_required: (optional) bool
    :param confirmation_required: Describes whether confirmation of the slot is required.
    :type confirmation_required: (optional) bool
    :param prompts: 
    :type prompts: (optional) ask_smapi_model.v1.skill.interaction_model.dialog_prompts.DialogPrompts
    :param validations: List of validations for the slot. if validation fails, user will be prompted with the provided prompt.
    :type validations: (optional) list[ask_smapi_model.v1.skill.interaction_model.slot_validation.SlotValidation]

    """
    deserialized_types = {
        'name': 'str',
        'object_type': 'str',
        'elicitation_required': 'bool',
        'confirmation_required': 'bool',
        'prompts': 'ask_smapi_model.v1.skill.interaction_model.dialog_prompts.DialogPrompts',
        'validations': 'list[ask_smapi_model.v1.skill.interaction_model.slot_validation.SlotValidation]'
    }  # type: Dict

    attribute_map = {
        'name': 'name',
        'object_type': 'type',
        'elicitation_required': 'elicitationRequired',
        'confirmation_required': 'confirmationRequired',
        'prompts': 'prompts',
        'validations': 'validations'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, name=None, object_type=None, elicitation_required=None, confirmation_required=None, prompts=None, validations=None):
        # type: (Optional[str], Optional[str], Optional[bool], Optional[bool], Optional[DialogPromptsV1], Optional[List[SlotValidationV1]]) -> None
        """

        :param name: The name of the slot that has dialog rules associated with it.
        :type name: (optional) str
        :param object_type: Type of the slot in the dialog intent.
        :type object_type: (optional) str
        :param elicitation_required: Describes whether elicitation of the slot is required.
        :type elicitation_required: (optional) bool
        :param confirmation_required: Describes whether confirmation of the slot is required.
        :type confirmation_required: (optional) bool
        :param prompts: 
        :type prompts: (optional) ask_smapi_model.v1.skill.interaction_model.dialog_prompts.DialogPrompts
        :param validations: List of validations for the slot. if validation fails, user will be prompted with the provided prompt.
        :type validations: (optional) list[ask_smapi_model.v1.skill.interaction_model.slot_validation.SlotValidation]
        """
        self.__discriminator_value = None  # type: str

        self.name = name
        self.object_type = object_type
        self.elicitation_required = elicitation_required
        self.confirmation_required = confirmation_required
        self.prompts = prompts
        self.validations = validations

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
        if not isinstance(other, DialogSlotItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
