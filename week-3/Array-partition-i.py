class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        if len(nums) == 2:
            return min(nums)

        for i in range(2, len(nums) + 1, 2):
            sum += min(nums[i - 2], nums[i - 1])

        return sum
