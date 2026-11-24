class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        i = 0
        res = ""
        while i<m and i<n:
            res += word1[i]
            res += word2[i]
            i += 1
        if i < n :
            while i < n:
                res += word1[i]
                i += 1

        if i < m:
            while i < m:
                res += word2[i]
                i += 1          

        return res
        