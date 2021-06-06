class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        for(auto it = prices.begin(); it < prices.end()-1; it++){
            if(*(it+1) > *(it)){
                profit += *(it+1) - *(it);
            }
        }
        return profit;
    }
};