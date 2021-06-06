class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not isThereDigitSub(board):
            return False
        
        if isThereRepetitionSub(board):
            return False
        
        #check sub group
        for gi in range(3):
            for gj in range(3):
                # print("group (%d, %d):", (gi, gj)) #sjdb
                subboard = []
                for j in range(3):
                    # subboard.append(board[gj*3+j][gi*3:gi*3+3]) 
                    subboard = subboard + board[gj*3+j][gi*3:gi*3+3] # flat it, need to be put into a list
                    # print(board[gj*3+j][gi*3:gi*3+3])
                print(subboard)    
                if not isThereDigitSub([subboard]):
                    # print("group(%d, %d) is not valid" % (gi, gj)) #sjdb
                    return False
                if isThereRepetitionSub([subboard]):
                    return False
        return True
        
        
        
def isThereDigitSub(subboard: List[List[str]]) -> bool:
    lenRow = len(subboard)
    lenColumn = len(subboard[0])
    isThereDigit = False
    
    for i in range(lenRow):
        isThereDigit = False
        for j in range(lenColumn):
            isThereDigit  = isThereDigit or subboard[i][j].isdigit()
            # print(j," :", isThereDigit) #sjdb
            if isThereDigit:
                break # there is digit in this row
        if not isThereDigit:
            # print("no digit in row %d" % i) #sjdb
            return False # no digit in row i
    return isThereDigit

    # !!! no check column if only ONE row
    if lenColumn == 1:
        print(isThereDigit)
        return isThereDigit  

    # check column
    for j in range(lenColumn):
        isThereDigit = False
        for i in range(lenRow):
            isThereDigit = isThereDigit or subboard[i][j].isdigit()
            # print(i, ",", j,",", subboard[i][j], " :", isThereDigit) #sjdb
            if isThereDigit:
                break # there is digit in this column
        if not isThereDigit:
            # print("no digit in column %d" % j) #sjdb
            return False


def isThereRepetitionSub(subboard: List[List[str]]) -> bool:
    lenRow = len(subboard)
    lenColumn = len(subboard[0])    
    isThereRepetion = False
    for i in range(lenRow):
        isThereRepetion = False
        dic = {}
        for j in range(lenColumn):
            if subboard[i][j].isdigit():
                try:
                    dic.pop(subboard[i][j])
                    # print("Row %d has repetition" % i) #sjdb
                    return True # repeated
                except:
                    dic[subboard[i][j]] = 1
    # check column
    for j in range(lenColumn):
        isThereRepetion = False
        dic = {}
        for i in range(lenRow):
            if subboard[i][j].isdigit():
                try:
                    dic.pop(subboard[i][j])
                    print("Column %d has repetition" % j) #sjdb
                    return True  # repeated
                except:
                    dic[subboard[i][j]] = 1
    return False