#
# @lc app=leetcode.cn id=904 lang=python3
#
# [904] 水果成篮
#

# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt = defaultdict(int)
        left = 0
        ans = 0
        for right,fruit in enumerate(fruits):
            cnt[fruit] += 1
            
            while len(cnt)>2:
                cnt[fruits[left]] -= 1
                if cnt[fruits[left]] == 0:
                    del cnt[fruits[left]]
                left += 1
            ans = max(ans, right - left + 1)
        return ans
# @lc code=end

