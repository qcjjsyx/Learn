#
# @lc app=leetcode id=2040 lang=python3
#
# [2040] Kth Smallest Product of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        i0 = bisect.bisect_left(nums1,0)
        j0 = bisect.bisect_left(nums2,0)
        n, m = len(nums1), len(nums2)
        def check(mx):
            if mx<0:
                cnt = 0
                i,j = 0,j0
                while i<i0 and j<m:
                    if nums1[i]*nums2[j]>mx:
                        j += 1
                    else:
                        cnt += m-j
                        i += 1

                i,j = i0,0
                while i<n and j<j0:
                    if nums1[i]*nums2[j]>mx:
                        i += 1
                    else:
                        cnt += n-i
                        j += 1
            else:
                cnt = 0
                i,j = 0,j0-1
                while i<i0 and j>=0:
                    if nums1[i]*nums2[j]>mx:
                        i += 1
                    else:
                        cnt += i0-i
                        i -= 1
                
                i,j = i0,m-1
                while i<n and j>=j0:
                    if nums1[i]*nums2[j]>mx:
                        j -= 1
                    else:
                        cnt += j-j0+1
                        i += 1
                        
            return cnt >= k
        
        corners = [nums1[0]*nums2[0], nums1[-1]*nums2[-1],nums1[0]*nums2[-1], nums1[-1]*nums2[0]]
        l,r = min(corners), max(corners)
        return l + bisect.bisect_left([l,r], True, key=lambda x: check(x))
                        
# @lc code=end

