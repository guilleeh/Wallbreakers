from collections import Counter


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        number_dict = Counter(nums)
        result = []
        for each in number_dict.most_common():
            result.append(each[0])
            break

        nums.sort()
        original_array = [x + 1 for x in range(len(nums))]

        for each in original_array:
            if each not in number_dict:
                result.append(each)
                break
        return result
