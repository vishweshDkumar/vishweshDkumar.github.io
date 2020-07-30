# DFS recursively 
def subsets1(nums):
    res = [] # watchvar res
    dfs(sorted(nums), 0, [], res)
    return res
    
def dfs(nums, index, path, res):
    res.append(path)
    for i in range(index, len(nums)):
        dfs(nums, i+1, path+[nums[i]], res)
        
def go():
	# https://leetcode.com/problems/subsets/
	subsets1([1,2,3])