#!/usr/bin/env python
"""Wordnik.com's Swagger generic API client. This client handles the client-
server communication, and is invariant across implementations. Specifics of
the methods and models for each application are generated from the Swagger
templates."""

import sys
import os
import re
import urllib
import urllib2
import httplib
import json

from models import *


class ApiClient:
    """Generic API client for Swagger client library builds"""

    def __init__(self, apiKey=None, apiServer=None):
        if apiKey == None:
            raise Exception('You must pass an apiKey when instantiating the '
                            'APIClient')
        self.apiKey = apiKey
        self.apiServer = apiServer
        self.cookie = None

    def callAPI(self, resourcePath, method, queryParams, postData,
                headerParams=None):

        url = self.apiServer + resourcePath
        headers = {}
        if headerParams:
            for param, value in headerParams.iteritems():
                headers[param] = value

        headers['api_key'] = self.apiKey

        if self.cookie:
            headers['Cookie'] = self.cookie

        data = None
        # What can safely be JSON serialized?
        safeToDump = [str, int, float, bool]

        if queryParams:
            # Need to remove None values, these should not be sent
            sentQueryParams = {}
            for param, value in queryParams.iteritems():
                if value != None:
                    sentQueryParams[param] = value
            url = url + '?' + urllib.urlencode(sentQueryParams)

        if method in ['POST', 'PUT', 'DELETE']:
            data = postData
            if data:
                headers['Content-type'] = 'application/json'
                if type(postData) == list:
                    # Could be a list of objects
                    if type(postData[0]) in safeToDump:
                        data = json.dumps(postData)
                    else:
                        data = json.dumps([datum.__dict__ for datum in postData])
                elif type(postData) not in safeToDump:
                    data = json.dumps(postData.__dict__)
        else:
            raise Exception('Method ' + method + ' is not recognized.')

        request = MethodRequest(method=method, url=url, headers=headers, data=data)

        # Make the request
        response = urllib2.urlopen(request)
        if 'Set-Cookie' in response.headers:
            self.cookie = response.headers['Set-Cookie']  
        string = response.read()

        try:
            data = json.loads(string)
        except ValueError: # PUT requests don't return anything
            data = None

        return data

    def toPathValue(self, obj):
        """Serialize a list to a CSV string, if necessary.
        Args:
            obj -- data object to be serialized
        Returns:
            string -- json serialization of object
        """
        if type(obj) == list:
            return ','.join(obj)
        else:
            return obj

    def deserialize(self, obj, objClass):
        """Derialize a JSON string into an object.

        Args:
            obj -- string or object to be deserialized
            objClass -- class literal for deserialzied object, or string
                of class name
        Returns:
            object -- deserialized object"""

        # Have to accept objClass as string or actual type. Type could be a
        # native Python type, or one of the model classes.

        # print obj, objClass

        if type(objClass) == str:
            if 'list[' in objClass:
                match = re.match('list\[(.*)\]', objClass)
                subClass = match.group(1)
                return [self.deserialize(subObj, subClass) for subObj in obj]

            # print objClass + ' is str'
            if (objClass in ['int', 'float', 'long', 'dict', 'list', 'str']):
                objClass = eval(objClass)
            else:  # not a native type, must be model class
                objClass = eval(objClass + '.' + objClass)

        if objClass in [str, int, long, float, bool]:
            return objClass(obj)

        instance = objClass()

        for attr, attrType in instance.swaggerTypes.iteritems():
            # print 'attr:', attr, 'obj:', obj
            if attr in obj:
                value = obj[attr]
                if attrType in ['str', 'int', 'long', 'float', 'bool']:
                    attrType = eval(attrType)
                    try:
                        value = attrType(value)
                    except UnicodeEncodeError:
                        value = unicode(value)
                    setattr(instance, attr, value)
                elif 'list[' in attrType:
                    match = re.match('list\[(.*)\]', attrType)
                    subClass = match.group(1)
                    subValues = []

                    for subValue in value:
                        subValues.append(self.deserialize(subValue, subClass))
                    setattr(instance, attr, subValues)
                else:
                    setattr(instance, attr, self.deserialize(value,
                                                             objClass))

        return instance


class MethodRequest(urllib2.Request):

    def __init__(self, *args, **kwargs):
        """Construct a MethodRequest. Usage is the same as for
        `urllib2.Request` except it also takes an optional `method`
        keyword argument. If supplied, `method` will be used instead of
        the default."""

        if 'method' in kwargs:
            self.method = kwargs.pop('method')
        return urllib2.Request.__init__(self, *args, **kwargs)

    def get_method(self):
        return getattr(self, 'method', urllib2.Request.get_method(self))

