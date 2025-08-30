# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Treenode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        if root is None:
            return True
               
        def isMirror(node_1, node_2):

            if node_1 is None and node_2 is None:
                return True
            elif node_1 is None or node_2 is None:
                return False
            elif node_1.val != node_2.val:
                return False
            else:
                return isMirror(node_1.left, node_2.right) and isMirror(node_1.right, node_2.left)
            
        return isMirror(root.left, root.right)  # return the result of the function call