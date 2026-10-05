class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            sortedS=''.join(sorted(s))
            res[srtedS].append(s)
        return list(res.value())