import re

fileName = input('Enter file name: ')

if len(fileName) < 1 : 
	handle = open("regTest.txt", 'r')
else:
	handle = open(fileName, 'r')

count = 0
for line in handle:
	line = line.strip()
	if re.search('^At', line):
		print('Starts with \'At\'')
		count += 1
print('Starts with \'At\'', count, 'times.')		


if len(fileName) < 1 : 
	handle = open("regTest.txt", 'r')
else:
	handle = open(fileName, 'r')

count = 0

for line in handle:
	line = line.rstrip()
	if re.search('had', line.lower()):
		print('Found \'hAd\'')
		count += 1

print('found had', count, 'times.')


if len(fileName) < 1 : 
	handle = open("regTest.txt", 'r')
else:
	handle = open(fileName, 'r')

count = 0

for line in handle:
	y = re.findall('[AEIOU+]', line)
	if len(y) < 1:
		continue
	count += len(y)
	print(y)

print("AEIOU found:", count, 'times.')

strn = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
h = re.findall( '\S+?@\S+', strn)
print(h)