from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter1 = Counter(s)
        counter2 = Counter(t)
        if len(counter1) == len(counter2):
            for i in counter1:
                if counter1[i] != counter2[i]:
                    return i

        for i in counter2:
            if i not in counter1:
                return i
