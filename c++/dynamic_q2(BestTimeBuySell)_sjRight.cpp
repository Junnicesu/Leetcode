class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ret = 0;
        auto it = prices.begin();
        int profit;
        bool isBought = false;
        int pBuyin;
        while(++it < prices.end()){
            if(!isBought){
                if(*it > *(it-1)){
                    pBuyin  = *(it-1);
                    profit = *it - *(it-1);
                    ret = profit > ret ? profit: ret;
                    isBought = true;
                }
            }
            else{
                if(*it > *(it-1)){
                    pBuyin =  *(it-1) < pBuyin ? *(it-1) : pBuyin;
                    profit = *it - pBuyin;
                    ret = profit > ret ? profit: ret;
                }
            }
        }
        return ret;
    }
};