class Solution {
public:
    int longestValidParentheses(string s) {
        deque<char> stack;
        vector<int> rets(1,0);
        int cnt = 0;
        for(auto c: s){
            if(stack.size() == 0 && c == ')') continue;
            stack.push_back(c);
            if(c==')'){
                int len = stack.size();
                int id = len -1;
                while(id > 0){
                    auto cur = stack[id];
                    auto pre = stack[id-1];
                    if(cur==')' && pre=='('){
                        cnt +=2;
                        stack.pop_back(); stack.pop_back();
                        id-=2;
                    }
                    else{
                        break;
                    }
                }
                if(stack.size() == 0){
                    rets.push_back(cnt);
                    cnt = 0;
                }
            }
        }        
        auto it = max_element(begin(rets), end(rets));
        return *it;
    }
};

/*
Your input : "(())(((())()))"

Your answer:
10

Expected answer:
14

sj: all contiguous valid parentheses are considered to be One

*/