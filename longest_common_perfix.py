class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #strs itu sebuah list yang berisi string
        #kita diminta untuk mencari karakter yang sama pada setiap i dalam strs
        if not strs:
            return ""
        
        prefix = ""
        for i in range(len(strs[0])):
            current_char = strs[0][i]

            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != current_char:
                    return prefix
            prefix += current_char
        return prefix
            


x= Solution()
star1 = ["flower","flow","flight"]
star2 = ["dog","racecar","car"]
print(x.longestCommonPrefix(star1))
print(x.longestCommonPrefix(star2))
