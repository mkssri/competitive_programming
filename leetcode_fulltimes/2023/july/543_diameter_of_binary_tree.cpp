#include <iostream>

/**
 * Definition for a binary tree node.*/
 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };



class Solution {

public:

    int result=0;

    int diameterOfBinaryTree(TreeNode* root) {
        helper(root);
        return result;
    }

    int helper( TreeNode* root ) {
        
        if(root==nullptr) 
            return 0;
        
        int le = helper(root->left);
        int ri = helper(root->right);

        result = std::max(result, le+ri);
        return 1+std::max(le,ri);        

    }

};
