class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit = "".join([str(num) for num in digits])
        digit = int(digit)
        new_digit = digit + 1
        new_digit = [int(num) for num in str(new_digit)]
        return new_digit

a = [1,2,3,4,5]
b = [1,9]

x = Solution()
print(x.plusOne(a))
print(x.plusOne(b))