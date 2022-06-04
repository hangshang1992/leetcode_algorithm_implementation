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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        return helper(inorder, 0, inorder.size() - 1, postorder, 0, postorder.size() - 1);
    }
    TreeNode* helper(vector<int>& inorder, int iLeft, int iRight, vector<int>& postorder, int pLeft, int pRight){
        if (iLeft > iRight or pLeft > pRight){
            return NULL;
        }
        TreeNode* cur = new TreeNode(postorder[pRight]);
        int i = 0;
        for(i = iLeft; i < iRight; i++){
            if (postorder[pRight] == inorder[i]){
                break;
            }
        }
        cur->left = helper(inorder, iLeft, i - 1, postorder, pLeft, pLeft + i - iLeft - 1);
        cur->right = helper(inorder, i + 1, iRight, postorder, pLeft + i - iLeft, pRight - 1);
        return cur;
    }
};
