module Pe_Shift (
    // 控制输入信号：来自 SelSplit 的驱动脉冲
    input               i_drive,          // 驱动输入脉冲（由控制链提供）
    input   [63:0]      i_data,           // 输入数据：{32bit控制字段, 32bit原始数据}         
    output              o_free,           // 操作完成后的释放信号

    output              o_drive,          // 输出驱动脉冲
    output  [63:0]      o_data,           // 输出数据：{32'b0, 32bit移位结果}
    input               i_free,           // 下游释放信号

    input               rst               // 复位信号
);

    // 拆分输入数据
    wire [31:0] ctrl     = i_data[63:32];   // 高32位为控制信息
    wire [31:0] data_in  = i_data[31:0];    // 低32位为输入数据

    //============================
    // 控制字段说明（ctrl[31:0]）：
    // ctrl[1:0]   : mode，移位模式选择
    //     00 => 逻辑左移（LSL）
    //     01 => 逻辑右移（LSR）
    //     10 => 算术右移（ASR）
    // ctrl[6:2]   : shift_amount，移位位数（0~31）
    // ctrl[31:7]  : 保留，未来可拓展用途
    //============================

    wire [1:0] mode         = ctrl[1:0];     // 模式字段
    wire [4:0] shift_amount = ctrl[6:2];     // 取出移位位数（5位支持0~31）

    reg  [31:0] shift_result;

    // 根据模式执行不同的移位操作
    always @(*) begin
        case (mode)
            2'b00: shift_result = data_in << shift_amount;                      // 逻辑左移
            2'b01: shift_result = data_in >> shift_amount;                      // 逻辑右移
            2'b10: shift_result = $signed(data_in) >>> shift_amount;            // 算术右移
            default: shift_result = 32'b0;                                       // 默认输出0
        endcase
    end

    // 输出格式：高32位清零，低32位为结果
    assign o_data = {32'b0, shift_result};

    delay_n #(.N(1)) delay_drive(.inR(i_drive),.outR(o_drive),.rst(rst));
    assign o_free  = i_free;

endmodule
