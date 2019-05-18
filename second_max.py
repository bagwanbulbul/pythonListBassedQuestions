 #SECOND MAXIMUM NUMBER
num = [50, 40, 70, 20, 58, 79, 45, 67, 98, 7, 90]
i=0
max = num[i]
new_list=[]
while (i<len(num)):
	if num[i]>max:
		max=num[i]
	j= 0
	second_max=num[i]
	while j<len(num):
		if max>num[j] and second_max<num[j]:
			second_max=num[j]
		j=j+1
	i=i+1
print max
print second_max
