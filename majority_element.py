class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # menggunakan ide kandidat dan hitungan
        # kandidat akan berperan ketika terdapat hitungan min 1
        # jika tidak ada maka return none
        # aksi akan -1 jika beda dan +1 jika sama
        
        # membuat base hitungan dan kandidat
        candidate = None
        count = 0

        # membuat loop untuk setiap komponen di nums
        for num in nums:
            # base case saat awal dan ketika count kembali menjadi 0 maka input nilai terakhir
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            
            else:
                count -= 1
        
        # return output candidate yang sudah diperbarui
        return candidate
