from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict = defaultdict(int)
        for c in s:
            char_dict[c] += 1

        for c in t:
            char_dict[c] -= 1

        for k, v in char_dict.items():
            if v != 0:
                return False

        return True
