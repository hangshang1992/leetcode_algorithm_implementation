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
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> res;
        vector<int> tmp;
        dfs(root, res, tmp, targetSum);
        return res;
    }
    void dfs(TreeNode* root, vector<vector<int>>& res, vector<int>& tmp, int target){
        if (root == NULL){
            return;
        }
        if (root->left == NULL and root->right ==NULL and root->val == target){
            tmp.push_back(root->val);
            res.push_back(tmp);
            tmp.pop_back();
            return;
        }
        tmp.push_back(root->val);
        dfs(root->left, res, tmp, target-root->val);
        dfs(root->right, res, tmp, target - root->val);
        tmp.pop_back();
    }
};
