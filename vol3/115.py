if __name__ == "__main__":
    N = 1000
    M = 50
    dp = [1] * (N + 1)
    for i in range(M, N + 1):
        dp[i] = dp[i - 1]
        for j in range(M, i):
            dp[i] += dp[i - j - 1]
        dp[i] += 1
        if dp[i] > 1e6:
            print i
            break
