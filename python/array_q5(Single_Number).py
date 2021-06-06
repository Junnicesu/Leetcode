#!/usr/bin/env python
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for var in nums:
            try:
                dic.pop(var)
                print("after pop: "+ str(dic))
            except:
                dic[var] = 1
                print("after set: " + str(dic))                
        return dic.popitem()[0]

def main():
    a = [*range(10)]
    b = [*range(10)]
    b.pop()
    a[:0] = b
    print(a)
    sln = Solution()
    single = sln.singleNumber(a)
    print("Single is {}".format(single))


if __name__ == '__main__':
    main()    