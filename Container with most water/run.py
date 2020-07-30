
def maxArea(height):
    i = 0 # watchvar i
    j = len(height)-1 # watchvar j

    maxi = 0 # watchvar maxi
    while i < j:
        if height[i] <= height[j]: 
            overall_height = height[i]
            i += 1
        else:
            overall_height = height[j]
            j -= 1

        maxi = max(maxi, (j-i+1)*overall_height)


    return maxi


def go():
	# https://leetcode.com/problems/container-with-most-water/
	maxArea([1,8,6,2,5,4,8,3,7])