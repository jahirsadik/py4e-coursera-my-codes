# apparently this is how you comment

name = input("Enter file:")
handle = open(name)

counts = dict()
for line in handle:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word.lower(),0) + 1
'''
stuffs = list()
 
for itr in counts:
	stuffs.append((counts[itr], itr))

stuffs = sorted(stuffs, reverse = True)

for val,key in stuffs[:10]:
	print(key, val)
	'''

print(sorted([(v,k) for (k,v) in counts.items()], reverse = True)[:10])

