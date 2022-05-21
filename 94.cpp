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
    vector<int> inorderTraversal(TreeNode* root) {
        if (root == NULL){
            return {};
        }
        vector<int> res;
        stack<TreeNode*> q;
        while(!q.empty() or root != NULL){
            if (root != NULL){
                q.push(root);
                root = root->left;
            }else{
                TreeNode* node = q.top();
                q.pop();
                res.push_back(node->val);
                root = node->right;
            }
        }
        return res;
    }
    
};
