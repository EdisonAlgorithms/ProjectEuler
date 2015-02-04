if __name__ == "__main__":
    LIMIT = 100000
    k = 10000
    
    E = [[1, n] for n in range(LIMIT)]
    for i in range(2, LIMIT):
        if E[i][0] == 1:
            for j in range(i, LIMIT, i):
                E[j][0] *= i

    print sorted(E)[k - 1][1]
