class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        auto sz = nums.size();
        auto times = k> sz? k%sz : k;
        while(times-- > 0){
            nums.insert(nums.begin(), *nums.rbegin());
            nums.erase(nums.end()-1);
        }
    }
};