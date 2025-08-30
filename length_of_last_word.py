class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        k = 0 
        
        for i in s[::-1]:
            if i != " ":
                k += 1
            else:
                if k == 0 and i == " ":
                    pass
                else:
                    break
        return k

a = "makan ayam goreng"
b = "nasi pustih buatan ibu "

x = Solution()
print(x.lengthOfLastWord(a))  
print(x.lengthOfLastWord(b))  