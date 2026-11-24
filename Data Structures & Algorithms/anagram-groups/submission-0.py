class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for i in range(0,len(strs)):
            count = [0]*26
            for j in range(0, len(strs[i])):
                count[ord(strs[i][j]) - ord('a')] += 1
            dic[tuple(count)].append(strs[i])
        return list(dic.values())        
        