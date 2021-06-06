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
        ret = True
        nxtRow = []
        while curRow:
            el = curRow.pop(0)
            nxtRow += [el.left, el.right]
            if not curRow:
                coutNodes(nxtRow) #sjdb
                rId = -1
                for id in range(len(nxtRow)):
                    if nxtRow[id] != nxtRow[rId] :
                        if nxtRow[id] and nxtRow[rId] and nxtRow[id].val == nxtRow[rId].val:
                            rId -=1
                        else:
                            return False
                    else:
                        rId -= 1
                curRow = [x for x in nxtRow if x!=None]
                nxtRow = []
        return ret
    
def coutNodes(row: List[TreeNode]):
    for x in row[:-1]:
        if x:
            print(x.val, end=", ")
        else:
            print("None, ", end="")
    x = row[-1].val if row[-1] else None
    print(x)