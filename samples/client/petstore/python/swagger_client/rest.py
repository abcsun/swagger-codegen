# coding: utf-8

"""
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

Credit: this file (rest.py) is modified based on rest.py in Dropbox Python SDK:
https://www.dropbox.com/developers/core/sdks/python
"""

import sys
import io
import json
import ssl
import certifi
import logging

# python 2 and python 3 compatibility library
from six import iteritems

try:
    import urllib3
except ImportError:
    raise ImportError('Swagger python client requires urllib3.')

try:
    # for python3
    from urllib.parse import urlencode
except ImportError:
    # for python2
    from urllib import urlencode


logger = logging.getLogger(__name__)


class RESTResponse(io.IOBase):

    def __init__(self, resp):
        self.urllib3_response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = resp.data

    def getheaders(self):
        """
        Returns a dictionary of the response headers.
        """
        return self.urllib3_response.getheaders()

    def getheader(self, name, default=None):
        """
        Returns a given response header.
        """
        return self.urllib3_response.getheader(name, default)


class RESTClientObject(object):

    def __init__(self, pools_size=4):
        # http pool manager
        self.pool_manager = urllib3.PoolManager(
            num_pools=pools_size
        )

        # https pool manager
        # certificates validated using Mozilla’s root certificates
        self.ssl_pool_manager = urllib3.PoolManager(
            num_pools=pools_size,
            cert_reqs=ssl.CERT_REQUIRED,
            ca_certs=certifi.where()
        )

    def agent(self, url):
        """
        Use `urllib3.util.parse_url` for backward compatibility.
        Return proper pool manager for the http/https schemes.
        """
        url = urllib3.util.parse_url(url)
        scheme = url.scheme
        if scheme == 'https':
            return self.ssl_pool_manager
        else:
            return self.pool_manager

    def request(self, method, url, query_params=None, headers=None,
                body=None, post_params=None):
        """
        :param method: http request method
        :param url: http request url
        :param query_params: query parameters in the url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencode`
                            and `multipart/form-data`
        """
        method = method.upper()
        assert method in ['GET', 'HEAD', 'DELETE', 'POST', 'PUT', 'PATCH']

        if post_params and body:
            raise ValueError(
                "body parameter cannot be used with post_params parameter."
            )

        post_params = post_params or {}
        headers = headers or {}

        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        # For `POST`, `PUT`, `PATCH`
        if method in ['POST', 'PUT', 'PATCH']:
            if query_params:
                url += '?' + urlencode(query_params)
            if headers['Content-Type'] == 'application/json':
                r = self.agent(url).request(method, url,
                                            body=json.dumps(body),
                                            headers=headers)
            if headers['Content-Type'] == 'application/x-www-form-urlencoded':
                r = self.agent(url).request(method, url,
                                            fields=post_params,
                                            encode_multipart=False,
                                            headers=headers)
            if headers['Content-Type'] == 'multipart/form-data':
                # must del headers['Content-Type'], or the correct Content-Type
                # which generated by urllib3 will be overwritten.
                del headers['Content-Type']
                r = self.agent(url).request(method, url,
                                            fields=post_params,
                                            encode_multipart=True,
                                            headers=headers)
        # For `GET`, `HEAD`, `DELETE`
        else:
            r = self.agent(url).request(method, url,
                                        fields=query_params,
                                        headers=headers)
        r = RESTResponse(r)

        # In the python 3, the response.data is bytes.
        # we need to decode it to string.
        if sys.version_info > (3,):
            r.data = r.data.decode('utf8')

        # log response body
        logger.debug("response body: %s" % r.data)

        if r.status not in range(200, 206):
            raise ApiException(http_resp=r)

        return r

    def GET(self, url, headers=None, query_params=None):
        return self.request("GET", url,
                            headers=headers,
                            query_params=query_params)

    def HEAD(self, url, headers=None, query_params=None):
        return self.request("HEAD", url,
                            headers=headers,
                            query_params=query_params)

    def DELETE(self, url, headers=None, query_params=None):
        return self.request("DELETE", url,
                            headers=headers,
                            query_params=query_params)

    def POST(self, url, headers=None, query_params=None, post_params=None, body=None):
        return self.request("POST", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            body=body)

    def PUT(self, url, headers=None, query_params=None, post_params=None, body=None):
        return self.request("PUT", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            body=body)

    def PATCH(self, url, headers=None, query_params=None, post_params=None, body=None):
        return self.request("PATCH", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            body=body)


class ApiException(Exception):

    def __init__(self, status=None, reason=None, http_resp=None):
        if http_resp:
            self.status = http_resp.status
            self.reason = http_resp.reason
            self.body = http_resp.data
            self.headers = http_resp.getheaders()
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None

    def __str__(self):
        """
        Custom error messages for exception
        """
        error_message = "({0})\n"\
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message


class RESTClient(object):
    """
    A class with all class methods to perform JSON requests.
    """

    IMPL = RESTClientObject()

    @classmethod
    def request(cls, *n, **kw):
        """
        Perform a REST request and parse the response.
        """
        return cls.IMPL.request(*n, **kw)

    @classmethod
    def GET(cls, *n, **kw):
        """
        Perform a GET request using `RESTClient.request()`.
        """
        return cls.IMPL.GET(*n, **kw)

    @classmethod
    def HEAD(cls, *n, **kw):
        """
        Perform a HEAD request using `RESTClient.request()`.
        """
        return cls.IMPL.GET(*n, **kw)

    @classmethod
    def POST(cls, *n, **kw):
        """
        Perform a POST request using `RESTClient.request()`
        """
        return cls.IMPL.POST(*n, **kw)

    @classmethod
    def PUT(cls, *n, **kw):
        """
        Perform a PUT request using `RESTClient.request()`
        """
        return cls.IMPL.PUT(*n, **kw)

    @classmethod
    def PATCH(cls, *n, **kw):
        """
        Perform a PATCH request using `RESTClient.request()`
        """
        return cls.IMPL.PATCH(*n, **kw)

    @classmethod
    def DELETE(cls, *n, **kw):
        """
        Perform a DELETE request using `RESTClient.request()`
        """
        return cls.IMPL.DELETE(*n, **kw)
