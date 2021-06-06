class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyInId = 0
        isBought = False
        profit = 0
        for id, var in enumerate(prices[1:]):
            print("Day {}: price: {}, dayB4 P {}".format(id, var, prices[id]))
            if not isBought and var > prices[id]:
                buyInId = id
                isBought = True
                print(str(id)+":"+str(var))
                continue
            if isBought and var < prices[id]:
                sellOutId = id
                print(str(id)+":"+str(var))
                profit +=  prices[sellOutId] - prices[buyInId]
                isBought = False
        if isBought:
            profit +=  prices[-1] - prices[buyInId]
        return profit

def main():
    prices = [1,2,3,4,5]
