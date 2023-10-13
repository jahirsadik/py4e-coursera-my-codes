import json 
data = '''{
	"person":{
		"name": "Chuck",
		"phone": {
			"type": "intl",
			"number": "+880 1551615724"
		},
		"email":{
			"hide": "no"
		}
	}
}'''


info = json.loads(data)
print(info,"\n\n")
print('Name:', info["person"]["name"])
print('Hide:', info["person"]["email"]["hide"])

