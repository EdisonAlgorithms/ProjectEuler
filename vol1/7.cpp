#include <iostream>
#include <cmath>

using namespace std;

bool isPrime(int x) {
	for(int i = 2; i <= sqrt(x); ++ i)
		if(x % i == 0)
			return false;
	return true;
}

int main() {
	int ret = 0;
	for(int i = 2; ; ++ i)
		if(isPrime(i)) {
			++ ret;
			if(ret == 10001) {
				cout << i << endl;
				return 0;
			}
		}
}