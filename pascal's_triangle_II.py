class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        # membuat base dari list dengan komponen index 0 
        triangle = [[1]]
        row = triangle[0]

        # inisiasi k untuk cek nilai dari tujuan 
        k = 0 

        # loop apabila k masih kurang dari tujuan karena jika tidak maka false dan langsung return hasil
        while k < rowIndex:
            # menambah komponen apabila true
            row.append(1)
            # jika kasusnya pada baris ke-3 dst
            if rowIndex > 1:
                # memodifikasi komponen dengan dimulai dari len(row) -2 jika dibandingkan dengan hanya -2 
                # perbandingan di atas membuat kode lebih dinamis 
                # dan berhenti di indeks 1 karena indeks 0 nilainya adalah 1
                for i in range(len(row) - 2, 0, -1):
                    # memodifikasi baris dari kanan ke kiri
                    # karena variabel 1 akan selalu ditambahkan di bagian paling akhir
                    row[i] = row[i] + row[i - 1]

            # mnambah nilai k setiap kali iterasi berjalan dan dalam kondisi true
            k += 1

        # return triangle jika loop false
        return row