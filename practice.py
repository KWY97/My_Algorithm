def fibo(n):
    if n <= 2:
        return dp[n]

    if n not in dp:
        dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]

dp = {
    1: 1,
    2: 1
}

print(fibo(int(input())))