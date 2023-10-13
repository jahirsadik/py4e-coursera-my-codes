file = open("filedemo.txt", 'r')
count = 0

for line in file:
	print(line.strip())
	words = line.split()
	for word in words:
		if word.lower().startswith('https'):
			count =  count + 1
print(count)
