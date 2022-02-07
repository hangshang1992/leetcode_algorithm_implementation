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
    TreeNode* buildTree(vector<int>& a, int &i, vector<int>& b, int left, int right){
        if (left>right){
            return NULL;
        }
        TreeNode *node = new TreeNode(a[i]);
        i++;
        if (i == a.size()){
            return node;
        }
        int j = left;
        while (b[j] != a[i-1]){
            j++;
        }
        node->left = buildTree(a, i, b, left, j-1);
        node->right = buildTree(a, i, b, j+1, right);
        return node;
    }
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int i = 0;
        return buildTree(preorder,i, inorder, 0, inorder.size() - 1);
    }
};
