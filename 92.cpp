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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* left1 = dummy;
        ListNode* right1 = dummy;
        ListNode* pre = NULL;
        for (int i = 0; i < left; i++){
            pre = left1;
            left1 = left1->next;
        }
        for (int i = 0; i < right;i++){
            right1 = right1->next;
        }
        ListNode* final1 = right1->next;
        
        pre->next = NULL;
        right1->next = NULL;
        ListNode* pree = NULL;
        ListNode* cur = left1;
        while(cur){
            ListNode* tmp = cur->next;
            cur->next = pree;
            pree = cur;
            cur = tmp;
        }
        pre->next = pree;
        left1->next = final1;
        return dummy->next;
    }
};
