class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 3
        # return recur_fibo(n+1)
        return resolve(n)
    
def resolve(n:int) -> int:
    aPP = 2
    aPre = 3
    ret = 0
    for id in range(4,n+1):
        ret = aPre + aPP
        aPP = aPre
        aPre = ret
    return ret


# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))    

'''
input 30:
Your answer
1346269

Recursion took 440ms to finish, while resolved from begin costs 36ms

'''