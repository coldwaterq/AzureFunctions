import os
import json
import time
import subprocess
import threading

postData = open(os.environ['req'], "r").read()
headers = {}
query = {}

for key in os.environ.keys():
    if(key.startswith('REQ_HEADERS_')):
        headers[key[12:].lower()] = os.environ[key]
    elif(key.startswith('REQ_QUERY_')):
        query[key[10:].lower()] = os.environ[key]
        
print(query)
print(headers)
print(postData)

def testTimeout():
    sleep = int(query['sleep'])
    time.sleep(sleep)
    
# All data to be returned to the client gets put into this dict
returnData = {
    #HTTP Status Code:
    "status": 200,
    
    #Response Body:
    "body": "FAIL!!!!!",
    
    # Send any number of HTTP headers
    "headers": {
        "Content-Type": "text/html",
        "X-Awesome-Header": "YesItIs"
    }
}

t = threading.Thread(target=testTimeout)
t.daemon = True
t.start()
t.join(1)

if t.is_alive():
    returnData['body'] = 'The secret is 42'

# Output the response to the client
output = open(os.environ['res'], 'w')
output.write(json.dumps(returnData))
