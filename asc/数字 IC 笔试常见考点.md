## 数字 IC 笔试常见考点

一般会覆盖这几块：

1. **数字电路与逻辑设计**
   - 组合逻辑、时序逻辑、有限状态机（FSM）
   - 时序约束（setup/hold time）
   - 时钟域跨越 (CDC)、亚稳态
   - pipeline、延迟计算
2. **CMOS 电路与 VLSI 基础**
   - CMOS 逻辑门电路，功耗、延迟公式
   - 版图相关（IR drop、时钟树、EM）
   - 工艺缩放、PVT 角、yield
3. **Verilog/SystemVerilog 基础**
   - always_comb / always_ff 区别
   - 阻塞/非阻塞赋值
   - testbench 基础、随机约束、覆盖率
4. **计算机体系结构 / 微架构**
   - cache、流水线、乱序执行、hazard
   - 多核一致性协议（MESI 等）
   - 总线/NoC 基础概念
5. **编程题 (类似 LeetCode 简单中等题)**
   - 字符串/数组/二分查找/位运算
   - 很多公司会要求 C/C++，有的用 Python
6. **概率/逻辑推理/脑筋急转弯**
   - 有些公司考“智力题”来测试思维方式

------

## 📚 刷题与学习资源

你说的“像 LeetCode 的刷题网站”确实有一些，但要分方向：

### 🔹 Verilog / 数字电路

- **EDA Playground** (在线写 Verilog/VHDL + 仿真)
   👉 https://www.edaplayground.com/
   可以写小题目，比如 FIFO、加法器、FSM。
- GitHub 上有很多 “Verilog practice problems”，比如
   👉 https://github.com/beyondacm/Verilog-Practice

### 🔹 计算机体系结构

- CMU 15-213 / 18-447 的实验题（流水线、cache、branch predictor 实验）。
- OpenCores 上的开源 CPU/NoC 设计，可以读源码练习。

### 🔹 编程刷题（笔试常用）

- **LeetCode**（数组/位运算/动态规划），重点练 C/C++。
- **LintCode、牛客网**（国内 IC 公司常用笔试题库，尤其华为、寒武纪、平头哥）
- **CS Academy / HackerRank**（算法基础 + bit manipulation）。

### 🔹 数字 IC 面试/笔试真题

- 《数字 IC 面试宝典》电子书（网上常见 PDF）
- VLSI Interview Questions 网站
   👉 https://www.vlsijobs.com/vlsi-interview-questions