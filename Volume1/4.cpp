#include <iostream>

using namespace std;

bool isPalindrome(int n) {
	int v[10], i = 0;
	while(n != 0) {
		v[i] = n % 10;
		n /= 10;
		++ i;
	}
	for(int j = 0; j < i / 2; ++ j)
		if(v[j] != v[i - 1 - j])
			return false;
	return true;
}

int main() {
	int ret = 0;
	for(int i = 999; i > 99; -- i)
		for(int j = 999; j >= i; -- j)
			if(isPalindrome(i * j)) {
				if(ret < i * j)
					ret = i * j;
			}
	cout << ret << endl;
	return 0;
}