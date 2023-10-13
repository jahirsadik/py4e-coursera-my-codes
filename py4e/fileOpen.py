# apparently this is how you comment

name = input("Enter file:")
handle = open(name)

counts = dict()
for line in handle:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word,0) + 1

bigcount = 0
bigword = None

for word,count in counts.items():
	if count > bigcount:
		bigword = word
		bigcount = count

print(bigword, bigcount)