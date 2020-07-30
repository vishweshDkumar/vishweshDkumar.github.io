def dfs1(nums, path, res):
    if len(nums)==0:
        res.append(path)
        return
        # return # backtracking
    for i in range(len(nums)):
        dfs1(nums[:i]+nums[i+1:], path+[nums[i]], res)
def permute(nums):
    res = [] # watchvar res
    dfs1(nums, [], res)
    return res

def go():
	# https://leetcode.com/problems/permutations/
	nums = [1,2,3]
	permute(nums)
