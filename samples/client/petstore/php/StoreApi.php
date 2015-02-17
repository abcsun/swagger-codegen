<?php
/**
 *  Copyright 2015 Reverb Technologies, Inc.
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */

/**
 *
 * NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
 */
class StoreApi {

	function __construct($apiClient) {
	  $this->apiClient = $apiClient;
	}

  
	/**
	 * getInventory
   *
	 * Returns pet inventories by status
   
	 * @return map[string,int]
	 */

   public function getInventory() {

  		// parse inputs
  		$resourcePath = "/store/inventory";
  		$resourcePath = str_replace("{format}", "json", $resourcePath);
  		$method = "GET";
      $queryParams = array();
      $headerParams = array();
      $formParams = array();
      $headerParams['Accept'] = 'application/json,application/xml';
      $headerParams['Content-Type'] = '';

      
      
      
      
      

      $body = $body ?: $formParams;

      if (strpos($headerParams['Content-Type'], "application/x-www-form-urlencoded") > -1) {
        $body = http_build_query($body);
      }

  		// make the API Call
  		$response = $this->apiClient->callAPI($resourcePath, $method,
  		                                      $queryParams, $body,
  		                                      $headerParams);

      if(! $response) {
        return null;
      }

  		$responseObject = $this->apiClient->deserialize($response,
  		                                                'map[string,int]');
  		return $responseObject;
  }
  
	/**
	 * placeOrder
   *
	 * Place an order for a pet
   * body, Order: order placed for purchasing the pet (required)
   * 
	 * @return Order
	 */

   public function placeOrder($body) {

  		// parse inputs
  		$resourcePath = "/store/order";
  		$resourcePath = str_replace("{format}", "json", $resourcePath);
  		$method = "POST";
      $queryParams = array();
      $headerParams = array();
      $formParams = array();
      $headerParams['Accept'] = 'application/json,application/xml';
      $headerParams['Content-Type'] = '';

      
      
      
      
      // body params
      $body = null;
      if (isset($body)) {
        $body = $body;
      }

      $body = $body ?: $formParams;

      if (strpos($headerParams['Content-Type'], "application/x-www-form-urlencoded") > -1) {
        $body = http_build_query($body);
      }

  		// make the API Call
  		$response = $this->apiClient->callAPI($resourcePath, $method,
  		                                      $queryParams, $body,
  		                                      $headerParams);

      if(! $response) {
        return null;
      }

  		$responseObject = $this->apiClient->deserialize($response,
  		                                                'Order');
  		return $responseObject;
  }
  
	/**
	 * getOrderById
   *
	 * Find purchase order by ID
   * orderId, string: ID of pet that needs to be fetched (required)
   * 
	 * @return Order
	 */

   public function getOrderById($orderId) {

  		// parse inputs
  		$resourcePath = "/store/order/{orderId}";
  		$resourcePath = str_replace("{format}", "json", $resourcePath);
  		$method = "GET";
      $queryParams = array();
      $headerParams = array();
      $formParams = array();
      $headerParams['Accept'] = 'application/json,application/xml';
      $headerParams['Content-Type'] = '';

      
      
      // path params
      if($orderId !== null) {
  			$resourcePath = str_replace("{" . "orderId" . "}",
  			                            $this->apiClient->toPathValue($orderId), $resourcePath);
  		}
      
      

      $body = $body ?: $formParams;

      if (strpos($headerParams['Content-Type'], "application/x-www-form-urlencoded") > -1) {
        $body = http_build_query($body);
      }

  		// make the API Call
  		$response = $this->apiClient->callAPI($resourcePath, $method,
  		                                      $queryParams, $body,
  		                                      $headerParams);

      if(! $response) {
        return null;
      }

  		$responseObject = $this->apiClient->deserialize($response,
  		                                                'Order');
  		return $responseObject;
  }
  
	/**
	 * deleteOrder
   *
	 * Delete purchase order by ID
   * orderId, string: ID of the order that needs to be deleted (required)
   * 
	 * @return 
	 */

   public function deleteOrder($orderId) {

  		// parse inputs
  		$resourcePath = "/store/order/{orderId}";
  		$resourcePath = str_replace("{format}", "json", $resourcePath);
  		$method = "DELETE";
      $queryParams = array();
      $headerParams = array();
      $formParams = array();
      $headerParams['Accept'] = 'application/json,application/xml';
      $headerParams['Content-Type'] = '';

      
      
      // path params
      if($orderId !== null) {
  			$resourcePath = str_replace("{" . "orderId" . "}",
  			                            $this->apiClient->toPathValue($orderId), $resourcePath);
  		}
      
      

      $body = $body ?: $formParams;

      if (strpos($headerParams['Content-Type'], "application/x-www-form-urlencoded") > -1) {
        $body = http_build_query($body);
      }

  		// make the API Call
  		$response = $this->apiClient->callAPI($resourcePath, $method,
  		                                      $queryParams, $body,
  		                                      $headerParams);

      
  }
  

}
