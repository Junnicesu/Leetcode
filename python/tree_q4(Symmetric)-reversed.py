# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        curRow = []
        if root:
            curRow = [root]
        else:
            return True
        nxtRow = []
        while curRow:
            el = curRow.pop(0)
            nxtRow += [el.left, el.right]
            if not curRow:
                nxtRowValue = [(x.val if x!=None else None) for x in nxtRow]
                print(nxtRowValue) #sjdb
                if nxtRowValue != [*reversed(nxtRowValue)]:
                    return False
                curRow = [x for x in nxtRow if x!=None]
                nxtRow = []
        return True
    