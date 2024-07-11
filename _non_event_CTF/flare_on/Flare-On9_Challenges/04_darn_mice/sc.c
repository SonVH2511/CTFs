#include <stdio.h>
void tmp()
{
    return;
}

int main()
{
    __asm__(
        "call 0x3c");
    return 0;
}