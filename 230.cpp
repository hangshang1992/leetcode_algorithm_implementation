/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        vector<int> res;
        stack<TreeNode*> t({root});
        while(!t.empty() or root != NULL){
            if (root != NULL){
                t.push(root);
                root = root->left;
            }else{
                TreeNode* node = t.top();
                t.pop();
                res.push_back(node->val);
                root = node->right;
            }
        }
        return res[k-1];
    }
};
