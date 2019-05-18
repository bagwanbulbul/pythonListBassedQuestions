#DIFFRENCE 
list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
i = 0
new_list = []
while i <len(list1):
	j = 0
	while j<len(list2):
		if list1[i] == list2[j]:
			new_list.append(list1[i])
		j=j+1
	i=i+1
print new_list
