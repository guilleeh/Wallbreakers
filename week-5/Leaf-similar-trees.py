# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def search(self, root, leafs):
        if not root:
            return

        if not root.left and not root.right:
            leafs.append(root.val)
        else:
            self.search(root.left, leafs)
            self.search(root.right, leafs)

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leafs_root1 = []
        leafs_root2 = []

        self.search(root1, leafs_root1)
        self.search(root2, leafs_root2)

        return leafs_root1 == leafs_root2
