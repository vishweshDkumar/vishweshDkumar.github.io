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
def go():
    # https://leetcode.com/problems/odd-even-linked-list/
    a = ListNode(1)
    b= ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    oddEvenList(a)