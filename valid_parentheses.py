class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        openings = "([{" # 0 1 2s
        closings = ")]}"
        box = []
        for char in s:
            if char in openings :
                box.append(char)
                
            else:
                if not box:
                    return False
                last_char = box.pop()
                if not openings.index(last_char) == closings.index(char):
                    return False
        return len(box) == 0

            

                

x = Solution()
r = "{}"
t = "[{)}]"
print(x.isValid(r))
print(x.isValid(t))