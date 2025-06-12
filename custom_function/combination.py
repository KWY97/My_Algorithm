def my_combination(n, m):
    def my_factorial(num):
        result = 1
        for i in range(2, num+1):
            result *= i
        return result
    if m > n-m:
        m = n-m

    a = 1
    b = my_factorial(m)

    for i in range(n, n-m, -1):
        a *= i
    return a // b