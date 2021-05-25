#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Easy (75.40%)
# Likes:    960
# Dislikes: 0
# Total Accepted:    432.4K
# Total Submissions: 573.4K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
# 
# 
# 示例 2：
# 
# 
# 输入：root = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：root = [1]
# 输出：[1]
# 
# 
# 示例 4：
# 
# 
# 输入：root = [1,2]
# 输出：[2,1]
# 
# 
# 示例 5：
# 
# 
# 输入：root = [1,null,2]
# 输出：[1,2]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [0, 100] 内
# -100 
# 
# 
# 
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 左子树 -> 根节点 -> 右子树
        res = []

        # 递归法
        # def get_dfs(node, res):
        #     if node:
        #         get_dfs(node.left, res)
        #         res.append(node.val)
        #         get_dfs(node.right, res)

        # get_dfs(root, res)

        # 迭代法
        stack = []
        while stack or root is not None:
            while root:
                stack.append(root)
                root = root.left

            # node = stack.pop()
            # res.append(node.val)
            # root = node.right
            # 直接使用root单个变量
            root = stack.pop()
            res.append(root.val)
            root = root.right

        return res

# @lc code=end
