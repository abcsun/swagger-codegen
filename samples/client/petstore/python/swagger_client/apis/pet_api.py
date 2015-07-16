#!/usr/bin/env python
# coding: utf-8

"""
PetApi.py
Copyright 2015 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from .. import configuration
from ..api_client import ApiClient

class PetApi(object):

    def __init__(self, api_client=None):
        if api_client:
            self.api_client = api_client
        else:
            if not configuration.api_client:
                configuration.api_client = ApiClient('http://petstore.swagger.io/v2')
            self.api_client = configuration.api_client
    
    
    def update_pet(self, **kwargs):
        """
        Update an existing pet
        

        :param Pet body: Pet object that needs to be added to the store (optional)
        
        :return: None
        """
        
        all_params = ['body']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method update_pet" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/pet'.replace('{format}', 'json')
        method = 'PUT'

        path_params = {}
        
        query_params = {}
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        if 'body' in params:
            body_params = params['body']
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json', 'application/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json', 'application/xml'])

        # Authentication setting
        auth_settings = ['petstore_auth']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response_type=None, auth_settings=auth_settings)
        
    def add_pet(self, **kwargs):
        """
        Add a new pet to the store
        

        :param Pet body: Pet object that needs to be added to the store (optional)
        
        :return: None
        """
        
        all_params = ['body']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method add_pet" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/pet'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        if 'body' in params:
            body_params = params['body']
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json', 'application/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json', 'application/xml'])

        # Authentication setting
        auth_settings = ['petstore_auth']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response_type=None, auth_settings=auth_settings)
        
    def find_pets_by_status(self, **kwargs):
        """
        Finds Pets by status
        Multiple status values can be provided with comma seperated strings

        :param list[str] status: Status values that need to be considered for filter (optional)
        
        :return: list[Pet]
        """
        
        all_params = ['status']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method find_pets_by_status" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/pet/findByStatus'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'status' in params:
            query_params['status'] = params['status']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json', 'application/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['petstore_auth']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response_type='list[Pet]', auth_settings=auth_settings)
        
        return response
        
    def find_pets_by_tags(self, **kwargs):
        """
        Finds Pets by tags
        Muliple tags can be provided with comma seperated strings. Use tag1, tag2, tag3 for testing.

        :param list[str] tags: Tags to filter by (optional)
        
        :return: list[Pet]
        """
        
        all_params = ['tags']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method find_pets_by_tags" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/pet/findByTags'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'tags' in params:
            query_params['tags'] = params['tags']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json', 'application/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['petstore_auth']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response_type='list[Pet]', auth_settings=auth_settings)
        
        return response
        
    def get_pet_by_id(self, pet_id, **kwargs):
        """
        Find pet by ID
        Returns a pet when ID < 10.  ID > 10 or nonintegers will simulate API error conditions

        :param int pet_id: ID of pet that needs to be fetched (required)
        
        :return: Pet
        """
        # verify the required parameter 'pet_id' is set
        if pet_id is None:
            raise ValueError("Missing the required parameter `pet_id` when calling `get_pet_by_id`")
        
        all_params = ['pet_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_pet_by_id" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/pet/{petId}'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        if 'pet_id' in params:
            path_params['petId'] = params['pet_id']  
        
        query_params = {}
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json', 'application/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['api_key', 'petstore_auth']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response_type='Pet', auth_settings=auth_settings)
        
        return response
        
    def update_pet_with_form(self, pet_id, **kwargs):
        """
        Updates a pet in the store with form data
        

        :param str pet_id: ID of pet that needs to be updated (required)
        :param str name: Updated name of the pet (optional)
        :param str status: Updated status of the pet (optional)
        
        :return: None
        """
        # verify the required parameter 'pet_id' is set
        if pet_id is None:
            raise ValueError("Missing the required parameter `pet_id` when calling `update_pet_with_form`")
        
        all_params = ['pet_id', 'name', 'status']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method update_pet_with_form" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/pet/{petId}'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        if 'pet_id' in params:
            path_params['petId'] = params['pet_id']  
        
        query_params = {}
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        if 'name' in params:
            form_params['name'] = params['name']
        
        if 'status' in params:
            form_params['status'] = params['status']
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json', 'application/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['petstore_auth']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response_type=None, auth_settings=auth_settings)
        
    def delete_pet(self, pet_id, **kwargs):
        """
        Deletes a pet
        

        :param int pet_id: Pet id to delete (required)
        :param str api_key:  (optional)
        
        :return: None
        """
        # verify the required parameter 'pet_id' is set
        if pet_id is None:
            raise ValueError("Missing the required parameter `pet_id` when calling `delete_pet`")
        
        all_params = ['pet_id', 'api_key']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method delete_pet" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/pet/{petId}'.replace('{format}', 'json')
        method = 'DELETE'

        path_params = {}
        
        if 'pet_id' in params:
            path_params['petId'] = params['pet_id']  
        
        query_params = {}
        
        header_params = {}
        
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json', 'application/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['petstore_auth']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response_type=None, auth_settings=auth_settings)
        
    def upload_file(self, pet_id, **kwargs):
        """
        uploads an image
        

        :param int pet_id: ID of pet to update (required)
        :param str additional_metadata: Additional data to pass to server (optional)
        :param file file: file to upload (optional)
        
        :return: None
        """
        # verify the required parameter 'pet_id' is set
        if pet_id is None:
            raise ValueError("Missing the required parameter `pet_id` when calling `upload_file`")
        
        all_params = ['pet_id', 'additional_metadata', 'file']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method upload_file" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/pet/{petId}/uploadImage'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        if 'pet_id' in params:
            path_params['petId'] = params['pet_id']  
        
        query_params = {}
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        if 'additional_metadata' in params:
            form_params['additionalMetadata'] = params['additional_metadata']
        
        if 'file' in params:
            files['file'] = params['file']
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json', 'application/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = ['petstore_auth']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response_type=None, auth_settings=auth_settings)
        









