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
        headers[key] = os.environ[key]
    elif(key.startswith('REQ_QUERY_')):
        query[key] = os.environ[key]
        
print(query)
print(headers)
print(postData)

def testTimeout():
    time.sleep(10)
    
# All data to be returned to the client gets put into this dict
returnData = {
    #HTTP Status Code:
    "status": 200,
    
    #Response Body:
    "body": "{\"Data\":\"Thank you for your data\"}",
    
    # Send any number of HTTP headers
    "headers": {
        "Content-Type": "text/html",
        "X-Awesome-Header": "YesItIs"
    }
}

t = threading.Thread(target=testTimeout,daemon=True) 
t.join(1)

if t.is_alive():
    returnData['body'] = 'The secret is 42'

# Output the response to the client
output = open(os.environ['res'], 'w')
output.write(json.dumps(returnData))
