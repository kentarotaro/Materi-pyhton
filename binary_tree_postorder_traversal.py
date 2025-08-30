# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        # struktur dalam postorder adalah kiri - kanan - akar
        # membuat base result
        result = []

        # membuat stack untuk setiap objek root
        stack = [root]

        # membuat kerangka iteratif dengan while
        # membuat loop jika stack masih ada
        while stack:
            # mengambil objek induk 
            node = stack.pop()

            # mengecek apabila node ada
            if node:
                # membuat kerangka jika node kiri ada dan node kanan ada 
                # karena penambahan struktur nya kiri - kanan - akar
                # akar akan di-apppend di bagian stack paling awal(sudah terjadi pada kerangka root di atas)
                # menuju ke bagian root paling kiri 
                # sturktur yang kita mau adalah kiri - kanan - root >< root - kanan - kiri (ini hampir sama dengan preorder traversal)
                # dengan catatan di atas kita mereturn reverse sebagai ouput nya

                # menambahkan root
                result.append(node.val)

                # karena urutannya adalah root - kanan - kiri maka kita append kiri terlebih dahulu karena terkahir
                if node.left:
                    stack.append(node.left)

                # append root kanan 
                if node.right:
                    stack.append(node.right)

        # setelah didapat hasilnya kita akan mereverse karena urutannya pada awal kita buat terbalik
        # jika kita menggunakan tool reverse maka kita harus membuat variabel baru
        # menggunakan step -1 agar kode lebih elegan 
        return result[::-1]

