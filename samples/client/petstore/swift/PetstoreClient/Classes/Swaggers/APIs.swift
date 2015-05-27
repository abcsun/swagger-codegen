// APIs.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation
import PromiseKit

class PetstoreClientAPI {
    static let basePath = "http://petstore.swagger.io/v2"
    static var credential: NSURLCredential?
    static var requestBuilderFactory: RequestBuilderFactory = AlamofireRequestBuilderFactory()
}

class APIBase {
    func toParameters(encodable: JSONEncodable?) -> [String: AnyObject]? {
        let encoded: AnyObject? = encodable?.encodeToJSON()

        if encoded! is [AnyObject] {
            var dictionary = [String:AnyObject]()
            for (index, item) in enumerate(encoded as! [AnyObject]) {
                dictionary["\(index)"] = item
            }
            return dictionary
        } else {
            return encoded as? [String:AnyObject]
        }
    }
}

class RequestBuilder<T> {
    var credential: NSURLCredential?
    var headers: [String:String] = [:]
    let parameters: [String:AnyObject]?
    let isBody: Bool
    let method: String
    let URLString: String
    
    required init(method: String, URLString: String, parameters: [String:AnyObject]?, isBody: Bool) {
        self.method = method
        self.URLString = URLString
        self.parameters = parameters
        self.isBody = isBody
    }
    
    func execute() -> Promise<Response<T>>  { fatalError("Not implemented") }

    func addHeader(#name: String, value: String) -> Self {
        if !value.isEmpty {
            headers[name] = value
        }
        return self
    }
    
    func addCredential() -> Self {
        self.credential = PetstoreClientAPI.credential
        return self
    }
}

protocol RequestBuilderFactory {
    func getBuilder<T>() -> RequestBuilder<T>.Type
}


