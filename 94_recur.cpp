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
        vector<int> a;
        recursive(root, a);
        return a;
    }
    void recursive(TreeNode* root, vector<int> &rec){
        if (root){
            recursive(root->left, rec);
            rec.push_back(root->val);
            recursive(root->right, rec);
        }
    }
};
