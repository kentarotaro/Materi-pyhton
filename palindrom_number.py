class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 :
            return False
        s =  str(x)
        return s == s[::-1]



x = Solution()
print(x.isPalindrome(12321))  # True
print(x.isPalindrome(-121))
print(x.isPalindrome(267))