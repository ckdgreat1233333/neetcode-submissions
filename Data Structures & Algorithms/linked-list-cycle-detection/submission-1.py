# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        c = []
        while head!= None:
            print(c)
            if head.next in c:
                return True
                break
            c.append(head.next)
            head = head.next
        else:
            return False      