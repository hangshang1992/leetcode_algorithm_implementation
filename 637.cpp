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
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> res;
        queue<TreeNode*> q({root});
        while(!q.empty()){
            // vector<int> tmp;
            double t = 0.0;
            int sum1 = 0;
            for (int i = q.size();i>0;--i){
                TreeNode* node = q.front();
                q.pop();
                // tmp.push_back(node->val);
                sum1++;
                t += node->val;
                if (node->left != NULL){
                    q.push(node->left);
                }
                if (node->right != NULL){
                    q.push(node->right);
                }
            }
            res.push_back(t/sum1);
        }
        return res;
    }
};
