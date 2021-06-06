from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        for var in nums1:
            if var in dic:
                dic[var] += 1
            else:
                dic[var] = 1
        # print(dic) #sjdb
         
        resultList = []
        for var in nums2:            
            if var in dic:
                resultList.append(var)
                if dic[var] >1:
                    dic[var] -= 1
                    # print("modify dic var")
                    # print(dic)
                else:
                    dic.pop(var)
                    # print("after pop up the key: %d", var)
                    # print(dic)
        return resultList