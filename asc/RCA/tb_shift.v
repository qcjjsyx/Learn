`timescale 1ns/1ps

module tb_shift;

    reg         i_drive;
    reg  [63:0] i_data;
    wire        o_free;
    wire        o_drive;
    wire [63:0] o_data;
    reg         i_free;
    reg         rst;

    // 实例化待测模块
    Pe_Shift dut (
        .i_drive(i_drive),
        .i_data(i_data),
        .o_free(o_free),
        .o_drive(o_drive),
        .o_data(o_data),
        .i_free(i_free),
        .rst(rst)
    );

    // 用例相关变量
    integer case_file, status, result_file;
    reg [255:0] line;
    reg [63:0] case_i_data;
    reg [31:0] expect_result;
    integer    lineno;
    reg        file_done;  // 添加文件结束标志

    initial begin
        $display("==== PE_SHIFT TB START ====");
        rst = 1;
        i_drive = 0;
        i_data = 0;
        i_free = 1;
        #10 rst = 0;

        // 打开用例文件
        case_file = $fopen("/team/asc/lu.yihua/Reconfigurable CA/fpga_proj/hy/tb_shift/test_shift.txt", "r");
        if (case_file == 0) begin
            $display("ERROR: Cannot open test_shift.txt");
            $finish;
        end

        // 打开结果文件
        result_file = $fopen("/team/asc/lu.yihua/Reconfigurable CA/fpga_proj/hy/tb_shift/result.txt", "w");
        if (result_file == 0) begin
            $display("ERROR: Cannot open pe_shift_tb_result.txt");
            $finish;
        end

        lineno = 0;
        file_done = 0;
     
        // 使用while循环替代标签
        while (!file_done && !$feof(case_file))  begin
            status = $fgets(line, case_file);
            if (status == 0) begin
                // 文件结束，设置标志并退出
                file_done = 1;
            end
            else begin
                lineno = lineno + 1;

                // 解析输入数据和期望结果
                status = $sscanf(line, "%h %*d %*d %*h %h", case_i_data, expect_result);
                if (status < 2) begin
                    $display("Line %0d format error: %s", lineno, line);
                    $fwrite(result_file, "ERROR: Line %0d format error\n", lineno);
                end else begin
                    // 驱动输入
                    i_data = case_i_data;
                    i_drive = 1;
                    #10;
                    i_drive = 0;
                    #10;

                    // 检查结果
                    if (o_data[31:0] !== expect_result) begin
                        $display("FAIL @ line %0d: i_data=%h, expect=%h, got=%h", lineno, i_data, expect_result, o_data[31:0]);
                        $fwrite(result_file, "FAIL @ line %0d: i_data=%h, expect=%h, got=%h\n", lineno, i_data, expect_result, o_data[31:0]);
                    end else begin
                        $display("PASS @ line %0d: i_data=%h, result=%h", lineno, i_data, o_data[31:0]);
                        $fwrite(result_file, "PASS @ line %0d: i_data=%h, result=%h\n", lineno, i_data, o_data[31:0]);
                    end
                    #10;
                end
            end
        end
        
        $fclose(case_file);
        $fclose(result_file);
        $display("==== PE_SHIFT TB END ====");
        $finish;
    end

endmodule