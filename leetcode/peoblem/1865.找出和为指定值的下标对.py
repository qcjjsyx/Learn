#
# @lc app=leetcode.cn id=1865 lang=python3
#
# [1865] 找出和为指定值的下标对
#

# @lc code=start
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.cnt1 = Counter(nums1)
        self.cnt2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        self.nums2[index] += val
        self.cnt2[old_val] -= 1
        if self.cnt2[old_val] == 0:
            del self.cnt2[old_val]
        if self.nums2[index] in self.cnt2:
            self.cnt2[self.nums2[index]] += 1
        else:
            self.cnt2[self.nums2[index]] = 1
        
    def count(self, tot: int) -> int:
        ans = 0
        for val1 in self.cnt1.keys():
            val2 = tot - val1
            if val2 in self.cnt2:
                ans += self.cnt1[val1] * self.cnt2[val2]
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
# @lc code=end

