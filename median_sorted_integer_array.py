import sys

def calculateMedian(intArray):
	"""
	Input: Sorted Array of Integers
	Calculates the median
	"""
	lengthOfArray = len(intArray)
	if lengthOfArray % 2 == 0:
		median = (intArray[lengthOfArray/2] + intArray[(lengthOfArray/2)-1])/2.0
	else:
		median = intArray[lengthOfArray/2]
	return median

def main(args=None):
    """The main routine"""
    inputArray = list(map(int,sys.argv[1].strip().split(',')))
    print "Median is", calculateMedian(inputArray)

if __name__ == "__main__":
    main()