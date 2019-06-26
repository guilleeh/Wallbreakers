class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        back_index = -1
        middle = int(length / 2)
        for each in range(length):
            front = s[each]
            back = s[back_index]
            if each + 1 > middle:
                break  # We have gotten to the middle of the list
            # Swap indexes
            s[each] = back
            s[back_index] = front
            back_index -= 1
