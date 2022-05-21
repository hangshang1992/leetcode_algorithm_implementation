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
    TreeNode* invertTree(TreeNode* root) {
        stack<TreeNode*> t({root});
        while(!t.empty()){
            TreeNode* node = t.top();
            t.pop();
            if (node != NULL){
                auto tmp = node->left;
                node->left = node->right;
                node->right = tmp;
                // node->left, node->right = node->right, node->left;
                t.push(node->right);
                t.push(node->left);
            }
        }
        return root;
    }
};
