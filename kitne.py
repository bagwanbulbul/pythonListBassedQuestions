#KITNE AADMI THE
elements = [23, 14, 56,12, 19, 9,15, 25, 31, 42, 43]
index = 0
even_list = []
odd_list = []
even_sum = 0
odd_sum = 0
average = 0
while index<len(elements):
	if (elements[index]%2 == 0):
		even_list.append(elements[index])
		even_length = len(even_list)
		even_sum = even_sum+elements[index]
		average = even_sum/even_length
	elif(elements[index]%2 == 1):
		odd_list.append(elements[index])
		odd_length = len(odd_list)
		odd_sum = odd_sum+elements[index]
		average = odd_sum/odd_length
	index = index+1

print "even number list = ",even_list
print "total even number in list =",len(even_list)
print "sum of even number = ", even_sum
print "avreage of even number" , average
print "odd number list = ", odd_list
print "total odd number in list = ",len(odd_list)
print "sum of odd number = ", odd_sum
print "avreage of odd number = ", average
