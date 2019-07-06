class Solution:
    def wordPattern(self, s: str, t: str) -> bool:
        t = t.split(" ")
        dictionary = {}
        dictionary2 = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in dictionary:
                if dictionary[s[i]] != t[i]:
                    return False
            dictionary[s[i]] = t[i]

        for i in range(len(t)):
            if t[i] in dictionary2:
                if dictionary2[t[i]] != s[i]:
                    return False
            dictionary2[t[i]] = s[i]
        return True
