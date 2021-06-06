#include <iostream>
#include <sstream>
#include <utility> 
#include <vector>
#include <map>
#include <deque>
#include <algorithm>

using namespace std;


struct BitsItem{
    BitsItem(const string& str): zeroes{-1},ones{-1}{
        m_s = str; 
    }
    int getZeroes(){
        if(zeroes!= -1) return zeroes;
        countBits();
        return zeroes;
    }
    int getOnes(){
        if(ones!=-1) return ones;
        countBits();
        return ones;
    }
    friend bool operator<(BitsItem left, BitsItem right){
        return left.m_s.size() < right.m_s.size();
    }
    friend bool operator==(BitsItem left, BitsItem right){
        return left.m_s.size() == right.m_s.size();
    }
    friend ostream& operator<<(ostream& os, BitsItem bits){
        return os << bits.m_s;
    }

private:
    string m_s;
    int zeroes;
    int ones;

    // sj!!!!!!!!!, "1" counted result as 2 ones, 0 Zeros!!! why??
    void countBits(){
        zeroes = 0;
        ones = 0;
        stringstream ss(m_s); 
        char c;
        while(ss){  //sj!!!!, while fs != EOF, or while(ss)
            ss >> c;
            if(c=='0') zeroes++;
            if(c=='1') ones++;
        }        
        cout << m_s << " ,after count, (zeroes, ones): " << zeroes << ", " << ones << endl; //sjdb
    }
};


class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        int filterSum = m+n;
        auto bitStrs = deque<BitsItem>{};
        for(const auto& str: strs){
            bitStrs.emplace_back(BitsItem(str));
        }

        sort(bitStrs.begin(), bitStrs.end());
        int zeroes = 0; 
        int ones = 0;
        int ret = 0;
        for(auto& x: bitStrs){
            if(zeroes+ x.getZeroes() <= m && ones+ x.getOnes() <= n ){
                zeroes += x.getZeroes();
                ones+= x.getOnes();
                ret++;
            }
        }
        cout << "Max Form : " << ret << '\n';
        return ret;
    }

};

int main(){
    Solution sln;
    auto s = vector<string> {"10","0001","111001","1","0"};
    auto bitStrs = deque<BitsItem>{};
    for(const auto& x: s){
        bitStrs.emplace_back(BitsItem(x));
    }
    std::sort(bitStrs.begin(), bitStrs.end());
    for(const auto& x: bitStrs){
        cout << x << "\n";
    }
    sln.findMaxForm(s, 5, 3);
}

/*
sj!!!! wrong design
The map's key is unique!! however, there could be multiple same items in the vector!!!!!

filter out usable strings in the vector, make it a self-defined object,
which is able to compare according to string size.
sort and push them into a container one by one.

take it out one by one from the smallest. 
How to let the zeroes/Ones counted when first use. 

thinking:
m = 5 n = 3

ret = 4
curZ = 3  --- 2 left "11"
curO = 1  ----2 left "00"

0 1
"11" "10" "10" "1100"

CurZ = 5, 0 left 
curO = 1 --- 2 left

00 10 10  ret = 7 (m=5, n =5)
11 00 00 
111 
100 100 100 m=6 n=3  000000 111 9

100 m=4 n=2 0000 11

111

m,n
findMaxForm(list,m, n) = findMaxForm(list-1, m-x, n-y) + 1


*/