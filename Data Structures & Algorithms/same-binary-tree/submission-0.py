# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        j =[]
        k = []
        def trav(root):
            if root == None:
                return [None]
            return [root.val] + trav(root.left) + trav(root.right)
        j = trav(p)
        k = trav(q)
        if len(j) ==len(k):
            for i in range(len(k)):
                if j[i] != k[i]:
                    return False
            else:
                return True
        else:
            return False



            