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
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* pre = NULL;
        while(fast and fast->next){
            fast = fast->next->next;
            ListNode* tmp = slow->next;
            slow->next = pre;
            pre = slow;
            slow = tmp;
        }
        if (fast){
            slow = slow->next;
        }
        while(pre and slow and pre->val == slow->val){
            pre = pre->next;
            slow = slow->next;
        }
        return pre == NULL;
    }
};
