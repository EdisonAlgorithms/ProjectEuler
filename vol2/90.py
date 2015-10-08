from itertools import combinations

def valid(c1, c2):
    return all(x in c1 and y in c2 or x in c2 and y in c1 for x, y in squares)

if __name__ == "__main__":
    squares = [(0,1), (0,4), (0,6), (1,6), (2,5), (3,6), (4,6), (8,1)]
    cube = list(combinations([0,1,2,3,4,5,6,7,8,6], 6))
    print sum(1 for i, c1 in enumerate(cube)
                for c2 in cube[i+1:] if valid(c1, c2))


