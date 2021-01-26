from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wdict = {}
        for s in strs:
            if tuple(sorted(s)) not in wdict:
                wdict[tuple(sorted(s))] = [s]
            else:
                wdict[tuple(sorted(s))].append(s)
        return list(wdict.values())

s = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(strs))
