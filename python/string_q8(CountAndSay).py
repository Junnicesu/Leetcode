class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 0:
            return "0"
        elif n == 1:
            return "1"
        elif n == 2:
            return say("1")
        else:
            return say(self.countAndSay(abs(n)-1))
        # ret = "1"
        # if n == 2:
        #     ret = say("1")
        # elif n>2:
        #     # print("n = %d" % n)
        #     return say(self.countAndSay(n-1))        
        # return ret
    
def say(n:str) -> str:
    dup = 1
    ret = ''
    for id,v in enumerate(n[:-1]):
        if v == n[id+1]:
            dup += 1
        else:
            ret += str(dup) + v
            dup = 1
    ret += str(dup) + n[-1]
    return ret

sln = Solution()
for i in range(-5, 5):
    print(sln.countAndSay(i))
