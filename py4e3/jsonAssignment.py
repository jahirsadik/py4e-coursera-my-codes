import json
import urllib.request, urllib.parse, urllib.error

url = 'http://py4e-data.dr-chuck.net/comments_647747.json'
data = urllib.request.urlopen(url).read().decode()
jsonData = json.loads(data)
lst = jsonData["comments"]
sum = 0
for item in lst:
	value = int(item["count"])
	sum += value
print(sum)