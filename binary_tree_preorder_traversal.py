# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # struktur dalam preorder adalah akar - kiri - kanan 
        # membuat base result
        result = []
        # membuat stack dari root
        stack = [root]

        # membuat fungsi iteratif dengan loop selama stack tidak kosong atau true
        while stack: 
            # pop stack / parent untuk diambil 
            node = stack.pop()
            # menambahkan nilai pop ke dalam result (push)
            if node:
                result.append(node.val)

                # mengecek apakah node kanan dan kiri ada
                # 1. membuat iterasi awal cek node kanan karena dia berada di urutan terakhir jika ada node kiri
                # 2. hal di atas bertujuan untuk menghindari node kiri di push ke dalam result sebelum node kanan
                # 3. karena pop akan mengambil node yang berada paling kanan
                if node.right:
                    stack.append(node.right)
                
                if node.left:
                    stack.append(node.left)

        # output hasil
        return result