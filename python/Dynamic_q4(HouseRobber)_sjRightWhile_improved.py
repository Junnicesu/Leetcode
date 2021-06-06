class Solution:
    def rob(self, nums: List[int]) -> int:
        sz = len(nums)
        if sz ==1:
            return nums[0]
        elif sz == 2:
            return nums[0] if nums[0] > nums[1] else nums[1]
        
        preMxs = [0,0,nums[0]]                       
        id = 1                
        while id < len(nums):
            print(preMxs) #sjdb
            mx = nums[id] + preMxs[-2]
            mxAlt = nums[id-1] + preMxs[-3]
            mxSofar = mx if mx > mxAlt else mxAlt
            preMxs.append(mxSofar)            
            print("End: id = %d, mxSofar = %d\n" % (id, mxSofar)) #sjdb                 
            id +=1
        return mxSofar

'''
input:
[1,3,1,3,5,100]

Your stdout:
[0, 1, 3]
1 + 1 ? 3 + 0
End: nums[2] = 1, mxSofar = 3

[0, 1, 3, 3]
3 + 3 ? 1 + 1
End: nums[3] = 3, mxSofar = 6

[0, 1, 3, 3, 6]
5 + 3 ? 3 + 3
End: nums[4] = 5, mxSofar = 8

[0, 1, 3, 3, 6, 8]
100 + 6 ? 5 + 3
End: nums[5] = 100, mxSofar = 106

Your input:
[1,7,9,4]

Your stdout:
[0, 1, 7]
End: id = 2, mxSofar = 10

[0, 1, 7, 10]
End: id = 3, mxSofar = 11

[0, 1, 7]
End: nums[2] = 9, mxSofar = 10

[0, 1, 7, 10]
End: nums[3] = 4, mxSofar = 11


Explain:
mx[id] = max( preMxs[id-2] + nums[id], nums[id-1] +  preMxs[id-3])
'''