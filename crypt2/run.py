import sys
sys.path.append('..')
import helper

req = helper.getRequest()

body = 'This is currently doing nothing :)'


helper.writeResponse(body=body)

#substituion cypher requireing simple character frequency analysis