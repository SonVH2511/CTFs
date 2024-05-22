#include <stdio.h>
#include <stdlib.h>

long long ans[] = {0x244B28BE, 0x0AF77805, 0x110DFC17, 0x7AFC3A1, 0x6AFEC533, 0x4ED659A2, 0x33C5D4B0,
                   0x286582B8, 0x43383720, 0x55A14FC, 0x19195F9F, 0x43383720, 0x63149380, 0x615AB299,
                   0x6AFEC533, 0x6C6FCFB8, 0x43383720, 0x0F3DA237, 0x6AFEC533, 0x615AB299, 0x286582B8,
                   0x55A14FC, 0x3AE44994, 0x6D7DFE9, 0x4ED659A2, 0x0CCD4ACD, 0x57D8ED64, 0x615AB299, 0x22E9BC2A};

int main()
{
    for (int j = 0; j <= 28; ++j)
        for (int i = 0; i < 0xff; ++i)
        {
            srand(i);
            if (rand() == ans[j])
            {
                printf("%c", i);
                break;
            }
        }
}