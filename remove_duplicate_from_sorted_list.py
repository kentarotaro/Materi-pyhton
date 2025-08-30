# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Tangani kasus dasar: List kosong atau hanya satu node
        # Jika head adalah None, atau head.next adalah None, tidak ada duplikat.
        if head is None or head.next is None:
            return head

        # Inisialisasi pointer 'current' ke head
        current = head
                
        # Loop selama 'current' bukan None DAN 'current' memiliki node berikutnya
        # yang bisa dibandingkan
        while current is not None and current.next is not None:
            # Jika nilai node saat ini sama dengan nilai node berikutnya (duplikat)
            if current.val == current.next.val:
                # Lewati node duplikat (current.next)
                # current.next yang baru akan menunjuk ke node setelah node duplikat
                current.next = current.next.next
                # Penting: current TIDAK bergerak, karena bisa jadi ada duplikat lain
                # yang perlu dihapus dari posisi current saat ini.
            else:
                # Jika nilai berbeda (tidak ada duplikat)
                # Geser 'current' ke node berikutnya
                current = current.next
        
        # Setelah loop selesai, kembalikan head dari list yang sudah dimodifikasi in-place
        return head
        




a = [1,1,2,2,3,4,5]
x = Solution()
print(x.deleteDuplicates(a))   










        