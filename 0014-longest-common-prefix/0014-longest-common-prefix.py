class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1,len(strs)):
                if i > len(strs[j]) -1 or  char!=strs[j][i]:
                    return res
            res+=char
        return res


