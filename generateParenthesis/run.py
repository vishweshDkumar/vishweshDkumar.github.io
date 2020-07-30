

def generateParenthesis(N):
    if N == 0: return ['']
    ans = [] # watchvar ans
    c = 0 # watchvar c
    left = []  # watchvar left
    right = [] # watchvar right
    for c in range(N): 
        for left in generateParenthesis(c):
            for right in generateParenthesis(N-1-c):
                ans.append('({}){}'.format(left, right))
    return ans


def go():
	# https://leetcode.com/problems/generate-parentheses/

	generateParenthesis(3)