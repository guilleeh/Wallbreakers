class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        twenty = 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                ten += 1
                if five <= 0:
                    return False
                five -= 1
            else:
                twenty += 1
                if ten >= 1 and five >= 1:
                    ten -= 1
                    five -= 1
                elif ten < 1 and five >= 3:
                    five -= 3
                else:
                    return False

        return True
