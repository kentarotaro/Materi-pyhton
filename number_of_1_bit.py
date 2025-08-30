class Solution:
    def hammingWeight(self, n: int) -> int:
        # memberikan output nilai 1 dari biner n 
        return bin(n).count('1') # menghitung nilai '1' yang ada pada baris biner n 

# mencoba pendekatan lain
class Solution:
    def hammingWeight(self, n: int) -> int:
        # menghitung nilai '1' yang ada pada baris biner n
        result = 0 
        for i in range(2, len(bin(n))):
            if bin(n)[i] == '1':
                result += 1
        
        return result 

# mencoba pendekatan dengan basis 2
class Solution:
    def hammingWeight(self, n: int) -> int:
        # menghitung nilai '1' yang ada pada baris biner n
        result = 0
        while n > 0:
            if n % 2 == 1:
                result += 1
            n //= 2
        return result 
