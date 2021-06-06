class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        topBtm = [prices[0]]
        sz = len(prices)
        isPreValley = True
        for id in range(1,sz):
            if isPreValley:
                if prices[id] > prices[id-1]:
                    topBtm.append(prices[id])
                    isPreValley = False
                else:
                    topBtm.pop()
                    topBtm.append(prices[id])
                    isPreValley = True
            else:
                if prices[id] > prices[id-1]:
                    topBtm.pop()
                    topBtm.append(prices[id]) 
                    isPreValley = False
                else:
                    topBtm.append(prices[id])
                    isPreValley = True
        #sj filtered the Peaks and Troughs one after another
        print(topBtm) #sjdb
        szTopBtm = len(topBtm)
        if szTopBtm <= 1:
            return 0
        else:
            profits = [] 
            buyIn = topBtm[0]
            id = 1
            while id < szTopBtm:
                if topBtm[id-1] < buyIn:
                    buyIn = topBtm[id-1]
                profit = topBtm[id] - buyIn
                profits.append(profit)
                id +=2
            return max(profits)

'''
Runtime: 120 ms for doing the longest test case
'''