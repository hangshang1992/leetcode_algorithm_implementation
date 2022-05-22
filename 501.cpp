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
    unordered_map<int, int> umap;
    vector<int> findMode(TreeNode* root) {
        if (root == NULL){
            return {};
        }
        inorder(root);
        priority_queue<pair<int,int>>pq;
        for (auto it = umap.begin(); it != umap.end(); it++){
            pq.push({it->second, it->first});
        }
        int maxCount = pq.top().first;
        vector<int> res;
        while(!pq.empty() and pq.top().first == maxCount){
            res.push_back(pq.top().second);
            pq.pop();
        }
        return res;
        
    }
    void inorder(TreeNode* root){
        if (root != NULL){
            umap[root->val]++;
            inorder(root->left);
            inorder(root->right);
        }
        return;
    }
};
