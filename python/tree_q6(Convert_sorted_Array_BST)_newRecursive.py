# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        sz = len(nums)
        if sz == 0:
            return None        
        return solve(nums, 0, sz-1)
    
def solve(nums: List[int], start:int, end:int) -> TreeNode:
    if end < start:
        return None
    if start == end:
        return TreeNode(nums[start])
    
    mid = start + (end-start)//2 #!!!!sj
    leftEnd = mid-1
    rightStart = mid+1 
    
    print("{}~{}, {}~{}".format(start, leftEnd, rightStart, end)) #sjdb

    root = TreeNode(nums[mid])
    root.left = solve(nums, start, leftEnd) 
    root.right = solve(nums, rightStart, end)
    return root