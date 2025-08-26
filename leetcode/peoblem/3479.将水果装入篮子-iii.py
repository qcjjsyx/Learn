#
# @lc app=leetcode.cn id=3479 lang=python3
#
# [3479] 将水果装入篮子 III
#
# 线段树，找最左边的>=x的数，改为-1.然后更新整颗线段树
# @lc code=start
#静态
class SegmentTree:
    def __init__(self,a):
        n = len(a)
        self.max = [0]*(4*n)
        self.build(a,1,0,n-1)
    def maintain(self,o):
        self.max[o] = max(self.max[2*o],self.max[2*o+1])
    
    def build(self,a,o,l,r):
        if l==r:
            self.max[o] = a[l]
            return 
        m = (l+r)//2
        self.build(a,2*o,l,m)
        self.build(a,2*o+1,m+1,r)
        self.maintain(o)        
    
    def update(self,o,l,r,i,x):
        if l==r:
            self.max[o] = x
            return 
        m = (l+r)//2
        if i<=m:
            self.update(2*o,l,m,i,x)
        else:
            self.update(2*o+1,m+1,r,i,x)
        self.maintain(o)
        return i
    
    def find_first(self,o,l,r,x):
        if self.max[o]<x:
            return -1
        if l==r:
            return l
        m = (l+r)//2
        i = self.find_first(2*o,l,m,x)
        if i<0:
            i = self.find_first(2*o+1,m+1,r,x)
        return i
    
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        t = SegmentTree(baskets)
        ans = 0 
        n = len(baskets)
        for fruit in fruits:
            i = t.find_first(1,0,n-1,fruit)
            if i<0:
                ans += 1
            else:
                t.update(1,0,n-1,i,-1)
        return ans
        
# @lc code=end

