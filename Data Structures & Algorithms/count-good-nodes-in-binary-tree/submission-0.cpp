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
    int dfs(TreeNode* root, int highest) {
        int val = 0;
        if (highest <= root->val) {
            highest = root->val;
            val++;
        }
        if (root->left) val += dfs(root->left,highest);
        if (root->right) val += dfs(root->right,highest);
        return val;
    }
    int goodNodes(TreeNode* root) { return dfs(root, root->val); }
};
