class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        s = str(self.val)
        if self.left:
            s = str(self.left) + " "+s
        if self.right:
            s += " " + str(self.right)
        return s
    def __repr__(self):
        return self.__str__()
    def __eq__(self,other):
        return self.__str__() == other.__str__()
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None
    def __str__(self):
        if not self.next: return str(self.val)
        else: return str(self.val) + " " + str(self.next)
    def __repr__(self):
        return self.__str__()
    def __eq__(self,other):
        return self.__str__() == other.__str__()

def inorderTraversal(root):
    head = root # watchvar btree:left:right:val head
    res, stack = [], [] # watchvar ref:head:btree root
    node = None # watchvar ref:head:btree node
    while True:
        while root: 
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right
def dfs1(nums, path, res):
    if not nums:
        res.append(path)
        # return # backtracking
    for i in range(len(nums)):
        dfs1(nums[:i]+nums[i+1:], path+[nums[i]], res)
def permute(nums):
    res = [] # watchvar res
    dfs1(nums, [], res)
    return res
    
def productExceptSelf(arr):
    n=len(arr)
    prefarr=[1]*(n+1) # watchvar prefarr
    # prefarr[0]=arr[0]
    for i in reversed(range(n)):
        prefarr[i]=prefarr[i+1]*arr[i]
    ans=[1]*n # watchvar ans
    p=arr[0]
    ans[0]=prefarr[1]
    for i in range(1,n):
        ans[i]=p*prefarr[i+1]
        p*=arr[i]
    return ans
def kthSmallest(root, k):
    head = root # watchvar btree:left:right:val head
    stack = [] # watchvar ref:head:btree root
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right
def oddEvenList(head):
    if head is None or head.next is None :return head
    mainhead=head # watchvar btree:prev:next:val mainhead
    firsteven=head.next # watchvar ref:mainhead:btree head
    c=1
    prev=head # watchvar ref:mainhead:btree prev
    while(head.next is not None):
        n=head.next
        prev=head 
        head.next=head.next.next
        head=n
        c+=1
    if c%2:head.next=firsteven
    else:prev.next=firsteven
    return mainhead
def longestpalindromicsubstring(s):
    """
    :type s: str
    :rtype: str
    """
    n = len(s)
    if n < 2: return s
    dp= [[0]*n for _ in range(n)] # watchvar dp
    ans = {} # watchvar ans
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and ((j - i + 1) <= 3 or dp[i + 1][j - 1]):
                dp[i][j] = True
                ans[j-i+1] = s[i:j+1]
            else:
                dp[i][j] = False
    return ans[max(ans)]
def maxArea(height) -> int:
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

def addTwoNumbers(l1, l2, previous_carry = 0):

    carry = 0
    head = ListNode(-1) # watchvar btree:prev:next:val head
    tail = head # watchvar ref:head:btree tail
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        n = v1 + v2 + carry
        carry = n // 10
        n = n % 10
        node = ListNode(n)
        if tail:
            tail.next = node
            tail = node
        else:
            head = node
            tail = node
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return head.next

def generateParenthesis(N):
    if N == 0: return ['']
    ans = [] # watchvar ans
    for c in range(N):
        for left in generateParenthesis(c):
            for right in generateParenthesis(N-1-c):
                ans.append('({}){}'.format(left, right))
    return ans

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

# DFS recursively 
def subsets1(nums):
    res = [] # watchvar res
    dfs(sorted(nums), 0, [], res)
    return res
    
def dfs(nums, index, path, res):
    res.append(path)
    for i in range(index, len(nums)):
        dfs(nums, i+1, path+[nums[i]], res)
        
# Bit Manipulation    
def subsets2(nums):
    res = []
    nums.sort()
    for i in range(1<<len(nums)):
        tmp = []
        for j in range(len(nums)):
            if i & 1 << j:  # if i >> j & 1:
                tmp.append(nums[j])
        res.append(tmp)
    return res
    
# Iteratively
def subsets(nums):
    res = [[]]
    for num in sorted(nums):
        res += [item+[num] for item in res]
    return res

def removeNthFromEnd(head, n):
    mainhead = head # # watchvar btree:prev:next:val mainhead
    fast = head # watchvar ref:mainhead:btree fast
    slow = head # watchvar ref:mainhead:btree slow
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head
def go():
    # https://leetcode.com/problems/binary-tree-inorder-traversal/
    # a = TreeNode(1)
    # b = TreeNode(2)
    # c = TreeNode(3)
    # d = TreeNode(4)
    # a.right = b
    # b.left = c
    # b.right = d
    # ans= inorderTraversal(a)

    # https://leetcode.com/problems/permutations/
    nums = [1,2,3]
    permute(nums)


    # https://leetcode.com/problems/product-of-array-except-self/
    # productExceptSelf([1,2,3,4])


    # https://leetcode.com/problems/kth-smallest-element-in-a-bst/
    # a = TreeNode(3)
    # b = TreeNode(1)
    # c = TreeNode(4)
    # d = TreeNode(2)
    # a.left = b
    # b.right = d
    # a.right = c
    # kthSmallest(a,1)

    # https://leetcode.com/problems/odd-even-linked-list/
    # a = ListNode(1)
    # b= ListNode(2)
    # c = ListNode(3)
    # d = ListNode(4)
    # a.next = b
    # b.next = c
    # c.next = d
    # oddEvenList(a)

    # https://leetcode.com/problems/longest-palindromic-substring/
    # longestpalindromicsubstring("babad")

    # https://leetcode.com/problems/container-with-most-water/
    # maxArea([1,8,6,2,5,4,8,3,7])

    # https://leetcode.com/problems/add-two-numbers/
    # a = ListNode(1)
    # b= ListNode(2)
    # c = ListNode(3)
    # d = ListNode(4)
    # a.next = b
    # c.next = d
    # addTwoNumbers(a,b)

    # https://leetcode.com/problems/generate-parentheses/

    # generateParenthesis(3)
    # https://leetcode.com/problems/longest-palindromic-substring/
    # lengthOfLongestSubstring("abcabcbb")

    # https://leetcode.com/problems/subsets/
    # subsets1([1,2,3])

    #https://leetcode.com/problems/remove-nth-node-from-end-of-list/
    # a = ListNode(1)
    # b= ListNode(2)
    # c = ListNode(3)
    # d = ListNode(4)
    # a.next = b
    # b.next = c
    # c.next = d
    # removeNthFromEnd(a,2)

