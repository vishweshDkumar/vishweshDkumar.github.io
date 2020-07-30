def lengthOfLongestSubstring(s):
    start = 0 # watchvar start
    maxLength = 0 # watchvar maxLength
    usedChar = {} # watchvar usedChar
    
    for i in range(len(s)):
        if s[i] in usedChar and start <= usedChar[s[i]]:
            start = usedChar[s[i]] + 1
        else:
            maxLength = max(maxLength, i - start + 1)

        usedChar[s[i]] = i 

    return maxLength

def go():
	 # https://leetcode.com/problems/longest-substring-without-repeating-characters/
	lengthOfLongestSubstring("abcabcbb")
