"""
Write a function that takes	a number and returns a list	of its digits
"""

def	solution(input):
	output = [int(i) for i in str(input)]
	return	output


assert	solution(123)	==	[1,2,3]
assert	solution(400)	==	[4,0,0]