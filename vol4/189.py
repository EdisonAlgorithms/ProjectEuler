import itertools

N = 8
M = 3
colors = range(M)

def flip1(arr):
    ok_colors = []
    for color in arr:
        ok_colors.append(filter(lambda c: c != color, colors))
    return itertools.product(*ok_colors)

def flip2(arr):
    ok_colors = [filter(lambda c: c != arr[0], colors)]
    for i in range(len(arr) - 1):
        ok_colors.append(filter(lambda c: c != arr[i] and c != arr[i + 1], colors))
    ok_colors.append(filter(lambda c: c != arr[-1], colors))
    return itertools.product(*ok_colors)

if __name__ == "__main__":
    dp = [{(i, ): 1 for i in colors}]
    for i in range(1, N):
        dp.append({})
        for arr, count in dp[-2].iteritems():
            for part1 in flip1(list(arr)):
                for part2 in flip2(part1):
                    dp[-1][part2] = dp[-1].get(part2, 0) + count
    
    ans = sum(count for arr, count in dp[-1].iteritems())
    print ans
