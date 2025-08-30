class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        # membuat base untuk result
        result = ""
        # membuat variabel baru untuk columnNumber 
        # fungsinya untuk menghindari merusak objek utama pada argument saat perubahan nilai dalam loop
        number = columnNumber
        
        # membuat loop untuk setiap coloumn number
        while number > 0:
            # modulo untuk alphabet dalam basis 26
            # membuat agar a = 0 ... z = 25 sebagai identitas 
            letter = (number - 1 ) % 26
            # menambahkan hasil ke dalam result dengan mengubah nilai letter menjadi chr
            result = chr(letter + 65) + result 

            # membuat logika apabila ternyata input tersebut lebih dari 26 
            # ingat untuk setiap kelipatan harus dikurangi satu karena nilai n akan kembali ke bentuk semula
            number = (number - 1) // 26
        # return output 
        # return dengan hasil terbalik karena input pertama pada letter adalah angka satuan 
        return result

x = Solution()
a = 52 # AZ
print(x.convertToTitle(a))