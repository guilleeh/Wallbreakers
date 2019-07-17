class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        table = {"}": "{", ")": "(", "]": "["}
        mapping = ["[", "(", "{"]
        stack = []

        for c in s:
            if c in mapping:
                stack.append(c)
            else:
                last = stack.pop() if stack else "#"
                if last != table[c]:
                    return False

        return not stack
