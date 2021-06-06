#include <map>

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::map<int, int> dict;
        for(const auto &x : nums){
            if(dict.find(x) != dict.end()){
                return true;
            }
            else{
                dict[x] = 1;
            }
        }
        return false;
    }
};

/*
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::map<int,int> dict;
        bool hasDup = false;
        // for(auto it = nums.begin(); it< nums.end(); it++){
        //     if(dict.find(*it) == dict.end()){
        //         dict[*it] = 1;
        //     }
        //     else{
        //         hasDup = true;
        //         break;
        //     }
        // }
        for(const auto &x: nums){
            if(dict.find(x) != dict.end()){
                hasDup = true;
                break;
            }
            else{
                dict[x] = 1;
            }
        }
        
        return hasDup;
    }
};
*/