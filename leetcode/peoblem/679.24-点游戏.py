#
# @lc app=leetcode.cn id=679 lang=python3
#
# [679] 24 点游戏
#

# @lc code=start
EPS = 1e-9
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        n = len(cards)
        if n == 1:
            return abs(cards[0] - 24) < EPS

        # 选两张牌 x=cards[i] 和 y=cards[j]
        for i, x in enumerate(cards):
            for j in range(i + 1, n):
                y = cards[j]

                # 六种情况：加减乘除，其中减和除都有两种不同的顺序
                candidates = [x + y, x - y, y - x, x * y]
                if abs(y) > EPS:  # 保证分母不为 0
                    candidates.append(x / y)
                if abs(x) > EPS:  # 保证分母不为 0
                    candidates.append(y / x)

                new_cards = cards[:j] + cards[j + 1:]  # 删除 j
                for res in candidates:
                    new_cards[i] = res  # 覆盖 i
                    if self.judgePoint24(new_cards):
                        return True

        return False
# @lc code=end

