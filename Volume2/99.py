from urllib2 import urlopen
import math

if __name__ == "__main__":
    f = urlopen('https://projecteuler.net/project/resources/p099_base_exp.txt')
    maxValue = 0
    ans = 0
    index = 0
    for line in f:
        value = math.log(int(line.split(',')[0])) * int(line.split(',')[1])
        if value > maxValue:
            maxValue = value
            ans = index
        index += 1
    print ans + 1
