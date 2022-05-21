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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (root == NULL){
            return {};
        }
        vector<vector<int>> res;
        queue<TreeNode*> q({root});
        int cnt = 0;
        while(!q.empty()){
            vector<int> tmp;
            for (int i = q.size(); i>0; --i){
                TreeNode* node = q.front();
                q.pop();
                tmp.push_back(node->val);
                if (node->left != NULL){
                    q.push(node->left);
                }
                if (node->right != NULL){
                    q.push(node->right);
                }
            }
            if (cnt % 2 == 1){
                reverse(tmp.begin(), tmp.end());
            }
            res.push_back(tmp);
            cnt++;
            
        }
        return res;
    }
};
