if __name__ == "__main__":
    N = 50
    M = [2, 3, 4]
    dp = [1] * (N + 1)
    for i in range(1, N + 1):    
        dp[i] = dp[i - 1]
        for m in M:
            if i >= m:
                dp[i] += dp[i - m]
    print dp[N]
