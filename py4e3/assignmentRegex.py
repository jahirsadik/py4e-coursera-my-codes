import re

handle = open('regex_sum_646996.txt', 'r')
sum = 0

for line in handle:
	numList = re.findall('[0-9]+', line)
	if len(numList) < 1:
		continue
	for number in numList:
		sum += int(number)

print(sum)