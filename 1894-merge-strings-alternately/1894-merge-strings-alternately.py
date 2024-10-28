class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        res = []
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[i])
            i+=1
            j+=1
        res.extend(word1[i:] or word2[j:])
        return "".join(res)