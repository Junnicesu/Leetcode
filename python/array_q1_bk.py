#!/usr/bin/env python

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for id,var in enumerate(nums):
            while id!=len(nums)-1 and var == nums[id+1]:
                del nums[id+1]
        return len(nums)


def main():
    a = [1, 1, 2]
    sln = Solution()
    sln.removeDuplicates(a)
    print(a)


if __name__ == '__main__':
    main()