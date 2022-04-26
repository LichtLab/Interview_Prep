# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.ttl_sum = 0
        self.low = None
        self.high = None

    def rangeSumBST(
            self,
            root: Optional[TreeNode],
            low: int,
            high: int) -> int:
        self.low = low
        self.high = high
        self.search_nodes(root)
        return self.ttl_sum

    def search_nodes(self, node):
        if self.low <= node.val <= self.high:
            self.ttl_sum += node.val
        if node.left is not None:
            self.search_nodes(node.left)
        if node.right is not None:
            self.search_nodes(node.right)
