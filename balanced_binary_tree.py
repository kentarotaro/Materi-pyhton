# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check_balance(node): # helper function to check balance (root)
            if node is None: # this is base case when node is none it return 0 
                return 0
            
            left_height = check_balance(node.left) # this is a recursive call to depth of left subtree
            right_height = check_balance(node.right)

            if (left_height == -1 or right_height == -1) or abs(left_height - right_height) > 1 :
                return -1
            
            return 1 + max(left_height, right_height)

    
        return check_balance(root) != -1
    
    