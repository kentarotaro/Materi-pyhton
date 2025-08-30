class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # jika kondisinya tidak ada aktivitas jual-beli
        if not prices or len(prices) == 1:
            return 0
        
        # inisiasi current max profit
        current_max_profit = 0

        # inisiasi current min price
        min_price = prices[0]

        # membuat loop program 
        for i in range(1, len(prices)):
            # kita menggunakan iterasi perbandingan langsung
            # perbandngan antara profit terakhir dengan iterasi loop indeks
            current_max_profit = max(current_max_profit, prices[i] - min_price)

            # setiap kondisi indeks akan selalu dicek apabila terdapat nilai yang lebih kecil
            # menggunakan perbandingan min antara nilai min price awal dengan prices indeks sekarang
            # iterasi ini akan berkerja pada indeks selanjutnya karena baru diinput variabel
            min_price = min(min_price, prices[i])

        # return nilai profit tertinggi yang diperoleh
        return current_max_profit

