import os
import json

# All data to be returned to the client gets put into this dict
returnData = {
    #HTTP Status Code:
    "status": 200,
    
    #Response Body:
    "body": "<h1>Azure 2 Works :)</h1>",
    
    # Send any number of HTTP headers
    "headers": {
        "Content-Type": "text/html",
        "X-Awesome-Header": "YesItIs"
    }
}

# Output the response to the client
output = open(os.environ['res'], 'w')
output.write(json.dumps(returnData))
