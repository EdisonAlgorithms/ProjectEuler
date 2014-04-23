#include <iostream>

using namespace std;

int gcd(int a, int b) {
	if (a < b)
		return gcd(b, a);
	while (a % b != 0) {
		int r = a % b;
		a = b;
		b = r;
	}
	return b;
}

long long lcm(long long a, int b) {
	return a * b / gcd(a, b);
}

int main() {
	long long ret = 1;
	for(int i = 2; i <= 20; ++ i) {
		ret = lcm(ret, i);
		cout << ret << endl;
	}
	cout << ret << endl;
	return 0;
}