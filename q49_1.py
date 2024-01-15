class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # return self.sortedTuple(strs)
        return self.hashingByCount(strs)
    
    def sortedTuple(self, strs):
        res = defaultdict(list)

        for i in range(0, len(strs)):
            res[tuple(sorted(strs[i]))].append(strs[i])
        
        return res.values()
    
    def hashingByCount(self, strs):
        res = defaultdict(list)

        for i in range(0, len(strs)):
            counter = [0] * 26
            for j in range(0, len(strs[i])):
                counter[ord(strs[i][j]) - ord('a')] += 1
            res[tuple(counter)].append(strs[i])
        
        return res.values()
