# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Treenode(object):
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # antisipasi apabila root tidak ada komponen
        if root is None:
            return 0
        
        # mencai kedalaman akar dengan fungsi rekursif dasar dan self agar value sebelumnya tersimpan
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # 1 merupakan induk yang akan ditambahkan untuk akar terdalam dengan max
        return 1 + max(left_depth, right_depth)
            
