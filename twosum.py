def twoSumAllPairs(nums, target):
    """
    Mencari SEMUA pasangan indeks yang jika dijumlahkan sama dengan target.
    
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    seen = {}
    result = []
    
    # Buat mapping: nilai -> list indeks
    for i, num in enumerate(nums):
        if num in seen:
            seen[num].append(i)
        else:
            seen[num] = [i]
    
    # Cari semua pasangan
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            if complement == num:
                # Kasus khusus: num + num = target
                # Hanya ambil pasangan dengan indeks > i untuk menghindari duplikasi
                for j in seen[complement]:
                    if j > i:
                        result.append([i, j])
            else:
                # Kasus normal: num + complement = target
                # Hanya proses jika num < complement untuk menghindari duplikasi
                if num < complement:
                    for j in seen[complement]:
                        result.append([i, j])
    
    return result

#menggunakan nested loop yang lebih sederhana

def twoSumAllPairsSimple(nums, target):
    """
    Versi yang lebih sederhana dengan nested loop.
    Lebih mudah dipahami tapi kurang efisien O(n²).
    """
    result = []
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                result.append([i, j])
    
    return result

# Test dengan data Anda
x = [2, 7, 4, 5]
y = 9
print(f"Input: nums = {x}, target = {y}")
print(f"Hasil (hash map): {twoSumAllPairs(x, y)}")
print(f"Hasil (simple): {twoSumAllPairsSimple(x, y)}")

