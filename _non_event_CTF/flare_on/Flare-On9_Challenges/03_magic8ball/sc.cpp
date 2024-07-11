#include <bits/stdc++.h>
using namespace std;

mt19937 rd(chrono::steady_clock::now().time_since_epoch().count());

long long Rand(long long l, long long h)
{
    return l + rd() % (h - l + 1);
}

long long mul(long long a, long long b, long long mod)
{
    long long res = 0;
    while (b)
    {
        if (b & 1)
            res = (res + a) % mod;
        a = (a + a) % mod;
        b /= 2;
    }
    return res;
}

long long Pow(long long a, long long b, long long mod)
{
    long long res = 1;
    while (b)
    {
        if (b & 1)
            res = mul(res, a, mod);
        a = mul(a, a, mod);
        b /= 2;
    }
    return res;
}

bool isPrime(long long n)
{
    if (n < 2)
        return false;
    if (n == 2)
        return true;

    for (int i = 1; i <= 100; i++)
    {
        long long x = Rand(2, n - 1);
        if (Pow(x, n - 1, n) != 1)
            return false;
    }
    return true;
}

int main()
{
    long long a, dec, inc, cnt = 0;
    cin >> a;
    unsigned long long pr = 0;
    while (true)
    {
        dec = a - cnt;
        inc = a + cnt;
        if (isPrime(dec))
        {
            inc = -1;
            break;
        }
        if (isPrime(inc))
        {
            dec = -1;
            break;
        }
        cnt += 1;
    }
    long long ans = (inc != -1) ? inc : dec;
    // cout << ans << endl
    //      << Pow(a, ans, 123456);
    cout << ans << endl
         << (a * ans) % 123456;

    // cout << Pow(a, b, n) << endl;

    return 0;
}