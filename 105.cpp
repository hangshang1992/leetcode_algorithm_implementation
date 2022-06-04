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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return helper(preorder,0, preorder.size() - 1, inorder, 0, inorder.size() - 1);
    }
    TreeNode* helper(vector<int>& preorder, int pLeft, int pRight, vector<int>& inorder, int iLeft, int iRight){
        if (pLeft > pRight or iLeft > iRight){
            return NULL;
        }
        int i = 0;
        for(i = iLeft ; i < iRight; i++){
            if (preorder[pLeft] == inorder[i]){
                break;
            }
        }
        TreeNode* node = new TreeNode(inorder[i]);
        node->left = helper(preorder, pLeft + 1, pLeft + i - iLeft, inorder, iLeft, i - 1);
        node->right = helper(preorder, pLeft + i - iLeft + 1, pRight, inorder, i+1, iRight);
        return node;
    }
};
