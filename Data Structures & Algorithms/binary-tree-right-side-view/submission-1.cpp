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
    vector<int> rightSideView(TreeNode* root) {
        int steps = 0;
        vector<int> output;
        queue<TreeNode*> temp;
        if(root)
            temp.push(root);
        while (!temp.empty()) {
            int size = temp.size();
            for (int i = 0; i < size - 1; i++) {
                if (temp.front()->left) temp.push(temp.front()->left);
                if (temp.front()->right) temp.push(temp.front()->right);
                temp.pop();
            }
            if (temp.front()->left) temp.push(temp.front()->left);
            if (temp.front()->right) temp.push(temp.front()->right);
            output.push_back(temp.front()->val);
            temp.pop();
        }
        return output;
    }
};
