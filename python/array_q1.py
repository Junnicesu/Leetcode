#!/usr/bin/env python

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newNums = list(set(nums))
        newNums.sort() # because set is {0, 3, -1}
        del nums[len(newNums):]
        for id, var in enumerate(newNums):
            nums[id] = var
        return len(nums)
    def changeStr(self, s):
        print("Original str is {}".format(s))
        s += "what"  # reassign a new instance to the variable s
        print("in Func, the str become \"{}\"".format(s))

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:


def main():
    a = [1, 1, 2]
    sln = Solution()
    sln.removeDuplicates(a)
    print(a)
    print("Hello")
    
    xStr = "okok"
    sln.changeStr(xStr)
    print("outside the func, the str is \"{}\"".format(xStr)) #sj!!!!!!!! xStr will be the original


if __name__ == '__main__':
    main()