class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def level_order(self, root):
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, level, res):
        if root:
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            self.dfs(root.left, level + 1, res)
            self.dfs(root.right, level + 1, res)
