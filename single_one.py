# Given an array of integers, every element appears twice except for one.
# Implement a program that will print that single one.

# Example: [1,1,2,2,3,3,4,5,5,6,6,7,7] - 4 would be the odd man out

# Note:
# Your algorithm should have a linear runtime complexity.


# *** your code here ***
def findSingle( array, n):

	res = array[0]

	for i in range(1,n):
		res = res ^ array[i]

	return res

array = [1,1,2,2,3,3,4,5,5,6,6,7,7]
print ( findSingle(array, len(array)))
