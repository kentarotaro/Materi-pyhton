class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        write_idx = 1
        for read_idx in range(1, len(nums)):
            if nums[read_idx] != nums[write_idx - 1]:
                nums[write_idx]= nums[read_idx]
                write_idx += 1
            else:
                None
        return write_idx
    
x = Solution()
a = [1,1,1,2,2,2,3,4,5]
print(x.removeDuplicates(a))