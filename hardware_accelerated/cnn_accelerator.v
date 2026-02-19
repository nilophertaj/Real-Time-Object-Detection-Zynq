module cnn_accelerator (
    input clk,
    input rst,
    input [7:0] pixel_in,
    output reg [15:0] conv_out
);

always @(posedge clk)
begin
    if (rst)
        conv_out <= 0;
    else
        conv_out <= pixel_in * 3;
end

endmodule
