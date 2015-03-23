if __name__ == "__main__":
    L = 10 ** 5
    p = [0] * L
    prime = []
    for i in range(2, L):
        if p[i] == 0:
            for j in range(2 * i, L, i):
                p[j] = 1
            prime.append(i)
    ans = 0
    for i in prime:
        if pow(10, 10 ** 20, 9 * i) != 1:
            ans += i
    print ans
        
