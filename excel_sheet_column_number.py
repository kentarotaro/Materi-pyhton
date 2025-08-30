class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        # soal ini sama seperti excel sheet column title tapi yang diminta adalah mengelurakan output int
        # menggunakan base result dalam bentuk None karena objek int
        result = 0

        # membuat loop untuk setiap columntitle
        # ide dalam pembuatan column title tetap menggunakan basis 26
        # namun perbedaannya adalah kita mengubah str menjadi int

        length_word = len(columnTitle)
  
        # ide dalam membuat loop ini dengan penggunaan pop apabila str masih ada
        # menggunakan setiap komponen word
        # menggunakan brute force untuk memecah pendekatan rumus
        # apabila panjang dari word > 2 maka kita perlu menghitung nya dengan rumus:
        # result = (26.(panjang word - 2) + n).26
        # jika panjang nya lebih dari 1 dan kurang dari tiga maka:
        # result = 26. n 
        # jika hanya 1 maka:
        # result = n
        # dengan catatan n sendiri adalah kode ascii 


        # mencoba menggunakan pendekatan iteratif dari kesimpulan di atas
        # mencba loop untuk setiap komponen dari awal serta mencari nilainya
        for i in range(length_word):
            # ini akan menjadi fungsi iteratif yang mana ia akan menginput nilai awal sebagai satuan 
            # lalu baru mengoperasikan puluhan dst pada value kedua
            word_val = ord(columnTitle[i]) - 64
            # konsepnya dengan menjadikan n.26 + m(m sebagai nilai batas akhir pada value akhir) 
            # yang lalu berkembang menjadi ((n.26 + m)*26) + m dst
            result = (result * 26) + word_val

        # return output, jika none maka 0 
        return result
    
x = Solution()
a = "AAB"
print(x.titleToNumber(a))
        