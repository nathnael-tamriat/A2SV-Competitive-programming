class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0
        for i in range(len(s)):
            #odd
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > res_len:
                    res = s[l:r+1]
                    res_len = r-l+1
                l-=1
                r+=1
            #even
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > res_len:
                    res = s[l:r+1]
                    res_len = r-l+1
                l-=1
                r+=1
        return res
