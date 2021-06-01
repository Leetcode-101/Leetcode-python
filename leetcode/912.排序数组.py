#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#
# https://leetcode-cn.com/problems/sort-an-array/description/
#
# algorithms
# Medium (58.21%)
# Likes:    294
# Dislikes: 0
# Total Accepted:    158.9K
# Total Submissions: 273.2K
# Testcase Example:  '[5,2,3,1]'
#
# 给你一个整数数组 nums，请你将该数组升序排列。
#
#
#
#
#
#
# 示例 1：
#
# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
#
#
# 示例 2：
#
# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 50000
# -50000 <= nums[i] <= 50000
#
#
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 顺序迭代法
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        # (超时)
        # def sort_inner(start, end):
        #     if start >= end:
        #         return
        #     # pivot = end
        #     store_index = start
        #     for i in range(start, end):
        #         # if nums[i] < nums[pivot]:
        #         if nums[i] < nums[end]:
        #             swap(i, store_index)
        #             store_index += 1
        #     # swap(store_index, pivot)
        #     swap(store_index, end)
        #     sort_inner(start, store_index-1)
        #     sort_inner(store_index+1, end)

        # sort_inner(0, len(nums)-1)

        # 使用随机pivot；将pivot -> end
        # 将<nums[end]的数字从列表头开始排
        # 将nums[end]与store_index交换，将pivot值放回中间
        def sort_inner(start, end):
            if start >= end:
                return
            # pivot = end
            pivot = random.randint(start, end)
            swap(pivot, end)
            # 将标准点换到最右边
            store_index = start
            for i in range(start, end):
                if nums[i] < nums[end]:
                    swap(i, store_index)
                    store_index += 1
            swap(store_index, end)
            sort_inner(start, store_index-1)
            sort_inner(store_index+1, end)

        sort_inner(0, len(nums)-1)

        return nums
# @lc code=end
