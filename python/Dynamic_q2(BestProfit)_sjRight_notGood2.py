class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sz = len(prices)
        if sz <=1:
            return 0
        
        id = 1
        profits = []
        isBought = False
        while id < sz:
            if isBought:
                profits.append(prices[id] - buyIn)        
                if prices[id] < buyIn:
                    buyIn = prices[id]
            else:
                if prices[id] > prices[id-1]:
                    buyIn = prices[id-1]
                    isBought = True
                    profits.append(prices[id] - buyIn)
            id += 1
        if len(profits) == 0:
            return 0
        else:
            return max(profits)

'''
Runtime: 164 ms for doing the longest test case, worse than the first one.
'''