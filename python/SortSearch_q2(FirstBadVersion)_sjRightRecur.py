# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n:int)->int:
        if isBadVersion(1):
            return 1        
        return solveBadUntil(1, n)

def solveBadUntil(goodN:int, badN: int)->int:    
    nxt = goodN + (badN+1-goodN)//2 #sj!!!!!!! to make sure badN is reachable 
    # print("goodN= %d , badN = %d nxt = %d" % (goodN, badN, nxt)) #sjdb
    if isBadVersion(nxt):
        if nxt-goodN == 1:            
            return nxt
        else:
            return solveBadUntil(goodN, nxt) 
    else:
        return solveBadUntil(nxt, badN)