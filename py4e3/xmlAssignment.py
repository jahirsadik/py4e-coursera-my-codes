import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET 
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

handle = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_647746.xml', context = ctx).read()

stuff = ET.fromstring(handle)
lst = stuff.findall('comments/comment')
sum = 0
for item in lst:
	value = item.find('count').text
	sum += int(value)
print(sum)