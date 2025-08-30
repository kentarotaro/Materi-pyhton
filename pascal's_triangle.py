class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        # jika diminta 0 maka return list kosong
        if numRows == 0:
            return []
        
        # base list dengan index 0
        triangle = [[1]]
        
        #jika diminta 1 maka return list dengan satu baris
        if numRows == 1:
            return triangle
        for i in range(1, numRows):
            #menginisiasi jumlah komponen pada baris i 
            row = [1] * (i + 1)

            # membuat nilai agar akurat dari baris 1 hingga sebelum baris terakhir  
            for j in range(1, i):
                # mengisi baris dengan kelipatan dari baris sebelumnya
                # mengganti nilai row secara in-place atau update list
                # nilai_row = triangle sebelumnya dengan index sebelum j dan j
                # nilai row sebelumnya yang 1 akan langsung diupdate dengan format 
                # row[j] = k 
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            # menambahkan baris baru ke triangle
            # ingat bahwa menaruh append jangan di dalam for i karena dia masih memproses nilai row
            triangle.append(row)
        # output
        return triangle