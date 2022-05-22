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
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == NULL or k == 0){
            return head;
        }
        ListNode* slow = head;
        ListNode* fast = head;
        int length = 0;
        while (fast != NULL){
            length++;
            fast = fast->next;
        }
        fast = head;
        k %= length;
        for (int i = 0; i < k; i++){
            fast = fast->next;
            
        }
        while (fast and fast->next){
            fast = fast->next;
            slow = slow->next;
        }
        // slow->next = NULL;
        fast->next = head;
        head = slow->next;
        slow->next = NULL;
        return head;
        
        
    }
};
