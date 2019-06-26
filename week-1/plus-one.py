class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus_one_array = []
        number_as_string = ""
        for each in digits:
            number_as_string += str(each)

        number_as_string = str(int(number_as_string) + 1)

        for each in number_as_string:
            plus_one_array.append(int(each))

        return plus_one_array
