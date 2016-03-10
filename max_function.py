
def maximum(items):
	m = items[0]
	for x in items:
		if m < x:
			m = x
	return m

assert maximum([2,5,5,7,8]) == 8