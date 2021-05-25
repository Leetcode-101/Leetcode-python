#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Easy (74.49%)
# Likes:    591
# Dislikes: 0
# Total Accepted:    234K
# Total Submissions: 314K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 后序 遍历。
# 
# 示例:
# 
# 输入: [1,null,2,3]  
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3 
# 
# 输出: [3,2,1]
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 左子树 -> 右子树 -> 根节点
        res = []
        # 递归法

        def get_dfs(node):
            if node:
                get_dfs(node.left)
                get_dfs(node.right)
                res.append(node.val)
        get_dfs(root)
        # TODO 后序遍历 迭代法
        return res
# @lc code=end
