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
        if (head->next == NULL){
            return NULL;
        }
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* pre = dummy;
        int length = 0;
        while (head){
            head = head->next;
            length++;
        }
        for(int i = 0; i < length - n; i++){
            dummy = dummy->next;
        }
        dummy->next = dummy->next->next;
        return pre->next;
    }
};
