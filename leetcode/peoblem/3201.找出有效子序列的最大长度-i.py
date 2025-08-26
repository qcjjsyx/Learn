#
# @lc app=leetcode.cn id=3201 lang=python3
#
# [3201] 找出有效子序列的最大长度 I
#

# @lc code=start
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        ans = 2
        n = len(nums)
        f = [[1,1] for _ in range(n)]
        f[1][(nums[0] + nums[1]) % 2] = 2
        mod_0 , mod_1 = -1,-1
        for i in range(0,n):
            if i==1 or i==0:
                mod_0 = i if nums[i] % 2 == 0 else mod_0
                mod_1 = i if nums[i] % 2 == 1 else mod_1
                continue
            if nums[i] % 2 == 0:
                f[i][0] = f[mod_0][0] + 1 if mod_0 != -1 else 1
                f[i][1] = f[mod_1][1] + 1 if mod_1 != -1 else 1
                mod_0 = i 
                
            else:
                f[i][0] = f[mod_1][0] + 1 if mod_1 != -1 else 1
                f[i][1] = f[mod_0][1] + 1 if mod_0 != -1 else 1
                mod_1 = i 
            ans = max(ans, f[i][0], f[i][1])
        print(f)
        return ans
# @lc code=end

