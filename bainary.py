# BINARY TO DECIMAL
binary_num = [1,0,0,1,1,0,1,1]
i= -1
multi = 1
sum = 0
length = len(binary_num)
while i>= -length:
	multi1 = binary_num[i]*multi
	sum = multi1+sum
	multi = multi*2
	i = i-1
print sum
