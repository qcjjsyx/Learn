#
# @lc app=leetcode.cn id=3307 lang=python3
#
# [3307] 找出第 K 个字符 II
#

# @lc code=start
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # n,i = 1,0
        # while n<k:
        #     i+=1
        #     n *= 2
        # d = 0
        # while n>1:
        #     if k>n//2:
        #         d += operations[i-1]
        #         k -= n//2
        #     n //= 2
        #     i -= 1
        # return chr(d%26+ord('a'))
        add_length = 1
        alphabet = "abcdefghijklmnopqrstuvwxyz"
       
# @lc code=end

