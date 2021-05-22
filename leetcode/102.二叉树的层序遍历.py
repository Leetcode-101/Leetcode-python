#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (64.15%)
# Likes:    876
# Dislikes: 0
# Total Accepted:    312.6K
# Total Submissions: 487.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
# 
# 
# 
# 示例：
# 二叉树：[3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回其层序遍历结果：
# 
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
# 
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []

        # 递归法
        i = 0

        def get_dfs(node, i, res):
            if node:
                if len(res) <= i:
                    res.append([node.val])
                else:
                    res[i].append(node.val)
                get_dfs(node.left, i+1, res)
                get_dfs(node.right, i+1, res)
        get_dfs(root, i, res)

        return res
# @lc code=end
