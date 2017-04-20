import sys
sys.path.append('..')
import helper
import time

req = helper.getRequest()

def testTimeout():
    sleep = int(req.query['sleep'])
    time.sleep(sleep)
    
if helper.timeout(testTimeout, 1):
    body = 'The secret is 42.'
else:
    body = 'I am still standing.'

helper.writeResponse(body=body)
