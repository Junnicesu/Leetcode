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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* ret = (l1 != nullptr) ? l1: nullptr;
        ListNode* toMerge = l2 != nullptr ? l2: nullptr;
        if(ret == nullptr || toMerge == nullptr){
            return (ret!=nullptr)? ret: toMerge;
        }
        else{
            if( ret->val > toMerge->val){
                auto tmp = ret;
                ret = toMerge;
                toMerge = tmp;
                printf("ret is %d, toMerge is %d\n", ret->val, toMerge->val);//sjdb
                
            }
        }

        //after this, both of ret and toMerge is not null, need merge
        ListNode dummy;
        ListNode* newCur = &dummy;  //good tricky, return dummy.next at the end
        ListNode* cur = ret;
        ListNode* toMergeCur = toMerge;
        while(cur!=nullptr){
            newCur->next = new ListNode(cur->val);
            printf("copied %d\n", cur->val);
            newCur = newCur->next; //point to new created Node
            ListNode* nxt = cur->next;
            if(toMergeCur==nullptr || (nxt!=nullptr && nxt->val < toMergeCur->val)){
                cur = nxt;
            }
            else
            {
                while(toMergeCur != nullptr){
                    if(nxt!=nullptr &&  nxt->val < toMergeCur->val){
                        break;
                    }
                    newCur->next = new ListNode(toMergeCur->val);
                    printf("inside copied %d\n", toMergeCur->val);
                    newCur = newCur->next;                    
                    toMergeCur = toMergeCur->next; 
                }
                cur = nxt;
            }
            
        }

        return dummy.next;
    }
};