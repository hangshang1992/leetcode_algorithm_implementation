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
    ListNode* swapPairs(ListNode* head) {
        if (head == NULL or head->next == NULL){
            return head;
        }
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* pre = dummy;
        while(pre->next and pre->next->next){
            ListNode* tmp = pre->next->next;
            pre->next->next = tmp->next;
            tmp->next = pre->next;
            pre->next = tmp;
            pre = pre->next->next;
        }
        return dummy->next;
    }
};
