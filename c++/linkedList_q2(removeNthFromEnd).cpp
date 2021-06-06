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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int totalNode = 0;
        ListNode* cur = head;
        while(cur!=nullptr){
            totalNode++;
            cur = cur->next;
        }        
        int id = totalNode - n ;
        printf("total Node: %d, to del %d", totalNode, id);
        if(id == 0){
            return head->next;
        }
        else{
            ListNode* nodeB4 = nullptr;
            cur = head;
            for(int i=0; i<id-1; i++){  //sj, Wronged once.
                cur = cur->next;
            }
            nodeB4 = cur;
            ListNode* theNode = nodeB4->next;
            nodeB4->next = theNode->next;
            delete theNode;
        }
        return head;
    }
};