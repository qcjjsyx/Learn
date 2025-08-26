#
# @lc app=leetcode.cn id=2410 lang=python3
#
# [2410] 运动员和训练师的最大匹配数
#

# @lc code=start
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        ans = 0
        i,j  = 0,0 
        while i<len(players) and j<len(trainers):
            if players[i] <= trainers[j]:
                ans += 1
                i += 1
            j += 1

        return ans
# @lc code=end

