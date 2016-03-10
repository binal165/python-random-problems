"""

Write	a	function	that	returns	the	elements	on	odd	positions	(0	based)	in	a	list

"""

def	solution(input):
	# 1st solution
	#output = [val for ind, val in enumerate(input) if ind % 2 != 0]
	
	# 2nd solution
	output = input[1::2]
	return output


# Test Code
assert	solution([0,1,2,3,4,5])	==	[1,3,5]
assert	solution([1,-1,2,-2])	==	[-1,-2]