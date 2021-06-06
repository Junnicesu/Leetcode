class Solution {
public:
    int longestValidParentheses(string s) {
        deque<char> stack;
        int ret =0;
        for(auto c: s){
            stack.push_back(c);
            if(c==')'){
                int len = stack.size();
                int id = len -1;
                while(id > 0){
                    auto cur = stack[id];
                    auto pre = stack[id-1];
                    if(cur==')' && pre=='('){
                        ret +=2;
                        stack.pop_back(); stack.pop_back();
                        id-=2;
                    }
                    else{
                        break;
                    }
                }
            }
        }
        return ret;
    }
};

/*
Input: "()(()"
Output: 4
Expected: 2

//sj!!! note: not summerize all pairs parentheses, but longest valid one

*/