
# print(e-s)

import idaapi
import idc
import ida_bytes


def read_memory(address, length):

    # Read the data from the specified address
    data = ida_bytes.get_bytes(address, length)
    if data is None:
        print(f"Failed to read data from address 0x{address:08X}")
    return data


s = 0x00000000000020E0
e = 0x00000000000214DF

print(read_memory(s, e-s+1))
