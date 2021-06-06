# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n:int)->int:
        goodN = 1
        firstBad = goodN
        while True:
            if isBadVersion(firstBad):
                if firstBad - goodN <= 1:
                    return firstBad
                else:
                    firstBad = goodN + (firstBad+1 - goodN)//2  #sj!!!!!!!! n+1 to make it reachable, 1.5hour experience.
            else:
                goodN = firstBad
                firstBad = goodN + (n+1-goodN)//2  #sj!!!!!!!! n+1 to make it reachable, 1.5hour experience.
            