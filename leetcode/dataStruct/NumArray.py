class NumArray_nlogn:
    __slots__ = 'nums', 'tree'
    def __init__(self, nums):
        n = len(nums)
        self.nums = [0]*n
        self.tree = [0]*(n+1)
        for i, x in enumerate(nums):
            self.update(i, x)
            
            
    def update(self, i, val):
        delta = val-self.nums[i]
        self.nums[i] = val
        i += 1
        while i< len(self.tree):
            self.tree[i] += delta
            i += i & -i#lowbit(i)的实现方式
            
    def prefixSum(self, i):
        i += 1
        res = 0
        while i>0:
            res += self.tree[i]
            i -= i & -i
        return res
    
    def sumRange(self, left, right):
        return self.prefixSum(right) - self.prefixSum(left-1) if left > 0 else self.prefixSum(right)
    
    
    
class NumArray_n:
    __slots__ = 'nums', 'tree'
    
    def __init__(self,nums):
        n = len(nums)
        self.nunms = nums
        tree = [0]*(n+1)
        for i,x in enumerate(nums,1):#从1开始
            tree[i] += x
            nxt = i+(i&-i)
            if nxt<=n:
                tree[nxt] += tree[i]
        self.tree = tree
        
    
    def update(self,index,val):
        delta = val-self.nunms[index]
        self.nums[index] = val
        i = 1+index
        while i<len(self.tree):
            self.tree[i] += delta
            i += i&-i
            
    def prefixSum(self,i):
        s = 0
        i += 1
        while i>0:
            s += self.tree[i]
            i -= (i&-i)
        return s
    
    def sumRange(self,left,right):
        return self.prefixSum(right) - self.prefixSum(left-1)