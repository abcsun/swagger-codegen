#import "SWGAccountApi.h"
#import "SWGFile.h"
#import "SWGApiClient.h"



@implementation SWGAccountApi
static NSString * basePath = @"http://api.wordnik.com/v4";

+(SWGAccountApi*) apiWithHeader:(NSString*)headerValue key:(NSString*)key {
    static SWGAccountApi* singletonAPI = nil;

    if (singletonAPI == nil) {
        singletonAPI = [[SWGAccountApi alloc] init];
        [singletonAPI addHeader:headerValue forKey:key];
    }
    return singletonAPI;
}

+(void) setBasePath:(NSString*)path {
    basePath = path;
}

+(NSString*) getBasePath {
    return basePath;
}

-(SWGApiClient*) apiClient {
    return [SWGApiClient sharedClientFromPool:basePath];
}

-(void) addHeader:(NSString*)value forKey:(NSString*)key {
    [[self apiClient] setHeaderValue:value forKey:key];
}

-(id) init {
    self = [super init];
    [self apiClient];
    return self;
}

-(void) setHeaderValue:(NSString*) value
           forKey:(NSString*)key {
    [[self apiClient] setHeaderValue:value forKey:key];
}

-(unsigned long) requestQueueSize {
    return [SWGApiClient requestQueueSize];
}


-(NSNumber*) getApiTokenStatusWithCompletionBlock:(NSString*) api_key        
        
        completionHandler: (void (^)(NSError* error))completionBlock {

    NSMutableString* requestUrl = [NSMutableString stringWithFormat:@"%@/account.json/apiTokenStatus", basePath];

    // remove format in URL if needed
    if ([requestUrl rangeOfString:@".{format}"].location != NSNotFound)
        [requestUrl replaceCharactersInRange: [requestUrl rangeOfString:@".{format}"] withString:@".json"];

    

    NSString* requestContentType = @"application/json";
    NSString* responseContentType = @"application/json";

        NSMutableDictionary* queryParams = [[NSMutableDictionary alloc] init];
    
        NSMutableDictionary* headerParams = [[NSMutableDictionary alloc] init];
    if(api_key != nil)
        headerParams[@"api_key"] = api_key;
    

    id bodyDictionary = nil;
        
    
    

    SWGApiClient* client = [SWGApiClient sharedClientFromPool:basePath];

    

    
    
    
    
    return [client stringWithCompletionBlock:requestUrl 
                                             method:@"GET" 
                                        queryParams:queryParams 
                                               body:bodyDictionary 
                                       headerParams:headerParams
                                 requestContentType: requestContentType
                                responseContentType: responseContentType
                                    completionBlock:^(NSString *data, NSError *error) {
                        if (error) {
                            completionBlock(error);
                            return;
                        }
                        completionBlock(nil);
                    }];
    
    
    
    

}

-(NSNumber*) authenticateWithCompletionBlock:(NSString*) username         password:(NSString*) password        
        
        completionHandler: (void (^)(NSError* error))completionBlock {

    NSMutableString* requestUrl = [NSMutableString stringWithFormat:@"%@/account.json/authenticate/{username}", basePath];

    // remove format in URL if needed
    if ([requestUrl rangeOfString:@".{format}"].location != NSNotFound)
        [requestUrl replaceCharactersInRange: [requestUrl rangeOfString:@".{format}"] withString:@".json"];

    [requestUrl replaceCharactersInRange: [requestUrl rangeOfString:[NSString stringWithFormat:@"%@%@%@", @"{", @"username", @"}"]] withString: [SWGApiClient escape:username]];
    

    NSString* requestContentType = @"application/json";
    NSString* responseContentType = @"application/json";

        NSMutableDictionary* queryParams = [[NSMutableDictionary alloc] init];
    if(password != nil)
        queryParams[@"password"] = password;
    
        NSMutableDictionary* headerParams = [[NSMutableDictionary alloc] init];
    

    id bodyDictionary = nil;
        
    
    

    SWGApiClient* client = [SWGApiClient sharedClientFromPool:basePath];

    

    
    
    
    
    return [client stringWithCompletionBlock:requestUrl 
                                             method:@"GET" 
                                        queryParams:queryParams 
                                               body:bodyDictionary 
                                       headerParams:headerParams
                                 requestContentType: requestContentType
                                responseContentType: responseContentType
                                    completionBlock:^(NSString *data, NSError *error) {
                        if (error) {
                            completionBlock(error);
                            return;
                        }
                        completionBlock(nil);
                    }];
    
    
    
    

}

-(NSNumber*) authenticatePostWithCompletionBlock:(NSString*) username         body:(NSString*) body        
        
        completionHandler: (void (^)(NSError* error))completionBlock {

    NSMutableString* requestUrl = [NSMutableString stringWithFormat:@"%@/account.json/authenticate/{username}", basePath];

    // remove format in URL if needed
    if ([requestUrl rangeOfString:@".{format}"].location != NSNotFound)
        [requestUrl replaceCharactersInRange: [requestUrl rangeOfString:@".{format}"] withString:@".json"];

    [requestUrl replaceCharactersInRange: [requestUrl rangeOfString:[NSString stringWithFormat:@"%@%@%@", @"{", @"username", @"}"]] withString: [SWGApiClient escape:username]];
    

    NSString* requestContentType = @"application/json";
    NSString* responseContentType = @"application/json";

        NSMutableDictionary* queryParams = [[NSMutableDictionary alloc] init];
    
        NSMutableDictionary* headerParams = [[NSMutableDictionary alloc] init];
    

    id bodyDictionary = nil;
        
    if(body != nil && [body isKindOfClass:[NSArray class]]){
        NSMutableArray * objs = [[NSMutableArray alloc] init];
        for (id dict in (NSArray*)body) {
            if([dict respondsToSelector:@selector(asDictionary)]) {
                [objs addObject:[(SWGObject*)dict asDictionary]];
            }
            else{
                [objs addObject:dict];
            }
        }
        bodyDictionary = objs;
    }
    else if([body respondsToSelector:@selector(asDictionary)]) {
        bodyDictionary = [(SWGObject*)body asDictionary];
    }
    else if([body isKindOfClass:[NSString class]]) {
        // convert it to a dictionary
        NSError * error;
        NSString * str = (NSString*)body;
        NSDictionary *JSON =
            [NSJSONSerialization JSONObjectWithData:[str dataUsingEncoding:NSUTF8StringEncoding]
                                            options:NSJSONReadingMutableContainers
                                              error:&error];
        bodyDictionary = JSON;
    }
    else if([body isKindOfClass: [SWGFile class]]) {
        requestContentType = @"form-data";
        bodyDictionary = body;
    }
    else{
        NSLog(@"don't know what to do with %@", body);
    }

    
    
    

    SWGApiClient* client = [SWGApiClient sharedClientFromPool:basePath];

    

    
    
    
    
    return [client stringWithCompletionBlock:requestUrl 
                                             method:@"POST" 
                                        queryParams:queryParams 
                                               body:bodyDictionary 
                                       headerParams:headerParams
                                 requestContentType: requestContentType
                                responseContentType: responseContentType
                                    completionBlock:^(NSString *data, NSError *error) {
                        if (error) {
                            completionBlock(error);
                            return;
                        }
                        completionBlock(nil);
                    }];
    
    
    
    

}

-(NSNumber*) getLoggedInUserWithCompletionBlock:(NSString*) auth_token        
        
        completionHandler: (void (^)(NSError* error))completionBlock {

    NSMutableString* requestUrl = [NSMutableString stringWithFormat:@"%@/account.json/user", basePath];

    // remove format in URL if needed
    if ([requestUrl rangeOfString:@".{format}"].location != NSNotFound)
        [requestUrl replaceCharactersInRange: [requestUrl rangeOfString:@".{format}"] withString:@".json"];

    

    NSString* requestContentType = @"application/json";
    NSString* responseContentType = @"application/json";

        NSMutableDictionary* queryParams = [[NSMutableDictionary alloc] init];
    
        NSMutableDictionary* headerParams = [[NSMutableDictionary alloc] init];
    if(auth_token != nil)
        headerParams[@"auth_token"] = auth_token;
    

    id bodyDictionary = nil;
        
    
    

    SWGApiClient* client = [SWGApiClient sharedClientFromPool:basePath];

    

    
    
    
    
    return [client stringWithCompletionBlock:requestUrl 
                                             method:@"GET" 
                                        queryParams:queryParams 
                                               body:bodyDictionary 
                                       headerParams:headerParams
                                 requestContentType: requestContentType
                                responseContentType: responseContentType
                                    completionBlock:^(NSString *data, NSError *error) {
                        if (error) {
                            completionBlock(error);
                            return;
                        }
                        completionBlock(nil);
                    }];
    
    
    
    

}

-(NSNumber*) getWordListsForLoggedInUserWithCompletionBlock:(NSString*) auth_token         skip:(NSNumber*) skip         limit:(NSNumber*) limit        
        
        completionHandler: (void (^)(NSError* error))completionBlock {

    NSMutableString* requestUrl = [NSMutableString stringWithFormat:@"%@/account.json/wordLists", basePath];

    // remove format in URL if needed
    if ([requestUrl rangeOfString:@".{format}"].location != NSNotFound)
        [requestUrl replaceCharactersInRange: [requestUrl rangeOfString:@".{format}"] withString:@".json"];

    

    NSString* requestContentType = @"application/json";
    NSString* responseContentType = @"application/json";

        NSMutableDictionary* queryParams = [[NSMutableDictionary alloc] init];
    if(skip != nil)
        queryParams[@"skip"] = skip;
    if(limit != nil)
        queryParams[@"limit"] = limit;
    
        NSMutableDictionary* headerParams = [[NSMutableDictionary alloc] init];
    if(auth_token != nil)
        headerParams[@"auth_token"] = auth_token;
    

    id bodyDictionary = nil;
        
    
    

    SWGApiClient* client = [SWGApiClient sharedClientFromPool:basePath];

    

    
    
    
    
    return [client stringWithCompletionBlock:requestUrl 
                                             method:@"GET" 
                                        queryParams:queryParams 
                                               body:bodyDictionary 
                                       headerParams:headerParams
                                 requestContentType: requestContentType
                                responseContentType: responseContentType
                                    completionBlock:^(NSString *data, NSError *error) {
                        if (error) {
                            completionBlock(error);
                            return;
                        }
                        completionBlock(nil);
                    }];
    
    
    
    

}



@end