#PALINDROM NUMBER
list = ["n", "i","t", "i", "n"]
i= 0
j=-1
length = len(list)
while i<length:
	if list[i] == list[j]:
		a = "palindram hai"
	else:
		a ="not  PALINDROM number"
		break
	j=j-1
	i=i+1
print a
