if __name__ == "__main__":
    doubles = [2 * x for x in range(1, 21)]
    doubles.append(50)
    singles = [x for x in range(1, 21)]
    singles.append(25)
    triples = [3 * x for x in range(1, 21)]
    scores = singles + doubles + triples
    scores.sort()

    limit = 100
    ans = 0
    for i in doubles:
        if i < limit:
            ans += 1
        else:
            break
    for i in scores:
        for j in doubles:
            if i + j < limit:
                ans += 1

    length = len(scores)
    for i in range(length):
        for j in range(i, length):
            if scores[i] + scores[j] >= limit:
                break
            for k in doubles:
                if scores[i] + scores[j] + k >= limit:
                    break
                ans += 1

    print ans
