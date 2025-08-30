# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # kondisi jika cll kosong atau komponen cll hanya ada satu maka return false
        if not head or not head.next:
            return False
        
        # membuat slow dan fast pointer 
        slow = head
        fast = head

        # membuat loop dengan fast untuk mencari jika bertemu kondisi cycle
        # menggunakan fast untuk mengantisipasi terjadinya break ketika kondisi dua komponen bertemu 
        while fast and fast.next:
            # membuat step atau langkah untuk slow dan fast
            # slow akan bergerak setiap satu langkah
            # fast akan bergerak setiap dua langkah 
            slow = slow.next
            fast = fast.next.next

            # membuat kondisi apabila benar listnode yang diberikan adalah cycle
            # yaitu ketika kondisi pointer slow dan fast sama
            if slow == fast:
                return True
        
        # jika tidak ada cycle maka return false
        return False
# kode di atas menggunakan algoritma "Floyd's Tortoise and Hare" (kura-kura dan kelinci)