#include <bits/stdc++.h>
using namespace std;

uint32_t Regs[16];
uint32_t Flag[40];

void Reg1()
{
    for (int a = 20; a <= 125; ++a)
    {
        for (int b = 20; b <= 125; ++b)
        {
            for (int c = 20; c <= 125; ++c)
            {
                for (int d = 20; d <= 125; ++d)
                {
                    Flag[4] = a;
                    Flag[5] = b;
                    Flag[6] = c;
                    Flag[7] = d;

                    Regs[1] = 0;

                    Regs[14] = Flag[4];
                    Regs[14] <<= 0;
                    Regs[1] |= Regs[14];

                    Regs[14] = Flag[5];
                    Regs[14] <<= 8;
                    Regs[1] |= Regs[14];

                    Regs[14] = Flag[6];
                    Regs[14] <<= 16;
                    Regs[1] |= Regs[14];

                    Regs[14] = Flag[7];
                    Regs[14] <<= 24;
                    Regs[1] |= Regs[14];

                    Regs[1] ^= 1176768057;
                    Regs[1] -= 2368952475;
                    Regs[1] ^= 2826144967;
                    Regs[1] += 1275301297;
                    Regs[1] -= 2955899422;
                    Regs[1] ^= 2241699318;
                    Regs[1] += 537794314;
                    Regs[1] += 473021534;
                    Regs[1] += 2381227371;
                    Regs[1] -= 3973380876;
                    Regs[1] -= 1728990628;
                    Regs[1] += 2974252696;
                    Regs[1] += 1912236055;
                    Regs[1] ^= 3620744853;
                    Regs[1] ^= 2628426447;
                    Regs[1] -= 486914414;
                    Regs[1] -= 1187047173;
                    // Regs[0] ^= 0xbed43826;

                    if (Regs[1] == 0x3084ff70)
                    {
                        cout << a << " " << b << " " << c << " " << d << endl;
                        return;
                    }
                }
            }
        }
    }
}

void Reg2()
{
    for (int a = 20; a <= 125; ++a)
    {
        for (int b = 20; b <= 125; ++b)
        {
            for (int c = 20; c <= 125; ++c)
            {
                for (int d = 20; d <= 125; ++d)
                {
                    Flag[8] = a;
                    Flag[9] = b;
                    Flag[10] = c;
                    Flag[11] = d;

                    Regs[2] = 0;

                    Regs[14] = Flag[8];
                    Regs[14] <<= 0;
                    Regs[2] |= Regs[14];

                    Regs[14] = Flag[9];
                    Regs[14] <<= 8;
                    Regs[2] |= Regs[14];

                    Regs[14] = Flag[10];
                    Regs[14] <<= 16;
                    Regs[2] |= Regs[14];

                    Regs[14] = Flag[11];
                    Regs[14] <<= 24;
                    Regs[2] |= Regs[14];

                    // Regs[2] ^= 3103274804;
                    // Regs[2] += 3320200805;
                    // Regs[2] += 3846589389;
                    // Regs[2] ^= 2724573159;
                    // Regs[2] -= 1483327425;
                    // Regs[2] ^= 1957985324;
                    // Regs[2] -= 1467602691;
                    // Regs[2] += 3142557962;
                    // Regs[2] ^= 2525769395;
                    // Regs[2] += 3681119483;
                    // Regs[2] -= 1041439413;
                    // Regs[2] -= 1042206298;
                    // Regs[2] -= 855860613; ^^^^^^^
                    // Regs[2] += 1865979270;
                    // Regs[2] += 2752636085;
                    // Regs[2] ^= 1389650363;
                    // Regs[2] -= 2721642985;
                    // Regs[2] += 3276518041;
                    // Regs[2] ^= 1965130376;

                    Regs[2] ^= 3103274804;
                    Regs[2] += 3320200805;
                    Regs[2] += 3846589389;
                    Regs[2] ^= 2724573159;
                    Regs[2] -= 1483327425;
                    Regs[2] ^= 1957985324;
                    Regs[2] -= 1467602691;
                    Regs[2] += 3142557962;
                    Regs[2] ^= 2525769395;
                    Regs[2] += 3681119483;
                    Regs[2] -= 1041439413;
                    Regs[2] -= 1042206298;
                    Regs[2] ^= 527001246;
                    Regs[2] -= 855860613;
                    Regs[2] += 1865979270;
                    Regs[2] += 2752636085;
                    Regs[2] ^= 1389650363;
                    Regs[2] -= 2721642985;
                    Regs[2] += 3276518041;
                    Regs[2] ^= 1965130376;

                    if (Regs[2] == 0x3e4f2492)
                    {
                        cout << a << " " << b << " " << c << " " << d << endl;
                        return;
                    }
                }
            }
        }
    }
}

void Reg3()
{
    for (int a = 20; a <= 125; ++a)
    {
        for (int b = 20; b <= 125; ++b)
        {
            for (int c = 20; c <= 125; ++c)
            {
                for (int d = 20; d <= 125; ++d)
                {
                    Flag[12] = a;
                    Flag[13] = b;
                    Flag[14] = c;
                    Flag[15] = d;

                    Regs[3] = 0;

                    Regs[14] = Flag[12];
                    Regs[14] <<= 0;
                    Regs[3] |= Regs[14];

                    Regs[14] = Flag[13];
                    Regs[14] <<= 8;
                    Regs[3] |= Regs[14];

                    Regs[14] = Flag[14];
                    Regs[14] <<= 16;
                    Regs[3] |= Regs[14];

                    Regs[14] = Flag[15];
                    Regs[14] <<= 24;
                    Regs[3] |= Regs[14];

                    Regs[3] ^= 3557111558;
                    Regs[3] ^= 3031574352;
                    Regs[3] -= 4226755821;
                    Regs[3] += 2624879637;
                    Regs[3] += 1381275708;
                    Regs[3] ^= 3310620882;
                    Regs[3] ^= 2475591380;
                    Regs[3] += 405408383;
                    Regs[3] ^= 2291319543;
                    Regs[3] += 4144538489;
                    Regs[3] ^= 3878256896;
                    Regs[3] -= 2243529248;
                    Regs[3] -= 561931268;
                    Regs[3] -= 3076955709;
                    Regs[3] += 2019584073;
                    Regs[3] += 1712479912;
                    Regs[3] ^= 2804447380;
                    Regs[3] -= 2957126100;
                    Regs[3] += 1368187437;
                    Regs[3] += 3586129298;

                    if (Regs[3] == 0x5ef76756)
                    {
                        cout << a << " " << b << " " << c << " " << d << endl;
                        return;
                    }
                }
            }
        }
    }
}

void Reg4()
{
    for (int a = 20; a <= 125; ++a)
    {
        for (int b = 20; b <= 125; ++b)
        {
            for (int c = 20; c <= 125; ++c)
            {
                for (int d = 20; d <= 125; ++d)
                {
                    Flag[16] = a;
                    Flag[17] = b;
                    Flag[18] = c;
                    Flag[19] = d;

                    Regs[4] = 0;

                    Regs[14] = Flag[16];
                    Regs[14] <<= 0;
                    Regs[4] |= Regs[14];

                    Regs[14] = Flag[17];
                    Regs[14] <<= 8;
                    Regs[4] |= Regs[14];

                    Regs[14] = Flag[18];
                    Regs[14] <<= 16;
                    Regs[4] |= Regs[14];

                    Regs[14] = Flag[19];
                    Regs[14] <<= 24;
                    Regs[4] |= Regs[14];

                    Regs[4] -= 1229526732;
                    Regs[4] -= 2759768797;
                    Regs[4] ^= 2112449396;
                    Regs[4] -= 1212917601;
                    Regs[4] ^= 1524771736;
                    Regs[4] += 3146530277;
                    Regs[4] ^= 2997906889;
                    Regs[4] += 4135691751;
                    Regs[4] += 1960868242;
                    Regs[4] -= 2775657353;
                    Regs[4] += 1451259226;
                    Regs[4] += 607382171;
                    Regs[4] -= 357643050;
                    Regs[4] ^= 2020402776;

                    if (Regs[4] == 0x5b2d0091)
                    {
                        cout << a << " " << b << " " << c << " " << d << endl;
                        return;
                    }
                }
            }
        }
    }
}

void Reg5()
{
    for (int a = 20; a <= 125; ++a)
    {
        for (int b = 20; b <= 125; ++b)
        {
            for (int c = 20; c <= 125; ++c)
            {
                for (int d = 20; d <= 125; ++d)
                {
                    Flag[20] = a;
                    Flag[21] = b;
                    Flag[22] = c;
                    Flag[23] = d;

                    Regs[5] = 0;

                    Regs[14] = Flag[20];
                    Regs[14] <<= 0;
                    Regs[5] |= Regs[14];

                    Regs[14] = Flag[21];
                    Regs[14] <<= 8;
                    Regs[5] |= Regs[14];

                    Regs[14] = Flag[22];
                    Regs[14] <<= 16;
                    Regs[5] |= Regs[14];

                    Regs[14] = Flag[23];
                    Regs[14] <<= 24;
                    Regs[5] |= Regs[14];

                    Regs[5] += 2408165152;
                    Regs[5] ^= 806913563;
                    Regs[5] -= 772591592;
                    Regs[5] ^= 2211018781;
                    Regs[5] -= 2523354879;
                    Regs[5] += 2549720391;
                    Regs[5] ^= 3908178996;
                    Regs[5] ^= 1299171929;
                    Regs[5] += 512513885;
                    Regs[5] -= 2617924552;
                    Regs[5] += 390960442;
                    Regs[5] += 1248271133;
                    Regs[5] += 2114382155;
                    Regs[5] -= 2078863299;
                    Regs[5] += 2857504053;
                    Regs[5] -= 4271947727;

                    if (Regs[5] == 0x4c33f178)
                    {
                        cout << a << " " << b << " " << c << " " << d << endl;
                        return;
                    }
                }
            }
        }
    }
}

void Reg6()
{
    for (int a = 20; a <= 125; ++a)
    {
        for (int b = 20; b <= 125; ++b)
        {
            for (int c = 20; c <= 125; ++c)
            {
                for (int d = 20; d <= 125; ++d)
                {
                    Flag[24] = a;
                    Flag[25] = b;
                    Flag[26] = c;
                    Flag[27] = d;

                    Regs[6] = 0;

                    Regs[14] = Flag[24];
                    Regs[14] <<= 0;
                    Regs[6] |= Regs[14];

                    Regs[14] = Flag[25];
                    Regs[14] <<= 8;
                    Regs[6] |= Regs[14];

                    Regs[14] = Flag[26];
                    Regs[14] <<= 16;
                    Regs[6] |= Regs[14];

                    Regs[14] = Flag[27];
                    Regs[14] <<= 24;
                    Regs[6] |= Regs[14];

                    Regs[6] ^= 2238126367;
                    Regs[6] ^= 1544827193;
                    Regs[6] += 4094800187;
                    Regs[6] ^= 3461906189;
                    Regs[6] -= 1812592759;
                    Regs[6] ^= 1506702473;
                    Regs[6] += 536175198;
                    Regs[6] ^= 1303821297;
                    Regs[6] += 715409343;
                    Regs[6] ^= 4094566992;
                    Regs[6] ^= 1890141105;
                    Regs[6] ^= 3143319360;

                    if (Regs[6] == 0x1ee6428f)
                    {
                        cout << a << " " << b << " " << c << " " << d << endl;
                        return;
                    }
                }
            }
        }
    }
}

void Reg7()
{
    for (int a = 20; a <= 125; ++a)
    {
        for (int b = 20; b <= 125; ++b)
        {
            for (int c = 20; c <= 125; ++c)
            {
                for (int d = 20; d <= 125; ++d)
                {
                    Flag[28] = a;
                    Flag[29] = b;
                    Flag[30] = c;
                    Flag[31] = d;

                    Regs[7] = 0;

                    Regs[14] = Flag[28];
                    Regs[14] <<= 0;
                    Regs[7] |= Regs[14];

                    Regs[14] = Flag[29];
                    Regs[14] <<= 8;
                    Regs[7] |= Regs[14];

                    Regs[14] = Flag[30];
                    Regs[14] <<= 16;
                    Regs[7] |= Regs[14];

                    Regs[14] = Flag[31];
                    Regs[14] <<= 24;
                    Regs[7] |= Regs[14];

                    Regs[7] -= 696930856;
                    Regs[7] ^= 926450200;
                    Regs[7] += 352056373;
                    Regs[7] -= 3857703071;
                    Regs[7] += 3212660135;
                    Regs[7] -= 3854876250;
                    Regs[7] += 3648688720;
                    Regs[7] ^= 2732629817;
                    Regs[7] -= 2285138643;
                    Regs[7] ^= 2255852466;
                    Regs[7] ^= 2537336944;
                    Regs[7] ^= 4257606405;

                    if (Regs[7] == 0x24015a4f)
                    {
                        cout << a << " " << b << " " << c << " " << d << endl;
                        return;
                    }
                }
            }
        }
    }
}

void Reg8()
{
    for (int a = 20; a <= 125; ++a)
    {
        for (int b = 20; b <= 125; ++b)
        {
            for (int c = 20; c <= 125; ++c)
            {
                for (int d = 20; d <= 125; ++d)
                {
                    Flag[32] = a;
                    Flag[33] = b;
                    Flag[34] = c;
                    Flag[35] = d;

                    Regs[8] = 0;

                    Regs[14] = Flag[32];
                    Regs[14] <<= 0;
                    Regs[8] |= Regs[14];

                    Regs[14] = Flag[33];
                    Regs[14] <<= 8;
                    Regs[8] |= Regs[14];

                    Regs[14] = Flag[34];
                    Regs[14] <<= 16;
                    Regs[8] |= Regs[14];

                    Regs[14] = Flag[35];
                    Regs[14] <<= 24;
                    Regs[8] |= Regs[14];

                    Regs[8] -= 3703184638;
                    Regs[8] -= 2165056562;
                    Regs[8] += 2217220568;
                    Regs[8] += 2088084496;
                    Regs[8] += 443074220;
                    Regs[8] -= 1298336973;
                    Regs[8] += 822378456;
                    Regs[8] += 2154711985;
                    Regs[8] -= 430757325;
                    Regs[8] ^= 2521672196;

                    if (Regs[8] == 0xaf4bf68d)
                    {
                        cout << a << " " << b << " " << c << " " << d << endl;
                        return;
                    }
                }
            }
        }
    }
}

void Reg9()
{
    for (int a = 20; a <= 125; ++a)
    {
        for (int b = 20; b <= 125; ++b)
        {
            for (int c = 20; c <= 125; ++c)
            {
                for (int d = 20; d <= 125; ++d)
                {
                    Flag[36] = a;
                    Flag[37] = b;
                    Flag[38] = c;
                    Flag[39] = d;

                    Regs[9] = 0;

                    Regs[14] = Flag[36];
                    Regs[14] <<= 0;
                    Regs[9] |= Regs[14];

                    Regs[14] = Flag[37];
                    Regs[14] <<= 8;
                    Regs[9] |= Regs[14];

                    Regs[14] = Flag[38];
                    Regs[14] <<= 16;
                    Regs[9] |= Regs[14];

                    Regs[14] = Flag[39];
                    Regs[14] <<= 24;
                    Regs[9] |= Regs[14];

                    Regs[9] -= 532704100;
                    Regs[9] -= 2519542932;
                    Regs[9] ^= 2451309277;
                    Regs[9] ^= 3957445476;
                    Regs[9] += 2583554449;
                    Regs[9] -= 1149665327;
                    Regs[9] += 3053959226;
                    Regs[9] += 3693780276;
                    Regs[9] ^= 609918789;
                    Regs[9] ^= 2778221635;
                    Regs[9] += 3133754553;
                    Regs[9] += 3961507338;
                    Regs[9] ^= 1829237263;
                    Regs[9] ^= 2472519933;
                    Regs[9] += 4061630846;
                    Regs[9] -= 1181684786;
                    Regs[9] -= 390349075;
                    Regs[9] += 2883917626;
                    Regs[9] -= 3733394420;
                    Regs[9] ^= 3895283827;
                    Regs[9] ^= 2257053750;
                    Regs[9] -= 2770821931;
                    Regs[9] ^= 477834410;

                    if (Regs[9] == 0x4a848e50)
                    {
                        cout << a << " " << b << " " << c << " " << d << endl;
                        return;
                    }
                }
            }
        }
    }
}

int main()
{
    Flag[0] = (int)'H';
    Flag[1] = (int)'T';
    Flag[2] = (int)'B';
    Flag[3] = (int)'{';

    Reg1();
    Reg2();
    Reg3();
    Reg4();
    Reg5();
    Reg6();
    Reg7();
    Reg8();
    Reg9();

    for (int i = 0; i < 40; ++i)
        cout << (char)Flag[i];
}

// HTB{
// m4n_
// 1_l0  _&t2
// v4_c
// XX_T
// eMpl
// 4t35
// _9fb
// 60c1
// 7b0}
// HTB{m4n__&t2v4_cXX_TeMpl4t35_9fb60c17b0}
// HTB{m4n_1_l0v4_cXX_TeMpl4t35_9fb60c17b0}
