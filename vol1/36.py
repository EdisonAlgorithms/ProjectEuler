def isPalindrome(s) :
	return s[::-1] == s

if __name__ == '__main__' :
	print sum(i for i in range(1, 1000000) if isPalindrome(str(i)) and isPalindrome(bin(i)[2:]))
			