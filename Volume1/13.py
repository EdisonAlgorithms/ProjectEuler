import sys

if __name__ == '__main__' :
	sum = 0
	for i in range(100) :
		number = int(sys.stdin.readline())
		sum += number
	sys.stdout.write("{}\n".format(str(sum)[0:10]))



