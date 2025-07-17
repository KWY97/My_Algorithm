def gcd(n1, n2):
    temp = n1 % n2

    while temp != 0:
        n1 = n2
        n2 = temp
        temp = n1 % n2

    return n2


c1, p1 = map(int, input().split())
c2, p2 = map(int, input().split())

cc = (c1 * p2) + (c2 * p1)
cp = p1 * p2

my_gcd = gcd(cc, cp)

ans_c = cc // my_gcd
ans_p = cp // my_gcd

print(ans_c, ans_p)