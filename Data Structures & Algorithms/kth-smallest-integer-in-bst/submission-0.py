# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # recursive
        # result = []
        # def _inorder(node):
            # if not node or len(result) == k:
                # return
            # _inorder(node.left)
            # result.append(node.val)
            # _inorder(node.right)
        # _inorder(root)
        # return result[-1]
        # iterative
        count = 0
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            count += 1
            if count == k:
                return node.val
            node = node.right



        