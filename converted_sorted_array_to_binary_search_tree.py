# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode(object):
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        
        # inisiasi apabila list kosong
        if nums is None:
            return None
        
        # inisiasi untuk mendapatkan nilai induk dan tahapan awal untuk menjalankan fungsi rekursif
        def convert_to_bst(left_idx, right_idx):

            # inisiasi apabila node kiri root sudah lebih besar maka return none agar pohon seimbang 
            # karena agar bagus root.left = root.right dan peran root akan terus bergant setelah induk 
            if left_idx > right_idx:
                return None
            
            # inisiasi mencari induk setiap root
            mid_idx = (left_idx + right_idx) // 2

            # memberi value untuk membuat node induk
            current_root_node = TreeNode(nums[mid_idx])

            # membuat node kiri dan kanan
            current_root_node.left = convert_to_bst(left_idx, mid_idx - 1)
            current_root_node.right = convert_to_bst(mid_idx + 1, right_idx)

            # memuat hasil dari current yang sudah di buat dari fungsi rekursif di atas
            return current_root_node
       
        return convert_to_bst(0, len(nums) - 1)

