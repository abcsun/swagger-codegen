#!/usr/bin/env python
"""
WordAPI.py
Copyright 2011 Wordnik, Inc.

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
import sys
import os

from models import *


class PetApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    def getPetById(self, petId, **kwargs):
        """Find pet by ID

        Args:
            petId, str: ID of pet that needs to be fetched (required)
            
        Returns: Pet
        """

        allParams = ['petId']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getPetById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pet.{format}/{petId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('petId' in params):
            resourcePath = resourcePath.replace('{' + 'petId' + '}',
                                                self.apiClient.toPathValue(params['petId']))
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Pet')
        return responseObject
        
        
    def addPet(self, body, **kwargs):
        """Add a new pet to the store

        Args:
            body, Pet: Pet object that needs to be added to the store (required)
            
        Returns: 
        """

        allParams = ['body']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addPet" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pet.{format}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        
    def updatePet(self, body, **kwargs):
        """Update an existing pet

        Args:
            body, Pet: Pet object that needs to be updated in the store (required)
            
        Returns: 
        """

        allParams = ['body']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updatePet" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pet.{format}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}

        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        
    def findPetsByStatus(self, status, **kwargs):
        """Finds Pets by status

        Args:
            status, str: Status values that need to be considered for filter (required)
            
        Returns: list[Pet]
        """

        allParams = ['status']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method findPetsByStatus" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pet.{format}/findByStatus'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('status' in params):
            queryParams['status'] = self.apiClient.toPathValue(params['status'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'list[Pet]')
        return responseObject
        
        
    def findPetsByTags(self, tags, **kwargs):
        """Finds Pets by tags

        Args:
            tags, str: Tags to filter by (required)
            
        Returns: list[Pet]
        """

        allParams = ['tags']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method findPetsByTags" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/pet.{format}/findByTags'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('tags' in params):
            queryParams['tags'] = self.apiClient.toPathValue(params['tags'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'list[Pet]')
        return responseObject
        
        
    


