class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        count = 0

        try:
            for cookie in s:
                if g[count] <= cookie:
                    count += 1
        except IndexError:
            pass
        finally:
            return count
