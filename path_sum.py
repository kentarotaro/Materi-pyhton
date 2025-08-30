# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        # jika root tidak memiliki komponen sama sekali maka tidak ada int yang cocok (False condition)
        if not root:
            return False
        
        # memberikan variabel pada value root agar mudah dibaca
        root_value = root.val
        
        # membuat variabel queue dengan pathnya adalah nilai dari root (bukan objek)
        sum_value = deque([(root, root_value)])

        while sum_value:
            # menginput data awal induk untuk operasi awal dan iterasi awal sistem
            node, val = sum_value.popleft()

            # memberikan fungsi recrusive call sebagai pemanggilan value lama dan baru untuk masing" node
            if node and node.left:
                sum_value.append((node.left, val + node.left.val))

            if node and node.right:
                sum_value.append((node.right, val + node.right.val))

            # apabilai value root sudah sama seperti target angka 
            if node and not node.right and not node.left:
                if targetSum == val :
                    return True
        # apabila root sudah habis dan tidak juga ketemu angka yang dituju 
        return False

