#Maximum Difference Between Even and Odd Frequency I

class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        comp = {}
        for char in s:
            comp[char] = comp.get(char, 0) + 1
        odd = []
        even = []
        for freq in comp.values():
            if freq % 2 == 0:
                even.append(freq)
            else:
                odd.append(freq)
        return abs(max(odd) - min(even)) 
    
  
    
x = "aabbccddeefffffjjjgghhhhh"
y = Solution()
print(f"Input: s = '{x}'")
print(f"Hasil: {y.maxDifference(x)}")

#jika menggunakan Counter dari collections

from collections import Counter
class SolutionCounter(object):
    def maxDifferenceCounter(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = Counter(s).values()
        return max(f for f in freq if f % 2 == 1) - min(f for f in freq if f % 2 == 0) 
x = "aabbccddeefffffjjjgghhhhh"
y_counter = SolutionCounter()
print(f"Input: s = '{x}'")
print(f"Hasil Counter: {y_counter.maxDifferenceCounter(x)}")