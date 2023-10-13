import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
handle = urllib.request.urlopen(url, context = ctx)
count = input('Enter count: ')
count = int(count)
position = input('Enter position: ')
position = int(position)
position -= 1

print('Retrieving: ',url)
for countNo in range(count):
	str = handle.read()
	soup = BeautifulSoup(str, 'html.parser')
	tags = soup('a')
	temp = tags[position].get('href', None)
	print('Retrieving: ',temp)
	handle = urllib.request.urlopen(temp, context = ctx)
			
