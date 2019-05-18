#TOTAL SUM
number = 30
list = [10, 11, 12, 13, 14, 17, 18, 19]
i = 0
new_list  = []
while i<len(list)/2:
	if list[i]+list[-i] == number:
		new_list.append([list[i],list[-i]])
	i = i+1
print new_list
