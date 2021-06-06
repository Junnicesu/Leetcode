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
        ListNode* fast = head;
        ListNode* slow = head;
        while (fast->next != nullptr && fast->next->next != nullptr)
        {
            fast = fast->next->next;
            slow = slow->next;
        }
        
        //copy the latter half of the List
        ListNode* cur = slow;        
        std::shared_ptr<ListNode> revCur = nullptr;
        while(cur!=nullptr){
            revCur = std::make_shared<ListNode>(cur->val, revCur.get());
            cur = cur->next;            
        }
                                
        std::shared_ptr<ListNode> revHead = revCur;
        //compare the hard new rev with         
        bool ret = true;
        cur = head;
        ListNode* newCur = revHead.get();
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

        //need to delete all the new pointers??  

        return ret;
    }
};

/*
Trying to mix using smart_ptr with traditional ptr. 
Run time error!!!!!
*/