# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def solution(self, root, isLeft, sum):
        if not root:
            return
        if not root.left and not root.right and isLeft:
            sum[0] += root.val

        self.solution(root.left, True, sum)
        self.solution(root.right, False, sum)

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        sum = [0]
        self.solution(root, False, sum)
        return sum[0]
