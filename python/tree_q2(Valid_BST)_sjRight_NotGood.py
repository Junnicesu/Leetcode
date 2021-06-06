# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -2**31 <= Node.val <= 2**31 - 1

'''
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        l = -2**31-1  #sj!!!!!! [-2147483648,null,2147483647] will get wrong answer.
        r = 2**31  #sj the boundary must be a unreachable one. How to do this in C++???, because max int is 2**31 -1  
        if not root:
            return True

        ret = l < root.val and root.val < r
        
        if not root.left and not root.right:
            return ret

        ret = solve(l, root, r)        
        return ret
    
def solve(lbn:int, node:TreeNode, rbn:int) -> bool:
    ret = True
    if node.left:
        ret =  lbn < node.left.val and node.left.val < node.val and solve(lbn, node.left, node.val)
    if not ret:
        return False
    if node.right:
        ret = node.val < node.right.val and node.right.val < rbn and solve(node.val, node.right, rbn)
    return ret

