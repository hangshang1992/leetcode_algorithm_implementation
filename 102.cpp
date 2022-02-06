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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ret;
        dfs(root, 0, ret);
        return ret;
    }
    void dfs(TreeNode* cur, int level, vector<vector<int>>& ret){
        if (cur == NULL)
            return;
        if (level == ret.size()){
            ret.push_back({cur->val});
        }else{
            ret[level].push_back(cur->val);
        }
        dfs(cur->left, level+1, ret);
        dfs(cur->right, level+1,ret);
    }
};
