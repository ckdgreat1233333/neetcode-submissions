# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) < 1:
            return
        p =[]
        for i in range(len(lists)):
            p.append(lists[i])
        k = []
        for i in range(len(p)):
            while p[i]!=None:
                k.append(p[i])
                p[i] =p[i].next
        if len(k) <1:
            return
        k.sort(key=lambda x: x.val)
        l = 0 
        head = k[0]
        for i in range(1,len(k)):
            k[l].next = k[i]
            l +=1
        k[-1].next = None
        return head