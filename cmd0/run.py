import sys
sys.path.append('..')
import helper
import subprocess

req = helper.getRequest()

body = '''<p>What IP would you like to ping?
<form action="POST">
	<label>Address<input name=address></input></label>
	<input type=submit/>
</form>
'''

if req.postData != '':
	data = req.postData.split('&')
	for keyVal in data:
		(key,val)=keyVal.split('=')
		if(key == 'address'):
			output = subprocess.check_output('ping '+val, shell=True)
			body += '<p>'+output+'</p>'

helper.writeResponse(body=body)



#; print flag