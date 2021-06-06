from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = list(pasTriAGenerator(numRows))
        return ret

def pasTriAGenerator(numRows):
    rowId = 0
    rowPre = []
    while rowId < numRows:
        rowNew = [] #sj!!!!!!!! missed
        rowNew += rowPre[:1]
        szPre = len(rowPre)
        # print("szPre: ", szPre, "rowPre: ", rowPre)
        id = 0
        while id < szPre -1:
            rowNew.append(rowPre[id] + rowPre[id+1])
            # print(rowNew)
            id+=1
        rowNew.append(1)
        rowPre = rowNew
        # print("b4 yield, rowNew : ", rowNew)
        yield rowNew
        rowId+=1 


def main():
    triAGnr = pasTriAGenerator(100)
    for row in triAGnr:
        print(row)

if __name__ == '__main__':
    main()

'''
Yield in C++:
https://stackoverflow.com/questions/9059187/equivalent-c-to-python-generator-pattern
https://www.youtube.com/watch?v=_fu0gx-xseY

'''