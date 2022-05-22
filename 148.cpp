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
    ListNode* sortList(ListNode* head) {
        if (head == NULL or head->next == NULL){
            return head;
        }
        ListNode *temp = head, *slow = head, *fast = head;
        while(fast and fast->next){
            temp = slow;
            fast = fast->next->next;
            slow = slow->next;
        }
        temp->next = NULL;
        ListNode* l1 = sortList(head);
        ListNode* l2 = sortList(slow);
        return merge(l1, l2);
    }
    ListNode* merge(ListNode* l1, ListNode* l2){
        ListNode* dummy = new ListNode(0);
        ListNode* d1 = dummy;
        while (l1 and l2){
            if (l1->val > l2->val){
                dummy->next = l2;
                l2 = l2->next;
                dummy = dummy->next;
            }
            else{
                dummy->next = l1;
                l1 = l1->next;
                dummy = dummy->next;
            }
        }
        if (l1){
            dummy->next = l1;
        }
        if (l2){
            dummy->next = l2;
        }
        return d1->next;
    }

    

};
