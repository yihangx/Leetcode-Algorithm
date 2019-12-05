class Treenode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lca(root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lca(root.left, p, q)
        right = self.lca(root.right, p, q)
        if left and right:
            return root
        return left or right
