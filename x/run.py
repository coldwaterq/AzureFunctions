import os
import json
import time
import subprocess

from functools import wraps
import errno
import os
import signal

class TimeoutError(Exception):
    pass

def timeout(seconds=10):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.setitimer(signal.ITIMER_REAL,seconds) #used timer instead of alarm
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return wraps(func)(wrapper)
    return decorator

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

@timeout(1)
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

try:
    testTimeout()
except TimeoutError as e:
    returnData['body'] = 'The secret is 42'

# Output the response to the client
output = open(os.environ['res'], 'w')
output.write(json.dumps(returnData))
