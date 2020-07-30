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
    #https://leetcode.com/problems/remove-nth-node-from-end-of-list/
    a = ListNode(1)
    b= ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    removeNthFromEnd(a,2)