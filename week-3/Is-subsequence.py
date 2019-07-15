class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        index = 0
        s_len = len(s)

        for c in t:
            if c == s[index]:
                index += 1

            if index == s_len:
                return True

        return False
