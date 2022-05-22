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
#include<iostream>
class Solution {
public:
    void reorderList(ListNode* head) {
        if (head == NULL){
            return;
        }
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast and fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* node = slow;
        ListNode* pre = NULL;
        // cout << "hello ";
        while (node){
            ListNode* tmp = node->next;
            node->next = pre;
            pre = node;
            node = tmp;
        }
        // cout << " hello1 " << pre->val << ' '<< pre->next->val << " 09 ";
        // cout << head->val << " 098 ";
        ListNode* first = head;
        ListNode* second = pre;
        while (second->next){
            ListNode* tmp1 = first->next;
            first->next = second;
            first = tmp1;
            ListNode* tmp2 = second->next;
            second->next = first;
            second = tmp2;
            // cout<< " po " << second->val << "\n";
            // cout<<  " poi " << first->val << " \n ";
        }
    }
};
