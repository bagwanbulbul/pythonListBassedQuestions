marks = [
	[78, 76, 94, 86, 88],
	[91, 71, 98, 65],
	[95, 45, 78],
	[87, 67, 49, 68, 88]
]
i = 0
total = 0
while i<len(marks):
	j = 0
	while j<len(marks[i]):
		total = total + marks[i][j]
		j= j+1
		avreage = total/j
	print i+1, "year ka average - ", avreage
	total = 0
	i = i+1
