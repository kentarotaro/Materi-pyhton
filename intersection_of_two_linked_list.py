# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # output mencari value di mana kedua linked list bertemu
        # 1. menghitung panjang dari kedua list dan menyamakan titik start mereka

        # membuat base panjang nilai dari kedua linked list
        len_headA = 0
        len_headB = 0

        # membuat variabel baru dari head a agar objek tidak rusak 
        # karena jika headA = headA.next maka objek akan error
        current_headA = headA
        current_headB = headB

        # membuat loop untuk setiap komponen linked list apabila masih ada
        while current_headA:
                len_headA += 1
                current_headA = current_headA.next

        while current_headB:
                len_headB += 1
                current_headB = current_headB.next

        # mencari nilai selisih dari kedua nilai panjang
        # nilai selisih berperan dalam pergerakan linked list yang lebih panjang untuk bergerak 
        selisih = abs(len_headA - len_headB)

        # 2.  membuat pointer baru untuk kedua nilai karena sebelumnya sudah bernilai none
        pA = headA
        pB = headB

        # membuat logika if untuk perbandingan kedua nilai dalam bergerak 
        if len_headA > len_headB:
              for i in range(selisih):
                    pA = pA.next

        elif len_headB > len_headA:
              for i in range(selisih):
                    pB = pB.next

        # 3. mencari titik pointer yang sama 
        # menggunakan loop while selama pointer belum sama
        while pA != pB:
              pA = pA.next
              pB = pB.next
        # return yang diminta berbentuk objek maka hanya return pA / pB
        # apabila tidak ada intersection maka otomatis akan return None
        return pA

        