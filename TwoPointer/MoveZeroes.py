"""
题号 283 移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

注意要保持非零元素的相对顺序

参考:https://leetcode-cn.com/problems/move-zeroes/solution/shuang-zhi-zhen-ti-huan-0-by-fan-shao-3/

举个例子:
nums = [0,0,0,0,1]
如何将所有的0移动到数组最后面?
当然是让指针j指向第一个0,i指针一直遍历到第一个非零的数,然后nums[i] = 0，nums[j] = nums[i]

"""
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0  # 指针j指向第一个非零的数
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != j:
                    nums[j] = nums[i]
                    nums[i] = 0
                j += 1


if __name__ == '__main__':
    nums = [0,1,0,3,12]
    solution = Solution()
    solution.moveZeroes(nums)
    print(nums)