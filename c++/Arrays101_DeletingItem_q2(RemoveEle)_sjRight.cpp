class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int id = 0;
        while(id < nums.size()){
            if(nums[id] == val){
                nums.erase(nums.begin()+id);  //sj!!!! nums.begin()+id
            }
            else
                id++;
        }
        return nums.size();
    }
};

//sj Right 2:
/*
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        auto it = nums.begin();
        while(it!=nums.end()){
            if(*it==val) nums.erase(it);
            else it++;
        }
        return nums.size();
    }
};
*/