#
# @lc app=leetcode.cn id=1394 lang=python3
#
# [1394] 找出数组中的幸运数
#

# @lc code=start
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        for i,x in enumerate(sorted(cnt.keys(),reverse=True)):
            if cnt[x] == x:
                return x
        return -1
# @lc code=end

