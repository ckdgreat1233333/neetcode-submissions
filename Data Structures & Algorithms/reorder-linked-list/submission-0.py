# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p = []
        while head!=None:
            p.append(head)
            head = head.next
        def arrange(p):
            l = []
            i = 0
            j = 1
            k = len(l)
            while k<len(p):
                l.append(p[i])
                l.append(p[len(p)-j])
                i +=1
                j += 1
                k = len(l)
            if len(p)%2 == 1:
                f = []
                for i in range(len(p)):
                    f.append(l[i])
                return f 
            else:
                return l
        k = arrange(p)
        head = k[0]
        u = 0
        for i in range(1,len(k)):
            k[u].next =k[i]
            u +=1
        k[-1].next = None
        return None






