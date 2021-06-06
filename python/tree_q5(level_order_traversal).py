# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        retLs = []
        curL = []
        if root:
            curL.append(root)
            
        nextL = []
        curEls = []
        while curL:
            el = curL.pop(0)
            curEls += [el.val]
            print(curEls) #sjdb
            if el.left:
                nextL += [el.left]
            if el.right:
                nextL += [el.right]
            
            if not curL:
                retLs.append(curEls)
                curL = nextL
                nextL = []
                curEls = []
        return retLs