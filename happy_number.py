class Solution:
    def isHappy(self, n: int) -> bool:
        # mengubah subjek n menjadi nilai string agar dapat diketahui panjangnya 
        n_str = str(n)

        # jika panjang n lebih dari 1
        while len(n_str) > 0:
            # memodifikasi nilai dari string n 
            # 1. mengubah string n menjadi digit dalam bentuk list
            # 2. sembari mengubah setiap nilai digit dikuadratkan 
            # 3. menambah semua nilai digit dengan sum
            # 4. mengembalikkan nilai sum menjadi string dan n_str yang baru'
            # 5. iteratif hingga sesuai dengan panjang list yang ditentukan 
            n_str = str(sum(int(digit) ** 2 for digit in n_str))
        
        # memberikan output hasil dengan mengembalikkan terlebih dahulu nilai n_str menjadi int
        # membandingkan dengan nilai 1 dan 7
        # 1**2 = 1

        # prov jika 7 akan memiliki happy number
        # 0**2 + 7**2 = 49
        # 4**2 + 9**2 = 97
        # 9**2 + 7**2 = 130
        # 1**2 + 3**2 + 0**2 = 10
        # 1**2 + 0**2 = 1 (happy number)
        return int(n_str) == 1 or int(n_str) == 7