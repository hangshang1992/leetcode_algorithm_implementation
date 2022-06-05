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
    void recoverTree(TreeNode* root) {
        vector<TreeNode*> list1;
        vector<int> res;
        inorder(root, list1, res);
        std:sort(res.begin(), res.end());
        for(int i = 0; i < list1.size(); i++){
            list1[i]->val = res[i];
        }
    }
    void inorder(TreeNode* root, vector<TreeNode*>& list1, vector<int>& res){
        if(root){
            inorder(root->left, list1, res);
            list1.push_back(root);
            res.push_back(root->val);
            inorder(root->right, list1, res);
        }
    }
};
