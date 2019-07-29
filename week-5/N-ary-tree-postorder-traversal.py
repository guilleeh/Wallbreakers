"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def __init__(self):
        self.order = []

    def postorder(self, root: "Node") -> List[int]:
        if not root:
            return

        for each in root.children:
            self.postorder(each)
            self.order.append(each.val)

        return self.order + [root.val]
