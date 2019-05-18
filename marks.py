marks = [
	[78, 76, 94, 86, 88],
	[91, 71, 98, 65],
	[95, 45, 78,],
	[87, 67, 49, 68, 88]
]
index = 0
total = 0
while index<len(marks):
	nested_index = 0
	while nested_index<len(marks[index]):
		total = total + marks[index][nested_index]
		nested_index = nested_index+1
	index = index+1
print total
