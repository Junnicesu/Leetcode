from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[1],[1,1]]
        if numRows <=2:
            return ret[:numRows]
        rowId = 3
        while rowId <= numRows:
            rowNew = [1]
            rowPre = ret[rowId-2]
            szPre = len(rowPre)
            id = 0
            while id < szPre-1:
                rowNew.append(rowPre[id]+rowPre[id+1])
                id+=1
            rowNew.append(1)
            ret.append(rowNew)
            rowId+=1
        return ret

def main():
    sln = Solution()
    retList = sln.generate(100)
    for row in retList:
        print(row)

if __name__ == '__main__':
    main()


'''
Not Good, because the list is stored in Memory, while yield is in the runtime. Yield is faster than this one.
For an example:
sln = Solution()
for i in range(100):
    print(sln.generate(i))  # the generate function will recount again and again. #sj!!!!! should not do like that.

ret = sln.generate(i);
for row in ret:
    print(row)

'''