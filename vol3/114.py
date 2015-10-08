if __name__ == "__main__":
    N = 50
    dp = [1] * (N + 1)
    for i in range(3, N + 1):
        dp[i] = dp[i - 1]
        for j in range(3, i):
            dp[i] += dp[i - j - 1]
        dp[i] += 1
    print dp[50]
