class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        retList = []
        mxV = -10**5
        sumRet = 0
        isNewSub = True
        for v in nums:
            if v<0:
                if isNewSub:
                    try:
                        if v > retList(-1):
                            retList.pop()
                            retList.append(v)
                            isNewSub = True
                    except:
                        retList.append(v)
                        isNewSub = True
                else:
                    sumRet +=v
                    if sumRet <= 0:
                        isNewSub = True
                        if sumRet > retList[-1]:
                            retList.pop()
                            retList.append(sumRet)
                        sumRet = 0
            else:
                if isNewSub:
                    sumRet = v
                    retList.append(sumRet)
                    isNewSub = False
                else:
                    sumRet +=v
                    if sumRet > retList[-1]:
                        retList.pop()
                        retList.append(sumRet)
            print(v, retList) #sjdb              
              
        return max(retList)