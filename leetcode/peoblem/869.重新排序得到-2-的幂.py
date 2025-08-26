#
# @lc app=leetcode.cn id=869 lang=python3
#
# [869] 重新排序得到 2 的幂
#

# @lc code=start
def isPowerOfTwo(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        nums = sorted(list(str(n)))
        m = len(nums)
        visited = [False] * m

        def backtrack(index: int, num: int) -> bool:
            if index == m:
                return isPowerOfTwo(num)
            for i,ch in enumerate(nums):
                if (num==0 and ch=='0') or visited[i] or (i>0 and not visited[i-1] and ch==nums[i-1]):
                    continue
                visited[i] = True
                if backtrack(index + 1, num * 10 + int(ch)):
                    return True
                visited[i] = False
            return False

        return backtrack(0, 0)
# @lc code=end

