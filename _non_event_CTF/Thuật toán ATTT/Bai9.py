import math
def sangSNT(n):
    prime = [True] * (n+1)
    prime[0] = prime[1] = False
    for i in range(2,int(math.sqrt(n)+1)):
        if (prime[i] == True):
            for j in range(i*i, n+1, i):
                prime[j] = False
    return [i for i in range(2,n+1) if prime[i] == True]

n = int(input("Nhap n: "))
dem = len(sangSNT(n))
print("So SNT nho hon hoac bang {} la: {}".format(n, dem))