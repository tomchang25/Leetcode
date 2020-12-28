# %%
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.val) + "\n"
        for child in [self.left, self.right]:
            if child is None:
                continue

            ret += child.__str__(level + 1)
        return ret


def CreateTree(treeList):
    treeList = [TreeNode(t) if t is not None else None for t in treeList]

    for key, node in enumerate(treeList):
        if node is None:
            continue

        try:
            subKey = key * 2 + 1
            node.left = treeList[subKey]
        except:
            node.left = None

        try:
            subKey = key * 2 + 2
            node.right = treeList[subKey]
        except:
            node.right = None

    return treeList[0]


# Input: root = [3,9,20,None,None,15,7]


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return True


if __name__ == "__main__":
    root = CreateTree([1, 2, 3, 4, 5, 6, 7, None, None, 10, 11])

    print(Solution().isBalanced(root))
# %%
