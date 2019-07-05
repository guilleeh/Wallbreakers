class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 0 or n == 1:
            return True
        total = 0
        seen_values = {}
        while total != 1:
            digits = []
            while n != 0:
                single_digit = n % 10
                digits.insert(0, single_digit)
                n = int(n // 10)

            current_total = 0
            for digit in digits:
                current_total += digit * digit

            total = current_total
            n = total
            if total in seen_values:
                return False
            seen_values[total] = total

        return True
