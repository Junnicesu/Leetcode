#include <vector>
#include <iostream>

using namespace std;
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        auto sz = nums.size();
        k = k> sz? k%sz : k;
        if(sz>0 && k<sz){
            //vector<int> *plastKnum = new vector<int>;  //sj!!!, new but not delete later
            //std::copy(nums.end()-k, nums.end(), plastKnum->begin()); 
            //sj!!!!!!! , wrong method of using std::copy. Only OutputIt  or ForwardIt for the 3rd param
            //copy(nums.end()-k, nums.end(), begin(*plastKnum)); //sj!!!!, Wrong either!!!! Because vector size 0 

            vector<int> lastNSlice; //sj!!!, unknown size, should use back_inserter as OutputIt
            copy(nums.end()-k, nums.end(), std::back_inserter(lastNSlice)); 
            // for(const auto& x: lastNSlice){ cout << x << ' '; }  cout << endl;  //sjdb

            vector<int> lastSlice(k);
            copy(nums.end()-k, nums.end(), lastSlice.begin()); 
            // for(const auto& x: lastSlice){ cout << x << ' '; }  cout << endl;  //sjdb

            auto pos = nums.begin();
            nums.insert(pos, lastSlice.begin(), lastSlice.end());
            // for(const auto& x: nums){ cout << x << ' '; }  cout << endl;  //sjdb
            nums.erase(nums.end()-k, nums.end());
            // for(const auto& x: nums){ cout << x << ' '; }  cout << endl;  //sjdb
        }
    }
};

int main(){
    vector<int> nums{1,4,5,8,3,7,4};
    for(const auto& x: nums){ cout << x << ' '; }  cout << endl;  //sjdb
    Solution sln;
    sln.rotate(nums, 3);
    for(const auto& x: nums){ cout << x << ' '; }  cout << endl;  //sjdb

}

//sj !!!! conclusion. If want to use begin() as the output It, the size of the vector should be reserved or initialized. 
//Otherwise, use std::back_inserter() instead.


/*
AddressSanitizer:DEADLYSIGNAL
=================================================================
==32==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x000000328895 bp 0x7ffe21002ad0 sp 0x7ffe21002288 T0)
==32==The signal is caused by a WRITE memory access.
==32==Hint: address points to the zero page.
    #4 0x7fbcdab200b2  (/lib/x86_64-linux-gnu/libc.so.6+0x270b2)
AddressSanitizer can not provide additional info.
==32==ABORTING
*/

/* 
http://stackoverflow.com/questions/14977632/ddg#14977748
 Generally I would strongly prefer v2 = v1:

    It is shorter and makes the intend more clear
    std::copy won't work if v2 doesn't have the same length as v1 (it won't resize it, so it will retain some of the old elements best case (v2.size() > v1.size() and overwrite some random data used elsewhere in the program worst case
    If v1 is about to expire (and you use C++11) you can easily modify it to move the contents
    Performancewise assignment is unlikely to be slower then std::copy, since the implementers would probably use std::copy internally, if it gave a performance benefit.

In conclusion, std::copy is less expressive, might do the wrong thing and isn't even faster. So there isn't really any reason to use it here.

--Grizzly
*/