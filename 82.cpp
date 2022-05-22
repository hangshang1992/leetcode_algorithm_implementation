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
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == NULL or head->next == NULL){
            return head;
        }
        ListNode* cmp = head->next;
        if (head->val == cmp->val){
            while(cmp and cmp->val == head->val){
                cmp = cmp->next;
            }
            head = cmp;
            return deleteDuplicates(head);
        }else{
            head->next = deleteDuplicates(head->next);
            return head;
        }
    }
};
