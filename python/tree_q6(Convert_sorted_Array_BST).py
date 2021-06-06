#!/bin/sh
from typing import List

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
        root = TreeNode(nums[sz//2])
        root.left = self.sortedArrayToBST(nums[:sz//2])
        root.right = self.sortedArrayToBST(nums[sz//2+1:])
        return root
		
'''
Q: Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Eg: 
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
'''