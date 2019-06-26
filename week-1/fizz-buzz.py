class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        multiple_of_three_and_five = "FizzBuzz"
        multiple_of_three = "Fizz"
        multiple_of_five = "Buzz"
        solution = []
        for number in range(1, n + 1):
            if number % 3 == 0 and number % 5 == 0:
                solution.append(multiple_of_three_and_five)
            elif number % 3 == 0:
                solution.append(multiple_of_three)
            elif number % 5 == 0:
                solution.append(multiple_of_five)
            else:
                solution.append(str(number))
        return solution
