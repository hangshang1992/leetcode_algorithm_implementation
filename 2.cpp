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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);
        ListNode* pre1 = dummy;
        int carry = 0;
        
        int left = 0;
        while(l1 or l2 or carry){
            int v1 = 0, v2 = 0;
            if(l1){
                v1 = l1->val;
                l1 = l1->next;
            }
            if (l2){
                v2 = l2->val;
                l2 = l2->next;
            }
            left = (carry + v1 + v2) % 10;
            carry = (carry + v1 + v2) / 10;
            ListNode* pre = new ListNode(left);
            dummy->next = pre;
            dummy = dummy->next;
        }
        return pre1->next;
    }
};
