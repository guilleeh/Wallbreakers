from collections import defaultdict


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        total_jewels = 0
        stones_dict = defaultdict(int)
        for stone in S:
            stones_dict[stone] += 1

        for jewel in J:
            if jewel in stones_dict:
                total_jewels += stones_dict[jewel]
        return total_jewels
