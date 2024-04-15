# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def preOrder(root, current_sum):
            if root == None:
                return 0

            current_sum = current_sum * 10 + root.val
            # print(current_sum)

            if root.left == None and root.right == None:
                return current_sum
            
            return preOrder(root.left, current_sum) + preOrder(root.right, current_sum)
        
        return preOrder(root, 0)

    