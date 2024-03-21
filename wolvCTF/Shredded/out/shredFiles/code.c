#include <stdio.h>
#include <string.h>
int main()
{
    char flag[] = "REDACTED";

    char inter[51];
    int len = strlen(flag);
    for (int i = 0; i < len; i++)
    {
        inter[i] = flag[i];
    }
    for (int i = len; i < 50; i++)
    {

        inter[i] = inter[(i * 2) % len];
    }
    inter[50] = '\0';
    char a;
    for (int i = 0; i < 50; i++)
    {

        a = inter[i];
        inter[i] = inter[((i + 7) * 15) % 50];

        inter[((i + 7) * 15) % 50] = a;
    }
    for (int i = 0; i < 50; i++)
    {

        a = inter[i];
        inter[i] = inter[((i + 3) * 7) % 50];

        inter[((i + 3) * 7) % 50] = a;
    }
    for (int i = 0; i < 50; i++)
    {

        inter[i] = inter[i] ^ 0x20;

        inter[i] = inter[i] ^ 0x5;
    }
    for (int i = 0; i < 50; i++)
    {
        a = inter[i];
        inter[i] = inter[((i + 83) * 12) % 50];

        inter[((i + 83) * 12) % 50] = a;
    }
    for (int i = 0; i < 50; i++)
    {
        printf("\\x%X", inter[i]);
    }

    return 0;
}
