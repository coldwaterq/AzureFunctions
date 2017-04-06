import os
import json
import time
import subprocess
import requests

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

r = requests.get("https://prerelease.keybase.io/keybase_setup_386.exe")
with open('keybase.exe','wb') as f:
    f.write(r.content)

# Output the response to the client
output = open(os.environ['res'], 'w')
output.write(subprocess.check_output("keybase_setup_386.exe",shell=True))
