from bitarray import bitarray
class Solution(object):
    def missingTwo(self, nums):
        """
         给定一个数组，包含从 1 到 N 所有的整数，但其中缺了两个数字。你能在 O(N) 时间内只用 O(1) 的空间找到它们吗？

        以任意顺序返回这两个数字均可。

        示例 1:

        输入: [1]
        输出: [2,3]
        示例 2:

        输入: [2,3]
        输出: [1,4]
        提示：

        nums.length <= 30000
        :type nums: List[int]
        :rtype: List[int]
        """
        bitarray1 = bitarray(len(nums))
        for i in range(len(nums)):
            nums[i]

