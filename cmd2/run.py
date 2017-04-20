import sys
sys.path.append('..')
import helper

req = helper.getRequest()

body = 'This is currently doing nothing :)'


helper.writeResponse(body=body)

#https://blog.nelhage.com/2011/03/exploiting-pickle/