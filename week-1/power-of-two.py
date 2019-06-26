class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1 or n == 2:
            return True

        base = 2
        while base < n:
            base = base * 2
            if n == base:
                return True

        return False

