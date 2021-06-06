class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        
        for(auto it= nums.begin(); it!=nums.end(); it++){
            // std::cout << *it << std::endl;
            while(it!=nums.end()-1 && *it == *(it+1)){
                nums.erase(it+1);
            }
        }
        return nums.size();
    }
};