"""
Write a function that returns the cumulative sum of	elements in	a list
"""
def	solution(input):
	output = []
	total = 0
	for i in input:
		total += i
		output.append(total)
	return	output


assert	solution([1,1,1])	==	[1,2,3]
assert	solution([1,-1,3])	==	[1,0,3]