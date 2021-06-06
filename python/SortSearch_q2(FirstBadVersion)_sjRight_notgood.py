# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 1
        if n-1>0:
            ret= solveBadUntil(1,n)
        return ret

def solveBadUntil(goodN:int, badN: int)->int:
    if isBadVersion(goodN) and goodN ==1:  
        return goodN  ##sj being about to reach the first.
    
    nxt = goodN + (badN+1-goodN)//2  #sj!!!!! badN+1 will make it being about to reach the end.
    if isBadVersion(nxt):
        if nxt-goodN == 1:
            return nxt
        else:
            return solveBadUntil(goodN, nxt)
    else:
        return solveBadUntil(nxt, badN)

'''
The solveBadUntil looks urgly. 
'''        