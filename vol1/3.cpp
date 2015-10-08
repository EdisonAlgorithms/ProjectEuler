#include <iostream>
#include <cstring>
#include <cmath>

using namespace std;

int main() {
	int ret = 1, i = 2;
	long number = 600851475143;
	while(true) {
		while(number % i == 0) {
			ret = i;
			number /= i;
		}
		if(i > sqrt(number)) {
			if(number > ret)
				ret = number;
			break;
		}
		++ i;
	}
	cout << ret << endl;
	return 0;
}