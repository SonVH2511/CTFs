#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdbool.h>

#define N 42         // Số lượng byte trong FLAG_TO_TEST
#define MAX_CHAR 128 // Giới hạn ký tự cho FLAG (ASCII)

// Tham chiếu data_std
const uint8_t data_std[N] = {
    0x30, 0x78, 0x9d, 0x56, 0x92, 0xf2, 0xfe, 0x23, 0xbb, 0x2c,
    0x5d, 0x9e, 0x16, 0x40, 0x66, 0x53, 0xb6, 0xcb, 0x21, 0x7c,
    0x95, 0x29, 0x98, 0xce, 0x17, 0xb7, 0x14, 0x37, 0x88, 0xd9,
    0x49, 0x95, 0x26, 0x80, 0xb4, 0xbc, 0xe4, 0xc3, 0x0a, 0x96,
    0xc7, 0x53};

// Hàm xử lý dữ liệu mô phỏng logic trong FPGA
void EzLogic_top(uint8_t data_in, bool valid_in, bool reset, uint8_t *data_out, bool *valid_out)
{
    static uint8_t register_file[8] = {0}; // Thanh ghi lưu trữ giá trị
    static bool valid_flag = false;        // Cờ báo hiệu valid_out

    if (!reset)
    {
        memset(register_file, 0, sizeof(register_file)); // Xóa thanh ghi khi reset
        valid_flag = false;
        *data_out = 0;
        *valid_out = false;
        return;
    }

    if (valid_in)
    {
        // Mô phỏng xử lý XOR giữa dữ liệu đầu vào và các thanh ghi
        register_file[0] = data_in ^ register_file[1];
        register_file[1] = data_in ^ register_file[2];
        register_file[2] = data_in ^ register_file[3];
        register_file[3] = data_in ^ register_file[4];
        register_file[4] = data_in ^ register_file[5];
        register_file[5] = data_in ^ register_file[6];
        register_file[6] = data_in ^ register_file[7];
        register_file[7] = data_in ^ register_file[0];

        // Gán giá trị đầu ra từ thanh ghi cuối cùng
        *data_out = register_file[7];
        valid_flag = true;
    }
    else
    {
        valid_flag = false;
    }

    *valid_out = valid_flag;
}

// Chương trình chính
int main()
{
    char FLAG_TO_TEST[N + 1] = {0}; // Chuỗi flag cần tìm
    uint8_t data_in;
    uint8_t data_out;
    bool valid_in;
    bool valid_out;
    bool reset = true;

    uint8_t data_out_all[N] = {0};
    size_t counter = 0, counter2 = 0;
    bool found = false;

    // Thử từng tổ hợp ký tự của FLAG
    for (int i = 0; i < MAX_CHAR; i++)
    {
        for (int j = 0; j < MAX_CHAR; j++)
        {
            for (int k = 0; k < MAX_CHAR; k++)
            {
                // Tạo FLAG_TO_TEST từ tổ hợp ký tự
                snprintf(FLAG_TO_TEST, N, "%c%c%c", i, j, k);

                // Mô phỏng reset
                EzLogic_top(0, false, false, &data_out, &valid_out);

                counter2 = 0;
                for (counter = 0; counter < N; counter++)
                {
                    data_in = FLAG_TO_TEST[counter];
                }
            }
        }
    }
}
