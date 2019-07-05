from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        char_dict = Counter(s)
        new_string = ""
        for each in char_dict.most_common():
            new_string += each[0] * each[1]

        return new_string
