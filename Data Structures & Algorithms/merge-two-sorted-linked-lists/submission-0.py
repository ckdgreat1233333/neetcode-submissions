# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return
        if list1 == None:
            return list2
        if list2 == None:
            return list1  
        p = []
        while list1!= None:
            p.append(list1.val)
            list1 = list1.next
        k = []
        while list2!= None:
            k.append(list2.val)
            list2 = list2.next
        p += k
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                if p[i] >= p[j]:
                    t = p[i]
                    p[i] = p[j]
                    p[j] = t
        n = None
        i = 0
        print(p)
        while i < len(p):
            u = ListNode(p[i],n)
            n = u
            i += 1
        cn = u
        prev = None
        while cn!=None:
            nn = cn.next
            cn.next = prev
            prev = cn
            cn = nn
        
        return prev





      