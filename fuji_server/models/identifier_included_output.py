# -*- coding: utf-8 -*-

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from fuji_server.models.base_model_ import Model
from fuji_server.models.identifier_included_output_inner import IdentifierIncludedOutputInner  # noqa: F401,E501
from fuji_server import util


class IdentifierIncludedOutput(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, object_content_identifier_included: List[IdentifierIncludedOutputInner] = None):  # noqa: E501
        """IdentifierIncludedOutput - a model defined in Swagger

        :param object_content_identifier_included: The object_content_identifier_included of this IdentifierIncludedOutput.  # noqa: E501
        :type object_content_identifier_included: List[IdentifierIncludedOutputInner]
        """
        self.swagger_types = {'object_content_identifier_included': List[IdentifierIncludedOutputInner]}

        self.attribute_map = {'object_content_identifier_included': 'object_content_identifier_included'}
        self._object_content_identifier_included = object_content_identifier_included

    @classmethod
    def from_dict(cls, dikt) -> 'IdentifierIncludedOutput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The IdentifierIncluded_output of this IdentifierIncludedOutput.  # noqa: E501
        :rtype: IdentifierIncludedOutput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def object_content_identifier_included(self) -> List[IdentifierIncludedOutputInner]:
        """Gets the object_content_identifier_included of this IdentifierIncludedOutput.


        :return: The object_content_identifier_included of this IdentifierIncludedOutput.
        :rtype: List[IdentifierIncludedOutputInner]
        """
        return self._object_content_identifier_included

    @object_content_identifier_included.setter
    def object_content_identifier_included(self,
                                           object_content_identifier_included: List[IdentifierIncludedOutputInner]):
        """Sets the object_content_identifier_included of this IdentifierIncludedOutput.


        :param object_content_identifier_included: The object_content_identifier_included of this IdentifierIncludedOutput.
        :type object_content_identifier_included: List[IdentifierIncludedOutputInner]
        """

        self._object_content_identifier_included = object_content_identifier_included
