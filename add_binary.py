class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        new_a = int(a, 2)
        new_b = int(b, 2)
        return bin(new_a + new_b)[2:]

p = "101"
q = "100"
x = Solution()
print(x.addBinary(p, q)) #output 1001


b = 56
c = format(b, '032b')
print(c)