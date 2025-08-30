class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # membuat variabel hasi = 0, menjadi base case awal dalam operasi xor
        hasil = 0 

        # membuat loop setiap angka di list untuk dicocokkan:
        for i in range(len(nums)):
            # memodifikasi nilai hasil dengan konsep awal 0 ^ n = n
            # jika hasilnya n^n makan akan menghailkan nilai 0 lagi
            # xor menggunakan konsep a U b - a n b 
            hasil ^= nums[i]
        
        # return nilai hasil yang sudah melewati operasi xor
        # otomatis hasil akan tunggal karena sistem kerja xor adalah mencari nilai yang bukan
        return hasil
        
        
