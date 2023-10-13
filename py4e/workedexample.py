sum = 0
count = 0
average = 0
while(True):
	var = input("Input: ")
	if var == "Done" :
		break
	else:
		try: 
			sum = sum + int(var)
			count = count + 1
		except:
			print("not a number")

print("Sum:", sum, "count:", count, "average:", (sum/count))	
