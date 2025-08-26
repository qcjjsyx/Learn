#
# @lc app=leetcode.cn id=3477 lang=python3
#
# [3477] 水果成篮 II
#

# @lc code=start
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        is_used = [False] * len(baskets)
        for fruit in fruits:
            for basket_id, basket in enumerate(baskets):
                if not is_used[basket_id] and basket >= fruit:
                    is_used[basket_id] = True
                    break
        return sum(1 for used in is_used if not used)
# @lc code=end

