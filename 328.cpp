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
    ListNode* oddEvenList(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode * pre = head;
        ListNode * cur = head->next;
        while(cur != nullptr && cur->next != nullptr)
        {
            ListNode * temp = pre->next;
            pre->next = cur->next;//奇数链表的连接
            cur->next = cur->next->next;//偶数的连接
            pre->next->next = temp;//奇数的后面接偶数
            //两个指针后移
            pre = pre->next;
            cur = cur->next;
        }
        return head;
    }
};
