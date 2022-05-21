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
    bool findTarget(TreeNode* root, int k) {
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
        unordered_map<int, int> umap;
        for (int i = 0; i < res.size(); i++){
            int tmp = k - res[i];
            if (umap.find(tmp) != umap.end()){
                return true;//{umap.find(tmp) -> second, i};
            }
            umap.insert(pair<int, int>(res[i],i));
        }
        return false;
    }
};
