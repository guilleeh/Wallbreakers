class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 97 122
        stripped_s = s.lower().split(" ")
        stripped_s = "".join(stripped_s)
        stack = []
        normal = []
        for c in stripped_s:
            if c.isalnum():
                stack.append(c)
                normal.insert(0, c)

        for c in normal[::-1]:
            popped = stack.pop()
            print(popped, c)
            if popped != c:
                return False
        return True
