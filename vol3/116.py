if __name__ == "__main__":
    N = 50
    M = [2, 3, 4]
    ans = 0
    for m in M:
        dp = [1] * (N + 1)
        for i in range(m, N + 1):
            dp[i] = dp[i - 1] + dp[i - m]
        ans += dp[N] - 1
    print ans
