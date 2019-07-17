class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        sum = 0
        for op in ops:
            if op == "C":
                popped = stack.pop()
                sum -= popped
            elif op == "D":
                stack.append(stack[-1] * 2)
                sum += stack[-1]
            elif op == "+":
                first = stack[-1]
                second = stack[-2]
                stack.append(first + second)
                sum += first + second
            else:
                stack.append(int(op))
                sum += int(op)
        return sum
