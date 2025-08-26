`timescale 1ns/1ps

module tb_pe_round;

    reg         i_drive;
    reg  [63:0] i_data;
    wire        o_free;
    wire        o_drive;
    wire [63:0] o_data;
    reg         i_free;
    reg         rst;

    // 实例化待测模块
    Pe_Round dut (
        .i_drive(i_drive),
        .i_data(i_data),
        .o_free(o_free),
        .o_drive(o_drive),
        .o_data(o_data),
        .i_free(i_free),
        .rst(rst)
    );

    integer case_file, status, result_file;
    reg [1023:0] line;
    reg [63:0] case_i_data;
    reg [63:0] expect_o_data;
    integer lineno;
    reg file_done;

    initial begin
        $display("==== PE_ROUND TB START ====");
        rst = 1;
        i_drive = 0;
        i_data = 0;
        i_free = 1;
        #10 rst = 0;

        // 打开用例文件
        case_file = $fopen("pe_round_cases.txt", "r");
        if (case_file == 0) begin
            $display("ERROR: Cannot open pe_round_cases.txt");
            $finish;
        end

        // 打开结果文件
        result_file = $fopen("result.txt", "w");
        if (result_file == 0) begin
            $display("ERROR: Cannot open result.txt");
            $finish;
        end

        lineno = 0;
        file_done = 0;

        while (!file_done && !$feof(case_file)) begin
            status = $fgets(line, case_file);
            if (status == 0) begin
                file_done = 1;
            end else begin
                lineno = lineno + 1;
                // 解析输入和期望输出
                status = $sscanf(line, "%h %h", case_i_data, expect_o_data);
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
                    if (o_data !== expect_o_data) begin
                        $display("FAIL @ line %0d: i_data=%h, expect=%h, got=%h", lineno, i_data, expect_o_data, o_data);
                        $fwrite(result_file, "FAIL @ line %0d: i_data=%h, expect=%h, got=%h\n", lineno, i_data, expect_o_data, o_data);
                    end else begin
                        $display("PASS @ line %0d: i_data=%h, result=%h", lineno, i_data, o_data);
                        $fwrite(result_file, "PASS @ line %0d: i_data=%h, result=%h\n", lineno, i_data, o_data);
                    end
                    #10;
                end
            end
        end

        $fclose(case_file);
        $fclose(result_file);
        $display("==== PE_ROUND TB END ====");
        $finish;
    end

endmodule