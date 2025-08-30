# Find the Index of the First Occurrence in a String
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_n = len(needle)
        len_h = len(haystack)

        for i in range(len_h - len_n + 1): # untuk mengantsipasi list out of range karena akan dibuat slice
            if haystack[i : i + len_n] == needle: # slice berhenti ketika indeks ada pada sebelum i + len_n
                return i
        return -1


    
haystack = "sadbutsad"
needle = "sad"
x = Solution()
print(x.strStr(haystack, needle))

haystack2 = "leetcode"
needle2 = "leeto"
print(x.strStr(haystack2, needle2))

haystack3 = "aomndandobrawijaya"
needle3 = "brawijaya"
print(x.strStr(haystack3, needle3))