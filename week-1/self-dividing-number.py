class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        number_array = []
        for i in range(left, right + 1):
            if i < 10:
                number_array.append(i)
            else:
                current_number = i
                is_self_dividing = True
                while current_number != 0:
                    single_digit = current_number % 10
                    if single_digit == 0:
                        is_self_dividing = False
                        break

                    if i % single_digit != 0:
                        is_self_dividing = False
                        break
                    current_number = int(current_number / 10)

                if is_self_dividing:
                    number_array.append(i)
                is_self_dividing = True
        return number_array


"""
**Understand**
check if number is self dividing by seeing if all of its digit can divide the number
a self dividing number is not allowed to have **ZERO**
the lower bond cannot be greater than the upper boud
lower == upper bound
lower will be 1 or greater
we go up to 10000

**Match**
Match we're gonna have to use an array

**Plan**
We are gonna have a for loop that goes from left to right inclusive, if a number < 10, we don't have to do the % 10 to get all of its terms. if not, then we are gonna have a nother loop which will get all the terms in the number until we have a single digit, then try to divide the original number by each term, if they can all divide the original number, make sure the original number is added to the list, then return the list

**Implement**
See code

**Review**
Could have solved it faster just by iterating through the number as a string 
**Evaluate**
Time Complexity: O(R), where R is the range of numbers we have to go through
Space Complexity: O(R), since in the worst case, we will have to store every number in the range to an array.

"""

