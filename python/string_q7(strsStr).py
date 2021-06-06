class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0   #!!! sj forgot. should considerate empty str
        elif len(needle) > len(haystack):
            return -1 #!!! sj forgot
        ret = -1
        # for pos,ch in enumerate(haystack):
        pos = 0
        szHayStack = len(haystack)
        szNeedle = len(needle)
        #!!!!!!!!sj do not need to compare the left if the left substring size less then size of needle.
        while szHayStack- pos  >= szNeedle: 
            ch = haystack(pos)
            if ch == needle[0]:
                isFound = True
                for id,ch2 in enumerate(needle):                    
                    if haystack[pos+id] != needle[id]:
                        isFound = False
                        break 
                if isFound:
                    ret = pos
                    break
            pos += 1
        return ret
                            