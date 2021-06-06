/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode* revHead = nullptr;
        ListNode* cur = head;
        ListNode* nxt = cur->next;

        while(cur!=nullptr){
            revHead  = new ListNode(cur->val, revHead);
            cur = cur->next;            
        }
                
        bool ret = true;
        cur = head;
        auto newCur = revHead;
        
        while(cur!=nullptr && revHead!=nullptr){
            // printf("cur is %d, newCur is %d\n", cur->val, newCur->val); //sjdb
            ret = (cur->val == newCur->val) ? true : false;
            if(ret){
                cur = cur->next;
                newCur = newCur->next;
            }
            else{
                break;
            }
        }
        //delete them
        newCur = revHead;
        auto prev = newCur;
        while(newCur!=nullptr){
            prev = newCur;
            auto nxt = newCur->next;
            newCur = nxt;
            delete prev;
        }

        return ret;
    }
};