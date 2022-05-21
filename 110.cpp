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
    bool isBalanced(TreeNode* root) {
        return helper(root);
    }
    
    bool helper(TreeNode* root){
        if (root != NULL){
            int leftHeight = getDepth(root->left, 1);
            int rightHeight = getDepth(root->right, 1);
            if (abs(leftHeight - rightHeight) > 1){
                return false;
            }
            return helper(root->left) and helper(root->right);
        }
        return true;
    }
    int getDepth(TreeNode* root,int depth){
        if (root != NULL){
            return max(getDepth(root->left, depth + 1), getDepth(root->right, depth + 1));
        }
        return depth - 1;
    }
};
