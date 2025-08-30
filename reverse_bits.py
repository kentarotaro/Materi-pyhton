class Solution:
    def reverseBits(self, n: int) -> int:
        # membuat program dengan menerjemahkan input binary reverse
        # mereverse binary 
        # mencoba mengerjakan dengan cara klasik 

        # base hasil
        result = 0
        
        # membuat loop untuk int 32 bit
        for i in range(32):
            
            # melihat operasi pada pemrosesan bitwise 
            # hasil digeser ke kiri sebagai base case dan agar angka input terakhir dapat menjadi paling awal
            # contoh: 0011 <<= 1 maka menjadi 0110 
            result <<= 1
            
            # mengambil bit terakhir terlebih dahulu dengan and
            # and(&) = bernilai true hanya 1 & 1
            # jadi hanya menginput antara 1 dengan 1 saja
            last_bit = n & 1

            # menggabungkan hasil terakhir dengan result 
            # menggunakan operasi or(|)
            # operasi or akan false jika hanya 0 dengan 0 dan sisanya true
            # kasus di atas berfungsi apabila base case masih 0 
            result |= last_bit

            # bit pada int/n digeser ke kanan untuk mengambil nilai last_bit yang baru 
            n >>= 1

        # output 
        return result
