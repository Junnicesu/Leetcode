class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        vector<int> buyinList;
        vector<int> selloutList;
        bool isBuyin = false;
        for(auto it = prices.begin(); it < prices.end()-1; it++){
            if(*(it) < *(it+1)){
                profit += *(it+1) - *it;
            }
            if(!isBuyin && *(it) < *(it+1) ){
                // printf("%d ", it-prices.begin());
                buyinList.push_back(it-prices.begin());
                isBuyin = true;  //why commented would cause runtime error?? Ans: no sellout point
            }
            if(isBuyin){
                if(*(it) > *(it+1) ){
                    // printf("--%d\n", it-prices.begin());
                    selloutList.push_back(it-prices.begin());
                    isBuyin = false; 
                }
                // !!!!sj, sellout Point is different
                else if( it+1 == prices.end()-1 ) {
                    selloutList.push_back(it+1-prices.begin());
                }
            }
        }
        
        //!!!!sj not good!!, no garrent selloutList is empty or not
        for(int id=0; id<buyinList.size(); id++){
            printf("%d - %d\n", buyinList[id], selloutList[id]);
        }
        
        return profit;
    }
};

/*
=================================================================
How to find out all the buyin index and the sellout index?? 
1, buyin point must be every first increasing point in a segment
2, if isBuyin, then sellout point must be the first decreasing point in a segment, or the end point.

*/
