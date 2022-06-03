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
        stack<int> q1;
        stack<int> q2;
        while(l1){
            q1.push(l1->val);
            l1 = l1->next;
        }
        while(l2){
            q2.push(l2->val);
            l2 = l2->next;
        }
        int left = 0;
        ListNode* cur = NULL;
        while(!q1.empty() or !q2.empty()){
            int sum = 0;
            if (!q1.empty()){
                sum += q1.top();
                q1.pop();
            }
            if (!q2.empty()){
                sum += q2.top();
                q2.pop();
            }
            int var = (sum + left)%10;
            ListNode* node = new ListNode(var);
            node->next = cur;
            cur = node;
            left = (sum + left) / 10;
        }
        if (left){
            ListNode* node = new ListNode(left);
            node->next = cur;
            cur = node;
        }
        return cur;
    }
};
