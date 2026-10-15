# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c = []
        while head!= None:
            c.append(head)
            head = head.next
        p =[]
        for i in range(1,len(c)+1):
            if i == n:
                continue
            else:
                p.append(c[-i])
        k = []
        for i in range(1,len(p)+1):
            k.append(p[-i])
        j = 0
        if len(k)<1:
            return
        for i in range(1,len(k)):
            k[j].next  = k[i]
            j += 1
        k[-1].next = None
        return k[0]