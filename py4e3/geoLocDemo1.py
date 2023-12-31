import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
	address = input('Enter address: ')
	if len(address) < 1:
		break

	url = serviceurl + urllib.parse.urlencode({'address': address})

	print('Retrieving -> ', url)
	uh = urllib.request.urlopen(url)
	data = uh.read().decode()
	print('Retrieved:', len(data), 'characters')

	try:
		js = json.loads(data)
	except:
		js = None

	if not js or 'status' not in js or js['status'] is not 'OK':
		print('==== Failure To Retrieve ====')
		print(data)
		continue

	print(js.dumps(data))
