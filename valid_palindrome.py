class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # membuat kasus jika input s kosong atau hanya spasi:
        if not s or s == " ":
            return True

        # membuat agar nilai input menjadi alphabet kecil semua
        s = s.lower()
        s_new =[]

        # membuat karakter bersih yang hanya berisi huruf dan angka saja
        for i in range(len(s)):
            # kita akan mengecek setiap komponen menggunakan isalnum() 
            # apabila true maka akan ditambahkan ke dalam s yang baru
            if s[i].isalnum() == True:
                s_new.append(s[i])
        
        # membuat variabel ruas kiri dan kanan untuk membandingkan objek
        left = 0
        right = len(s_new) - 1

        # membuat loop ketika left kurang dari right jadi jika nilai sama maka loop berhenti
        while left < right:
            # membuat kondisi jika ujung kanan dan kiri sama
            if s_new[left] == s_new[right]:
                # input kanan dan kiri harus selalu diperbarui setiap karakter
                left += 1
                right -= 1

            # jika karakter yang dibandingkan tidak sama, return false
            else:
                return False

        # return hasil akhir apabila true
        return True
    

# versi yang lebih efisien dan pythonic
# import regex 
import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # membuat agar input alphabet kecil semua 
        s_new = s.lower()

        # memisahkan setiap komponen s yang nanti akan diubah
        s_new = s_new.split()

        # menggabungkan setiap komponen s tanpa spasi
        s_new = "".join(s_new)
        
        # menggunkan regex dengan cara bacanya [^a-z0-9] : ^ (bukan) a-z (dan) 0-9
        # dan diganti dengan '' yang artinya menghapus selain komponen di atas
        # s_new sebagai model yang mau diubah
        s_new = re.sub(r'[^a-z0-9]', '', s_new)

        # return perbandingan nilai s yang sudah diupdate
        # menggunakan perbandingan nilai list s update awal dengan yang terbalik
        # return akan menghasilkan nilai boolean(True/False)
        return s_new == s_new[::-1]