class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        auto sz = nums.size();
        k = k> sz? k%sz : k;
        if(sz>0 && k<sz){
            auto pos = nums.begin();
            vector<int> lstN(k);  //sj !!!!, Compile error, if lstN is not given a size greater than k
            std::copy(nums.end()-k, nums.end(), lstN.begin());
            nums.insert(pos, lstN.begin(), lstN.end());
            nums.erase(nums.end()-k, nums.end());            
        }
    }
};