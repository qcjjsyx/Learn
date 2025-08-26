#
# @lc app=leetcode.cn id=3478 lang=python3
#
# [3478] 选出和最大的 K 个元素
#Top K 变化的堆

# @lc code=start
class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        a = sorted((x,y,i) for i,(x,y) in enumerate(zip(nums1,nums2)))#这个排序技巧需要知道，让y按照x所需要的顺序来进行排序
        n = len(a)
        ans = [0]*n
        h = []
        s = i = 0
        while i<n:
            start = i
            x = a[i][0]
            while i<n and a[i][0]==x:
                ans[a[i][2]] = s
                i += 1
            for j in range(start,i):
                y = a[j][1]
                s += y
                heapq.heappush(h,y)
                if len(h)>k:
                    s -= heapq.heappop(h)
                    
        return ans
        
# @lc code=end

