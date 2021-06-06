class Solution:
    def countPrimes(self, n: int) -> int:
        if n <=2:
            return 0
        prLst = [2]
        rootN = n**0.5//1
        i = 3
        while i< n:
            if isPrime(i, prLst):
                prLst.append(i)
            i += 1
        print(prLst) #sjdb
        return len(prLst)

def isPrime(x: int, primes: list) -> bool:
    root = x**0.5//1
    id = 0
    while primes[id] <= root:
        if x % primes[id] ==0:
            return False
        id +=1
    return True