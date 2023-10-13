def lenstr(str):
	len = 0
	while str[len:]: # str[len:]: ???
		len += 1
	return len

print(str(lenstr("Hello")))