#Maximum Difference Between Adjacent Elements in a Circular Array
class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
   
        """
        diff = abs(nums[-1] - nums[0])
        for i in range(1, len(nums)):
            diff = max(diff, abs(nums[i] - nums[i - 1]))
        return diff
                    
x = [2, 7, 4, -5]
y = Solution()
print(f"Input: nums = {x}")
print(f"Hasil: {y.maxAdjacentDistance(x)}")