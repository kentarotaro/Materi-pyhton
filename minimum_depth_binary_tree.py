# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # apabila treenode kosong maka output 0
        if not root:
            return 0
        
        # jika treenode hanya memiliki induk saja maka ouput 1 
        # fungsi ini juga berlaku sebagai base case daun memberikan nilai 1 
        elif not root.left and not root.right:
            return 1
        
        # recurisive call dengan self agar value pemanggilan dapat merujuk ke fungsi selanjutnya
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        # kasus jika hanya ada akar sebagian dengan penambahan akar yang ada + 1 (nilai dari induk akar)
        if not root.left:
            return right_depth + 1
        
        elif not root.right:
            return left_depth + 1

        # return fungsi membandingkan nilai kiri dan kanan dengan jarak terpendek menggunakan min()
        return 1 + min(left_depth, right_depth)



## cara lain menggunakan BFS 

class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        depth = 0 

        # berperan sebagai queue untuk BFS sebagai urutan pemanggilan stack 
        stack = [(root, depth + 1)]

        # loop jika stack masih ada (True condition)
        while stack:
            node, depth = stack.pop(0) # mengambil iterasi pertama dari stack

            # kondisi percabangan harus dilakukan bersama maka dari itu menggunakan if tunggal  
            if node and node.left:
                # kondisi ketika terdapat akar kiri maka tambahkan ke stack dengan penambahan kedalaman 1
                stack.append((node.left, depth + 1))
                # kondisi ketika terdapat akar kanan maka tambahkan ke stack dengan penambahan kedalam 1 
            if node and node.right:
                stack.append((node.right, depth + 1))
            if node and not node.left and not node.right:
                # kondisi di mana tidak ada akar kiri dan kanan lagi 
                return depth
        # kondisi ketika stack dalam keadaan kosong atau false di awal iterasi maka return 0 
        return 0 

