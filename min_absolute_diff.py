
def min_absolute_diff(items):
	return min([abs(j-i) for i, j in zip(items[:-1], items[1:])])


