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
    vector<int> postorderTraversal(TreeNode* root) {
        if (root == NULL){
            return {};
        }
        vector<int> res;
        stack<TreeNode*> t({root});
        while(!t.empty()){
            TreeNode* node = t.top();
            t.pop();
            res.push_back(node->val);
            if (node->left != NULL){
                t.push(node->left);
            }
            if (node->right != NULL){
                t.push(node->right);
            }
        }
        reverse(res.begin(), res.end());
        return res;
        
    }
    
};
