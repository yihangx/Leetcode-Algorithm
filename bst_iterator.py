class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BST_Iterator:
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        node = self.stack.pop()
        x = node.right
        while x:
            self.stack.append(x)
            x = x.left
        return node.val

    def hasNext(self):
        return len(self.stack) > 0
