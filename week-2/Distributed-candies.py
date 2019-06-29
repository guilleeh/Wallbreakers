class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        candy_dict = set(candies)

        return min(len(candy_dict), int(len(candies) / 2))

