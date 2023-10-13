import json
data = '''
{
	"persons":[
		{
			"name": "jahir sadik monon",
			"id": "32",
			"attribute": "none"
		},
		{
			"name": "farhan mahmud",
			"id": "16",
			"attribute": "hujur"
		}
	]
}
'''

print(json.loads(data)["persons"][0])