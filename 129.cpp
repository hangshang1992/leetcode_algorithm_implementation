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
    int res = 0;
    int sumNumbers(TreeNode* root) {
        if (root == NULL){
            return res;
        }
        dfs(root, 0);
        return res;
    }
    void dfs(TreeNode* root, int num){
        if(root == NULL){
            return ;
        }
        num = 10 * num + root->val;
        if(!root->left and !root->right){
            res += num;
        }
        if(root->left){
            dfs(root->left, num);
        }
        if(root->right){
            dfs(root->right, num);
        }
    }
};
