from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset = set(nums)
        if len(numset) < len(nums) : 
            return True
        else:
            return False

# # method 2, Accept
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         hashTable = {}
#         isDuplicate = False
#         for var in nums:
#             try:
#                 hashTable.pop(var)
#                 isDuplicate = True
#                 break
#             except:
#                 hashTable[var] = 1
#         return isDuplicate


# Wrong answer, Time Limit Exceeded
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         isDuplicate = False
#         for id in range(len(nums)-1, 0, -1):
#             if nums[id] in nums[:id]:
#                 isDuplicate = True
#                 break
#         return isDuplicate