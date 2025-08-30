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
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        def traverse(node):

            if node is None:
                return

            traverse(node.left) #sistem akan membuka komponen left dari node awal
            result.append(node.val) #nilai data apabila tidak memiliki left komponen atau left sudah didefinisikan
            traverse(node.right) #inisisi kode apabila akar sudah didefinisikan

        traverse(root)
        return result


    
        
    
    
    
