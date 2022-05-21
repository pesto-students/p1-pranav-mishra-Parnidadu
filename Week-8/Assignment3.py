# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root:
            output = []
            level_node = [root]
            while level_node:
                new_level = []
                output.append([])
                for node in level_node:
                    output[-1].append(node.val)
                    if node.left:
                        new_level.append(node.left)
                    if node.right:
                        new_level.append(node.right)
                level_node = new_level
            return output
        else:
            return
        

# This program is tested and verified on leetcode,

# Success
# Details
# Runtime: 47 ms, faster than 52.13% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 14.2 MB, less than 52.36% of Python3 online submissions for Binary Tree Level Order Traversal.