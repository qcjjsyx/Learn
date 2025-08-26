import random

def gen_case(mode, shift_amount, data_in):
    ctrl = (mode & 0x3) | ((shift_amount & 0x1F) << 2)
    ctrl = ctrl & 0x7F  # 只用低7位，其他位保留为0
    ctrl = ctrl  # 高位保留为0
    i_data = ((ctrl << 32) | (data_in & 0xFFFFFFFF))
    # 计算预期结果
    if mode == 0:  # LSL
        result = (data_in << shift_amount) & 0xFFFFFFFF
    elif mode == 1:  # LSR
        result = (data_in >> shift_amount) & 0xFFFFFFFF
    elif mode == 2:  # ASR
        # 需要符号扩展
        signed = data_in if data_in < 0x80000000 else data_in - 0x100000000
        result = (signed >> shift_amount) & 0xFFFFFFFF
    else:
        result = 0
    return f"{i_data:016x} {mode} {shift_amount} {data_in:08x} {result:08x}"

def main():
    cases = []
    # 随机补充一些用例
    for _ in range(100):
        mode = random.randint(0,2)
        shift_amount = random.randint(0,31)
        data_in = random.randint(0,0xFFFFFFFF)
        cases.append(gen_case(mode, shift_amount, data_in))
    # 保存到文件
    with open("pe_shift_cases.txt", "w") as f:
        for line in cases:
            f.write(line + "\n")

if __name__ == "__main__":
    main()