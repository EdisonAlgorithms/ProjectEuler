if __name__ == "__main__":
    L = 10 ** 7
    dic = {1:1, 89:89}
    ans = 0
    for i in range(1, L):
        s = i
        while s not in dic:
            s = sum((ord(x) - ord('0')) ** 2 for x in str(s))
        dic[i] = dic[s]
        if dic[i] == 89:
            ans +=1
        print i
    print ans
