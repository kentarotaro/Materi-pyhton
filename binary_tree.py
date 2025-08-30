# Definisi kelas untuk setiap Node di Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # Nilai dari node saat ini
        self.left = left      # Pointer ke anak kiri (jika ada)
        self.right = right    # Pointer ke anak kanan (jika ada)

# --- Contoh Cara Membuat Tree di Atas dalam Kode ---

# 1. Buat node-node daun terlebih dahulu (yang tidak punya anak)
node_2 = TreeNode(2) # Node dengan nilai 2
node_5 = TreeNode(5) # Node dengan nilai 5

# 2. Buat node root, lalu hubungkan dengan anak-anaknya
root_node = TreeNode(4, left=node_2, right=node_5)
print(root_node) #output print tidak merepresentasikan gambar di bawah secara langsung, tetapi bentuknya masih kode
 
# Sekarang kita punya tree:
#       4
#      / \
#     2   5


# contoh 2
#      7
#     / \
#    2   9
#   /   / \
#  1   8  12
# /
#0

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # Nilai dari node saat ini
        self.left = left      # Pointer ke anak kiri (jika ada)
        self.right = right    # Pointer ke anak kanan (jika ada)

node_2 = TreeNode(2)
node_9 = TreeNode(9)
node_1 = TreeNode(1)
node_8 = TreeNode(8)
node_12 = TreeNode(12)
node_0 = TreeNode(0)
node_7 = TreeNode(7)


node_1.left = node_0

node_9.left = node_8
node_9.right = node_12

node_2.left = node_1

node_7.left = node_2
node_7.right = node_9

root = node_7

