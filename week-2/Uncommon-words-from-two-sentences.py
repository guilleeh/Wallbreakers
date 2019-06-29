from collections import Counter


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        list_a = A.split(" ")
        list_b = B.split(" ")
        result = []

        counter = Counter(list_a)
        counter.update(list_b)

        for key, value in counter.items():
            if value == 1:
                result.append(key)
        return result
