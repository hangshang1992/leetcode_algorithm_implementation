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
    ListNode* partition(ListNode* head, int x) {
        if (head == NULL or head->next == NULL){
            return head;
        }
        ListNode* first = new ListNode(0);
        ListNode* second = new ListNode(0);
        ListNode* first_v1 = first;
        ListNode* second_v1 = second;
        
        while(head){
            if (head->val < x){
                second->next = head;
                head = head->next;
                second = second->next;
            }else{
                first->next = head;
                head = head->next;
                first = first->next;
            }
        }
        // first->next = second_v1->next;
        // return first_v1->next;
        first->next = NULL;
        second->next = first_v1->next;
        return second_v1->next;

    }
};
