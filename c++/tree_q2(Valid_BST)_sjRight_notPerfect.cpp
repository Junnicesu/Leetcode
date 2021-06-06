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
    bool isValidBST(TreeNode* root) {
        if(root == nullptr) return true;
        
        bool ret = INT_MIN <= root->val && root->val <=INT_MAX;
        cout << INT_MIN << "~" << INT_MAX << endl;
        if(root->left==nullptr && root->right==nullptr){
            return ret;
        }
        long lbn = INT_MIN;
        lbn--;
        long rbn = INT_MAX;
        rbn++;
        return ret && isValidBSTUntil(lbn, root, rbn);
    }

    bool isValidBSTUntil(long long lbn, TreeNode* node, long long rbn){
        bool ret;
        if(node->left!=nullptr){
            ret = lbn < node->left->val && node->left->val < node->val 
                      && isValidBSTUntil(lbn, node->left, node->val);
            if(!ret) return false;
        }
        if(node->right!=nullptr){
            ret = node->val < node->right->val && node->right->val < rbn 
                     && isValidBSTUntil(node->val, node->right, rbn);
        }
        return ret;
    }
};