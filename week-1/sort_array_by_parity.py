class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even_array = []
        odd_array = []
        for num in A:
            if num % 2 == 0:
                even_array.append(num)
            else:
                odd_array.append(num)
        even_array.extend(odd_array)
        return even_array
    
'''
NOTES

**Understad**

We are given an array of *NON NEGATIVE INTEGERS* therefore we don't have to worry about negatives in our array. 
We have to return an array **NEW ARRAY?** with even elements first and then all the odd elements. 
As seen from the first sample test case, the order of the even and odd elements does not appear to matter. 
What happens with an empty array? [] -> [] ? 
What happens when they are all odd? [1,1,1,1] - > [1,1,1,1]?
Same for even ^^

**MATCH**

We can use arrays, or lists in python, to divide the odd and even elements in the array

**PLAN**

We are going to iterate through the whole array once, we are going to check if an element is odd or even by % 2, if 0, it is even, else it is odd. 
We are going to put all the even numbers into even_array and all the odds into odd_array. 
At the end, we will return even_array.join(odd_array)

**IMPLEMENT**

Will be done through the code

**REVIEW**
        input = [3,1,2,4]
        even_array = [2, 4]
        odd_array = [3, 1]
        num = 4
        return [2,4].extend([3,1])

**EVALUATE**

TIME COMPLEXITY: O(N) SINCE WE ARE PASSING THROUGH THE ARRAY ONCE
SPACE COMPLEXITY: O(N) SINCE, IN THE WORST CASE, WE WILL STORE ALL ELEMENTS AGAIN INTO TWO SEPERATE ARRAYS

'''