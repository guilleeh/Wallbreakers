class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for each in range(len(nums)):
            complement = target - nums[each]
            if complement in seen:
                return [seen[complement], each]
            seen[nums[each]] = each
