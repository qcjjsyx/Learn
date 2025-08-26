module Pe_Round (
    input               i_drive,          
    input   [63:0]      i_data,           // 输入数据格式：{ctl1, fp1, ctl0, fp0}
    output              o_free,           
    output              o_drive,         
    output  [63:0]      o_data,           // 输出数据格式：{ctl1, fp1_rounded, ctl0, fp0_rounded}
    input               i_free,           
    input               rst               
);

    // 拆解输入
    wire [15:0] ctl0 = i_data[15:0];
    wire [15:0] fp0  = i_data[31:16];
    wire [15:0] ctl1 = i_data[47:32];
    wire [15:0] fp1  = i_data[63:48];

    wire [1:0] mode0 = ctl0[1:0];
    wire [1:0] mode1 = ctl1[1:0];

    wire sign0 = fp0[15];
    wire [4:0] exp0 = fp0[14:10];
    wire [9:0] frac0 = fp0[9:0];

    wire sign1 = fp1[15];
    wire [4:0] exp1 = fp1[14:10];
    wire [9:0] frac1 = fp1[9:0];

    reg [9:0] frac0_rnd, frac1_rnd;

    // 组合逻辑实现 rounding
    always @(*) begin
        // ---- fp0 ----
        case (mode0)
            2'b00: begin  // Round to nearest even
                if (frac0[0] == 1'b1 && frac0[1] == 1'b1)
                    frac0_rnd = frac0 + 1'b1;
                else
                    frac0_rnd = frac0;
            end
            2'b01: begin  // Toward zero (truncate)
                frac0_rnd = frac0;
            end
            2'b10: begin  // Toward +inf
                if (sign0 == 1'b0 && frac0 != 0)
                    frac0_rnd = frac0 + 1'b1;
                else
                    frac0_rnd = frac0;
            end
            2'b11: begin  // Toward -inf
                if (sign0 == 1'b1 && frac0 != 0)
                    frac0_rnd = frac0 + 1'b1;
                else
                    frac0_rnd = frac0;
            end
            default: frac0_rnd = frac0;
        endcase

        // ---- fp1 ----
        case (mode1)
            2'b00: begin
                if (frac1[0] == 1'b1 && frac1[1] == 1'b1)
                    frac1_rnd = frac1 + 1'b1;
                else
                    frac1_rnd = frac1;
            end
            2'b01: frac1_rnd = frac1;
            2'b10: begin
                if (sign1 == 1'b0 && frac1 != 0)
                    frac1_rnd = frac1 + 1'b1;
                else
                    frac1_rnd = frac1;
            end
            2'b11: begin
                if (sign1 == 1'b1 && frac1 != 0)
                    frac1_rnd = frac1 + 1'b1;
                else
                    frac1_rnd = frac1;
            end
            default: frac1_rnd = frac1;
        endcase
    end

    // 组装输出
    wire [15:0] fp0_out = {sign0, exp0, frac0_rnd};
    wire [15:0] fp1_out = {sign1, exp1, frac1_rnd};
    assign o_data = {ctl1, fp1_out, ctl0, fp0_out};

    delay_n #(.N(1)) delay_drive(.inR(i_drive),.outR(o_drive),.rst(rst));
    assign o_free  = i_free;

endmodule