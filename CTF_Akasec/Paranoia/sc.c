#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()
{
    int flag[36];
    // int flag[] = {157, 97, 139, 62, 224, 28, 232, 120, 137, 76, 238, 96, 108, 78, 189, 66, 136, 193, 119, 198, 69, 130, 234, 107, 39, 68, 206, 81, 114, 250, 180, 118, 160, 179, 19, 101};
    for (int i = 0; i < 36; ++i)
    {
        scanf("%d", &flag[i]);
    }
    unsigned int v3 = time(0LL);
    srand(v3);
    for (int i = 0LL; i <= 35; ++i)
    {
        int v4 = flag[i];
        int v5 = rand();
        printf("%c", v4 ^ (v5 & 0xff));
    }
    putchar(10);
    return 0;
}
// akasec{n0t_t00_m4ny_br41nc3lls_l3ft}