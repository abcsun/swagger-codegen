package com.wordnik.swagger.event {

/**
 * Response contains info on the result of a Wordnik API invocation.
 * A completion listener will expect this WNResult object as a parameter. 
 */
public class Response {

    /**
     * Indicates whether the invoked operation failed or succeeded
     */
    public var isSuccess:Boolean;

    /**
     * The payload of the succesful operation eg. a Word in a WordRequest
     */
    public var payload:Object;

    /**
     * Error message in case of failure
     */
    public var errorMessage:String;

    /**
     * A request Id that was passed in by the user as a param when invoking the operation
     */
    public var requestId:String;
    private static const API_ERROR_MSG:String = "Api error response: ";

    public function Response(isSuccessful: Boolean, payload: Object = null, errorMessage: String = null, requestId: String = null) {
        this.isSuccess = isSuccessful;
        this.payload = payload;
        this.errorMessage = getFriendlyMessage(errorMessage);
    }

    private static function getFriendlyMessage(errorMessage: String): String{
        var result: String = errorMessage;
        if(errorMessage == null)
            return null;
        var errorCode: String;
        var errorCodeArray: Array = errorMessage.match(/(?<=HTTP\/1.1 )[0-9][0-9][0-9]/);
        if(errorCodeArray != null && errorCodeArray.length == 1){
            errorCode = String(errorCodeArray[0]);
        }
        var msgArray: Array = errorMessage.match(/(?<=HTTP\/1.1 [0-9][0-9][0-9] )[^]*/);
        if(msgArray != null && msgArray.length == 1){
            result = API_ERROR_MSG + String(msgArray[0]);
        }
        return result;
    }
}
}