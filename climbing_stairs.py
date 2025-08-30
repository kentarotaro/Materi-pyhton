class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways = [1, 2]

        if n == 1:
            return ways[0]
        elif n == 2:
            return ways[1]
        else:
            for i in range(2, n):
                next_way = ways[i - 1] + ways[i - 2]
                ways.append(next_way)
        return ways[n - 1]

        
                

n = 6
x = Solution()
print(x.climbStairs(n)) #output 5