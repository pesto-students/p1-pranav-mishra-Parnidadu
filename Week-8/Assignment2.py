# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.valid(root,float('-inf'),float('inf'))
    
    def valid(self,root,lower,upper):
        if not root:
            return True
        
        if (root.val<=lower or root.val>=upper):
            return False
        
        return self.valid(root.left,lower,root.val) and self.valid(root.right,root.val,upper)
        

# Success
# Details
# Runtime: 58 ms, faster than 55.82% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.4 MB, less than 77.83% of Python3 online submissions for Validate Binary Search Tree.