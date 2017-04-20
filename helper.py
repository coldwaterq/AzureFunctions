import os
import collections
import time
import json
import threading

def getRequest():
    request = collections.namedtupple('request','postData headers query')
    request.postData = open(os.environ['req'], "r").read()
    request.headers = {}
    request.query = {}

    for key in os.environ.keys():
        if(key.startswith('REQ_HEADERS_')):
            request.headers[key[12:].lower()] = os.environ[key]
        elif(key.startswith('REQ_QUERY_')):
            request.query[key[10:].lower()] = os.environ[key]
    return request

def writeResponse(status=200, body='', headers={"Content-Type": "text/html"}):
    returnData = {
        #HTTP Status Code:
        "status": status,
        
        #Response Body:
        "body": body,
        
        # Send any number of HTTP headers
        "headers": headers
    }
    output = open(os.environ['res'], 'w')
    output.write(json.dumps(returnData))
            
def timeout(function, t):
	t = threading.Thread(target=function)
	t.daemon = True
	t.start()
	t.join(t)
	if t.is_alive():
		return True
	return False