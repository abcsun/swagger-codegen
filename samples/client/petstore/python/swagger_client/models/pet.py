# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class Pet(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Pet - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'category': 'Category',
            'name': 'str',
            'photo_urls': 'list[str]',
            'tags': 'list[Tag]',
            'status': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'category': 'category',
            'name': 'name',
            'photo_urls': 'photoUrls',
            'tags': 'tags',
            'status': 'status'
        }

        self._id = None
        self._category = None
        self._name = None
        self._photo_urls = None
        self._tags = None
        self._status = None

    @property
    def id(self):
        """
        Gets the id of this Pet.


        :return: The id of this Pet.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Pet.


        :param id: The id of this Pet.
        :type: int
        """
        self._id = id

    @property
    def category(self):
        """
        Gets the category of this Pet.


        :return: The category of this Pet.
        :rtype: Category
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this Pet.


        :param category: The category of this Pet.
        :type: Category
        """
        self._category = category

    @property
    def name(self):
        """
        Gets the name of this Pet.


        :return: The name of this Pet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Pet.


        :param name: The name of this Pet.
        :type: str
        """
        self._name = name

    @property
    def photo_urls(self):
        """
        Gets the photo_urls of this Pet.


        :return: The photo_urls of this Pet.
        :rtype: list[str]
        """
        return self._photo_urls

    @photo_urls.setter
    def photo_urls(self, photo_urls):
        """
        Sets the photo_urls of this Pet.


        :param photo_urls: The photo_urls of this Pet.
        :type: list[str]
        """
        self._photo_urls = photo_urls

    @property
    def tags(self):
        """
        Gets the tags of this Pet.


        :return: The tags of this Pet.
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Pet.


        :param tags: The tags of this Pet.
        :type: list[Tag]
        """
        self._tags = tags

    @property
    def status(self):
        """
        Gets the status of this Pet.
        pet status in the store

        :return: The status of this Pet.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Pet.
        pet status in the store

        :param status: The status of this Pet.
        :type: str
        """
        allowed_values = ["available", "pending", "sold"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )
        self._status = status

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

