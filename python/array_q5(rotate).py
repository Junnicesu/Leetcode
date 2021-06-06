from typing import List

class Solution:
    def rotate(self, nums: List[int], k:int) -> None:
        sz = len(nums)
        middle = sz - k%sz
        if sz>0 and middle < sz:
            next = middle
            first = 0
            last = len(nums)
            while first != next:
                # print("first: %d, next: %d" % (first,next))
                nums[first], nums[next] = nums[next], nums[first]
                # print(nums)
                first+=1
                next+=1
                if next == last:
                    # print("in next == last")
                    next = middle
                elif first == middle:
                    # print("in first == middle")
                    middle = next 
                # print("After: first: %d, next: %d" % (first,next))