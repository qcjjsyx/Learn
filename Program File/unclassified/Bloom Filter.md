Bloom Filter是一种概率性数据结构，用于快速判断一个元素是否可能存在于一个集合中。它的特点是：

- **空间效率高**：使用很少的存储空间
- **查询速度快**：O(1)时间复杂度
- **概率性判断**：可能产生假正例（说存在但实际不存在），但不会产生假负例（说不存在但实际存在）
算法：
1. 首先需要k个hash函数，每个函数可以把key散列成为1个整数  
2. 初始化时，需要一个长度为n比特的数组，每个比特位初始化为0  
3. 某个key加入集合时，用k个hash函数计算出k个散列值，并把数组中对应的比特位置为1  
4. 判断某个key是否在集合时，用k个hash函数计算出k个散列值，并查询数组中对应的比特位，如果所有的比特位都是1，认为在集合中。

优点：不需要存储key，节省空间
缺点：  
1. 算法判断key在集合中时，有一定的概率key其实不在集合中  
2. 无法删除
示例代码
```
import hashlib

import math

import bitarray

  

class BloomFilter:

    def __init__(self, capacity, error_rate=0.01):

        self.capacity = capacity

        self.error_rate = error_rate

        self.size = self._get_size(capacity, error_rate)

        self.hash_count = self._get_hash_count(self.size, capacity)

        self.bit_array = bitarray.bitarray(self.size)

        self.bit_array.setall(0)

  

    def _get_size(self, n, p):

        m = -(n * math.log(p)) / (math.log(2) ** 2)

        return int(m)

  

    def _get_hash_count(self, m, n):

        k = (m / n) * math.log(2)

        return int(k)

  

    def _hashes(self, item):

        item = item.encode('utf-8')

        hash1 = int(hashlib.md5(item).hexdigest(), 16)

        hash2 = int(hashlib.sha1(item).hexdigest(), 16)

        for i in range(self.hash_count):

            yield (hash1 + i * hash2) % self.size

  

    def add(self, item):

        for idx in self._hashes(item):

            self.bit_array[idx] = 1

  

    def __contains__(self, item):

        return all(self.bit_array[idx] for idx in self._hashes(item))

  

# 示例用法

if __name__ == "__main__":

    bf = BloomFilter(1000, 0.01)

    bf.add("hello")

    bf.add("world")

    print("hello" in bf)  # True

    print("python" in bf) # 可能为False（也可能为True，误判概率很小）
```

### False Positive的概率推导
对于长度为m的bitarray，经过哈希函数，将某一位置为1的概率为$\frac{1}{m}$,那么经过k次哈希以后，没有被置为1的概率是$(1-\frac{1}{m})^k$。插入了n个元素以后，仍然为0的概率是$(1-\frac{1}{m})^{kn}$。对于一个字符check，经过k次哈希，发现每一位都被置为了1的概率是P(假阳率)
$$(1-(1-\frac{1}{m})^{kn})^k \approx (1-e^{-kn/m})^k$$
### Hash Function K数目的确定
$$f(k) = (1-e^{-kn/m})^k$$
令$a=e^{n/m}$，对k进行求导，我们可以得到$\frac{f'(k)}{f(k)} = \ln(1-a^{-k})+\frac{a^{-k}k\ln a}{1-a^{-k}}$
求得极值点，知道$k = \frac{m}{n}\ln2$

### BitArray 的大小m
根据上述求得的k的式子以及P，联立可得
$$P = \frac{1}{2}^{\frac{m}{n}\ln2}$$
 $$ m = -\frac{n\ln P}{(\ln2)^2}$$
 

