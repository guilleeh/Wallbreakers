class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        candidates = []
        indexes = []

        for i in range(len(s) - len(p) + 1):
            candidates.append(s[i : i + len(p)])

        for i in range(len(candidates)):
            if sorted(candidates[i]) == sorted(p):
                indexes.append(i)
        return indexes

