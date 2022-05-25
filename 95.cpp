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
    vector<TreeNode*> generateTrees(int n) {
        if (n==0){
            return {};
        }
        cout << "hello";
        return helper(1, n);
    }
    vector<TreeNode*> helper(int start, int end){
        if ( start > end){
            return {NULL};
        }
        cout << " dld ";
        vector<TreeNode*> res;

        for (int i = start; i<= end;i++){
            auto left = helper(start, i - 1), right = helper(i + 1, end);

            
            for(auto left_item: left){
                for(auto right_item: right){
                
                    TreeNode* root = new TreeNode(i);
                    root->left = left_item;
                    root->right = right_item;
                    res.push_back(root);
                }
            }
        }
        return res;
    }
};
