preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

def construct(preorder, inorder):
    if inorder:
        start = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[start])
        root.left = construct(preorder, inorder[:start])
        root.right = construct(preorder, inorder[start+1:])
        return root
