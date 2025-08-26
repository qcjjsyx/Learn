import random

def round_frac(frac, mode, sign):
    # frac: 10位
    # mode: 2位
    # sign: 1位
    if mode == 0:  # Round to nearest even
        # 仅当最低两位都为1时进位
        if (frac & 0b11) == 0b11:
            return (frac + 1) & 0x3FF
        else:
            return frac
    elif mode == 1:  # Toward zero
        return frac
    elif mode == 2:  # Toward +inf
        if sign == 0 and frac != 0:
            return (frac + 1) & 0x3FF
        else:
            return frac
    elif mode == 3:  # Toward -inf
        if sign == 1 and frac != 0:
            return (frac + 1) & 0x3FF
        else:
            return frac
    else:
        return frac

def gen_case():
    # 随机生成ctl0, fp0, ctl1, fp1
    mode0 = random.randint(0, 3)
    mode1 = random.randint(0, 3)
    sign0 = random.randint(0, 1)
    sign1 = random.randint(0, 1)
    exp0 = random.randint(0, 31)
    exp1 = random.randint(0, 31)
    frac0 = random.randint(0, 1023)
    frac1 = random.randint(0, 1023)

    ctl0 = (mode0 & 0x3) | (random.randint(0, 0x3FFF) << 2)
    ctl1 = (mode1 & 0x3) | (random.randint(0, 0x3FFF) << 2)
    fp0 = ((sign0 & 0x1) << 15) | ((exp0 & 0x1F) << 10) | (frac0 & 0x3FF)
    fp1 = ((sign1 & 0x1) << 15) | ((exp1 & 0x1F) << 10) | (frac1 & 0x3FF)

    # 计算舍入结果
    frac0_rnd = round_frac(frac0, mode0, sign0)
    frac1_rnd = round_frac(frac1, mode1, sign1)
    fp0_out = ((sign0 & 0x1) << 15) | ((exp0 & 0x1F) << 10) | (frac0_rnd & 0x3FF)
    fp1_out = ((sign1 & 0x1) << 15) | ((exp1 & 0x1F) << 10) | (frac1_rnd & 0x3FF)

    # 输入数据
    i_data = (ctl1 << 48) | (fp1 << 32) | (ctl0 << 16) | fp0
    # 期望输出
    o_data = (ctl1 << 48) | (fp1_out << 32) | (ctl0 << 16) | fp0_out

    # 格式：i_data ctl1 fp1 ctl0 fp0 | o_data fp1_out fp0_out
    return f"{i_data:016x} {ctl1:04x} {fp1:04x} {ctl0:04x} {fp0:04x} {o_data:016x} {fp1_out:04x} {fp0_out:04x}"

def main():
    with open("pe_round_cases.txt", "w") as f:
        for _ in range(200):
            f.write(gen_case() + "\n")

if __name__ == "__main__":
    main()