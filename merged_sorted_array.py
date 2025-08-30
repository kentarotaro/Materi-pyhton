class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1 #posisi akhir nums1
        p2 = n - 1 #posisi akhir nums2
        p_merge = (m + n) -1 #inisiasi posisi list baru bagian terakhir   

        #iterasi dengan konsep input mundur 
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] >= nums2[p2]: #jika indeks p1 lebih besar maka iterasi akan mengisi bagian paling belakang
                nums1[p_merge] = nums1[p1]
                p1 -= 1
            else: #jika kondisi lain maka iterasi lain aan menginput balik
                nums1[p_merge] = nums2[p2]
                p2 -= 1
            p_merge -= 1 #agar iterasi list kompleks selalu mundur
        return nums1 #mengembalikkan nilai nums1 yang sudah diiterasi

                
                     
