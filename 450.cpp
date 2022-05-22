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
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (root == NULL){
            return NULL;
        }
        if (root -> val > key){
            root->left = deleteNode(root->left, key);
        }
        else if (root->val < key){
            root->right = deleteNode(root->right, key);
        }
        else if (root->left != NULL and root->right != NULL){
            auto tmp = root->right;
            while (tmp->left != NULL){
                tmp = tmp->left;
            }
            root->val = tmp->val;
            root->right = deleteNode(root->right, tmp->val);
        }else{
            auto tmp = root;
            if (tmp->left != NULL){
                root = root->left;
            }else{
                root = root->right;
            }
            delete tmp;
            tmp = NULL;
            
        }
        return root;
    }
};
