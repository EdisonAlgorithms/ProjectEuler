import re
import urllib2

if __name__ == "__main__":
    file_url = 'https://projecteuler.net/project/resources/p089_roman.txt'
    rows = urllib2.urlopen(file_url).read()
    ans = len(rows) - len(re.sub("DCCCC|LXXXX|VIIII|CCCC|XXXX|IIII", "  ", rows))
    print ans
